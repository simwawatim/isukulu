document.addEventListener("DOMContentLoaded", function () {
    const monthlyChartCanvas = document.getElementById('monthlyAttendanceChart');
    const monthlyAttendanceUrl = monthlyChartCanvas.getAttribute("data-monthly-attendance-data-url");

    if (!monthlyChartCanvas) {
        console.error("Error: Canvas element with ID 'monthlyAttendanceChart' not found.");
        return;
    }

    fetch(monthlyAttendanceUrl)
        .then(response => response.json())
        .then(data => {
            console.log("API Response:", data);

            const monthlyTotalDays = data.total_working_days || 30;
            const monthlyCoveredDays = data.total_monthly_days_covered || 0;
            const monthlyMissedDays = data.total_monthly_days_missed || 0;

            document.getElementById("total-monthly-days").textContent = monthlyTotalDays;
            document.getElementById("monthly-covered-days").textContent = monthlyCoveredDays;
            document.getElementById("monthly-missed-days").textContent = monthlyMissedDays;

            const ctx = monthlyChartCanvas.getContext("2d");

            if (window.monthlyAttendanceChart instanceof Chart) {
                window.monthlyAttendanceChart.destroy();
            }

            window.monthlyAttendanceChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Days Covered', 'Days Missed'],
                    datasets: [{
                      
                        data: [monthlyMissedDays, monthlyCoveredDays],  
                        backgroundColor: ['rgba(190, 65, 65, 0.8)', 'rgba(14, 124, 124, 0.8)'],
                        borderWidth: 2,
                        borderColor: "#fff",
                        hoverOffset: 4,
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    rotation: -Math.PI / 2, 
                    cutout: "70%",
                    plugins: {
                        legend: {
                            position: "bottom"
                        }
                    }
                }
            });
        })
        .catch(error => {
            console.error("Error fetching monthly attendance data:", error);
        });
});
