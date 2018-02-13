from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("http://www.google.com")
print driver.title
#driver.save_screenshot("test.png")
try:
 assert "Google" in driver.title
except:
    print "failed"

driver.find_element_by_name('q').send_keys("harsha")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(4)
#elem.send_keys("harsha")
driver.quit()
