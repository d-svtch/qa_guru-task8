from selene import browser, have, command, by
from qa_guru_task8_tests.resources import path


class RegistrationPage:
    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def fill_email(self, param):
        browser.element("#userEmail").type(param)

    def choose_gender(self, selector):
        browser.element(selector).perform(command.js.click())

    def fill_phonenumber(self, number):
        browser.element("#userNumber").type(number)

    def fill_date_of_birth(self, day, month, year):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").click().element(f'[value="{month}"]').click()
        browser.element(".react-datepicker__year-select").click().element(f'[value="{year}"]').click()
        browser.element(f".react-datepicker__day--0{day}").click()

    def choose_subjects(self, subject):
        browser.element("#subjectsInput").click().type(subject).press_enter()

    def choose_hobbies(self, selector_1, selector_2):
        browser.element(f"#hobbies-checkbox-{selector_1}").perform(command.js.click())
        browser.element(f"#hobbies-checkbox-{selector_2}").perform(command.js.click())

    def upload_picture(self, file_name):
        browser.element("#uploadPicture").send_keys(path(file_name))

    def input_current_address(self, address):
        browser.element("#currentAddress").type(address)

    def scroll(self, destitation):
        browser.element(destitation).perform(command.js.scroll_into_view)

    def state_select(self, state):
        browser.element('#state').click().element(by.text(state)).click()

    def city_select(self, city):
        browser.element('#city').click().element(by.text(city)).click()

    def submit(self):
        browser.element("#submit").click()

    def filled_form_validation(self,
                               full_name,
                               email,
                               gender,
                               phone,
                               date_of_birth,
                               subjects,
                               hobbies,
                               file_name,
                               address,
                               state_and_city
                               ):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
        browser.all("//div[@class='table-responsive']//td[2]").should(
            have.exact_texts(full_name,
                             email,
                             gender,
                             phone,
                             date_of_birth,
                             subjects,
                             hobbies,
                             file_name,
                             address,
                             state_and_city))


