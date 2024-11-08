from selene import browser, be, have

def test_valid_login():
    browser.open('https://school.qa.guru')
    browser.element('[name="email"]').type('bazaleev.roma@ya.ru')
    browser.element('[name="password"]').type('3953558232r').press_enter()

    browser.element('.page-header').should(have.text('Список тренингов'))