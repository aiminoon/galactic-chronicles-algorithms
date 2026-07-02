import pandas as pd
import numpy as np

# Load the dataset
file_path = "Compartment_Sensor_Data.csv"
df_compartments = pd.read_csv(file_path)

def find_stowaway_protocol(df):
    # Make a copy to avoid modifying the original DataFrame
    df_processed = df.copy()

    # Step 1: Calculate raw composite likelihood score
    df_processed['raw_likelihood'] = (
        df_processed['Crew Movement Count'] +
        df_processed['Oxygen Anomaly (%)'] +
        np.abs(df_processed['Heat Deviation (°C)'])
    )

    # Step 2: Calculate probability for each compartment
    # Normalize raw_likelihoods to sum to 1
    total_raw_likelihood = df_processed['raw_likelihood'].sum()
    if total_raw_likelihood == 0:
        # Handle case where all likelihoods are zero to avoid division by zero
        df_processed['probability'] = 1 / len(df_processed)  # Assign equal probability if no clues
    else:
        df_processed['probability'] = df_processed['raw_likelihood'] / total_raw_likelihood

    # Step 3: Sort compartments by probability in descending order
    sorted_compartments = df_processed.sort_values(by='probability', ascending=False).reset_index(drop=True)

    # Step 4: Calculate Expected Number of Trials
    expected_trials = 0
    for i, row in sorted_compartments.iterrows():
        trial_number = i + 1  # First compartment is trial 1
        expected_trials += (row['probability'] * trial_number)

    return sorted_compartments, expected_trials


# ------------------------------------------------------------------------------
search_order_df, expected_num_trials = find_stowaway_protocol(df_compartments)

print("\n--- Part 3: The Stowaway Protocol ---")
print("Recommended Compartment Search Order (by decreasing probability):")
print(search_order_df[['Compartment ID', 'Crew Movement Count', 'Oxygen Anomaly (%)',
                        'Heat Deviation (°C)', 'raw_likelihood', 'probability']].to_markdown(index=False))

print(f"\nExpected Number of Trials Until Success: {expected_num_trials:.2f}")

print("\nInput Data Snapshot (Compartment_Sensor_Data.csv head):")
print(df_compartments.head().to_markdown(index=False))
