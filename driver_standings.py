import pandas as pd
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://www.formula1.com/en/drivers.html"
driver.get(url)

def get_element_by_xpath(driver, xpath):
    try:
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except StaleElementReferenceException:
        return get_element_by_xpath(driver, xpath)
    
# Create a folder named "Driver_Images" if it doesn't exist
folder_name = "Driver_Profile_Images"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

folder_name_number = "Driver_Number_Images"
if not os.path.exists(folder_name_number):
    os.makedirs(folder_name_number)


# Set the number of iterations
num_iterations = 22

# Initialize an empty list to store the extracted data
all_data = []

for iteration in range(1, num_iterations + 1):
    print(f"Processing iteration: {iteration}")
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

    # Construct the XPaths with the current iteration index
    champ_standing = driver.find_element(By.XPATH, f"//div[{iteration}]/a/fieldset/div[1]/div[1]")
    points = driver.find_element(By.XPATH, f"//div[{iteration}]/a/fieldset/div[1]/div[2]/div[1]")
    first_name = driver.find_element(By.XPATH, f"//div[{iteration}]/a/fieldset/div[2]/div/div[1]/span[1]")
    last_name = driver.find_element(By.XPATH, f"//div[{iteration}]/a/fieldset/div[2]/div/div[1]/span[2]")
    car = driver.find_element(By.XPATH, f"//div[{iteration}]/a/fieldset/p")
    image = driver.find_element(By.XPATH, f"//div[{iteration}]/a/fieldset/div[3]/picture[1]/img")
    numbers_image = driver.find_element(By.XPATH, f"//div[{iteration}]/a/fieldset/div[3]/picture[2]/img")
    # Extract image source URL

    # Extract image source URL
    try:
        number_url = numbers_image.get_attribute("data-src")  # use data-src attribute

        # Save the image locally in the "Driver_Images" folder
        driver_name = first_name.text.lower()  # Convert spaces to underscores and make lowercase
        number_filename = f"{folder_name_number}/{driver_name}_number.png"
        with open(number_filename, "wb") as img_file:
            img_file.write(requests.get(number_url).content)
    except StaleElementReferenceException:
        pass

    try:
        image_url = image.get_attribute("data-src")  # use data-src attribute

    # Save the image locally in the "Driver_Images" folder
        drivers_name = first_name.text.lower()  # Convert spaces to underscores and make lowercase
        image_filename = f"{folder_name}/{drivers_name}_image.png"
        with open(image_filename, "wb") as img_file:
            img_file.write(requests.get(image_url).content)
    except: 
        pass

    # Extract data and store in a dictionary
    data = {
        'Championship Standing': champ_standing.text,
        'Points': points.text,
        'Driver': first_name.text + " " + last_name.text,
        'Car': car.text,
        'Image Filename': image_filename,
        'Number Filename': number_filename  # Add the image filename to the data
    }

    # Append the data to the list
    all_data.append(data)

# Create a DataFrame from the collected data
final_df = pd.DataFrame(all_data)

# Save DataFrame as an Excel file
final_df.to_excel("datasets/driver_world_standings.xlsx", index=False, engine="openpyxl")
