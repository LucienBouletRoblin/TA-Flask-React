import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from database import db_session
from models.restaurant import Restaurant as RestaurantModel


class Restaurant(SQLAlchemyObjectType):
    class Meta:
        model = RestaurantModel


class Query(graphene.ObjectType):
    restaurants = graphene.List(Restaurant)
    restaurant = graphene.Field(lambda: Restaurant, id=graphene.ID())

    def resolve_restaurant(self, context, id):
        query = Restaurant.get_query(context)
        return query.filter(RestaurantModel.id == id).first()

    def resolve_restaurants(self, info):
        query = Restaurant.get_query(info)  # SQLAlchemy query
        return query.all()


class CreateRestaurant(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        address = graphene.String()
        email = graphene.String()
        user_id = graphene.ID()

    ok = graphene.Boolean()
    restaurant = graphene.Field(lambda: Restaurant)

    # TODO Erreur si un ou plusieurs arguements sont manquants
    def mutate(self, info, name, address, email, user_id):
        restaurant = RestaurantModel(name=name, address=address, email=email, user_id=user_id)
        db_session.add(restaurant)
        db_session.commit()
        ok = True
        return CreateRestaurant(restaurant=restaurant, ok=ok)


class RestaurantMutations(graphene.ObjectType):
    create_restaurant = CreateRestaurant.Field()
