import pandas as pd

# Load the dataset
file_path = "AI_Override_System_Data.csv"
df_ai = pd.read_csv(file_path)

max_power = 20
max_time = 10

dp = [[0] * (max_time + 1) for _ in range(max_power + 1)]
selection = [[[] for _ in range(max_time + 1)] for _ in range(max_power + 1)]

for idx, row in df_ai.iterrows():
    power = row['Power Requirement']
    time = row['Time to Restore (min)']
    score = row['Criticality Score']
    for p in range(max_power, power - 1, -1):
        for t in range(max_time, time - 1, -1):
            if dp[p - power][t - time] + score > dp[p][t]:
                dp[p][t] = dp[p - power][t - time] + score
                selection[p][t] = selection[p - power][t - time] + [idx]

best_score = 0
best_indices = []
best_power = 0
best_time = 0
for p in range(max_power + 1):
    for t in range(max_time + 1):
        if dp[p][t] > best_score:
            best_score = dp[p][t]
            best_indices = selection[p][t]
            best_power = p
            best_time = t

optimal_df = df_ai.loc[best_indices].reset_index(drop=True)

print("Optimal System Restoration Plan:")
print(optimal_df)
print(f"\nTotal Power Used: {best_power}%")
print(f"Total Time Used: {best_time} minutes")
print(f"Total Criticality Score: {best_score}")

print("\nSystems to Restore:\n")

for i, row in optimal_df.iterrows():
    print(f"{i+1}. {row['System Name']}")
    print(f"   Power Required: {row['Power Requirement']}%")
    print(f"   Time to Restore: {row['Time to Restore (min)']} minutes")
    print(f"   Criticality Score: {row['Criticality Score']}")
    print("-" * 40)

print(f"\nTotal Criticality Score: {best_score}")
print(f"Total Power Used: {best_power}%")
print(f"Total Time Used: {best_time} minutes")
