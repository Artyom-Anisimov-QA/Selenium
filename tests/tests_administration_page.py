from pages.administration_page import AdminPage


#1. Проверка наличия инпута Username на странице Administration
def test_check_input_username_admin_page(browser):
    AdminPage(browser).open_url()
    input_username = AdminPage(browser).find(AdminPage.LOGIN)
    assert input_username.is_displayed()
    assert input_username.get_attribute('name') == 'username'

#2. Проверка наличия элемента Username на странице Administration
def test_check_element_username_admin_page(browser):
    AdminPage(browser).open_url()
    element_username = AdminPage(browser).find(AdminPage.USERNAME)
    assert element_username.is_displayed()
    assert element_username.text == 'Username'

#4. Проверка наличия инпута Password на странице Administration
def test_check_input_password_admin_page(browser, base_url):
    AdminPage(browser).open_url()
    input_password = AdminPage(browser).find(AdminPage.PASSWD)
    assert input_password.is_displayed()
    assert input_password.get_attribute('name') == 'password'

#5. Проверка наличия элемента Password на странице Administration
def test_check_element_password_admin_page(browser, base_url):
    AdminPage(browser).open_url()
    element_username = AdminPage(browser).find(AdminPage.PASSWORD_ELEM)
    assert element_username.is_displayed()
    assert element_username.text == 'Password'