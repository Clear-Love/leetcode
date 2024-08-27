import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def distance_point_to_line(x1, y1, x2, y2, x0, y0):
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    distance = abs(A * x0 + B * y0 + C) / math.sqrt(A**2 + B**2)
    if distance == 0:
        return min(dist(x0, y0, x1, y1), dist(x0, y0, x2, y2))
    return distance


t = int(input())
for _ in range(t):
    ax, ay = list(map(int ,input().split()))
    bx, by = list(map(int , input().split()))
    cx, cy = list(map(int , input().split()))
    print(f"{distance_point_to_line(ax, ay, bx, by, cx, cy):.2f}")