class StatusDAO:

    def __init__(self, status_id: int, text: str = None, grade: int = None):
        self.id = status_id
        self.text = text
        self.grade = grade
