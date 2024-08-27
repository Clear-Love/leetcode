def equal(a, b, tolerance=1e-9):
    if a > 180:
        a = 360-a
    if b > 180:
        b = 360-b
    return abs(a - 2*b) < tolerance


for h in range(0, 12):
    for f in range(0, 60):
        for m in range(0, 60):
            mm = m*6
            ff = f*6 + (m/60)
            hh = h*15 + (ff/24)
            if h == 0 and f == 0 and m == 0:
                continue
            if equal(abs(hh-ff), abs(ff - mm)):
                print(f"{h} {f} {m}")