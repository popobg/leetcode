# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climb_stairs(n: int) -> int:
    if n == 0:
        return 0

    elif n == 1:
        return 1

    a = 1
    b = 1
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
        # b, a = a + b, b

    return b

print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(4))
print(climb_stairs(5))
print(climb_stairs(6))
print(climb_stairs(18))
print(climb_stairs(45))