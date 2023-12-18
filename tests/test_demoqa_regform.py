from data import users
from pages.registration_page import RegistrationPage


def test_reg_page():
    reg_page = RegistrationPage()
    reg_page.open()
    # WHEN
    reg_page.user_registration(users.guest)
    # THEN
    reg_page.assert_user_info(
        'Nikita Safonov', 'nicksaff@gmail.com', 'Male', '9151232211',
        '15 December,1990', 'English, Maths', 'Sports, Reading, Music', 'avatar.jpg',
        'Zombie Land', 'NCR Delhi'
    )
    reg_page.close_modal_window()