from selene import browser, be, have, command
from paths import path

class MidLevelRegPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).with_(type_by_js=True).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).with_(type_by_js=True).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).with_(type_by_js=True).type(value)

    def choose_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_phone_number(self, value):
        browser.element('#userNumber').should(be.blank).with_(type_by_js=True).type(value)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def choose_subjects(self, subj1, subj2):
        browser.element('#subjectsContainer').click()
        browser.element('#subjectsInput').type(subj1).press_enter()
        browser.element('#subjectsInput').type(subj2).press_enter()

    def choose_hobbies(self, hobbie1, hobbie2, hobbie3):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobbie1)).click()
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobbie2)).click()
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobbie3)).click()

    def upload_picture(self, value):
        browser.element("#uploadPicture").set_value(path.path(value))

    def fill_address(self, value):
        browser.element('#currentAddress').should(be.blank).with_(type_by_js=True).type(value)

    def choose_state_and_city(self, state, city):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(city)).click()

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)

    def check_header(self, value):
        browser.element('.modal-header').should(have.text(value))

    def check_user_info(self,
                        full_name,
                        email,
                        gender,
                        mobile_number,
                        date_of_birth,
                        subjects,
                        hobbies,
                        picture,
                        current_address,
                        state_and_city):
        browser.element('.table-responsive').all('td').even.should(
            have.exact_texts(full_name,
                        email,
                        gender,
                        mobile_number,
                        date_of_birth,
                        subjects,
                        hobbies,
                        picture,
                        current_address,
                        state_and_city))

    def close_form(self):
        browser.element('#closeLargeModal').perform(command.js.scroll_into_view).click()
