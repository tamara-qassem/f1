# F1 Stats Dashboard

Welcome to the F1 Stats Dashboard, your pit stop for all things Formula 1! Imagine a place where data meets the racetrack, bringing you the exhilarating world of Formula 1 racing through the lens of data analysis.

We all have our obsessions, and mine revolves around the fast-paced, high-octane world of Formula 1. What do you do when you're passionate about something? You create a project around it, obviously! So, in a burst of enthusiasm, I decided to bring together my love for data and the thrilling universe of F1. Get ready for a data-driven ride that's faster than a pit stop!

Dataset Wonderland 📊🏎️

And guess what? All the datasets are right here, neatly parked in the `datasets` folder. Ready for your convenience! But, if you fancy the thrill of the track and want to scrape it yourself, buckle up and follow the instructions. It's like being your own pit crew—because who needs a pit stop when you can have a pit start?

## Project Overview

This project is organized into three main components, each represented by a Python script:

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

## Requirements

To run the project, ensure you have the necessary dependencies installed. You can install them using:

```bash
pip install -r requirements.txt
