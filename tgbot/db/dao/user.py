class UserDAO:

    def __init__(self, user_id: int, name: str = None, gender: str = None, age: int = None):
        self.id = user_id
        self.name = name
        self.gender = gender
        self.age = age
