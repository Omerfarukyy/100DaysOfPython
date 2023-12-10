# Learning about oop
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.count = 0


user1 = User(5, "omer")
print(user1.id, user1.name)
