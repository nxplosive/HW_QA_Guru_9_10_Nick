from selene import have
from pages.registration_page import MidLevelRegPage


def test_reg_form():
    reg_page = MidLevelRegPage()
    reg_page.open()
    # WHEN
    reg_page.fill_first_name('Nikita')
    reg_page.fill_last_name('Safonov')
    reg_page.fill_email('niksaff@gmail.com')
    reg_page.choose_gender('Male')
    reg_page.fill_phone_number('9151232211')
    reg_page.fill_date_of_birth('15', 'December', '1990')
    reg_page.choose_subjects('English', 'Maths')
    reg_page.choose_hobbies('Sports', 'Reading', 'Music')
    reg_page.upload_picture('avatar.jpg')
    reg_page.fill_address('Zombie Land')
    reg_page.choose_state_and_city('NCR', 'Delhi')
    reg_page.submit_form()
    # THEN
    reg_page.check_header('Thanks for submitting the form')
    reg_page.check_user_info(
        'Nikita Safonov',
        'niksaff@gmail.com',
        'Male',
        '9151232211',
        '15 December,1990',
        'English, Maths',
        'Sports, Reading, Music',
        'avatar.jpg',
        'Zombie Land',
        'NCR Delhi')
    reg_page.close_form()