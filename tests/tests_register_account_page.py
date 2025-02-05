from pages.register_accaunt_page import RegisterPage


#1. Проверка тайтла на странице Register Account
def test_check_title_register_account(browser):
    RegisterPage(browser).open_url()
    assert 'Register Account' in browser.title

#2. Проверка чекбокса Subscribe на странице Register Account
def test_check_checkbox_subscribe(browser):
    RegisterPage(browser).open_url()
    assert RegisterPage(browser).get_element_checkbox_policy().is_displayed()

#3. Проверка чекбокса 'I have read and agree to the Privacy Policy' на странице Register Account
def test_check_checkbox_privacy_policy(browser):
    RegisterPage(browser).open_url()
    assert RegisterPage(browser).get_element_checkbox_subscribe().is_displayed()

#4. Проверка наличия кнопки Continue на странице Register Account
def test_check_button_continue(browser):
    RegisterPage(browser).open_url()
    assert RegisterPage(browser).get_element_button_continue().is_displayed()
    assert RegisterPage(browser).get_element_button_continue().is_enabled()