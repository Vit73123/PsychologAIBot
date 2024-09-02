class StatusDAO:

    def __init__(self, status_id: int, text: str = None, grade: int = None, user_id: int = None):
        self.id = status_id
        self.text = text
        self.grade = grade
        self.user_id = user_id

    def __repr__(self):
        return (f"id={self.id} "
                f"text={self.text} "
                f"grade={self.grade} "
                f"user_id={self.user_id}")
