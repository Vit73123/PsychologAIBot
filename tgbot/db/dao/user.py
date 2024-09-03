from tgbot.db.models.user import Gender


class UserDAO:

    def __init__(self, user_id: int, name: str = None, gender: Gender = None, age: int = None):
        self.id = user_id
        self.name = name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return (f"id={self.id} "
                f"name={self.name} "
                f"gender={self.gender} "
                f"age={self.age}")
