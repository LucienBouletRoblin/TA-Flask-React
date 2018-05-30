# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_restaurants 1'] = {
    'data': {
        'restaurants': [
            {
                'address': 'test2 address',
                'email': 'restaurant2@email.com',
                'id': '2',
                'name': 'restaurant2',
                'userId': 1
            },
            {
                'address': 'test3 address',
                'email': 'restaurant3@email.com',
                'id': '3',
                'name': 'restaurant3',
                'userId': 2
            },
            {
                'address': 'address test',
                'email': 'email@email.email',
                'id': '4',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': None,
                'email': None,
                'id': '5',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': None,
                'email': None,
                'id': '1',
                'name': 'updated name oh yes',
                'userId': 1
            },
            {
                'address': 'address test',
                'email': 'email@email.email',
                'id': '6',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': None,
                'email': None,
                'id': '7',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': 'address test',
                'email': 'email@email.email',
                'id': '8',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': None,
                'email': None,
                'id': '9',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': 'address test',
                'email': 'email@email.email',
                'id': '10',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': None,
                'email': None,
                'id': '11',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': 'address test',
                'email': 'email@email.email',
                'id': '12',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': None,
                'email': None,
                'id': '13',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': 'address test',
                'email': 'email@email.email',
                'id': '14',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': None,
                'email': None,
                'id': '15',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': 'address test',
                'email': 'email@email.email',
                'id': '16',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': None,
                'email': None,
                'id': '17',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': 'address test',
                'email': 'email@email.email',
                'id': '18',
                'name': 'azeaze',
                'userId': 1
            },
            {
                'address': None,
                'email': None,
                'id': '19',
                'name': 'azeaze',
                'userId': 1
            }
        ]
    }
}

snapshots['test_get_restaurant_by_id 1'] = {
    'data': {
        'restaurant': {
            '__typename': 'Restaurant',
            'address': None,
            'email': None,
            'id': '1',
            'name': 'updated name oh yes',
            'user': {
                'email': 'aze@aze.aze',
                'firstName': 'aze',
                'lastName': 'aze'
            },
            'userId': 1
        }
    }
}

snapshots['test_create_restaurant_with_all_args 1'] = {
    'data': {
        'createRestaurant': {
            'ok': True,
            'restaurant': {
                '__typename': 'Restaurant',
                'address': 'address test',
                'email': 'email@email.email',
                'name': 'azeaze',
                'user': {
                    'email': 'aze@aze.aze',
                    'firstName': 'aze',
                    'lastName': 'aze'
                },
                'userId': 1
            }
        }
    }
}

snapshots['test_create_restaurant_with_minimal_args 1'] = {
    'data': {
        'createRestaurant': {
            'ok': True,
            'restaurant': {
                '__typename': 'Restaurant',
                'address': None,
                'email': None,
                'id': '21',
                'name': 'azeaze',
                'user': {
                    'email': 'aze@aze.aze',
                    'firstName': 'aze',
                    'lastName': 'aze'
                },
                'userId': 1
            }
        }
    }
}

snapshots['test_update_restaurant_name 1'] = {
    'data': {
        'updateRestaurant': {
            'ok': True,
            'restaurant': {
                '__typename': 'Restaurant',
                'address': None,
                'email': None,
                'id': '1',
                'name': 'updated name oh yes',
                'user': {
                    'email': 'aze@aze.aze',
                    'firstName': 'aze',
                    'lastName': 'aze'
                },
                'userId': 1
            }
        }
    }
}

snapshots['test_update_restaurant_name_with_wrong_user 1'] = {
    'data': {
        'updateRestaurant': {
            'ok': None,
            'restaurant': None
        }
    }
}
