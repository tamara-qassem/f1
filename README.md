# F1 Stats Dashboard

Welcome to the F1 Stats Dashboard project! This project aims to provide an interactive dashboard displaying driver standings and race results data from Formula 1.

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
