import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.attendance_per_period import AttendancePerPeriod as AttendancePerPeriodModel


class AttendancePerPeriod(SQLAlchemyObjectType):
    class Meta:
        model = AttendancePerPeriodModel


class Query(graphene.ObjectType):
    attendance_per_periods = graphene.List(AttendancePerPeriod)
    attendance_per_period = graphene.Field(lambda: AttendancePerPeriod, id=graphene.ID())

    def resolve_attendance_per_period(self, context, id):
        query = AttendancePerPeriod.get_query(context)
        return query.filter(AttendancePerPeriodModel.id == id).first()

    def resolve_attendance_per_periods(self, info):
        query = AttendancePerPeriod.get_query(info)  # SQLAlchemy query
        return query.all()
