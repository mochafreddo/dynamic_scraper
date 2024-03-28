import csv


def write_to_csv(keyword, jobs_data):
    fieldnames = ["title", "company_name", "link"]
    with open(f"{keyword}_jobs.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(jobs_data)
