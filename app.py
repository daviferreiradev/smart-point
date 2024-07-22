# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# profile_path = "C:/Users/DaviJoseFerreira/AppData/Local/Google/Chrome/User Data"

# chrome_options = Options()
# chrome_options.add_argument(f"user-data-dir={profile_path}")
# chrome_options.add_argument("profile-directory=Default")

# driver = webdriver.Chrome(options=chrome_options)

# driver.get("http://selenium.dev")

# driver.quit()

from datetime import datetime, timedelta


def calculate_remaining_time(entry_time, lunch_start_time, lunch_end_time):
    workHours = 6

    current_date = datetime.now().date()

    entry_time = datetime.strptime(entry_time, '%H:%M').replace(
        year=current_date.year, month=current_date.month, day=current_date.day)
    lunch_start_time = datetime.strptime(lunch_start_time, '%H:%M').replace(
        year=current_date.year, month=current_date.month, day=current_date.day)
    lunch_end_time = datetime.strptime(lunch_end_time, '%H:%M').replace(
        year=current_date.year, month=current_date.month, day=current_date.day)

    morning_work_duration = lunch_start_time - entry_time

    now = datetime.now()
    afternoon_work_duration = now - lunch_end_time

    total_worked_time = morning_work_duration + afternoon_work_duration

    remaining_time = timedelta(hours=workHours) - total_worked_time

    remaining_time_in_seconds = remaining_time.total_seconds()
    hours = int(remaining_time_in_seconds // 3600)
    minutes = int((remaining_time_in_seconds % 3600) // 60)
    seconds = int(remaining_time_in_seconds % 60)

    remaining_time_formatted = f"{hours:02}:{minutes:02}:{seconds:02}"

    return remaining_time_formatted


# Exemplo de uso da função
entry_time = '09:00'
lunch_start_time = '12:00'
lunch_end_time = '13:14'

print("O tempo restante para completar 6 horas de trabalho é:",
      calculate_remaining_time(entry_time, lunch_start_time, lunch_end_time))
