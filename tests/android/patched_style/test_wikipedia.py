from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step as title

from mobile_tests_lesson_13.model import app


def test_search():
    app.given_opened()

    browser.element((AppiumBy.ACCESSIBILITY_ID, "Поиск по Википедии")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).send_keys("BrowserStack")
    browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))


def test_search_is_efficient_enough_to_find_selene_as_python_package():
    app.given_opened()

    with title('Search for content'):
        browser.element('Поиск по Википедии').click()
        browser.element('#search_src_text').type('Selene')

    with title('Content should be found'):
        browser.all('#page_list_item_title').first.should(
            have.text('User-oriented Web UI browser tests in Python')
        )
