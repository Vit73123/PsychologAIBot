class AppointmentDAO:

    def __init__(self, appointment_id: int = None, review: str = None, user_id: int = None):
        self.id = appointment_id
        self.review = review
        self.user_id = user_id

    def __repr__(self):
        return (f"id={self.id} "
                f"review={self.review}")
