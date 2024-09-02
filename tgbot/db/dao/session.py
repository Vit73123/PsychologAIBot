class SessionDAO:

    def __init__(self, session_id: int, review: str = None):
        self.id = session_id
        self.review = review
