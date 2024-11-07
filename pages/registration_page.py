from selene import browser, have, command

from tests.resources import util


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.state = browser.element('#state')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.user_number = browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all('.custom-checkbox')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.city = browser.element('#city')
        # self.submit = browser.element('button#submit')

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=3).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def fill_gender(self, param):
        self.gender.element_by(have.value(param)).element('..').click()

    def fill_mobile_number(self, value):
        self.user_number.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self, value):
        self.subjects.type(value).press_enter()
        return self

    def fill_hobbies(self, value):
        self.hobbies.element_by(have.exact_text(value)).click()
        return self

    def fill_picture(self, value):
        self.picture.set_value(util.path(value))
        return self

    def fill_address(self, value):
        self.address.type(value)
        return self

    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_city(self, name):
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self


    def should_have_registered(self, full_name, email, gender, mobile_number, date_of_birth, subjects, hobbies, picture, address, state_city):
        browser.element('.modal-content').element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile_number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                address,
                state_city
            )
        )
        return self






