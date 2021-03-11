# **User Manual - *FormulaML***

## Group Members

  + Kealan O'Connor - 18348311
  + Peter Browne - 18424692
  
# **1. Introduction**
## 1.1 About
FormulaML is a web app designed by and for Formula 1 fans. The web app provides information about all the current F1 drivers and teams in an interesting and easily interpretable way using graphs. The web app also provides a race predictor that will allow fans of F1 to see predictions of how races will finish. This app was built to help fans understand the sport better and to help them understand the general consensus driver opinions, or possibly in some cases debunk the consensus.

## 1.2 Ethics
Due to the nature of our app, there is no necessity for logins or passwords or any information on users being stored. Therefore there is no possibility of any unethical use of information or data from our users. Any use of FIA data or 3rd party API, is strictly under open source licenses.

# 2. User Manual

## 2.1 Installation

- Ensure Docker is installed
- Open CMD or your terminal if using Linux  International motorsport.
- Navigate to the “dash” folder using the command line
- Enter the command “sudo docker run -p 8050:8050 formula_ml” if on Linux, otherwise if you are on Windows “docker run -p 8050:8050 formula_ml”

## 2.2 Navigate to Dashboard

- At the top of the web app on all dashboards you will find the nav bar.
- To get to any team dashboard, hover over the dropdown and click the team of your choice.
- To get to any driver dashboard, hover over the dropdown and click the driver of your choice.
- To get to the season/home dashboard you originally loaded to, click the “Home” button at the left side of the nav bar.
- To get to the predictor dashboard, hover over the dropdown and choose either “Predictor Information” which explains how the predictor works and makes its predictions or click “Predictor” to see the dashboard with the actual predictions

## 2.3 Downloading Graphs
- When looking at any graph or figure, hover over it with your mouse.
- In the top right you will see a number of icons.
- Click the camera icon and the graph will be downloaded to your device as a PNG file.
