from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    subjects: list
    hobbies: list
    picture: str
    current_address: str
    state: str
    city: str


guest = User(
    first_name='Nikita',
    last_name='Safonov',
    email='nicksaff@gmail.com',
    gender='Male',
    phone_number='9151232211',
    day_of_birth='15', month_of_birth='December', year_of_birth='1990',
    subjects=['English', 'Maths'],
    hobbies=['Sports', 'Reading', 'Music'],
    picture='avatar.jpg',
    current_address='Zombie Land',
    state='NCR', city='Delhi'
)