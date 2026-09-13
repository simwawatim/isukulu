from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db import connection
from functools import wraps


def tenant_member_required(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        print(f"[tenant_member_required] view={view_func.__name__} schema={connection.schema_name} user={request.user}")

        if not request.user.is_authenticated:
            print(f"[tenant_member_required] not authenticated -> redirecting to login")
            return redirect("login")

        if connection.schema_name == "public":
            print(f"[tenant_member_required] public schema -> allowing through")
            return view_func(request, *args, **kwargs)

        session_schema = request.session.get("tenant_schema")
        print(f"[tenant_member_required] session_schema={session_schema} current_schema={connection.schema_name}")

        if session_schema != connection.schema_name:
            print(f"[tenant_member_required] MISMATCH — session belongs to '{session_schema}', not '{connection.schema_name}' -> logging out")
            logout(request)
            return redirect("login")

        print(f"[tenant_member_required] schema match -> allowing through")
        return view_func(request, *args, **kwargs)

    return _wrapped