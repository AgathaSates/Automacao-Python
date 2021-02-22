from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://youtube.com')
searchbox =  driver.find_element_by_id("search")
searchbox.send_keys('manual do mundo')
searchButton = driver.find_element_by_id('search-icon-legacy')
searchButton.click()

