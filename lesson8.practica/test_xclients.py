import requests
from CompanyApi import CompanyApi

api = CompanyApi("https://x-clients-be.onrender.com")

def test_get_companies():
		body = api.get_company_list()
		assert len(body) > 0 # == x

def test_get_active_companies():
		# Получить список всех компаний
		full_list = api.get_company_list()
		# Получить список активных компаний 
		filtered_list = api.get_company_list(params_to_add={'active' : 'true'})

		# Проверить, что список 1 > списка 2
		assert len(full_list) > len(filtered_list)

def test_add_new():
		#Получить количество компаний
		body = api.get_company_list()
		len_before = len(body)

		#Создать новую компанию
		name = "Autotest"
		descr = "Descr"
		result = api.create_company(name, descr)
		new_id = result['id']

		# Получить кол-во компаний
		body = api.get_company_list()
		len_after = len(body)

		# Проверить, что +1
		assert len_after - len_before == 1

		# Проверить описание и id
		assert body[-1]["name"] == name
		assert body[-1]["description"] == descr
		assert body[-1]["id"] == new_id
		
def test_get_one_company():
		#Создаем компанию
		name = "VS Code"
		descr = "IDE"
		result = api.create_company(name, descr)
		new_id = result["id"]
		#Обращаемся к компании
		new_company = api.get_company(new_id)
		#Проверим id, название, описание и статус новой компании:
		assert new_company["id"] == new_id
		assert new_company["name"] == name
		assert new_company["description"] == descr
		assert new_company["isActive"] == True

def test_edit():
    name = "Company to be edited"
    descr = "Edit me"
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_name = "Updated"
    new_descr = "_upd_"

    edited = api.edit(new_id, new_name, new_descr)
    # Проверяем, что ID у компании тот же
    assert edited["id"] == new_id
    # Проверяем, что название компании поменялось
    assert edited["name"] == new_name
    # Проверяем, что описание компании поменялось
    assert edited["description"] == new_descr
    # Проверяем, что компания осталась активной
    assert edited["isActive"] == True
	
def test_delete():
    name = "Company to be deleted"
    descr = "Delete me"
    result = api.create_company(name, descr)
    new_id = result["id"]

    #Удаляем организацию с новым ID
    edited = api.delete(new_id)
    #Проверяем, что ID последней созданной компании = ID удаленной компании
    assert edited["id"] == new_id
    #Проверяем, что название последней созданной компании = названию удаленной компании
    assert edited["name"] == name
    #Проверяем, что описание пустое
    assert edited["description"] == descr
    #Проверяем, что компания активна
    assert edited["isActive"] == True

    # Проверяем, что ID удаленной компании нет в обновленном списке
    body = api.get_company_list()
    assert body[-1]["id"] != new_id
	
def test_deactivate():
    #Создаем компанию
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]
    #Деактивируем компанию
    body = api.set_active_state(new_id, False)

    #Проверяем, что у компании статус «неактивная»
    assert body["isActive"] == False

def test_deactivate_and_activate_back():
    #Создаем компанию:
    name = "Company to be deactivated"
    result = api.create_company(name)
    new_id = result["id"]
    # Деактивируем компанию с помощью параметра False
    api.set_active_state(new_id, False)
    # Активируем компанию с помощью параметра True
    body = api.set_active_state(new_id, True)
    # Проверяем, что компания активная
    assert body["isActive"] == True