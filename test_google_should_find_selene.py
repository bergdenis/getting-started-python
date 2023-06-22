from selene.support.shared import browser
from selene import be, have, by


def test_google():
    browser.open('https://google.com')
    browser.element(by.css("button#L2AGLb")).click()
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in ...'))


def test_no_results_in_google():
    browser.open('https://google.com')
    # browser.element(by.css("button#L2AGLb")).click()
    browser.element('[name="q"]').should(be.blank).type('n.r.strukturalizovateln.mu').press_enter()
    browser.element('[id="res"]').should(have.text(' - nebyl nalezen žádný odkaz.'))
