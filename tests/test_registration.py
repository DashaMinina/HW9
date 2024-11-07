import time

from pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Daria').fill_last_name('Tomilova')
    registration_page.fill_email('name@example.com')
    registration_page.fill_gender('Female')
    registration_page.fill_mobile_number('1234567891')
    registration_page.fill_date_of_birth('1999', 'May', '11')
    registration_page.fill_subjects('Computer Science')
    registration_page.fill_hobbies('Reading')
    registration_page.fill_picture('picture.jpg')
    registration_page.fill_address('Moscowskaya Street 18')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')
    registration_page.submit()

    # THEN
    registration_page.should_have_registered(
        'Daria Tomilova',
        'name@example.com',
        'Female',
        '1234567891',
        '11 May,1999',
        'Computer Science',
        'Reading',
        'picture.jpg',
        'Moscowskaya Street 18',
        'NCR Delhi'
    )