from selenium import webdriver  
from selenium.webdriver.common.keys import Keys    
from settings import *
import time

def main():
	for i in settings:
		openNewWind(settings[i]['url'],settings[i]['account'],settings[i]['password'])	
		time.sleep(5)

def openNewWind(URL,account,password):
	driver = webdriver.Chrome()
	if URL == "http://www.pspme.cn/":
		driver.get(URL)
		driver.set_page_load_timeout(30)
	else:
		driver.get(URL)
		driver.set_page_load_timeout(30) 
		elem_user = driver.find_element_by_id("form-username")
		elem_user.send_keys(account)
		elem_pwd = driver.find_element_by_id("form-password")
		elem_pwd.send_keys(password)
		driver.find_element_by_tag_name("form").submit()
	

if __name__=="__main__":
	main()