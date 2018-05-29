# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_query 1'] = {
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
            }
        ]
    }
}
