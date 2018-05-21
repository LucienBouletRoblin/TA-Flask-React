import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.restaurant import Restaurant as RestaurantModel


class Restaurant(SQLAlchemyObjectType):
    class Meta:
        model = RestaurantModel


class Query(graphene.ObjectType):
    restaurants = graphene.List(Restaurant)
    restaurant = graphene.Field(lambda: Restaurant, id=graphene.Int())

    def resolve_restaurant(self, context, id):
        query = Restaurant.get_query(context)
        return query.filter(RestaurantModel.id == id).first()

    def resolve_restaurants(self, info):
        query = Restaurant.get_query(info)  # SQLAlchemy query
        return query.all()
