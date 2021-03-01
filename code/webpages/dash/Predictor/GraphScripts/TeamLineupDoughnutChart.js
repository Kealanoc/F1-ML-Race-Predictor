            const drivers = [];
            const numRaces = [];
            const colours = [];

            const lineupData = {
                labels: drivers,
                datasets: [
                    {
                        data: numRaces,
                        backgroundColor: colours,
                    }]
            };

            var chartOptions = {

            cutoutPercentage: 30,
            legend: {
                position: 'left'
            },
            };
            makeChart();

            
            async function makeChart(){
                await getLineup();
                const lineupChart = document.getElementById("Driver Lineup History");
                Chart.defaults.global.defaultFontFamily = "Lato";
                Chart.defaults.global.defaultFontSize = 18;
                const doughnut = new Chart(lineupChart, {
                    type: 'doughnut',
                    data: lineupData,
                    options: chartOptions
                    });
            }
            async function getLineup(){
                const lineup = await fetch("../../code/Data/TeamLineups/Renault.csv");
                const data = await lineup.text();
                const lineups = data.split("\n");
                for (var i=1; i < lineups.length-1; i++){
                    const row = lineups[i].split(",");
                    const driver = row[0];
                    const races = row[1];
                    drivers.push(driver);
                    numRaces.push(races);
                    colours.push(dynamicColors());
                }
            }

            var dynamicColors = function() {
            var r = Math.floor(Math.random() * 255);
            var g = Math.floor(Math.random() * 255);
            var b = Math.floor(Math.random() * 255);
            return "rgb(" + r + "," + g + "," + b + ")";
            };
