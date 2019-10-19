import numpy as np

def log(base: float, n: float):
    x = 1.0
    best_loss = 1_000_000.0

    for _ in range(100_000):
        random_adj = np.random.normal()
        x += random_adj
        new_loss = ((base ** x) - n) ** 2

        if new_loss < best_loss:
            best_loss = new_loss
        else:
            x -= random_adj
    return x


print(calculate_log(base=3.0, n=9.0))