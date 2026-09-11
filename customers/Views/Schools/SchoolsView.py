from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from customers.forms.School.SchoolForm import TierForm
from customers.models import Client, Domain, Tier


@login_required(login_url="login")
def schools(request):
    today = timezone.now().date()
    soon = today + timedelta(days=30)

    clients = Client.objects.exclude(schema_name="public").order_by("name")

    domains = {
        d.tenant_id: d.domain
        for d in Domain.objects.filter(tenant__in=clients, is_primary=True)
    }

    tenants = []
    paid_count = 0
    trial_count = 0
    expiring_soon_count = 0

    for client in clients:
        tenants.append({
            "name": client.name,
            "domain": domains.get(client.id),
            "on_trial": client.on_trial,
            "paid_until": client.paid_until,
        })
        if client.on_trial:
            trial_count += 1
        else:
            paid_count += 1
            if client.paid_until and today <= client.paid_until <= soon:
                expiring_soon_count += 1

    context = {
        "tenants": tenants,
        "total_schools": len(tenants),
        "paid_count": paid_count,
        "trial_count": trial_count,
        "expiring_soon_count": expiring_soon_count,
        "tenant_port": getattr(settings, "TENANT_PORT", None),
    }
    return render(request, "Admin/AdminSchools.html", context)


@login_required(login_url="login")
def tiers(request):
    all_tiers = Tier.objects.all()
    total_tiers = all_tiers.count()
    active_tiers_count = all_tiers.filter(is_active=True).count()
    inactive_tiers_count = total_tiers - active_tiers_count

    editing_tier = None
    edit_id = request.GET.get("edit")
    if edit_id:
        editing_tier = Tier.objects.filter(id=edit_id).first()

    context = {
        "tiers": all_tiers,
        "total_tiers": total_tiers,
        "active_tiers_count": active_tiers_count,
        "inactive_tiers_count": inactive_tiers_count,
        "tier_form": TierForm(instance=editing_tier) if editing_tier else TierForm(),
        "editing_tier": editing_tier,
    }
    return render(request, "Admin/Tiers.html", context)


@login_required(login_url="login")
def add_tier(request):
    if request.method == "POST":
        form = TierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tier added.")
        else:
            messages.error(request, "Couldn't save tier — check the fields.")
    return redirect("tiers")


@login_required(login_url="login")
def edit_tier(request, tier_id):
    tier = get_object_or_404(Tier, id=tier_id)
    if request.method == "POST":
        form = TierForm(request.POST, instance=tier)
        if form.is_valid():
            form.save()
            messages.success(request, "Tier updated.")
        else:
            messages.error(request, "Couldn't update tier — check the fields.")
    return redirect("tiers")


@login_required(login_url="login")
def delete_tier(request, tier_id):
    if request.method == "POST":
        Tier.objects.filter(id=tier_id).delete()
        messages.success(request, "Tier removed.")
    return redirect("tiers")