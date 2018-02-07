from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import time  
  

driver = webdriver.Chrome()  
driver.get("https://psdemo.pspme.cn/web/")  
 
elem_user = driver.find_element_by_id("form-username")  
elem_user.send_keys("abc123@qq.com")  
elem_pwd = driver.find_element_by_id("form-password")  
elem_pwd.send_keys("abc123")  
driver.find_element_by_tag_name("form").submit()
