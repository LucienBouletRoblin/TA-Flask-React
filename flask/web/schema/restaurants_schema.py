import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models.restaurant import Restaurant as RestaurantModel
from database import db_session


class Restaurants(SQLAlchemyObjectType):
    class Meta:
        model = RestaurantModel
        interfaces = (graphene.Node,)


# mutation {
#   createRestaurant(name: "abc", email: "hello@abc.com", address: "abd") {
#     restaurant {
#       name,
#       email,
#       address
#     }
#     ok
#   }
# }
#

# Used to Create New restaurant
class CreateRestaurant(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        email = graphene.String()
        address = graphene.String()

    ok = graphene.Boolean()
    restaurant = graphene.Field(lambda: Restaurants)

    def mutate(self, _, name, email, address):
        restaurant = RestaurantModel(name=name, email=email, address=address)
        db_session.add(restaurant)
        db_session.commit()
        ok = True
        return CreateRestaurant(restaurant=restaurant, ok=ok)


# mutation {
#   changeName(name: "dazazeazeaz", email: "hello@abc.com") {
#     restaurant {
#       name,
#       email
#     }
#     ok
#   }
# }
# Used to Change Name
class ChangeName(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        email = graphene.String()

    ok = graphene.Boolean()
    restaurant = graphene.Field(Restaurants)

    def mutate(self, context, email, name):
        query = Restaurants.get_query(context)
        email = email
        name = name
        restaurant = query.filter(RestaurantModel.email == email).first()
        restaurant.name = name
        db_session.commit()
        ok = True

        return ChangeName(restaurant=restaurant, ok=ok)


# {
#   findRestaurant(name: "abc") {
#     id,
#     name,
#     email
#   }
#
#   allRestaurants {
#     edges {
#       node {
#         name,
#         email,
#         address
#       }
#     }
#   }
# }

class Query(graphene.ObjectType):
    restaurant = SQLAlchemyConnectionField(Restaurants)
    find_restaurant = graphene.Field(lambda: Restaurants, name=graphene.String())
    all_restaurants = SQLAlchemyConnectionField(Restaurants)

    def resolve_find_restaurant(self, context, name):
        query = Restaurants.get_query(context)
        name = name
        # you can also use and_ with filter() eg: filter(and_(param1, param2)).first()
        return query.filter(RestaurantModel.name == name).first()


class MyMutations(graphene.ObjectType):
    create_restaurant = CreateRestaurant.Field()
    change_name = ChangeName.Field()


restaurants_schema = graphene.Schema(query=Query, mutation=MyMutations)
