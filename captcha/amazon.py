from amazoncaptcha import AmazonCaptcha
from selenium import webdriver
import selenium as sel
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def solve_captcha(driver):
    
    max_attempts = 5
    attempts = 0
    
    while attempts < max_attempts:
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        img_tag = soup.find('img')
        img_src = img_tag['src']

        captcha = AmazonCaptcha.fromlink(img_src)

        solution = captcha.solve()
        
        if solution != "Not Solved":
            input_element = driver.find_element(By.ID, 'captchacharacters')
            input_element.send_keys(solution)

            # Find the button and click it
            button_element = driver.find_element(By.XPATH, '//button[@type="submit"]')
            button_element.click()
            return True
        else:
            attempts += 1
            a_element = driver.find_element(By.XPATH, '//a[@onclick="window.location.reload()"]')
            a_element.click()
            
            
    return False