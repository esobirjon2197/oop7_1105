
# 7-m
class Phone:
    def __init__(self, brand, number):
        self.brand = brand
        self.number = number

    def call(self, person_name):
        print(f"{person_name} ga qo‘ng‘iroq qilinmoqda")


class Tablet:
    def watch_video(self):
        print("Video ko‘rilmoqda")


class User:
    def make_call(self, device, person_name):
        if hasattr(device, "call"):
            device.call(person_name)
        else:
            print("call method topilmadi")


phone = Phone("iPhone", "99890...")
tablet = Tablet()

user = User()
user.make_call(phone, "Vali")

user.make_call(tablet, "Vali")
