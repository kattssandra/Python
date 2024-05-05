class User:
	    
	def __init__(self, first_name, last_name):
		#print("я создался")
		self.username1 = first_name
		self.username2 = last_name

	def sayName1(self):
		print("Мое имя ", self.username1)

	def sayName2(self): #создали метод
		print("Моя фамилия ", self.username2) #создали тело метода
		
	def sayName3(self): #создали метод
		print("Меня зовут ", self.username1, self.username2) #создали тело метода


#alex = User("Alex", "Иванов")
#mark = User("Mark", "Петров")
#marta = User("Marta", "Сидоров")

#alex.sayName3()

