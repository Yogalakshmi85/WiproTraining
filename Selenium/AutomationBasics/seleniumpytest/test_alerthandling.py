import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    yield driver
    driver.quit()

def test_simple_js_alert(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert", "Alert text was Wrong"
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "You successfully clicked an alert" in result, 'Result text was wrong'

def test_js_confirm_dismiss(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm", "Confirm text was Wrong"
    time.sleep(3)
    alert.dismiss()
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "You clicked: Cancel" in result, 'Result text was wrong'

def test_js_confirm_ok(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm", "Confirm text was Wrong"
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "You clicked: Ok" in result, 'Result text was wrong'

def test_js_prompt(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS prompt", "Prompt text was Wrong"
    alert.send_keys("Selenium")
    time.sleep(5)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, "result").text
    assert "Selenium" in result, 'Result text was wrong'










