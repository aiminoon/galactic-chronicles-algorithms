import pandas as pd
import numpy as np

# Load the dataset
file_path = "Docking_Requests_Dataset.csv"
df_docking = pd.read_csv(file_path)

def binarySearch(df_docking, current_index):
    # Find the rightmost ship that ends before the start of the ship at current_index.
    # ships must be sorted by 'End Time (hr)'.
    low, high = 0, current_index - 1
    result = -1
    current_start = df_docking.at[current_index, 'Start Time (hr)']
    while low <= high:
        mid = (low + high) // 2
        if df_docking.at[mid, 'End Time (hr)'] <= current_start:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result


def maxPriority(df_docking):
    # Filter ships that end within the 15 hour limit
    df_docking = df_docking[df_docking['End Time (hr)'] <= 15.0].copy()
    # Sort ships by their end time
    df_docking = df_docking.sort_values(by='End Time (hr)').reset_index(drop=True)

    print("Ships in the 15 hour time limit range, sorted by end time:")
    print(df_docking)
    print()

    n = len(df_docking)

    # Precompute prev[i] - index of previous non-overlapping ship before i
    prev = [-1] * n
    for i in range(n):
        prev[i] = binarySearch(df_docking, i)

    # Initialize DP arrays
    dp = [0] * n  # dp[i]: max priority achievable considering ships 0 to i
    included = [False] * n  # Track which ships are included in optimal solution

    # Base case
    dp[0] = df_docking.at[0, 'Priority Weight']
    included[0] = True

    for i in range(1, n):
        # Option 1: Include current ship
        include_weight = df_docking.at[i, 'Priority Weight']
        if prev[i] != -1:
            include_weight += dp[prev[i]]
        # Option 2: Exclude current ship
        exclude_weight = dp[i - 1]

        if include_weight > exclude_weight:
            dp[i] = include_weight
            included[i] = True
        else:
            dp[i] = exclude_weight
            included[i] = False

    # Backtrack to find the order of ships
    selected_ships = []
    total_time = 0.0
    i = n - 1
    while i >= 0:
        if included[i]:
            # Ship i is included in optimal solution
            selected_ships.append(df_docking.at[i, 'Ship ID'])
            start = df_docking.at[i, 'Start Time (hr)']
            end = df_docking.at[i, 'End Time (hr)']
            total_time += end - start
            # Move to the last non-overlapping ship
            i = prev[i]
        else:
            # Ship i is not included, move to previous ship
            i -= 1

    # Reverse to get ships in chronological order
    selected_ships.reverse()

    return selected_ships, dp[-1], total_time


# Main program
if __name__ == "__main__":
    selected, total_priority, total_time = maxPriority(df_docking)
    print("Selected Ships:", selected)
    print("Total Priority:", total_priority)
    print("Total Docking Time:", f"{total_time: .2f}", "hours")
