import requests

class EmployeeApi:
    # Инициализация 
    def __init__(self, url) -> None:
        self.url = url

    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
            }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', json=company, headers=my_headers)
        return resp.json()

    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()

    def get_employee(self,id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json() 

    # Получить список сотрудников для компани 
    def get_employee_list(self, params_to_add=None):
        resp = requests.get(self.url + '/employee', params=params_to_add)
        return resp.json()
    
    # Получить токен авторизации
    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
    # Добавить нового сотрудника:
    def create_employee(self, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive):
        employee = {
            "firstName": firstName,
            "lastName": lastName,
            "middleName": middleName,
            "companyId": companyId,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee',json=employee, headers=my_headers)
        return resp.json()
    
    def edit_employee(self, id, new_email, new_url, new_phone, new_isActive):
        employee = {

           "email": new_email,
           "url":  new_url,
           "phone": new_phone,
           "isActive": new_isActive
           }
        
        my_headers = {"x-client-token": self.get_token()} 
        resp = requests.patch(self.url + '/employee/' + str(id), headers=my_headers, json=employee)
        print(resp.json)
        return resp.json()    
    
    