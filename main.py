import os
import csv
from collections import defaultdict


def main(folder_path):
    city_stats = defaultdict(lambda: {"count": 0, "min": float("inf"), "max": float("-inf"), "sum": 0})

    # Overall statistics
    overall_stats = {"count": 0, "min": float("inf"), "max": float("-inf"), "sum": 0}

    # Read all CSV files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, mode="r", newline="") as file:
                reader = csv.reader(file)
                header = next(reader)  # Skip header row

                for row in reader:
                    city, temp = row[0].strip(), float(row[1])

                    # Update city statistics
                    stats = city_stats[city]
                    stats["count"] += 1
                    stats["sum"] += temp
                    stats["min"] = min(stats["min"], temp)
                    stats["max"] = max(stats["max"], temp)

                    # Update overall statistics
                    overall_stats["count"] += 1
                    overall_stats["sum"] += temp
                    overall_stats["min"] = min(overall_stats["min"], temp)
                    overall_stats["max"] = max(overall_stats["max"], temp)

    # Compute average temperature for each city
    for city, stats in city_stats.items():
        stats["avg"] = round(stats["sum"] / stats["count"], 2)
        del stats["sum"]  # Remove sum key

    # Compute overall average temperature
    overall_stats["avg"] = round(overall_stats["sum"] / overall_stats["count"], 2)
    del overall_stats["sum"]  # Remove sum key

    # Final output dictionary
    output = {
        "all_cities": overall_stats,
         **dict(city_stats)
    }
    return output

