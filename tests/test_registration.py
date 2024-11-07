import time

from data.users import User
from pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()

    daria = User(
        first_name = 'Daria',
        last_name = 'Tomilova',
        email = 'name@example.com',
        gender = 'Female',
        mobile_number = '1234567891',
        date_of_birth = {"year":1999, "month":11,"day":11},
        subjects = 'Computer Science',
        hobbies = 'Reading',
        picture = 'picture.jpg',
        address ='Moscowskaya Street 18',
        state ='NCR',
        city = 'Delhi')

    registration_page.open()
    registration_page.register(daria)
    registration_page.should_have_registered(daria)