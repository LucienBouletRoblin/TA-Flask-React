import logging

from graphene.test import Client

from general_schema import schema

log = logging.getLogger('custom_logger')

client = Client(schema)


def test_query(snapshot):
    query = '''
        query {
            restaurants {
                name
                id
            }
        }
    '''
    query_result = client.execute(query)
    assert 'errors' not in query_result
    snapshot.assert_match(query_result)
