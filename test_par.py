import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
class Test_par():
    list = [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1',
    ]
    @pytest.mark.parametrize('url', list)
    def test_func(self, browser, url):
        link = url
        browser.implicitly_wait(10)
        browser.get(link)
        area = browser.find_element_by_tag_name('textarea')
        area.send_keys(str(math.log(int(time.time()))))
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
        button.click()
        answer = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'pre')))
        text_answer = answer.text
        assert text_answer == 'Correct!', 'Answer wrong'


