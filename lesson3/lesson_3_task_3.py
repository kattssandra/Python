from Address import Address
from Mailing import Mailing

addressone = Address(index:"523", city: "Gomel", street: "Port", house: 17, flat: 2)
addresstwo = Address(index:"475", city: "Minsk", street: "Mark", house: 77, flat: 5)



mail=Mailing(addressone, addresstwo, cost: 5412, track: "999")
print(mail.track, mail.city, mail.street, mail.house, mail.flat)