import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome("C:\QA\chrome\chromedriver.exe")
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    pytest.driver.find_element_by_id('email').send_keys('sveta_egorova@inbox.ru')
    pytest.driver.find_element_by_id('pass').send_keys('Sveta101091')
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

    yield
    pytest.driver.quit()

#Проверка наличия всех питомцев в списке
def test_my_pets():
    element = WebDriverWait(pytest.driver, 5).until(EC.presence_of_element_located(('id','navbarNav')))
    #находим количество питомцев
    my_pets = len(pytest.driver.find_elements_by_xpath('//tbody/tr'))
    my_pets_statistika = pytest.driver.find_element_by_xpath('//*[h2][1]').text.split()
    assert my_pets_statistika[3] == str(my_pets)


#Проверка наличия фото в карточке, хотя бы у половины питомцев
def test_half_pets_have_photo(web_browser):
   WebDriverWait(web_browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//body/div[1]/div/div[1]')))
   number_of_pets = int(web_browser.find_element_by_xpath('//body/div[1]/div/div[1]').text.split()[2])
   WebDriverWait(web_browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//img[@src=""]')))
   number_of_pets_without_photo = len(web_browser.find_elements_by_xpath('//img[@src=""]'))

   assert (number_of_pets / 2) >= number_of_pets_without_photo, "WARNING the number of pets without " \
                                                                "a photo is more than 50%"

#Проверка наличия возраста, имени и породы
def test_names_descr_ages():
    names = pytest.driver.find_elements_by_xpath('//tbody/tr/td[1]')
    poroda = pytest.driver.find_elements_by_xpath('//tbody/tr/td[2]')
    ages = pytest.driver.find_elements_by_xpath('//tbody/tr/td[3]')
    for i in range(len(names)):
        assert names[i].text != ''
        assert poroda[i].text != ''
        assert ages[i].text != ''

#Питомцы не повторяются
def test_repeat_names():
    names = pytest.driver.find_elements_by_xpath('//tbody/tr/td[1]')
    data_names = []
    for name in names:
        name = name.text
        data_names.append(name)
    i = 0
    k = 0
    while i < len(data_names) - 1:
        if data_names[i] == data_names[i + 1]:
            k += 1
        i += 1

    assert k == 0
