from tgbot.db.models.user import Gender


class UserDAO:

    def __init__(self, user_id: int,
                 name: str = None,
                 gender: Gender = None,
                 age: int = None,
                 session_review: str = None,
                 status_text: str = None,
                 status_grade: int = None):
        self.id = user_id
        self.name = name
        self.gender = gender
        self.age = age
        self.session_review = session_review
        self.status_text = status_text
        self.status_grade = status_grade

    def __repr__(self):
        return (f"id={self.id} "
                f"name={self.name} "
                f"gender={self.gender} "
                f"age={self.age} "
                f"session_review={self.session_review} "
                f"status_text={self.status_text }"
                f"status_grad={self.status_grade}")
