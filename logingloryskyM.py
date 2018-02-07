from selenium import webdriver  
from selenium.webdriver.common.keys import Keys    
from settings import *
print(len(settings['URL']))


driver = webdriver.Chrome()  
for i in rang(1,len(settings['URL'])):
	

# driver.get("https://glorysky.pspme.cn/Manager/")  
 
# elem_user = driver.find_element_by_id("form-username")  
# elem_user.send_keys(gloryskyM['account'])  
# elem_pwd = driver.find_element_by_id("form-password")  
# elem_pwd.send_keys(gloryskyM['password'])  
# driver.find_element_by_tag_name("form").submit()
