class User:
    users = []

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.users.append(self)
        self.id = len(self.users) + 1





class Person:

    persons = []

    def __init__(self, name, last_name, gender, date_birth, zodiac_sign,height, weight):
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.date_birth = date_birth
        self.zodiac_sign = zodiac_sign
        self.height = height
        self.weight = weight
        self.persons.append(Person)







if __name__ == '__main__':

    user1 = User('dddddd','ffffff')
    user2 = User('aaaaa', 'fffff')




