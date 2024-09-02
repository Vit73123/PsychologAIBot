class SessionDAO:

    def __init__(self, session_id: int, review: str = None):
        self.id = session_id
        self.review = review

    def __repr__(self):
        return (f"id={self.id} "
                f"review={self.review}")
