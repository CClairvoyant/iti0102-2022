"""Create schedule from the given file."""


import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    input_file = open(input_filename, "r")
    contents = input_file.read()
    output_file = open(output_filename, "w")
    output_file.write(create_schedule_string(contents))
    input_file.close()
    output_file.close()


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    timeline = create_schedule_dict(input_string)
    if not timeline:
        return("--------------------" + "\n"
               "|  time | entries  |" + "\n"
               "--------------------" + "\n"
               "| No entries found |" + "\n"
               "--------------------")
    sizes = get_table_sizes(create_schedule_dict(input_string))
    time = "time"
    entries = "entries"
    schedule = ""
    schedule += "-" * (sizes[0] + sizes[1] + 5) + "\n"
    schedule += f"|{time:>{sizes[0]}} | {entries:<{sizes[1]}}|" + "\n"
    schedule += "-" * (sizes[0] + sizes[1] + 5) + "\n"
    for times in timeline:
        temp = ", ".join(timeline[times])
        schedule += f"|{get_formatted_time(times):>{sizes[0]}} | {temp:<{sizes[1]}}|" + "\n"
    schedule += "-" * (sizes[0] + sizes[1] + 5) + "\n"
    return schedule


def create_schedule_dict(input_string: str):
    """Create dictionary with all the values"""
    timeline = {}
    for match in re.finditer(r"(?<=[ \n])([0,1]?[0-9]|2[0-3])\D([0-5]?[0-9]) +([A-ZÕÄÖÜŠŽa-zõäöüžš]+)", input_string):
        time = f"{match.group(1)}:{match.group(2)}"
        if add_zero_to_hours(time) not in timeline:
            timeline[add_zero_to_hours(time)] = [match.group(3).lower()]
        elif match.group(3).lower() not in timeline[add_zero_to_hours(time)]:
            timeline[add_zero_to_hours(time)].append(match.group(3).lower())
    sorted_by_time = sorted(timeline.items(), key=lambda x: x[0])
    timeline = dict(sorted_by_time)
    return timeline


def create_table():
    """Create table."""


def get_table_sizes(timeline: dict):
    """Get the maximum sizes for table."""
    time_list = []
    for time in timeline:
        time_list.append(len(get_formatted_time(time)))
    time_length = max(time_list) + 1
    time_list.append(len("time"))
    entries_list = []
    for entry in timeline.values():
        entries_list.append(len(", ".join(entry)))
    entries_list.append(len("entries"))
    entry_length = max(entries_list) + 1
    return time_length, entry_length


def add_zero_to_hours(time: str):
    h_and_m = time.split(":")
    h = h_and_m[0]
    m = h_and_m[1]
    if len(h) == 1:
        h = f"0{h}"
    if len(m) == 1:
        m = f"0{m}"
    return f"{h}:{m}"


def normalize(time: str):
    """Add missing 0's to the minutes and to the hours."""
    h_and_m = time.split(":")
    h = h_and_m[0]
    m = h_and_m[1]
    if len(h) == 2 and h[0] == "0":
        h = h[1]
    if len(m) == 1:
        m = f"0{m}"
    return f"{h}:{m}"


def get_formatted_time(time: str):
    """Format 24 hour time to the 12 hour time."""
    time = normalize(time)
    if 0 <= int(time[:-3]) < 12:
        day = "AM"
    else:
        day = "PM"
    if int(time[:-3]) == 0 or int(time[:-3]) == 12:
        formatted_hours = "12"
    else:
        formatted_hours = str(int(time[:-3]) % 12)
    return f"{formatted_hours}:{time[-2:]} {day}"


if __name__ == '__main__':
    print(create_schedule_dict("a 1:2 tere 1:2 tsau 1:2 tere"))
