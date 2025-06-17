import random
import math


def sphere_function(x):
    return sum(xi ** 2 for xi in x)

# Алгоритм Hill Climbing

def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
   
    n = len(bounds)
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        prev_value = current_value

        neighbor = []
        for j, (lower, upper) in enumerate(bounds):
            step = (upper - lower) * 0.1 
            delta = random.uniform(-step, step)
            xj = current[j] + delta
            xj = max(min(xj, upper), lower)
            neighbor.append(xj)
        neighbor_value = func(neighbor)

        if prev_value - neighbor_value > epsilon:
            current, current_value = neighbor, neighbor_value
            if abs(prev_value - current_value) < epsilon:
                break
        else:
            continue

    return current, current_value

# Алгоритм випадкового локального пошуку

def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):

    n = len(bounds)
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        prev_value = current_value
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)

        if prev_value - candidate_value > epsilon:
            current, current_value = candidate, candidate_value
            if abs(prev_value - current_value) < epsilon:
                break

    return current, current_value

# Алгоритм імітації відпалу

def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):

    n = len(bounds)

    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)
    T = temp

    for _ in range(iterations):
        prev_value = current_value
        neighbor = []
        for j, (lower, upper) in enumerate(bounds):
            step = (upper - lower) * 0.1
            delta = random.uniform(-step, step)
            xj = current[j] + delta
            xj = max(min(xj, upper), lower)
            neighbor.append(xj)
        neighbor_value = func(neighbor)

        delta_val = neighbor_value - current_value
        if delta_val < 0 or random.random() < math.exp(-delta_val / T):
            current, current_value = neighbor, neighbor_value
            if abs(prev_value - current_value) < epsilon:
                break
        T *= cooling_rate
        if T < epsilon:
            break

    return current, current_value


if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
