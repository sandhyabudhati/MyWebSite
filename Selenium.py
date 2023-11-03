from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set the path to the ChromeDriver executable
chrome_driver_path = '/path/to/chromedriver'

# Create a new instance of the Chrome web driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open a website
driver.get('http://54.171.216.105')  # Replace with the URL of the website you want to test

# Find an element by its CSS selector or XPath that contains the text you want to check
element = driver.find_element_by_xpath('//div[contains(text(), "Hellow World")]') # Replace with your CSS selector
# Example using XPath: element = driver.find_element_by_xpath('//div[contains(text(), "Your Text")]')

# Check if the text is present
if "Your Text" in element.text:
    print("Text is present on the web page")
else:
    print("Text is not present on the web page")

# Close the browser
driver.close()
