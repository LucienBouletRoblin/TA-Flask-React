import graphene

from schema.restaurants_schema import Query as RestaurantQuery
from schema.user_schema import Query as UserQuery, UserMutations
from schema.serving_period_schema import Query as ServingPeriodQuery
from schema.attendance_per_period_schema import Query as AttendancePerPeriodQuery


class Query(RestaurantQuery, UserQuery, ServingPeriodQuery, AttendancePerPeriodQuery, graphene.ObjectType):
    pass


class Mutation(UserMutations, graphene.ObjectType):
     pass


schema = graphene.Schema(query=Query, mutation=Mutation)
