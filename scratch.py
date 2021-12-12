board = [
    [(0, 'Jan'), (0, 'Feb'), (0, 'Mar'), (0, 'Apr'),
     (0, 'May'), (0, 'Jun'), (1, None)],
    [(0, 'Jul'), (0, 'Aug'), (0, 'Sep'), (0, 'Oct'),
     (0, 'Nov'), (0, 'Dec'), (1, None)],
    [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)],
    [(0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14)],
    [(0, 15), (0, 16), (0, 17), (0, 18), (0, 19), (0, 20), (0, 21)],
    [(0, 22), (0, 23), (0, 24), (0, 25), (0, 26), (0, 27), (0, 28)],
    [(0, 29), (0, 30), (0, 31), (1, None), (1, None), (1, None), (1, None)],
]

shapes = [
    [
        [1, 1, 1],
        [1, 1, 1],
    ],
    [
        [1, 0, 0],
        [1, 1, 1],
        [0, 0, 1],
    ],
    [
        [1, 1, 1],
        [1, 1, 0],
    ],
    [
        [1, 0],
        [1, 1],
        [0, 1],
        [0, 1],
    ],
    [
        [1, 0],
        [1, 1],
        [0, 1],
        [0, 1],
    ],
    [
        [1, 1],
        [1, 0],
        [1, 1],
    ],
    [
        [1, 0],
        [1, 0],
        [1, 1],
        [1, 0],
    ],
    [
        [1, 0],
        [1, 0],
        [1, 0],
        [1, 1],
    ],
    [
        [1, 0, 0],
        [1, 0, 0],
        [1, 1, 1],
    ],
]


def get_solution(month, day):
    monthDict = {
        "Jan": 0,
        "Feb": 1,
        "Mar": 2,
        "Apr": 3,
        "May": 4,
        "Jun": 5,
        "Jul": 0,
        "Aug": 1,
        "Sep": 2,
        "Oct": 3,
        "Nov": 4,
        "Dec": 5,
    }
    monthInd = 0
    dayInd = 0
    if month == "Jan" or \
            month == "Feb" or \
            month == "Mar" or \
            month == "Apr" or \
            month == "May" or \
            month == "Jun":
        monthInd = 0
    else:
        monthInd = 1

    if day <= 7:
        dayInd = 2
    elif day <= 14:
        dayInd = 3
    elif day <= 21:
        dayInd = 4
    elif day <= 28:
        dayInd = 5
    else:
        dayInd = 6

    solution = board.copy()
    for i, j in enumerate(solution):
        for k, l in enumerate(j):
            temp = list(l)
            temp[0] = 1
            solution[i][k] = tuple(temp)

    temp = list(solution[dayInd][(day % 7) - 1])
    temp[0] = 0
    solution[dayInd][(day % 7) - 1] = tuple(temp)

    temp = list(solution[monthInd][monthDict[month]])
    temp[0] = 0
    solution[monthInd][monthDict[month]] = tuple(temp)

    return solution


sol = get_solution("Dec", 6)


s = [[str(e) for e in row] for row in sol]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))
