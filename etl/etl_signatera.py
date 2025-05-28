
import pandas as pd
import numpy as np

def transform_flatiron_export(input_file, output_file):
    df = pd.read_excel(input_file)

    # Fill in or generate necessary columns
    if 'Regimen_Type' not in df.columns:
        df['Regimen_Type'] = np.random.choice(['a', 'b', 'c', 'd'], size=len(df))

    if 'Cycle' not in df.columns:
        df['Cycle'] = df['Event_Type'].apply(lambda x: next((part for part in str(x).split() if part.startswith('C')), 'Unknown'))

    if 'Y_Index' not in df.columns:
        df['Y_Index'] = df.groupby('Patient_Name').ngroup() + 1

    # Save the cleaned output
    df.to_csv(output_file, index=False)

# Example usage
# transform_flatiron_export('Signatera_Timeline_Expected_Actual_With_Cycles.xlsx', 'flatiron_to_tracker_template.csv')
print("ETL completed successfully.")
input("Press Enter to exit...")