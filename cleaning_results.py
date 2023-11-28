import pandas as pd

df = pd.read_excel('datasets/race_results.xlsx')

# Create two separate DataFrames based on the "Country" column
df_overall = df[df['Country'] == 'ALL']
df_detail = df[df['Country'] != 'ALL']

# Save DataFrames to Excel files
df_overall.to_excel('datasets/race_results_overall.xlsx', index=False)
df_detail.to_excel('datasets/race_results_detail.xlsx', index=False)