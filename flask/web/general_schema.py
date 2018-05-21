import graphene

from schema.restaurants_schema import Query as RestaurantQuery, Mutations as RestaurantMutations
from schema.user_schema import Query as UserQuery


class Query(RestaurantQuery, UserQuery, graphene.ObjectType):
    pass


class Mutation(RestaurantMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
