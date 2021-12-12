A_orientations = [
    [
        ['A', 'A', 'A'],
        ['A', 'A', 'A'],
    ],
    [
        ['A', 'A'],
        ['A', 'A'],
        ['A', 'A'],
    ],
]
A_illegal = {
    0: [
        (0, 4)
    ]
}

B_orientations = [
    [
        ['B',   None,   None],
        ['B',   'B',    'B'],
        [None,  None,   'B'],
    ],
    [
        [None,  'B',    'B'],
        [None,  'B',    None],
        ['B',   'B',    None],
    ],
    [
        [None,   None,  'B'],
        ['B',   'B',    'B'],
        ['B',   None,   None],
    ],
    [
        ['B',   'B',    None],
        [None,  'B',    None],
        [None,  'B',    'B'],
    ],
]

B_illegal = {
    0: [
        (0, 4),
        (3, 0),
    ],
    1: [
        (0, 0),
        (4, 3)
    ],
    2: [
        (0, 0),
        (0, 4),
        (4, 3)
    ],
    3: [
        (0, 4),
        (3, 0),
        (4, 2),
    ],
}


C_orientations = [
    [
        ['C', 'C', 'C'],
        ['C', 'C', None],
    ],
    [
        ['C', 'C', None],
        ['C', 'C', 'C'],
    ],
    [
        [None, 'C', 'C'],
        ['C', 'C', 'C'],
    ],
    [
        ['C', 'C', 'C'],
        [None, 'C', 'C'],
    ],
    [
        ['C', None],
        ['C', 'C'],
        ['C', 'C'],
    ],
    [
        [None, 'C'],
        ['C', 'C'],
        ['C', 'C'],
    ],
    [
        ['C', 'C'],
        ['C', 'C'],
        [None, 'C'],
    ],
    [
        ['C', 'C'],
        ['C', 'C'],
        ['C', None],
    ],
]

C_illegal = {
    2: [
        (4, 0)
    ],
    3: [
        (4, 0)
    ],
    1: [
        (4, 0)
    ],
}

D_orientations = [
    [
        ['D', None],
        ['D', 'D'],
        [None, 'D'],
        [None, 'D'],
    ],
    [
        [None, 'D'],
        ['D', 'D'],
        ['D', None],
        ['D', None],
    ],
    [
        ['D', None],
        ['D', None],
        ['D', 'D'],
        [None, 'D'],
    ],
    [
        [None, 'D'],
        [None, 'D'],
        ['D', 'D'],
        ['D', None],
    ],
    [
        [None, None, 'D', 'D'],
        ['D', 'D', 'D', None]
    ],
    [
        ['D', 'D', None, None],
        [None, 'D', 'D', 'D']
    ],
    [
        [None, 'D', 'D', 'D'],
        ['D', 'D', None, None]
    ],
    [
        ['D', 'D', 'D', None],
        [None, None, 'D', 'D']
    ],
]

D_illegal = {
    0: [
        (0, 3)
    ],
    1: [
        (5, 2)
    ],
    2: [
        (5, 2)
    ],
    4: [
        (0, 0),
        (0, 4)
    ],
    5: [
        (0, 4),
        (2, 0)
    ],
    6: [
        (3, 4)
    ],
}

E_orientations = [
    [
        ['E',   'E'],
        ['E',   None],
        ['E',   'E'],
    ],
    [
        ['E',   'E',    'E'],
        ['E',   None,   'E'],
    ],
    [
        ['E',   'E'],
        [None,  'E'],
        ['E',   'E'],
    ],
    [
        ['E',   None,   'E'],
        ['E',   'E',    'E'],
    ],
]

E_illegal = {
    3: [
        (0, 4)
    ],
}

F_orientations = [
    [
        ['F',   None],
        ['F',   None],
        ['F',   'F'],
        ['F',   None],
    ],
    [
        ['F',   'F',    'F',    'F'],
        [None,  'F',    None,   None]
    ],
    [
        [None,  'F'],
        ['F',   'F'],
        [None,  'F'],
        [None,  'F'],
    ],
    [
        [None,  None,   'F',    None],
        ['F',   'F',    'F',    'F'],
    ],
    [
        [None,  'F'],
        [None,  'F'],
        ['F',   'F'],
        [None,  'F'],
    ],
    [
        [None,  'F',   None,    None],
        ['F',   'F',    'F',    'F'],
    ],
    [
        ['F',   None],
        ['F',   'F'],
        ['F',   None],
        ['F',   None],
    ],
    [
        ['F',   'F',    'F',    'F'],
        [None,  None,   'F',    None],
    ],
]

F_illegal = {
    0: [
        (4, 0),
        (5, 1),
        (5, 2)
    ],
    1: [
        (0, 5),
        (3, 4)
    ],
    2: [
        (0, 3)
    ],
    3: [
        (0, 4)
    ],
    5: [
        (0, 0),
        (0, 4),
        (2, 0),
    ],
    6: [
        (5, 2)
    ],
    7: [
        (0, 5)
    ],
}


G_orientations = [
    [
        ['G',   None],
        ['G',   None],
        ['G',   None],
        ['G',   'G']
    ],
    [
        [None,  'G'],
        [None,  'G'],
        [None,  'G'],
        ['G',   'G']
    ],
    [
        ['G',   'G'],
        ['G',   None],
        ['G',   None],
        ['G',   None]
    ],
    [
        ['G',   'G'],
        [None,  'G'],
        [None,  'G'],
        [None,  'G']
    ],
    [
        ['G',   'G',    'G',    'G'],
        [None,  None,   None,   'G']
    ],
    [
        ['G',   'G',    'G',    'G'],
        ['G',  None,   None,    None]
    ],
    [
        ['G',  None,   None,   None],
        ['G',   'G',    'G',    'G']
    ],
    [
        [None,  None,   None,   'G'],
        ['G',   'G',    'G',    'G']
    ],
]

G_illegal = {
    0: [
        (5, 1),
        (5, 2)
    ],
    1: [
        (0, 0)
    ],
    2: [
        (5, 2)
    ],
    3: [
        (0, 3),
        (0, 3)
    ],
    5: [
        (0, 5),
        (3, 4),
    ],
    6: [
        (0, 4),
        (2, 0)
    ],
    7: [
        (0, 0),
        (0, 4),
    ],
}


H_orientations = [
    [
        ['H', None, None],
        ['H', None, None],
        ['H', 'H', 'H']
    ],
    [
        ['H', 'H', 'H'],
        ['H', None, None],
        ['H', None, None]
    ],
    [
        ['H', 'H', 'H'],
        [None, None, 'H'],
        [None, None, 'H']
    ],
    [
        [None, None, 'H'],
        [None, None, 'H'],
        ['H', 'H', 'H']
    ],
]

H_illegal = {
    0: [
        (3, 0),
        (4, 0)
    ],
    1: [
        (4, 3)
    ],
    2: [
        (0, 4)
    ],
    3: [
        (0, 0)
    ],
}

pieces_dict = {
    'A': [A_orientations, A_illegal],
    'B': [B_orientations, B_illegal],
    'C': [C_orientations, C_illegal],
    'D': [D_orientations, D_illegal],
    'E': [E_orientations, E_illegal],
    'F': [F_orientations, F_illegal],
    'G': [G_orientations, G_illegal],
    'H': [H_orientations, H_illegal],
}
