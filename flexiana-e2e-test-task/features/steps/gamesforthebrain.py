import time 

from xml.dom.minidom import Element
from behave import *
from browser import driver;
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = driver.browser()

@given(u'start a new game by restarting')
def step_impl(context):
    browser.get("https://www.gamesforthebrain.com/game/checkers/")

    restartLink = browser.find_element(By.LINK_TEXT, "Restart...")
    restartLink.click()

    message = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "message")))

    assert "Select an orange piece to move." in message.text
    browser.get_screenshot_as_file('./screenshots/01-restarted-page.png')


@when(u'make your first move')
def step_impl(context):
    myPiece = browser.find_element(By.NAME, "space02")
    myPiece.click()
    
    targetSpot = browser.find_element(By.NAME, "space13")
    targetSpot.click()
    
    text = "Make a move."
    message = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), '" + text + "')]")))
    
    assert "Make a move." in message.text
    browser.get_screenshot_as_file('./screenshots/02-make-fist-move.png')


@when(u'let computer move')
def step_impl(context):
    foeSpot = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@src='me1.gif' and @name='space24']")))
    foeImage = foeSpot.get_attribute("src")
    
    assert "me1.gif" in foeImage
    browser.get_screenshot_as_file('./screenshots/03-computer-moved.png')


@when(u'make your second move')
def step_impl(context):
    myPiece = browser.find_element(By.NAME, "space22")
    myPiece.click()
    
    targetSpot = browser.find_element(By.NAME, "space33")
    targetSpot.click()
    
    text = "Make a move."
    message = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), '" + text + "')]")))
    assert text in message.text
    
    browser.get_screenshot_as_file('./screenshots/04-make-second-move.png')


@when(u'let computer take your piece')
def step_impl(context):
    foeSpot = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@src='me1.gif' and @name='space02']")))
    foeImage = foeSpot.get_attribute("src")
    
    assert "me1.gif" in foeImage


@then(u'make sure your piece is taken')
def step_impl(context):

    myPieces = browser.find_elements(By.XPATH, "//img[@src='you1.gif']")
    assert len(myPieces) == 11
    browser.get_screenshot_as_file('./screenshots/05-computer-takes-my-piece.png')


@then(u'start a new game')
def step_impl(context):
    restartLink = browser.find_element(By.LINK_TEXT, "Restart...")
    restartLink.click()

    message = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "message")))

    assert "Select an orange piece to move." in message.text
    browser.get_screenshot_as_file('./screenshots/06-brand-new-game.png')

    driver.closeBrowser(browser)
