            const team_list = ["mercedes", "red_bull", "mclaren", "racing_point", "renault", "ferrari", "alphatauri", "alfa", "haas", "williams"];
            const xlabels = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17];
            const team_positions = [];
            console.log(team_positions)
            makeChart();
            async function makeChart(){
                await getStanding();
                const ctx = document.getElementById('TeamPoints_stats').getContext('2d');
                const myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: xlabels,
                        datasets: [{
                        label: team_list[0],
                        data: team_positions[0],
                        fill: false,
                        backgroundColor: ['#00D2BE',],
                    borderColor: ['#00D2BE',],
                    borderWidth: 2
                                    },
                                    {
                        label: team_list[1],
                        data: team_positions[1],
                        fill: false,
                        backgroundColor: ['#1E41FF',],
                    borderColor: ['#1E41FF',],
                    borderWidth: 2
                                    },
                                    {
                        label: team_list[2],
                        data: team_positions[2],
                        fill: false,
                        backgroundColor: ['#FF8700',],
                    borderColor: ['#FF8700',],
                    borderWidth: 2
                                    },
                                    {
                        label: team_list[3],
                        data: team_positions[3],
                        fill: false,
                        backgroundColor: ['#F596C8',],
                    borderColor: ['#F596C8',],
                    borderWidth: 2
                                    },
                                    {
                        label: team_list[4],
                        data: team_positions[4],
                        fill: false,
                        backgroundColor: ['#FFF500',],
                    borderColor: ['#FFF500',],
                    borderWidth: 2
                                    },
                                    {
                        label: team_list[5],
                        data: team_positions[5],
                        fill: false,
                        backgroundColor: ['#C80000',],
                    borderColor: ['#C80000',],
                    borderWidth: 2
                                    },
                                    {
                        label: team_list[6],
                        data: team_positions[6],
                        fill: false,
                        backgroundColor: ['#FFFFFF',],
                    borderColor: ['#FFFFFF',],
                    borderWidth: 2
                                    },
                                    {
                        label: team_list[7],
                        data: team_positions[7],
                        fill: false,
                        backgroundColor: ['#9B0000',],
                    borderColor: ['#9B0000',],
                    borderWidth: 2
                                    },
                                    {
                        label: team_list[8],
                        data: team_positions[8],
                        fill: false,
                        backgroundColor:['#787878',],
                    borderColor: ['#787878',],
                    borderWidth: 2
                                    },
                                    {
                        label: team_list[9],
                        data: team_positions[9],
                        fill: false,
                        backgroundColor: ['#0082FA',],
                    borderColor: ['#0082FA',],
                    borderWidth: 2
                                    }
                                    ]
                            },
                    options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                reverse: true,
                                beginAtZero: true
                            }
                        }]
                            }
                            }
                    });
                }
        async function getStanding(){
        for (var j = 0; j < team_list.length; j++){
            const points_data = [];
            const team = team_list[j]
            const standings = await fetch('../../Data/ConstructorStandings.csv');
            const data = await standings.text();
            const d_standings = data.split('\n');
            const round_list = [];
            const point_list = [];
            for (var i = 0; i < d_standings.length; i++){
                const row = d_standings[i].split(',');
                const year = row[0]; 
                const round = row[1];
                const Constructor = row[2];
                const points = row[5];
                if (Constructor == team && year == "2020"){
                    point_list.push(points);
                    points_data.push(point_list[point_list.length -1]);
                }      
            };
            team_positions.push(points_data)
        }};
