from selenium import webdriver
from math import log, sin
import time

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Firefox()
    browser.get(link)

    browser.find_element_by_tag_name("button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(0.5)
    x = browser.find_element_by_id("input_value").text
    x = str(log(abs(12 * sin(int(x)))))
    input1 = browser.find_element_by_id("answer").send_keys(x)
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()
