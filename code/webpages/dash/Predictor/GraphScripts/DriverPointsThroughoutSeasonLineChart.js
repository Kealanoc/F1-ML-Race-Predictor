            const xlabel = [];
            console.log("hello another script is here");
            const point_data = [];
            makeChart();
            async function makeChart(){
                await getStanding();
                const ctx = document.getElementById('driver_stats').getContext('2d');
                const myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: xlabel,
                        datasets: [{
                        label: 'Points Earned',
                    data: point_data,
                    fill: false,
                    backgroundColor: [
                        'white',
                    ],
                    borderColor: [
                        'black',
                    ],
                    borderWidth: 1
                                    }]
                            },
                    options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                            }
                            }
                    });
                }
        async function getStanding(){
        const standings = await fetch('../static/Data/DriverStandings.csv');
        const data = await standings.text();
        const d_standings = data.split('\n');
        const year_list = [];
        const point_list = [];
        for (var i = 0; i < d_standings.length; i++){
            const row = d_standings[i].split(',');
            const year = row[0]; 
            const round = row[1];
            const driver = row[2];
            const points = row[3];
            if (driver == d_name && year == "2020"){
                year_list.push(year);
                point_list.push(points);
                xlabel.push(year);
                point_data.push(point_list[point_list.length -1]);
            }      
        };
        }
