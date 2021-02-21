const xlabels = [];
console.log("hello the script is here");
const points_data = [];
makeChart();
async function makeChart(){
    await getStanding();
    const ctx = document.getElementById("driver_points").getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xlabels,
            datasets: [{
            label: 'Points Earned',
        data: points_data,
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
    const point_list = [];
    const year_list = [];
    const round_list = [];
    for (var i = 0; i < d_standings.length; i++){
        const row = d_standings[i].split(',');
        const year = row[0]; 
        const round = row[1];
        const driver = row[2];
        const points = row[3];
        if (driver == d_name){
            year_list.push(year);
            point_list.push(points);
            round_list.push(round);
        }    
    };
    round_list.push("1");
    for (var i = 1; i < year_list.length && point_list.length; i++){
        if(!xlabels.includes(year_list[i])){
            xlabels.push(year_list[i]);
        }
        if(parseFloat(round_list[i]) > parseFloat(round_list[i + 1])){
            points_data.push(point_list[i]);
        }
    }
}