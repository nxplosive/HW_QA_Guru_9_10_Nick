from demoqa_tests.pages.registration_page import MidLevelRegPage


def test_registration_form():
    reg_page = MidLevelRegPage()
    reg_page.open()

    reg_page.fill_first_name('Nikita')
    reg_page.fill_last_name('Safonov')
    reg_page.fill_email('nicksaff@Gmail.com')
    reg_page.fill_gender()
    reg_page.fill_phone_number('9151232211')
    reg_page.fill_birthday("1990", "December", "15")
    reg_page.fill_subjects('English')
    reg_page.fill_hobbies()
    reg_page.fill_picture('avatar.jpg')
    reg_page.fill_address('Zombie Land')
    reg_page.fill_state('NCR')
    reg_page.fill_city('Noida')
    reg_page.fill_submit()

    reg_page.should_registered_user_with(
        'Nikita Safonov',
        'nicksaff@Gmail.com',
        'Male',
        '9151232211',
        '15 December,1990',
        'English',
        'Sports',
        'avatar.jpg',
        'Zombie Land',
        'NCR Noida',
    )
