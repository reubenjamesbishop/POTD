with open('log.txt', 'r') as r:
    total = 0
    count = 0
    for l in r:
        count += 1
        s = (l.find('Runtime: '))+9
        e = (l.find(' seconds'))
        total += float(l[s:e])
    print(f"Average time: {total/count} seconds.")
