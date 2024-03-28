import csv


def save_to_file(keyword, jobs_data):
    fieldnames = ["title", "company_name", "link"]
    with open(f"{keyword}.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(jobs_data)
