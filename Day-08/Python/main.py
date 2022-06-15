numbers = list(map(int, input().split()))

scan = 0
def sum_meta_val():
    global scan
    num = numbers[scan]
    scan += 1
    meta = numbers[scan]
    scan += 1
    s, v = 0, []
    while len(v) != num:
        ds, nv = sum_meta_val()
        s += ds
        v.append(nv)
    scan += meta
    val, s2 = 0, 0
    for m in numbers[scan-meta:scan]:
        s2 += m
        try:    val += v[m - 1]
        except: pass
    return s + s2, (val if num else s2)

m, v = sum_meta_val()
print('Part 1:', m)
print('Part 2:', v)