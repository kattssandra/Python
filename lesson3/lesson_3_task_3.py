from Address import Address
from Mailing import Mailing

addressone = Address(index ="523", city = "Gomel", street = "Port", house = 17, flat = 2)
addresstwo = Address(index ="475", city = "Minsk", street = "Mark", house = 77, flat = 5)



mail=Mailing(addressone, addresstwo, cost = 5412, track = "999")


# Печать информации об отправлении
print(f"Отправление {mail.track} из {mail.addressone.index}, {mail.addressone.city}, {mail.addressone.street}, {mail.addressone.house} - {mail.addressone.flat} "
      f"в {mail.addresstwo.index}, {mail.addresstwo.city}, {mail.addresstwo.street}, {mail.addresstwo.house} - {mail.addresstwo.flat}. "
      f"Стоимость {mail.cost} рублей")