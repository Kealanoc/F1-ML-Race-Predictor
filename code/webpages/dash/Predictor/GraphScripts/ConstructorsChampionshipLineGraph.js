
            const xlabels = [];
            const championship_data = [];
            makeChart();
            async function makeChart(){
                await getStanding();
                const ctx = document.getElementById('TeamPoints_stats').getContext('2d');
                const myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: xlabels,
                        datasets: [{
                        label: 'Points Earned',
                    data: championship_data,
                    fill: false,
                    backgroundColor: [
                        'white',
                    ],
                    borderColor: [
                        "#0600EF",
                    ],
                    borderWidth: 1
                                    }]
                            },
                    options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: false,
                                reverse : true,
                                suggestedMin: 1,
                                suggestedMax: 10
                                
                            }
                        }]
                            }
                            }
                    });
                }
        async function getStanding(){
        const standings = await fetch('data/ConstructorStandings.csv');
        const data = await standings.text();
        const d_standings = data.split('\n');
        const point_list = [];
        const year_list = [];
        const round_list = [];
        const position_list = [];
        for (var i = 0; i < d_standings.length; i++){
            const row = d_standings[i].split(',');
            const year = row[0]; 
            const round = row[1];
            const team = row[2];
            const points = row[3];
            const position = row[5]
            if (team == "red_bull"){
                year_list.push(year);
                point_list.push(points);
                round_list.push(round);
                position_list.push(position)
            }    
        };
        round_list.push("1");
        for (var i = 1; i < year_list.length && position_list.length; i++){
                if(!xlabels.includes(year_list[i])){
                    xlabels.push(year_list[i]);
                }
                if(parseFloat(round_list[i]) > parseFloat(round_list[i + 1])){
                    championship_data.push(position_list[i]);
        }
    }
}
