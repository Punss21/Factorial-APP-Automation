
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from selenium.common.exceptions import NoSuchElementException


class Factorial(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        s = Service(ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=s)

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("https://6945-106-203-205-226.ngrok.io/ ")
        time.sleep(3)

    def testStep1(self):

        print("Verify the factorial functionality when user enters any number in the text field.")
        input_data = 1000
        result = None
        self.search_field = self.driver.find_element(by=By.NAME, value="number")
        self.search_field.send_keys(input_data)
        time.sleep(3)
        self.driver.find_element(by=By.ID,value="getFactorial").click()
        time.sleep(3)
        result = self.driver.find_element(by=By.ID,value="resultDiv").text
        time.sleep(3)
        self.assertNotIn('The factorial',result,"Unable to get the result for input as {}".format(input_data))

    def testStep2(self):

        # get the search textbox
        print("Verify if calculator responds with proper error message when user directly clicks calculate button without giving any number to test field.")

        self.search_field = self.driver.find_element(by=By.NAME, value="number")
        self.driver.find_element(by=By.ID,value="getFactorial").click()
        result = self.driver.find_element(by=By.ID,value="resultDiv").text
        self.assertIn('Please enter an integer',result,"Unable to get expected error message")

    def testStep3(self):

        print("Verify the functionality when user enter a non-integer value and clicks on calculate button.")
        input_data = 'INVALID_VALUE'
        self.search_field = self.driver.find_element(by=By.NAME, value="number")
        self.search_field.send_keys(input_data)
        time.sleep(3)
        self.driver.find_element(by=By.ID,value="getFactorial").click()
        time.sleep(3)
        result = self.driver.find_element(by=By.ID,value="resultDiv").text
        self.assertIn('Please enter an integer',result,"Unable to get expected error message")

    def testStep4(self):

        print("Verify the functionality when user enter a negative integer.")
        input_data = -5
        self.search_field = self.driver.find_element(by=By.NAME, value="number")
        self.search_field.send_keys(input_data)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="getFactorial").click()
        time.sleep(3)
        result = self.driver.find_element(by=By.ID, value="resultDiv").text
        time.sleep(3)
        self.assertIn('Please enter an positive integer', result, "Unable to get expected error message")

    def testStep05(self):

        print('Verify the range of the acceptable positive integers by the calculator.')
        self.fail('No such data is mentioned over the app.')

    def testStep06(self):

        print('Verify the boundry value of the acceptable range of integers.')
        input_data = [1,99]
        self.search_field = self.driver.find_element(by=By.NAME, value="number")
        random_int = random.choice(input_data)
        self.search_field.send_keys(random_int)
        self.driver.find_element(by=By.ID, value="getFactorial").click()
        time.sleep(3)
        result = self.driver.find_element(by=By.ID, value="resultDiv").text
        time.sleep(3)
        self.assertIn('The factorial', result, "Unable to get the result for input as {}".format(random_int))

    def testStep07(self):
        print("Verify the out of boundry values over the input field of the calculator.")
        input_data = [-1, 100]
        self.search_field = self.driver.find_element(by=By.NAME, value="number")
        random_int = random.choice(input_data)
        self.search_field.send_keys(random_int)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="getFactorial").click()
        time.sleep(3)
        result = self.driver.find_element(by=By.ID, value="resultDiv").text
        time.sleep(3)
        self.assertIn('Out of range Value', result, "Unable to get the result for input as {}".format(random_int))

    def testStep08(self):

        print("Verify the functionality when user enter a decimal value and clicks on calculate button.")
        input_data = 0.5
        self.search_field = self.driver.find_element(by=By.NAME, value="number")
        self.search_field.send_keys(input_data)
        self.driver.find_element(by=By.ID,value="getFactorial").click()
        time.sleep(3)
        result = self.driver.find_element(by=By.ID,value="resultDiv").text
        time.sleep(3)
        self.assertIn('Please enter an integer',result,"Unable to get expected error message")

    def testStep09(self):

        print('Verify the positive value of the acceptable range of integers.')
        input_data = +5
        self.search_field = self.driver.find_element(by=By.NAME, value="number")
        self.search_field.send_keys(input_data)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="getFactorial").click()
        time.sleep(3)
        result = self.driver.find_element(by=By.ID, value="resultDiv").text
        time.sleep(3)
        self.assertIn('The factorial', result, "Unable to get the result for input as {}".format(input_data))

    def testStep10(self):

        print('Verify the functionality when user enters symbolic signs and click on calculate button.')
        input_data = '#$@%^'
        self.search_field = self.driver.find_element(by=By.NAME, value="number")
        self.search_field.send_keys(input_data)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="getFactorial").click()
        time.sleep(3)
        result = self.driver.find_element(by=By.ID, value="resultDiv").text
        self.assertIn('Please enter an integer', result, "Unable to get expected error message")

    def testStep11(self):

        print('Verify the functionality when user enters only empty spaces in the text field and click on calculate button.')
        input_data = '      '
        self.search_field = self.driver.find_element(by=By.NAME, value="number")
        self.search_field.send_keys(input_data)
        time.sleep(3)
        self.driver.find_element(by=By.ID, value="getFactorial").click()
        time.sleep(3)
        result = self.driver.find_element(by=By.ID, value="resultDiv").text
        time.sleep(3)
        self.assertIn('Please enter an integer', result, "Unable to get expected error message")

    def testStep12(self):

        print('Verify if the calculator range is mentioned over the UI or not.')
        self.fail('No such data is mentioned over the app.')


    def testStep13(self):

        print("Verify the functionality when user clicks on 'Terms and Conditions' hyper link.")
        self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/p/a[1]").click()
        fetch_text = self.driver.find_element(by=By.XPATH,value='/html/body').text

        self.assertNotIn('This is the privacy document. We are not yet ready with it. Stay tuned!',fetch_text,'Invalid Data found while navif'
                                                                                                              'gating to Terms and Conditions link.')

    def testStep14(self):
        print("Verify the functionality when user clicks on 'Privacy' hyper link.")
        self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/p/a[2]").click()
        fetch_text = self.driver.find_element(by=By.XPATH, value='/html/body').text

        self.assertNotIn('This is the terms and conditions document. We are not yet ready with it. Stay tuned!', fetch_text,
                         'Invalid Data found while navif'
                         'gating to Privacy link.')

    def testStep15(self):
        print('Verify if the user have a clear button to clear the entered text over the text field.')

        try:
            self.driver.find_element(by=By.ID, value="clr-button").click()
        except NoSuchElementException:
            self.fail('No such button found over the UI')

    def testStep16(self):

        print('Verify the functionality when user enters 0 or any value with in range as a integer over the text field and click on calculate button. ')
        num = random.randint(0,99)
        factorial = 1

        if num == 0:
            factorial = 1
        else:
            for i in range(1, num + 1):
                factorial = factorial * i

            self.search_field = self.driver.find_element(by=By.NAME, value="number")
            self.search_field.send_keys(num)
            self.driver.find_element(by=By.ID, value="getFactorial").click()
            result = self.driver.find_element(by=By.ID, value="resultDiv").text

            self.assertEqual(int(result), factorial, 'Mismatch found in the factorial calculator. ')



    def tearDown(self):
        # close the browser window
        self.driver.quit()