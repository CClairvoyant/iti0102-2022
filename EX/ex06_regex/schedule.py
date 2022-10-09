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
        schedule += f"|{get_formatted_time(times):>{sizes[0]}} | {temp.lower():<{sizes[1]}}|" + "\n"
    schedule += "-" * (sizes[0] + sizes[1] + 5) + "\n"
    return schedule


def create_schedule_dict(input_string: str):
    """Create dictionary with all the values"""
    timeline = {}
    for match in re.finditer(r"(?<=[ \n])([0,1]?[0-9]|2[0-3])\D([0-5]?[0-9]) +([A-ZÕÄÖÜŠŽa-zõäöüžš]+)", input_string):
        time = f"{match.group(1)}:{match.group(2)}"
        if add_zero_to_hours(time) not in timeline:
            timeline[add_zero_to_hours(time)] = [match.group(3)]
        else:
            timeline[add_zero_to_hours(time)].append(match.group(3))
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
    print(create_schedule_string("sdasfa 1.3 hi"))
#     print(create_schedule_string("A 11:00 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed euismod nibh, non vehicula libero. Fusce ac eros\
#  lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam 10:0 a bibendum enim. Praesent dictum\
#  ante eget turpis tempor, porta placerat dolor ultricies. Mauris quis dui porttitor, ultrices turpis vitae, pulvinar nisl.\
#  Suspendisse potenti. Ut nec cursus sapien, convallis sagittis purus. Integer mollis nisi sed fermentum efficitur.\
#  Suspendisse sollicitudin sapien dui, vitae tempus lacus elementum ac. Curabitur id purus diam. 24:01 Donec blandit,\
#  est nec semper convallis, arcu libero lacinia ex, eu placerat risus est non tellus.\
# Orci varius natoque penatibus et magnis dis 0:12 parturient montes, nascetur ridiculus mus. Curabitur pretium at metus\
# eget euismod. Nunc sit amet fermentum urna. Maecenas commodo ex turpis, et malesuada tellus sodales non. Fusce elementum\
#  eros est. Phasellus nibh magna, tincidunt eget magna nec, rhoncus lobortis dui. Sed fringilla risus a justo tincidunt,\
#  in tincidunt urna interdum. Morbi varius lobortis tellus, vitae accumsan justo commodo in. 12:001 Nullam eu lorem leo.\
#  Vestibulum in varius magna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\
#   0:00 Aliquam ac velit sit amet nunc dictum aliquam pulvinar at enim. Nulla aliquam est quis sem laoreet, eu venenatis\
#   risus hendrerit. Donec ac enim lobortis, bibendum lacus quis, egestas nisi.\
# \
# 08:01 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed euismod nibh, non vehicula libero. Fusce ac eros\
#  lectus. Pellentesque interdum nisl sem, eget facilisis mauris malesuada eget. Nullam 18:19 a bibendum enim. Praesent\
#  dictum ante eget turpis tempor, 00:0 porta placerat dolor ultricies. Mauris quis dui porttitor, ultrices turpis vitae,\
#  pulvinar nisl. Suspendisse potenti. Ut nec cursus sapien, convallis sagittis purus. 8:8 Integer mollis nisi sed fermentum\
#   efficitur. Suspendisse sollicitudin sapien dui, vitae tempus lacus elementum ac. Curabitur id 18:19 purus\
#   diam. 18:19 Donec blandit, est nec semper convallis, arcu 7.01 libero lacinia ex, eu placerat risus est non tellus.\
# \
# 11:0 lorem\
# 0:60 bad\
#  1:2 goodone yes\
# 15:0 nocomma,\
#  18:19 yes-minus\
#   21:59 nopoint.\
# 23-59 canuseminusthere  22,0 CommaIsAlsoOk\
# 5:6\
# "))
# why not work
    #create_schedule_file("schedule_input.txt", "schedule_output.txt")
