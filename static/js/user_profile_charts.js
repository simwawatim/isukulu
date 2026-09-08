document.addEventListener("DOMContentLoaded", function () {
    const pieChartDiv = document.getElementById("pie_chart");
    const leaveChartUrl = pieChartDiv.getAttribute("data-url");

    fetch(leaveChartUrl)
        .then(response => response.json())
        .then(data => {
            console.log("Leave Data:", data);

            if (typeof data.days_taken === "undefined" || typeof data.days_accumulated === "undefined") {
                console.error("Invalid data received:", data);
                return;
            }

            let daysTaken = data.days_taken;
            let daysAccumulated = data.days_accumulated;
            let hasNoLeaveData = (daysTaken === 0 && daysAccumulated === 0);
            let series = hasNoLeaveData ? [1] : [daysTaken, daysAccumulated];
            let labels = hasNoLeaveData ? ["No Leave Data"] : [`Days Taken: ${daysTaken} days`, `Total Accumulated: ${daysAccumulated} days`];
            let colors = hasNoLeaveData ? ["#d3d3d3"] : ["#d00115", "#AFAFAF"];

            var options = {
                series: series,
                chart: {
                    type: 'pie',
                    height: 300
                },
                labels: labels,
                colors: colors,
                legend: {
                    position: "bottom"
                }
            };

            var chart = new ApexCharts(pieChartDiv, options);
            chart.render();
        })
        .catch(error => console.error("Error fetching leave data:", error));
});



document.addEventListener("DOMContentLoaded", function () {
    const donutChartDiv = document.getElementById("donut_chart");
    const salaryAdvanceDataUrl = donutChartDiv.getAttribute("advance-date-url");

    fetch(salaryAdvanceDataUrl)
        .then(response => {
            if (!response.ok) {
                if (response.status === 404) {
                    return { total_advance: 0, amount_paid: 0, remaining_balance: 0 };
                }
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            console.log("Advance Data:", data);

            let totalAdvance = parseFloat(data.total_advance) || 0;
            let amountPaid = parseFloat(data.amount_paid) || 0;
            let remainingBalance = parseFloat(data.remaining_balance) || 0;
            
            let series, chartColors, labels;
            if (totalAdvance === 0) {
            
                series = [100, 0]; 
                chartColors = ["#32CD32", "#32CD32"];
                labels = ["No Advance", "Remaining"];
            } else {
                series = [amountPaid, remainingBalance];
                chartColors = ["#77bff3", "#d00115"];
                labels = ["Amount Paid", "Remaining Balance"];
            }
            
            var options = {
                series: series,
                chart: {
                    type: 'donut',
                    height: 300
                },
                labels: labels,
                colors: chartColors,
                legend: {
                    position: "bottom"
                }
            };

            new ApexCharts(donutChartDiv, options).render();
        })
        .catch(error => {
            console.error("Error fetching salary advance data:", error);
            var options = {
                series: [100, 0],
                chart: {
                    type: 'donut',
                    height: 300
                },
                labels: ["No Advance", "Remaining"],
                colors: ["#32CD32", "#32CD32"],
                legend: {
                    position: "bottom"
                }
            };
            new ApexCharts(donutChartDiv, options).render();
        });
});
