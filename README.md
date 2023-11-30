# F1 Stats Dashboard

Welcome to the F1 Stats Dashboard, your pit stop for all things Formula 1! Imagine a place where data meets the racetrack, bringing you the exhilarating world of Formula 1 racing through the lens of data analysis.

We all have our obsessions, and mine revolves around the fast-paced, high-octane world of Formula 1. What do you do when you're passionate about something? You create a project around it, obviously! So, in a burst of enthusiasm, I decided to bring together my love for data and the thrilling universe of F1. Get ready for a data-driven ride that's faster than a pit stop!

Dataset Wonderland 📊🏎️

And guess what? All the datasets are right here, neatly parked in the `datasets` folder. Ready for your convenience! But, if you fancy the thrill of the track and want to scrape it yourself, buckle up and follow the instructions. It's like being your own pit crew—because who needs a pit stop when you can have a pit start?

## Project Overview

This project is organized into four main components, each represented by a Python script:

1. **`driver_standings.py`**
   - Webscraped data about driver standings.
   - Data saved in `datasets/driver_world_standings.xlsx`.
   - Driver profile images saved in the `Driver_Profile_Images` folder.
   - Driver number images saved in the `Driver_Number_Images` folder.

2. **`race_results.py`**
   - Webscraped data about race results from 1950 to 2023.
   - Data saved in `datasets/race_results.xlsx`.

3. **`cleaning_results.py`**
   - Separates race results into two different Excel files.
     - `datasets/race_results_overall.xlsx`: Overall race winners from 1950 to 2023.
     - `datasets/race_results_detail.xlsx`: Detailed results for each driver per race.

4. **`standings_page.py`**
   - Displays a very simple 2023 driver standings.
   - Utilizes data from `datasets/driver_world_standings.xlsx`.
   - Run this script to view the current driver standing of 2023 using Streamlit.

## Requirements

To run the project, ensure you have the necessary dependencies installed. You can install them using:

```bash
pip install -r requirements.txt
```


## Usage

1. **Webscrape and Save Driver Standings Data**
   
To gather the 2023 driver standings data, run the following command:
```bash
python driver_standings.py
```
This script extracts Championship Standing position, Points, Driver names, Car details, and the file paths of the Image Filename and Number Filename. The scraped data is then saved in `datasets/driver_world_standings.xlsx`. Profile images of drivers are stored in the `Driver_Profile_Images` folder, and number images are stored in the `Driver_Number_Images` folder.



2. **Webscrape Race Results Data**
   
Retrieve comprehensive race results data from 1950 to 2023 with the command:
```bash
python race_results.py
```
The script webscrapes race results and saves the data in `datasets/race_results.xlsx`. The data includes the Country the race took place in, the driver's finshing Position, the driver's Number, the Driver name, the Car they drove, the number of Laps completed, the finishing Time, Points earned, and the Year the race occured.


3. **Clean and Separate Race Results Data**

Clean and organize the race results data with the following command:
```bash
python cleaning_results.py
```
This script separates the race results into two files: `datasets/race_results_overall.xlsx` contains overall winners from 1950 to 2023 per race, while `datasets/race_results_detail.xlsx` provides detailed results for each driver per race.


4. **Run Streamlit App**

Initiate your Streamlit app with the following command:
```bash
streamlit run standings_page.py
```
This will allow you to view the driver standings data extracted at `http://localhost:8501`.

I have personally deployed this app, you can check it out by clicking on this [link](https://tamara-f1.streamlit.app/)!

