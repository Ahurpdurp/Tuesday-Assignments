class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print("The restaurant is open!")


restaurant = Restaurant("heheh","haha")
restaurant.describe_restaurant()
restaurant.open_restaurant

class User():
    def __init__(self,first_name, last_name, gender, height, race, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender 
        self.height = height
        self.race = race
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f"Name: {self.last_name}, {self.first_name}\nGender: {self.gender}\nHeight: {self.height}\nRace: {self.race}")
    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Jim","Halpert","Male","6 feet","Asian", 0)
user1.describe_user()
user1.greet_user()

user2 = User("Pam","Beesely","Female","5 feet","White", 0)
user2.describe_user()
user2.greet_user()

user3 = User("Fucking","LizardKing","Male","6 feet","White", 0)
user3.describe_user()
user3.greet_user()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
print(user3.login_attempts)
user3.reset_login_attempts()
print(user3.login_attempts)