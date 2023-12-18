from selene import browser, have, be, by
from selene.support.shared.jquery_style import s

from qaguru_tests.controls import resource
from qaguru_tests.data.users import User, guest


class HighLevelRegPage:
    def __init__(self):
        self.first_name = s('#firstName')
        self.last_name = s('#lastName')
        self.user_email = s('#userEmail')
        self.user_gender = s('#gender-radio-1')
        self.user_phone_number = s('#userNumber')
        self.user_birthday = s('#dateOfBirthInput')
        self.month = s('.react-datepicker__month-select')
        self.year = s('.react-datepicker__year-select')
        self.day = s(f'.react-datepicker__day--0{guest.day}')
        self.user_subject = s('#subjectsInput')
        self.user_hobby = s('[for="hobbies-checkbox-1"]')
        self.user_picture = s('#uploadPicture')
        self.user_current_address = s('#currentAddress')
        self.user_state = s('#react-select-3-input')
        self.user_city = s('#react-select-4-input')
        self.submit = s('#submit')

    def open(self):
        browser.open('/automation-practice-form')
        s('.pattern-backgound').should(have.exact_text('Practice Form'))
        return self

    def should_registered_user_with(self, user):
        s('.table-responsive').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.user_email,
                user.user_gender,
                user.user_phone_number,
                f'{user.day} {user.month},{user.year}',
                user.user_subject,
                user.user_hobby,
                user.user_picture,
                user.user_current_address,
                f'{user.user_state} {user.user_city}',
            )
        )
        return self

    def register(self, user: User):
        self.open()
        self.first_name.should(be.blank).type(user.first_name)
        self.last_name.should(be.blank).type(user.last_name)
        self.user_email.should(be.blank).type(user.user_email)
        self.user_gender.double_click()
        self.user_phone_number.type(user.user_phone_number)
        self.user_birthday.click()
        self.month.click().element(by.text(user.month)).click()
        self.year.click().element(by.text(user.year)).click()
        self.day.click()
        self.user_subject.should(be.blank).type(user.user_subject).press_enter()
        self.user_hobby.click()
        self.user_picture.send_keys(resource.path(user.user_picture))
        self.user_current_address.should(be.blank).type(user.user_current_address)
        self.user_state.should(be.blank).type(user.user_state).press_enter()
        self.user_city.should(be.blank).type(user.user_city).press_enter()
        self.submit.press_enter()
