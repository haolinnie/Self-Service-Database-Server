from sqlalchemy import func

from api.core import Mixin
from api.models.base import db


class diagnosis_deid(Mixin, db.Model):
    """diagnosis_deid table
    """

    __tablename__ = "diagnosis_deid"
    diagnosis_id = db.Column(db.INT, unique=True, primary_key=True)
    pt_id = db.Column(db.INT, db.ForeignKey("pt_deid.pt_id"))

    diagnosis_code = db.Column(db.VARCHAR, nullable=False)
    diagnosis_code_set = db.Column(db.VARCHAR)
    diagnosis_start_dt = db.Column(db.DateTime)
    diagnosis_end_dt = db.Column(db.DateTime)
    diagnosis_name = db.Column(
        db.VARCHAR
    )  ## This isn't in the sqldbm.com model but is in the sample data

    def __repr__(self):
        return "<diagnosis_deid {!r}, pt_id {!r}>".format(self.diagnosis_id, self.pt_id)

    @staticmethod
    def get_pt_id_by_diagnosis_names(diagnosis_names: list) -> list:
        """Get pt_id by diagnosis_name
        Currently uses OR logic -- consider AND in the future

        :param diagnosis_names <list<str>> list of diagnosis_name
        :returns <list<int>> list of pt_id
        """
        qry = diagnosis_deid.query.with_entities(diagnosis_deid.pt_id).distinct()
        qry = qry.filter(
            func.lower(diagnosis_deid.diagnosis_name).in_(
                [v.lower() for v in diagnosis_names]
            )
        )

        return [v.pt_id for v in qry.all()]
