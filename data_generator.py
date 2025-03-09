import csv
import random

from pathlib import Path

CURRENT_DIR = Path(__file__).parent

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami", "Dallas", "San Francisco", "Seattle", "Boston",
          "Denver"]


# Define temperature range (e.g., 15°C to 35°C)
TEMP_MIN = 15.0
TEMP_MAX = 35.0


def generate_csv_files(subfolder, num_chunks, rows_per_chunk):
    for chunk_num in range(num_chunks):
        # Output CSV file
        csv_filename = Path(CURRENT_DIR, subfolder, f"chunk_{chunk_num}.csv")

        # Write CSV header
        with open(csv_filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["city", "temperature"])

            # Generate temperature readings
            for _ in range(rows_per_chunk):
                city = random.choice(cities)
                temperature = round(random.uniform(TEMP_MIN, TEMP_MAX), 2)
                writer.writerow([city, temperature])

        print(f"Temperature simulation complete. Data saved in '{csv_filename}'.")


if __name__ == "__main__":
    # 17_000_000 # ~ 256 MB
    # 68_000_000 # ~ 1 GB
    subfolder = "sample_data"
    num_chunks = 4
    rows_per_chunk = 10
    generate_csv_files(subfolder, num_chunks, rows_per_chunk)
