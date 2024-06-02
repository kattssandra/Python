import requests
import json
from Employee import EmployeeApi

api = EmployeeApi("https://x-clients-be.onrender.com")

def test_get_employee_list():
	body = api.get_employee_list()
	assert len(body) > 0 # == x

def test_add_new():
    name = "QA"
    descr = "тестировщик"
    result = api.create_company(name, descr)
    new_id = result["id"]
    
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    
    body = api.get_employees_list(companyId)
    len_before = len(body)
	
	#Создать нового сотрудника
    firstName = "Екатерина"
    lastName = "Аверьянова"
    middleName = "Петровна"
    companyId = 777
    email = "flay86@yandex.by"
    url = "dgfdbhfdzH"
    phone = "123456789"
    birthdate = "07.09.1986"
    isActive= True
    new_employee = api.create_employee(id, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]

    body = api.get_employees_list(companyId) 
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "Екатерина"
    assert body[-1]["lastName"] == "Аверьянова"
    assert body[-1]["middleName"] == "Петровна"
    assert body[-1]["email"] == "flay86@yandex.by"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "89991234567"
    assert body[-1]["birthdate"] == "07.09.1986"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id
    
# Получить сотрудника по id
def test_get_employees_id():
    name = "Yoga"
    descr = "Йогатерапия"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
  
    new_company = api.get_company(new_id)
    companyId = new_company['id']
   
    body = api.get_employees_list(companyId)
    begin_list = len(body) 
   
    firstName = "Катя"
    lastName = "Аверьянова"
    middleName = "Петровна"
    company = companyId
    email = "flay777@yandex.ru"
    url = "string"
    phone = "12347856"
    birthdate = "07/09/1986"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
   
    body = api.get_employee_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1
 
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    assert body[-1]["firstName"] == "Катя"
    assert body[-1]["lastName"] ==  "Аверьянова"
    assert body[-1]["middleName"] == "Петровна"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] ==  "12347856"
    assert body[-1]["birthdate"] == "07/09/1986"
    assert body[-1]["isActive"] == True
    assert body[-1]["id"] == emp_id
    
# Изменить информацию о сотруднике
def test_patch_employee():
    name = "Всегда ДА"
    descr = "Обувь для йогов"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]
    
    new_company = api.get_company(new_id)
    companyId = new_company["id"]
    
    firstName = "Иван"
    lastName = "Иванов"
    middleName = "Петрович"
    company = companyId
    email = "gggg789@mail.ru"
    url = "string"
    phone = "12589632"
    birthdate = "01/02/2012"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = new_employee["id"]
   
    body = api.get_employee_list(companyId) 
   
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]

    new_email = "785u@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated123"
    new_isActive = False
    edited = api.edit_employee(employee_id, new_email, new_url, new_phone, new_isActive)
    assert edited["email"] == "785u@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] == False