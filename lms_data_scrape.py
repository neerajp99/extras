from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

def clone_data():
	browser = webdriver.Chrome()
	browser.maximize_window()
	browser.get("https://lms.ashoka.edu.in")
	gmail_login_field = browser.find_element_by_xpath("//*[@id='identifierId']").send_keys("your email id")
	browser.find_element_by_xpath("//*[@id='identifierNext']/span").click()
	time.sleep(3)
	gmail_password_field = browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys("your ashoka password")
	browser.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()
	time.sleep(3)
	browser.find_element_by_xpath("//*[@id='ProcessRptr_lnkbtnProcess_1']").click()
	time.sleep(3)
	browser.find_element_by_xpath("//*[@id='divMenuNav']/li[3]/a").click()
	time.sleep(1)
	browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_ddlSession']").click()
	time.sleep(1)
	browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_ddlSession']/option[21]").click()
	time.sleep(1)
	browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_btnGetIt']").click()	
	time.sleep(1)
	# x = browser.find_element_by_xpath("//*[@id='ContentPlaceHolder1_lvStudents_ctrl0_imgStudent_0']").get_attribute("title")
	# print(x)

	l = list()
	ctr = 0
	email = open('email.txt', 'w+')
	for x in range(0, 101):
		for y in range(0, 6):
			imageTitle = browser.find_element_by_xpath(f"//*[@id='ContentPlaceHolder1_lvStudents_ctrl{x}_imgStudent_{ctr}']").get_attribute("title")
			l.append(imageTitle)
			email.write(imageTitle + '\n')
			ctr = ctr + 1
	print(l)
	# scraping the data here
	# lms_url = "https://lms.ashoka.edu.in/Contents/Report/ViewstudentDirectory.aspx"
	# headers = {
	#     "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
	# }
	# lms_data = requests.get(lms_url, headers = headers)
	# soup = BeautifulSoup(lms_data.content, 'html.parser')
	# print(soup)

clone_data()


