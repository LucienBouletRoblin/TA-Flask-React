import logging
import uuid
from pytest import raises

from graphene.test import Client
from graphql.error.located_error import GraphQLLocatedError, GraphQLError

from general_schema import schema

_log = logging.getLogger('custom_logger')

client = Client(schema)


def test_get_restaurants(snapshot):
    query = '''
        query {
            restaurants {
                name,
                email,
                address,
                userId,
                id
            }
        }
    '''
    query_result = client.execute(query)
    assert 'errors' not in query_result
    snapshot.assert_match(query_result)


def test_get_restaurant_by_id(snapshot):
    query = '''
        query {
            restaurant(id:1) {
                id
                name
                email
                address
                userId
                user {
                    lastName
                    firstName
                    email
                }
                __typename
            }
        }
    '''
    query_result = client.execute(query)
    assert 'errors' not in query_result
    snapshot.assert_match(query_result)


def test_create_restaurant_with_all_args(snapshot):
    query = '''
        mutation {
            createRestaurant(name:"azeaze", userId:"1", email:"email@email.email", address:"address test") {
                ok
                restaurant {
                    name
                    email
                    address
                    userId
                    user {
                        lastName
                        firstName
                        email
                    }
                    __typename
                }
            }
        }
    '''
    query_result = client.execute(query)
    assert 'errors' not in query_result
    snapshot.assert_match(query_result)


def test_create_restaurant_with_minimal_args(snapshot):
    query = '''
        mutation {
            createRestaurant(name:"azeaze", userId:"1") {
                ok
                restaurant {
                    id
                    name
                    email
                    address
                    userId
                    user {
                        lastName
                        firstName
                        email
                    }
                    __typename
                }
            }
        }
    '''
    query_result = client.execute(query)
    assert 'errors' not in query_result
    snapshot.assert_match(query_result)


def test_update_restaurant_name(snapshot):
    new_name = str(uuid.uuid4()).replace("-", "")
    query = '''
        mutation {
            updateRestaurant(name:"%s", restaurantId:"1", userId:"1") {
                ok
                restaurant {
                    id
                    name
                    email
                    address
                    userId
                    user {
                        lastName
                        firstName
                        email
                    }
                    __typename
                }
            }
        }
    ''' % new_name
    query_result = client.execute(query)
    assert 'errors' not in query_result
    snapshot.assert_match(query_result)


# def test_update_restaurant_name_with_wrong_user():
#     query = '''
#         mutation {
#             updateRestaurant(name:"lhglhghlg name oh yes", restaurantId:"1", userId:"1654654") {
#                 ok
#                 restaurant {
#                     id
#                     name
#                     email
#                     address
#                     userId
#                     user {
#                         lastName
#                         firstName
#                         email
#                     }
#                     __typename
#                 }
#             }
#         }
#     '''
#     with raises(GraphQLError):
#         client.execute(query)
