from selene import browser, command, have, command
import os
from selene.core import match


def test_full_complited_form():
    browser.open("/automation-practice-form")
    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Ivanovich")
    browser.element("#userEmail").type("Ivanovich@testmail.com")
    browser.element('#gender-radio-1').perform(command.js.click())
    browser.element("#userNumber").type("7999999999")
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click().element('[value="5"]').click()
    browser.element(".react-datepicker__year-select").click().element('[value="1999"]').click()
    browser.element(".react-datepicker__day--028").click()
    browser.element("#subjectsInput").click().type("Eng").press_enter()
    browser.element("#hobbies-checkbox-1").perform(command.js.click())
    browser.element("#hobbies-checkbox-2").perform(command.js.click())
    browser.element("#uploadPicture").send_keys(os.path.abspath("images.png"))
    browser.element("#currentAddress").type("Test adress, 11/1")
    browser.element("#state").perform(command.js.scroll_into_view).click().element("#react-select-3-option-2").click()
    browser.element("#city").click().element("#react-select-4-option-1").click()
    browser.element("#submit").click()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.all("//div[@class='table-responsive']//td[2]").should(
        have.exact_texts('Ivan Ivanovich', 'Ivanovich@testmail.com', 'Male', '7999999999', '28 June,1999', 'English',
                         'Sports, Reading', 'images.png', 'Test adress, 11/1', 'Haryana Panipat'))


def test_only_required_data():
    browser.open("/automation-practice-form")
    browser.element("#firstName").type("Ivan")
    browser.element("#lastName").type("Ivanovich")
    browser.element('#gender-radio-1').perform(command.js.click())
    browser.element("#userNumber").type("7999999999")
    browser.element("#submit").perform(command.js.scroll_into_view).click()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.all("//div[@class='table-responsive']//td[2]").should(have.exact_texts('Ivan Ivanovich', '', 'Male', '7999999999', '18 February,2025', '', '', '', '', ''))


def test_required_data_not_filled():
    browser.open("/automation-practice-form")
    browser.element("#firstName").type("Ivan")
    browser.element("#userNumber").type("7999999999")
    browser.element("#submit").perform(command.js.scroll_into_view).click()

    browser.element('#example-modal-sizes-title-lg').should(have.no.exact_text('Thanks for submitting the form'))
    # browser.element("#lastName").perform(command.js.scroll_into_view).should(have.attribute('class').value('form-control:invalid'))
    browser.element('#userForm').should(have.attribute('class').value('was-validated'))