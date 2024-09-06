class AppointmentDAO:

    def __init__(self, appointment_id: int, review: str = None):
        self.id = appointment_id
        self.review = review

    def __repr__(self):
        return (f"id={self.id} "
                f"review={self.review}")
