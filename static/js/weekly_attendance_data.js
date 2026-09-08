document.addEventListener("DOMContentLoaded", function () {
    const pieChartDiv = document.getElementById("pieChart");
    const weeklyAttendanceUrl = pieChartDiv.getAttribute("data-weekly-attendance-data-url"); 

    console.log("Weekly Attendance Data URL:", weeklyAttendanceUrl); 

    fetch(weeklyAttendanceUrl)
        .then(response => response.json()) 
        .then(data => {
            console.log("Fetched Data:", data); 

            const totalDays = data.total_days || 7; 
            const covered = data.covered || 0;
            const missed = totalDays - covered; 

            console.log("Total Days:", totalDays); 
            console.log("Covered Days:", covered); 
            console.log("Missed Days:", missed); 

            document.getElementById("total-days").textContent = totalDays;
            document.getElementById("covered-days").textContent = covered;
            document.getElementById("missed-days").textContent = missed;

            var ctx = document.getElementById("pieChart").getContext("2d");

            new Chart(ctx, {
                type: "pie",  // Change to "pie"
                data: {
                    labels: ["Covered", "Missed"],
                    datasets: [{
                        data: [covered, missed],
                        backgroundColor: ['rgba(14, 124, 124, 0.8)', 'rgba(190, 65, 65, 0.8)'],  
                        hoverOffset: 4
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'bottom'
                        }
                    }
                }
            });
        })
        .catch(function (error) {
            console.log('Error fetching data:', error); 
        });
});
