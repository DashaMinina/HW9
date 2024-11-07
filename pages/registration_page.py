from selene import browser, have, command

from data.users import User
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
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        return self

    def register(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.gender.element_by(have.value(user.gender)).element('..').click()
        self.user_number.type(user.mobile_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(user.date_of_birth["month"])
        browser.element('.react-datepicker__year-select').type(user.date_of_birth["year"])
        browser.element(f'.react-datepicker__day--0{user.date_of_birth["day"]}:not(.react-datepicker__day--outside-month)').click()
        self.subjects.type(user.subjects).press_enter()
        self.hobbies.element_by(have.exact_text(user.hobbies)).click()
        self.picture.set_value(util.path(user.picture))
        self.address.type(user.address)
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(user.state)
        ).click()
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(user.city)
        ).click()
        browser.element('#submit').perform(command.js.click)



    def should_have_registered(self, user: User):
        birthday_format_mouth = f"{user.date_of_birth['day']} November,{user.date_of_birth['year']}"
        browser.element('.modal-content').element('.table').all('td').even.should(
            have.exact_texts(
                user.first_name + ' ' + user.last_name,
                user.email,
                user.gender,
                user.mobile_number,
                birthday_format_mouth,
                user.subjects,
                user.hobbies,
                user.picture,
                user.address,
                user.state + ' ' + user.city
            )
        )
        return self






