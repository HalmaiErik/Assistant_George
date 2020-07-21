from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup


class Fetcher:
	def __init__(self, url, mode):
		options = webdriver.ChromeOptions()
		options.add_argument("headless")
		self.driver = webdriver.Chrome(executable_path=".\\ChromeDriver\\chromedriver.exe", chrome_options=options)
		self.driver.wait = WebDriverWait(self.driver, 5)
		self.url = url
		self.mode = mode
		print(self.url)

	def look_up(self):
		self.driver.get(self.url)
		try:
			ip = self.driver.wait.until(EC.presence_of_element_located(
				(By.CLASS_NAME, "med")
			))
		except:
			print("Couldn't find any answers :(")

		soup = BeautifulSoup(self.driver.page_source, "html.parser")

		if self.mode == "def":
			answers = soup.find_all(class_="QIclbb XpoqFe")				# define command
		elif self.mode == "weather":
			answers = soup.find_all(class_="wob_t")						# weather in command
		else:
			answers = soup.find_all(class_="FLP8od")					# this appears for Who is the president of ...
		if not answers:
			answers = soup.find_all(class_="hgKElc")					# this appears for other searches

		self.driver.quit()
		return answers
