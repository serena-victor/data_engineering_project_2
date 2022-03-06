import unittest
import requests
import time
from selenium import webdriver
import re


class TestSite(unittest.TestCase):
    url='http://127.0.0.1:5000/'

#unit tests
    def test_site_is_working(self):
        response = requests.get(self.url).status_code
        self.assertEqual(response, 200)

    def test_input_is_working(self):
        response = requests.post(self.url, data={'text_to_send':'test input'})
        self.assertIn('id="result"', response.text)

    def test_model_is_working(self):
        response = requests.post(self.url, data={'text_to_send':'youre a white trash redneck'})
        match = re.search('identity_attack : \d+.\d+', response.text)
        self.assertGreater(float(match[0].split(':')[1]), 60)

 ## end to end tests
    def test_click_button_is_working(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(self.url)
        input = driver.find_element(by='id', value='input')
        button = driver.find_element(by='id', value='button')
        input.send_keys('this is a toxicity test')
        button.click()
        result = driver.find_element(by='id', value='result').is_displayed()
        driver.quit()
        self.assertTrue(result)    

    def test_submit_is_working(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(chrome_options=options)        
        driver.get(self.url)
        input = driver.find_element(by='id', value='input')
        input.send_keys('this is a toxicity test')
        input.submit()
        result = driver.find_element(by='id', value='result').is_displayed()
        driver.quit()
        self.assertTrue(result)   
   
# stress tests
    def test_site_stress(self):
        elapsed_time = time.time()
        for x in range(100) :
            request = requests.post(self.url, data={'text_to_send':'stress test'})
        elapsed_time = time.time()-elapsed_time
        print("elasped time for 100 requess = ", elapsed_time)
        self.assertTrue(elapsed_time < 60)

if __name__ == '__main__':
    unittest.main()