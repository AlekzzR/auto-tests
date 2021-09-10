import unittest
from selenium import webdriver
import time

class Test_Mode(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_tag_name('div.first_block .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_tag_name("div.first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_tag_name('div.first_block .third')
        input3.send_keys("123@mail.ru")
        time.sleep(3)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Error")

    def test_reg2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element_by_tag_name('div.first_block .first')
            input1.send_keys("Ivan")
            input2 = browser.find_element_by_tag_name("div.first_block .second")
            input2.send_keys("Petrov")
            input3 = browser.find_element_by_tag_name('div.first_block .third')
            input3.send_keys("123@mail.ru")
            time.sleep(3)

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(3)
        finally:
        # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Error!!!!!!!!!!!!!!!!")
if __name__ == "__main__":
    unittest.main()