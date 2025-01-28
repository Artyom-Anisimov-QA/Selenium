from pages.catalog_page import CatalogPage

# 1. Проверка наличия элемента счётчик в каталоге
def test_check_element_counter(browser):
    CatalogPage(browser).open_url()
    element = CatalogPage(browser).get_element_counter()
    assert element.is_displayed()

# 2. Проверка открытия дропдауна Show с выбором отображаемых элементов на странице.
def test_check_dropdown_show(browser):
    CatalogPage(browser).open_url()
    CatalogPage(browser).get_element_dropdown_show().click()
    CatalogPage(browser).check_values_in_show()

# 3. Проверка открытия дропдауна Show с выбором отображаемых элементов на странице.
def test_check_dropdown_sort_by(browser):
    CatalogPage(browser).open_url()
    CatalogPage(browser).get_element_default().click()
    CatalogPage(browser).check_values_in_sort_by()

# 4. Проверка элементов в <div class="list-group mb-3">
def test_check_div(browser):
    CatalogPage(browser).open_url()
    CatalogPage(browser).check_list_group_item()

# 5. Проверка наличия кнопки grid в каталоге
def test_check_button_grid(browser):
    CatalogPage(browser).open_url()
    assert CatalogPage(browser).get_button_grid().is_displayed()