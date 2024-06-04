from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime


def get_driver():
    # Options to make browsing easier
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument(
        'disable-dev-shm-usage')
    options.add_argument(
        'no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get('https://automated.pythonanywhere.com/login/')
    return driver


def login():
    driver = get_driver()
    sleep(2)
    driver.find_element(by='id', value='id_username').send_keys('automated')
    sleep(2)
    driver.find_element(by='id', value='id_password').send_keys('automatedautomated' + Keys.RETURN)
    sleep(2)
    return driver


def clean_text(element):
    element = element.split(': ')[1]
    return element


def get_text(driver):
    driver.find_element(by='xpath', value='/html/body/nav/div/a').click()
    sleep(2)
    element = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]/div')
    element = element.text
    return clean_text(element)


def scrape_and_save():
    for i in range(3):
        data = get_text(login())
        print(data)
        name = str(datetime.datetime.now().strftime('%Y-%m-%d.%H_%M_%S'))
        name = name + '.txt'
        with open(name, 'w') as file:
            file.write(data + '\n')
        sleep(2)


def main():
    scrape_and_save()


main()
