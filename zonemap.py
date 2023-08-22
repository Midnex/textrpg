#### TODO: rework this into a class ####
# class Zone:
# def __init__(
#    self,
#   name: str = "",
#    desc: str = "",
#    look: str = "",
#    n: str | None = None,
#    s: str | None = None,
#    e: str | None = None,
#    w: str | None = None),

# zonemap = {
#    "a1": Zone("Library", "Erast Library", "You see a librarian.", s="b1",w="a2")
# }
###

""" make n, s, e, w point to other zone objects
to traverse node tree"""

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
        'ZoneName': "Library",
        'Description': "Erast Library",
        'Look': "You see a librarian.",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': '',
        's': 'b1',
        'e': '',
        'w': 'a2',
    },
    'a2': {
        'ZoneName': "",
        'Description': "Welcome to A2",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': '',
        's': 'b3',
        'e': 'a1',
        'w': 'a3',
    },
    'a3': {
        'ZoneName': "",
        'Description': "Welcome to A3",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': '',
        's': 'b3',
        'e': 'a3',
        'w': 'a4',
    },
    'a4': {
        'ZoneName': "",
        'Description': "Welcome to A4",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': '',
        's': 'b4',
        'e': 'a4',
        'w': '',
    },
    'b1': {
        'ZoneName': "",
        'Description': "Welcome to B1",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': 'a1',
        's': 'c1',
        'e': '',
        'w': 'b2',
    },
    'b2': {
        'ZoneName': "",
        'Description': "This is your home.",
        'Look': "You look around at your wonderful home.",
        'Solved': True,
        'n': 'a2',
        's': 'c2',
        'e': 'b1',
        'w': 'b3'
    },
    'b3': {
        'ZoneName': "",
        'Description': "Welcome to B3",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': 'a3',
        's': 'c3',
        'e': 'b2',
        'w': 'b4',
    },
    'b4': {
        'ZoneName': "",
        'Description': "Welcome to B4",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': 'a4',
        's': 'c4',
        'e': 'b3',
        'w': '',
    },
    'c1': {
        'ZoneName': "",
        'Description': "Welcome to C1",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': 'b1',
        's': 'd1',
        'e': '',
        'w': 'c2',
    },
    'c2': {
        'ZoneName': "",
        'Description': "Welcome to C2",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': 'b2',
        's': 'd2',
        'e': 'c1',
        'w': 'c3',
    },
    'c3': {
        'ZoneName': "",
        'Description': "Welcome to C3",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': 'b3',
        's': 'd3',
        'e': 'c2',
        'w': 'c4',
    },
    'c4': {
        'ZoneName': "",
        'Description': "Welcome to C4",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': 'b4',
        's': 'd4',
        'e': 'c3',
        'w': '',
    },
    'd1': {
        'ZoneName': "",
        'Description': "Welcome to D1",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': 'c1',
        's': '',
        'e': '',
        'w': 'd2',
    },
    'd2': {
        'ZoneName': "",
        'Description': "Welcome to D2",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': 'c2',
        's': '',
        'e': 'd1',
        'w': 'd3',
    },
    'd3': {
        'ZoneName': "",
        'Description': "Welcome to D3",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': 'c3',
        's': '',
        'e': 'd2',
        'w': 'd4',
    },
    'd4': {
        'ZoneName': "",
        'Description': "Welcome to D4",
        'Look': "Nothing yet",
        'Riddle': '',
        'Answer': '',
        'Solved': False,
        'n': 'c4',
        's': '',
        'e': 'd3',
        'w': '',
    }
}
