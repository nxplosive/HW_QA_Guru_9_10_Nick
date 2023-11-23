from selene import browser, have, be, by
import os


def test_reg_from():
    browser.open('/')
    browser.element('').should(be.blank).type('')