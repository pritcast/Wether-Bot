# Chrome Driver Path
chrome_driver_path = "C:\\driver\\chromedriver.exe"

# Importing Module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


# Create a selenium driver object
driver = webdriver.Chrome(executable_path=chrome_driver_path)


# City 
city = "Kolkata"


# Navigate Weather Website
url = "https://mausam.imd.gov.in/"
driver.get(url)

# Search_Field and search the city
search_field = driver.find_element(By.NAME, "sr")
search_field.send_keys(city)
search_field.send_keys(Keys.ENTER)

# Click the first link
first_link = driver.find_element(By.CSS_SELECTOR,"#ssep_results a")
first_link.click()

# Make an empty dictionary to store current weather information
current_weather_report = {}


# Changing the tab or handling the tab
# obtain window handle of browser in focus
p = driver.current_window_handle

# obtain parent window handle
parent = driver.window_handles[0]


# Obtain child window handle
child = driver.window_handles[1]

# Switch child window handle
driver.switch_to.window(child)


# weather information list creation with city as the first element to store weather value
weather_information = [city]

# Find the temperature
temp_obj = driver.find_element(By.CLASS_NAME,"temp")
curr_temp = temp_obj.text
weather_information.append(curr_temp)


# Find the Sunrise, Sunset, Moon-Rise, Moon-Set timing value in a weather information list
containers = driver.find_elements(By.CSS_SELECTOR, ".right-box-equal span")

for info in containers:
    weather_information.append(info.text[-11:])

# Store the weather parameter of in our result dictionary
weather_parameter = ["City","Temperature(deg celcius)","Sunrise", "Sunset", "Moonrise", "Moonset"] 


# weather report dictionary creaion
current_weather_report.update({
    "Parameter Name":weather_parameter,
    "Values": weather_information,
})


time.sleep(3)

# Close the current tab
driver.close()


# Switch to parent tab
driver.switch_to.window(parent)
driver.close()


# --------------------------------------------------

# Representing the weather report as dataframe
print("\n--------------------------------------------------------------------")
df = pd.DataFrame(current_weather_report)
print(df)

# Creating a csv file if user needs 
user_file = input("Do you need any CSV File of that current information?(Y/N): ").lower()
if user_file == "y":
    df.to_csv("WeatherReport.csv")
    print("Your file has been saved successfully!")
else:
    print("Thank You!")
    