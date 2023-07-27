import itertools

# Define the events and their corresponding weights
events = ['ins', 'del', 'dup', 'fDNA']
weights = [0.15, 0.05, 0.30, 0.50]

# Function to calculate the total weight of a given combination of events
def calculate_total_weight(combination):
    total_weight = 0
    for event in combination:
        total_weight += weights[events.index(event)]
    return total_weight

# Generate all permutations of the events
all_permutations = itertools.permutations(events)

# Filter permutations that contain all events at once
all_at_once_permutations = [perm for perm in all_permutations if len(perm) == len(events)]

# Sort permutations based on total weight
sorted_permutations = sorted(all_at_once_permutations, key=calculate_total_weight)

# Print all possible combinations and their total weights
for idx, perm in enumerate(sorted_permutations, 1):
    total_weight = calculate_total_weight(perm)
    print(f"{idx}. Combination: {', '.join(perm)}, Total Weight: {total_weight:.2f}")
