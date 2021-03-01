            const chartOptions = {
            scales: {
                    yAxes: [{barPercentage: 0.5}]
                    },
                    elements: {
                    rectangle: {
                    borderSkipped: 'left',}}};
            const colours = [];
            const xlabels_round = [];
            const quali_data = [];
            console.log('Yet another chart');

            makeChart();
            async function makeChart(){
                await getStanding();
                const ctx = document.getElementById('TeamPoints_stats').getContext('2d');
                const myChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: xlabels_round,
                        datasets: [{
                        label: 'Qualifying Gap to Teammate 2020 (Lower is better)',
                        data: quali_data,
                        backgroundColor: colours,
                        fill: false,
                        borderWidth: 1
                                        }]
                            },
                    options: { chartOptions,
                        scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                suggestedMin: -1,
                                suggestedMax: 1
                                
                            }
                        }]
                            }
                            }
                    });
                }

        var dynamicColors = function() {
        var r = 6
        var g = 0
        var b = 239
            return "rgb(" + r + "," + g + "," + b + ")";
        };

        async function getStanding(){
        const standings = await fetch('../static/Data/QualiComparison/'+d_code+'.csv');
        const data = await standings.text();
        const d_standings = data.split('\n');
        const rounds = [];
        const times = [];
        for (var i = 0; i < d_standings.length; i++){
            const row = d_standings[i].split(',');
            const round = row[0];
            const time = row[1];
                quali_data.push(time);
                console.log(time);
                xlabels_round.push(round);
                colours.push(dynamicColors());
            }    
        };
