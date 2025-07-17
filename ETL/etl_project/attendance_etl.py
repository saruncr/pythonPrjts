import pandas as pd

# Step 1: Load the CSV
df = pd.read_csv('data/attendance.csv')

# Step 2: Preview the first 5 rows
#print(df.head())

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Fill missing 'status' values (if any)
df['status'] = df['status'].fillna('Unknown')

# Function to calculate work hours from check-in and check-out
def calc_work_hours(row):
    if pd.notnull(row['check_in']) and pd.notnull(row['check_out']):
        try:
            in_time = pd.to_datetime(row['check_in'], format='%H:%M')
            out_time = pd.to_datetime(row['check_out'], format='%H:%M')
            return round((out_time - in_time).seconds / 3600, 2)
        except:
            return 0
    return 0

# Apply the function
df['work_hours'] = df.apply(calc_work_hours, axis=1)

# Preview updated data
print(df[['name', 'date', 'status', 'work_hours','check_in', 'check_out']].head(10))

summary = df.groupby('name')['work_hours'].sum().reset_index()
summary = summary.sort_values(by='work_hours', ascending=False)

# Export summary to Excel
summary.to_excel('data/employee_hours_summary.xlsx', index=False)

print("\n✅ Summary exported to 'employee_hours_summary.xlsx'")
