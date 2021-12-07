#!/usr/bin/env python3

input_data = []
with open('input.txt', 'r', encoding="utf-8") as f:
    input_data = f.read().splitlines()

crabs = [int(x) for x in input_data.pop(0).split(",")]
max_crabs = max(crabs)
min_crabs = min(crabs)

def moving_cost(series, target):
    """
    Find the moving cost of a series to a specific value.
    The moving cost is the sum of the addition/soustractions needed to have
    all numbers in the series equal to the target.
    Return the moving_cost (the sum).
    """
    cost = 0
    for a_point in series:
        cost += abs(a_point - target)
    return cost

def moving_cost_2(series, target):
    """
    Find the moving cost of a series to a specific value.
    The moving cost is the sum of the addition/soustractions needed to have
    all numbers in the series equal to the target.
    Return the moving_cost (the sum).
    """
    cost = 0
    for a_point in series:
        cost += sum(range(abs(a_point - target) + 1))
    return cost


computed_costs = {}
for target in range(min_crabs, max_crabs):
    # Use the other moving_cost function for part 1
    cost = moving_cost_2(crabs, target)
    computed_costs[cost] = target
    print(f"Target: {target} - Moving cost: {cost}")

min_cost = min(computed_costs.keys())
print(f"Best target is {computed_costs[min_cost]} with a cost of {min_cost}")
