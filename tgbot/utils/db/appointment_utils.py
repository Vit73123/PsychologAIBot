from tgbot.db.dao import AppointmentDAO
from tgbot.db.models import Appointment


def create_appointment_to_dao(appointment: Appointment) -> AppointmentDAO | None:
    if appointment:
        return AppointmentDAO(
            appointment_id=appointment.id,
            review=appointment.review
        )


def create_appointment_from_dao(appointment_dao: AppointmentDAO) -> Appointment | None:
    if appointment_dao:
        appointment = Appointment()
        appointment.id = appointment_dao.id
        appointment.review = appointment_dao.review
        return appointment
