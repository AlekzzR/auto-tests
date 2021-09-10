import pytest
import time
import math
from selenium import webdriver

link1 = 'https://stepik.org/lesson/236895/step/1'
answer = math.log(int(time.time()))

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

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()
@pytest.mark.parametrize('url', list)
def test_guest_should_see_login_link(browser, url):
    link = url
    browser.get(link)
    area = browser.find_element_by_tag_name('textarea')
    area.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    answer = browser.find_element_by_tag_name('pre')
    text_answer = answer.text
    print(text_answer)
    assert text_answer == 'Correct!', 'Answer wrong'


