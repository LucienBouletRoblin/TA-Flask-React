import logging

from graphene.test import Client

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
    query = '''
        mutation {
            updateRestaurant(name:"updated name oh yes", restaurantId:"1", userId:"1") {
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

def test_update_restaurant_name_with_wrong_user(snapshot):
    query = '''
        mutation {
            updateRestaurant(name:"updated name oh yes", restaurantId:"1", userId:"1654654") {
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
    assert query_result['data']['updateRestaurant']['ok'] is None
    assert query_result['data']['updateRestaurant']['restaurant'] is None
    snapshot.assert_match(query_result)
