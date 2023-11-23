from selene import browser, have, be, by
import os.path


def test_reg_from():
    browser.open('/')

    #Enter data
    browser.element('.pattern-backgound').should(have.exact_text('Practice Form'))

    browser.element('#firstName').should(be.blank).type('Nikitron')
    browser.element('#lastName').should(be.blank).type('Safronoffskikh')
    browser.element('#userEmail').should(be.blank).type('niksaff@gmail.com')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').should(be.blank).type('9151232211')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').type('1988').press_enter()
    browser.element('.react-datepicker__month-select').type('December').press_enter()
    browser.element('.react-datepicker__day--015').click()

    browser.element('#subjectsInput').should(be.blank).type('English').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('picture/avatar.jpg'))

    browser.element('#currentAddress').should(be.blank).type('Morder, Zombie street, 666')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()

    #Check
    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text(
        'Nikitron Safronoffskikh' and
        'niksaff@gmail.com' and
        'Male' and
        '9151232211' and
        '15 December,1988' and
        'English' and
        'Music' and
        'avatar.jpg' and
        'Morder, Zombie street, 666' and
        'NCR Delhi'
    ))
    #Bye
    browser.element('#closeLargeModal').press_enter()

