from selenium import webdriver

driver=webdriver.Chrome()

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https:google.com")

el1=driver.find_element_by_name("q")

el1.send_keys("Automation")

driver.find_element_by_name("btnK").click()


print("Test Completed")