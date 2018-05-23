import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.serving_period import ServingPeriod as ServingPeriodModel


class ServingPeriod(SQLAlchemyObjectType):
    class Meta:
        model = ServingPeriodModel


class Query(graphene.ObjectType):
    serving_periods = graphene.List(ServingPeriod)
    serving_period = graphene.Field(lambda: ServingPeriod, id=graphene.ID())

    def resolve_serving_period(self, context, id):
        query = ServingPeriod.get_query(context)
        return query.filter(ServingPeriodModel.id == id).first()

    def resolve_serving_periods(self, info):
        query = ServingPeriod.get_query(info)  # SQLAlchemy query
        return query.all()
