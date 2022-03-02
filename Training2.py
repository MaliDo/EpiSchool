def solve_quadratic(a,b,c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = ((-1 * b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a)
        x2 = ((-1 * b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a)
        return(int(x1), int(x2))
    if d == 0:
        return int((-1 * b / 2 * a))
    if d < 0:
        return None