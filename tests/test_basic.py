from qa_guru_task8_tests.model import RegistrationPage


def test_full_complited_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Ivanovich')
    registration_page.fill_email("Ivanovich@testmail.com")
    registration_page.choose_gender('#gender-radio-1')
    registration_page.fill_phonenumber("7999999999")
    registration_page.fill_date_of_birth(28, 5, 2005)
    registration_page.choose_subjects("Eng")
    registration_page.choose_hobbies(1, 2)
    registration_page.upload_picture("images.png")
    registration_page.input_current_address("Test adress, 11/1")
    registration_page.scroll("#state")
    registration_page.state_select("Haryana")
    registration_page.city_select("Panipat")
    registration_page.submit()

    registration_page.filled_form_validation('Ivan Ivanovich', 'Ivanovich@testmail.com', 'Male', '7999999999',
                                             '28 June,2005', 'English',
                                             'Sports, Reading', 'images.png', 'Test adress, 11/1', 'Haryana Panipat')


