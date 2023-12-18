import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    user_gender: str
    user_phone_number: str
    month: str
    year: str
    day: str
    user_subject: str
    user_hobby: str
    user_picture: str
    user_current_address: str
    user_state: str
    user_city: str


guest = User(
    first_name='Nikita',
    last_name='Safonov',
    user_email='nicksaff@gmail.com',
    user_gender='Male',
    user_phone_number='9151232211',
    month='December',
    year='1990',
    day='15',
    user_subject='English',
    user_hobby='Sports',
    user_picture='avatar.jpg',
    user_current_address='Zombie Land',
    user_state='NCR',
    user_city='Noida',
)
