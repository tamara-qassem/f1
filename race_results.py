import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# List of years to iterate through
years = list(range(2023, 1949, -1))  # Update the range accordingly

# Create empty lists to store the data
all_data_start = []

for year in years:
    url = f"https://www.formula1.com/en/results.html/{year}/races.html"
    driver.get(url)
    
    # Handle the consent message for each country
    try:
        consent_frame = WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.ID, "sp_message_iframe_877301"))
            )
        accept_all_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="ACCEPT ALL"]'))
            )
        accept_all_button.click()
        driver.switch_to.default_content()
    except:
        pass

    try:
        table_present = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//table[@class="resultsarchive-table"]'))
        )
    except:
        print(f"No data table found for {year}. Moving to the next year.")
        continue

        
    # Starting index for the list
    start_index = 1

    while start_index <= 25:
        try:
            xpath = f"//article/div/div[2]/div[1]/div[3]/ul/li[{start_index}]"
            print(f"Processing index: {start_index}")
            
            try:
                element = driver.find_element(By.XPATH, xpath)
                element.click()
            except NoSuchElementException:
                print(f"Element not found for index {start_index}. Skipping to the next index.")
                start_index += 1
                continue
        except:
            pass

        # Handle the consent message for each country
        try:
            consent_frame = WebDriverWait(driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.ID, "sp_message_iframe_877301"))
            )
            accept_all_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="ACCEPT ALL"]'))
            )
            accept_all_button.click()
            driver.switch_to.default_content()
        except:
            pass
        
        try:
            table_present = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.XPATH, '//table[@class="resultsarchive-table"]'))
                            )
        except:
            print(f"No data table found for index {start_index}. Moving to the next index.")
            start_index += 1
            continue
                
        # Extract data for the second section
        country_element = driver.find_element(By.XPATH, f"//article/div/div[2]/div[1]/div[3]/ul/li[{start_index}]/a/span[@class='clip']")
        country = country_element.text
        pos = driver.find_elements(By.XPATH, "//tbody/tr/td[2]")
        no = driver.find_elements(By.XPATH, "//tbody/tr/td[3]")
        driver_f1 = driver.find_elements(By.XPATH, "//tbody/tr/td[4]")
        car = driver.find_elements(By.XPATH, "//tbody/tr/td[5]")
        laps = driver.find_elements(By.XPATH, "//tbody/tr/td[6]")
        time_done = driver.find_elements(By.XPATH, "//tbody/tr/td[7]")
        points = driver.find_elements(By.XPATH, "//tbody/tr/td[8]")
        data_start = []

        for i in range(len(pos)):
            temp = {'Country': country,
                            'POS': pos[i].text,
                            'NO': no[i].text,
                            'DRIVER': driver_f1[i].text,
                            'CAR': car[i].text,
                            'LAPS': laps[i].text,
                            'TIME': time_done[i].text,
                            'PTS':points[i].text}
            data_start.append(temp)

        for item in data_start:
            item['Year'] = year

        # Add the data from the second section to the all_data_start list
        all_data_start.extend(data_start)

        # Increment the index
        start_index += 1

        # Add a delay between clicks if needed
        time.sleep(2)

    # Reset the start_index for the next year
    start_index = 1

# Create DataFrames from the collected data
final_df = pd.DataFrame(all_data_start)

# Save DataFrames as Excel files
final_df.to_excel("datasets/race_results.xlsx", index=False, engine="openpyxl")
