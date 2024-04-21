from datetime import datetime

# Function to find the days difference between today's date and the input date in the format %Y-%m-%d
def get_days_from_today(data: str) -> int:
    try:
        return (datetime.today().date() - datetime.strptime(data, "%Y-%m-%d").date()).days
    except ValueError:
        print(f"{data} is not a valid string. Waiting format %Y-%m-%d")

    

# print(get_days_from_today("2021-10-09"))
# print(get_days_from_today("2021.10.09"))
# print(get_days_from_today(""))
