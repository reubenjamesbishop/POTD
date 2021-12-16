with open('log.txt', 'r') as r:
    total = 0
    count = 0
    longest_runtime = 0
    date_time = ("", 0)

    for l in r:
        count += 1
        s = (l.find('Runtime: '))+9
        e = (l.find(' seconds'))
        d = (l.find('date ')+5)
        de = (l.find('No. i'))

        total += float(l[s:e])
        if longest_runtime < float(l[s:e]):
            longest_runtime = float(l[s:e])
            date = l[d:de]

    # print(count)
    print(f"Average time: {total/count} seconds. Total time: {total} seconds.")
    print(
        f"Longest runtime: {longest_runtime} seconds. Date: {date}")
