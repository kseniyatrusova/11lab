class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print(" Название ресторана: ",self.restaurant_name,"\n Тип кухни:  ", self.cuisine_type)
    def open_restaurant(self):
        print(" Ресторан открыт")

r1 = Restaurant("KFC","Испанская")
r2 = Restaurant("Бургер Кинг","Китайская")
r3 = Restaurant("Сабвей","Домашняя")

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()
