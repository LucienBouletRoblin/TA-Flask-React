import logging

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from database import db_session
from models.restaurant import Restaurant as RestaurantModel

log = logging.getLogger('custom_logger')


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

    def mutate(self, info, name, user_id, address=None, email=None):
        restaurant = RestaurantModel(name=name, address=address, email=email, user_id=user_id)
        db_session.add(restaurant)
        db_session.commit()
        ok = True
        return CreateRestaurant(restaurant=restaurant, ok=ok)


class UpdateRestaurant(graphene.Mutation):
    class Arguments:
        restaurant_id = graphene.ID()
        name = graphene.String()
        address = graphene.String()
        email = graphene.String()
        user_id = graphene.ID()

    ok = graphene.Boolean()
    restaurant = graphene.Field(lambda: Restaurant)

    def mutate(self, info, restaurant_id, name, user_id, address=None, email=None):
        restaurant = RestaurantModel.query.get(restaurant_id)
        if restaurant.user_id == int(user_id):
            restaurant.name, restaurant.address, restaurant.email = name, address, email
            db_session.commit()
            ok = True
            return UpdateRestaurant(restaurant=restaurant, ok=ok)
        return False


class RestaurantMutations(graphene.ObjectType):
    create_restaurant = CreateRestaurant.Field()
    update_restaurant = UpdateRestaurant.Field()
