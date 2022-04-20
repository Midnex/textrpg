##### Map #####
"""
a1 a2 a3 a4 x = player home
-------------
|  |  |  |  | a4
-------------
|  |X |  |  | b4
-------------
|  |  |  |  | c4
-------------
|  |  |  |  | d4
-------------
"""

zonemap = {
        'a1': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to A1",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': '',
            'South': 'b1',
            'East': '',
            'West': 'a2',
        },
        'a2': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to A2",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': '',
            'South': 'b3',
            'East': 'a1',
            'West': 'a3',
        },
        'a3': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to A3",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': '',
            'South': 'b3',
            'East': 'a3',
            'West': 'a4',
        },
        'a4': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to A4",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': '',
            'South': 'b4',
            'East': 'a4',
            'West': '',
        },
        'b1': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to B1",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': 'a1',
            'South': 'c1',
            'East': '',
            'West': 'b2',
        },
        'b2': {
            'ZONENAME': "",
            'DESCRIPTION': "This is your home.",
            'EXAMINE': "You look around at your wonderful home.",
            'SOLVED': True,
            'North': 'a2',
            'South': 'c2',
            'East': 'b1',
            'West': 'b3'
        },
        'b3': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to B3",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': 'a3',
            'South': 'c3',
            'East': 'b2',
            'West': 'b4',
        },
        'b4': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to B4",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': 'a4',
            'South': 'c4',
            'East': 'b3',
            'West': '',
        },
        'c1': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to C1",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': 'b1',
            'South': 'd1',
            'East': '',
            'West': 'c2',
        },
        'c2': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to C2",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': 'b2',
            'South': 'd2',
            'East': 'c1',
            'West': 'c3',
        },
        'c3': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to C3",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': 'b3',
            'South': 'd3',
            'East': 'c2',
            'West': 'c4',
        },
        'c4': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to C4",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': 'b4',
            'South': 'd4',
            'East': 'c3',
            'West': '',
        },
        'd1': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to D1",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': 'c1',
            'South': '',
            'East': '',
            'West': 'd2',
        },
        'd2': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to D2",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': 'c2',
            'South': '',
            'East': 'd1',
            'West': 'd3',
        },
        'd3': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to D3",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': 'c3',
            'South': '',
            'East': 'd2',
            'West': 'd4',
        },
        'd4': {
            'ZONENAME': "",
            'DESCRIPTION': "Welcome to D4",
            'EXAMINE': "Nothing yet",
            'RIDDLE': '',
            'ANSWER': '',
            'SOLVED': False,
            'North': 'c4',
            'South': '',
            'East': 'd3',
            'West': '',
        }
}