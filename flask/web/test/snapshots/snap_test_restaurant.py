# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_restaurants 1'] = {
    'data': {
        'restaurants': [
            {
                'address': 'test1 address',
                'email': 'restaurant@email.com',
                'id': '1',
                'name': 'restaurant1',
                'userId': 1
            },
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
                'name': '0c66db2897cf44709b173a2ab03cc6b7',
                'userId': 1
            }
        ]
    }
}

snapshots['test_get_restaurant_by_id 1'] = {
    'data': {
        'restaurant': {
            '__typename': 'Restaurant',
            'address': 'test1 address',
            'email': 'restaurant@email.com',
            'id': '1',
            'name': 'restaurant1',
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
                'id': '7',
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
                'id': '7',
                'name': '17b98f9c8d66452daac8a2ce02662eae',
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
