import json

input_file = "indy_philly_restaurant_aggregated.json"
temp_file = "temp_filtered.json"

# Filter and write to temporary file
with open(input_file, "r", encoding="utf-8") as infile, \
     open(temp_file, "w", encoding="utf-8") as outfile:

    for line in infile:
        record = json.loads(line)

        if record.get("is_open") == 1:
            outfile.write(json.dumps(record) + "\n")

# Replace original file
import os
os.replace(temp_file, input_file)

print("Done! File updated to only include open restaurants.")