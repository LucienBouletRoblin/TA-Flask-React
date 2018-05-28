# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_hero_name_query 1'] = {
    'data': {
        'restaurants': [
            {
                'id': '1',
                'name': 'restaurant1'
            },
            {
                'id': '2',
                'name': 'restaurant2'
            },
            {
                'id': '3',
                'name': 'restaurant3'
            }
        ]
    }
}
