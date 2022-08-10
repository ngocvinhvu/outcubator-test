import os, random, string
from config import config
from sqlalchemy import DateTime, event
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from models import db
from models.common_model import CommonModel
from models.applicants import Status
from models.common_model import UtcNow


ENV = os.environ.get("ENV", "development")
CONF = config[ENV]


def model_oncreate_listener(mapper, connection, instance):
    instance.processed_dttm = UtcNow()


def generate_key(length):
    letters_and_digits = string.ascii_letters + string.digits
    return "".join((random.choice(letters_and_digits) for i in range(length)))


def check_dob_odd_or_even(dob):
    date = dob.strftime("%d")
    print(date)
    if int(date) % 2 == 0:
        status = Status.processed
    else:
        status = Status.failed
    return status


class Results(CommonModel):
    __tablename__ = "results"

    applicant_status = db.Column(pgEnum(Status), default=Status.pending)
    applicant_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("applicants.id"), nullable=False
    )
    client_key = db.Column(db.String)
    applicant = relationship("Applicants")
    processed_dttm = db.Column(DateTime(), server_default=UtcNow())

    def __init__(self, applicant_id, applicant_status, client_key):
        self.applicant_id = applicant_id
        self.applicant_status = applicant_status
        self.client_key = client_key


event.listen(Results, "before_insert", model_oncreate_listener, propagate=True)
