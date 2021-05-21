
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox 
browser = webdriver.Firefox(executable_path="./geckodriver")
# Step 2) Navigate to Facebook
browser.get("http://localhost:8081/")
# Step 3) 
wait = WebDriverWait( browser, 5 )
proof_name = browser.find_element_by_tag_name('h1')
assert proof_name.text == "Testpage"
browser.close()
