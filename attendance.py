import pandas as pd

# Load the CSV
df = pd.read_csv("students.csv")

# Add Attendance column, default everyone to Absent
df["Attendance"] = "Absent"

print("=== Attendance System ===")
print("Enter student names (type 'done' when finished):\n")

# Take input from user
while True:
    name = input("Enter name: ").strip()
    if name.lower() == "done":
        break
    # Case-insensitive matching
    match = df["Name"].str.lower() == name.lower()
    if match.any():
        df.loc[match, "Attendance"] = "Present"
        print(f"  ✓ {name} marked Present")
    else:
        print(f"  ✗ {name} not found in list")

# Save updated CSV
df.to_csv("students.csv", index=False)

print("\n=== Final Attendance ===")
print(df.to_string(index=False))
print("\nAttendance saved to students.csv!")