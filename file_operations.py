# Day 19 - File Handling with Smart Meter Readings

# Write initial data
data = [
    "2025-04-28, 12.5\n",
    "2025-04-29, 13.7\n",
    "2025-04-30, 11.9\n"
]

with open("meter_data.txt", "w") as fh:
    fh.writelines(data)

# Read full content
with open("meter_data.txt", "r") as fh:
    print("Full File Content:\n", fh.read())

# Read line by line
with open("meter_data.txt", "r") as fh:
    print("Line-by-Line:")
    for line in fh:
        print(line.strip())

# Read all lines into list
with open("meter_data.txt", "r") as fh:
    lines = fh.readlines()
    print("All Lines:", lines)

# Append new reading
with open("meter_data.txt", "a") as fh:
    fh.write("2025-05-01, 14.3\n")

# Re-read and print updated data
with open("meter_data.txt", "r") as fh:
    updated = fh.read()
    print("Updated Data:\n", updated)

# Calculate average consumption
with open("meter_data.txt", "r") as fh:
    readings = [float(line.split(",")[1]) for line in fh]
    avg = sum(readings) / len(readings)
    print(f"Average Consumption: {avg:.2f} kWh")