"""Operations with files."""


import datetime
import os


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename) as file:
        file_contents = file.read()
    return str(file_contents)


def read_file_contents_to_list(filename: str) -> list:
    r"""
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    with open(filename) as file:
        contents = file.read()
        content_list = contents.split("\n")
    return content_list


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    with open(filename) as file:
        contents = file.read()
        content_list = contents.split("\n")
        new_list = []
        for item in content_list:
            data = item.split(",")
            new_list.append(data)
    if new_list == [[""]]:
        return []
    else:
        return new_list


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exist, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(filename, "w") as file:
        file.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(filename, "w") as file:
        file.write("\n".join(lines))


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, "w") as file:
        new_list = []
        for item in data:
            csv_item = ",".join(item)
            new_list.append(csv_item)
        file.write("\n".join(new_list))
        if new_list:
            file.write("\n")


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    with open(dates_filename) as file_dates, open(towns_filename) as file_towns, open(csv_output_filename, "w") as \
            csv_output:
        content_dates = file_dates.read()
        content_towns = file_towns.read()
        csv = "name,town,date\n"
        csv_dict = {}
        dates_list = content_dates.split("\n")
        for dates in dates_list:
            csv_dict[dates.split(":")[0]] = [dates.split(":")[1]]
        towns_list = content_towns.split("\n")
        for town in towns_list:
            if town.split(":")[0] in csv_dict:
                csv_dict[town.split(":")[0]].append(town.split(":")[1])
            else:
                csv_dict[town.split(":")[0]] = ["-"]
                csv_dict[town.split(":")[0]].append(town.split(":")[1])
        for element in csv_dict:
            if len(csv_dict[element]) == 1:
                csv_dict[element].append("-")
        for element in csv_dict:
            csv += f"{element},{csv_dict[element][-1]},{csv_dict[element][0]}\n"
        csv_output.write(csv)


def read_csv_file_into_list_of_dicts(filename: str) -> list:
    """
    Read csv file into list of dictionaries.

    Header line will be used for dict keys.
    Each line after header line will result in a dict inside the result list.
    Every line contains the same number of fields.

    Example:
    name,age,sex
    John,12,M
    Mary,13,F

    Header line will be used as keys for each content line.
    The result:
    [
      {"name": "John", "age": "12", "sex": "M"},
      {"name": "Mary", "age": "13", "sex": "F"},
    ]

    If there are only header or no rows in the CSV-file,
    the result is an empty list.

    The order of the elements in the list should be the same
    as the lines in the file (the first line becomes the first element etc.)

    :param filename: CSV-file to read.
    :return: List of dictionaries where keys are taken from the header.
    """
    with open(filename) as file:
        content = file.read()
    csv_items = []
    output = []
    for item in content.split("\n"):
        csv_items.append(item.split(","))
    for i in range(len(csv_items)):
        if i != 0:
            output.append(dict(zip(csv_items[0], csv_items[i])))
    return output


def write_list_of_dicts_to_csv_file(filename: str, data: list) -> None:
    """
    Write list of dicts into csv file.

    Data contains a list of dictionaries.
    Dictionary key represents the field.

    Example data:
    [
      {"name": "john", "age": "23"}
      {"name": "mary", "age": "44"}
    ]
    Will become:
    name,age
    john,23
    mary,44

    The order of fields/headers is not important.
    The order of lines is important (the same as in the list).

    Example:
    [
      {"name": "john", "age": "12"},
      {"name": "mary", "town": "London"}
    ]
    Will become:
    name,age,town
    john,12,
    mary,,London

    Fields which are not present in one line will be empty.

    The order of the lines in the file should be the same
    as the order of elements in the list.

    :param filename: File to write to.
    :param data: List of dictionaries to write to the file.
    :return: None
    """
    with open(filename, "w") as file:
        first_line = []
        for dictionary in data:
            for key in dictionary:
                if key not in first_line:
                    first_line.append(key)
        file.write(",".join(first_line))
        for dictionary in data:
            person = []
            for item in first_line:
                try:
                    person.append(dictionary[item])
                except KeyError:
                    person.append("")
            file.write("\n" + ",".join(person))


def are_all_digits(content: str, index: int) -> bool:
    """Check if all values of a category are integers."""
    result = True
    for line in content.split("\n")[1:]:
        if not line.split(",")[index].isdigit() and line.split(",")[index] != "-":
            result = False
    return result


def are_all_dates(content: str, index: int) -> bool:
    """Check if all values of a category are in the following date format: dd.mm.yyyy."""
    result = True
    for line in content.split("\n")[1:]:
        if line.split(",")[index] != "-":
            try:
                datetime.datetime.strptime(line.split(",")[index], "%d.%m.%Y")
            except ValueError:
                result = False
            except TypeError:
                result = False
    return result


def read_csv_file_into_list_of_dicts_using_datatypes(filename: str) -> list:
    """
    Read data from file and cast values into different datatypes.

    If a field contains only numbers, turn this into int.
    If a field contains only dates (in format dd.mm.yyyy), turn this into date.
    Otherwise the datatype is string (default by csv reader).

    Example:
    name,age
    john,11
    mary,14

    Becomes ('age' is int):
    [
      {'name': 'john', 'age': 11},
      {'name': 'mary', 'age': 14}
    ]

    But if all the fields cannot be cast to int, the field is left to string.
    Example:
    name,age
    john,11
    mary,14
    ago,unknown

    Becomes ('age' cannot be cast to int because of "ago"):
    [
      {'name': 'john', 'age': '11'},
      {'name': 'mary', 'age': '14'},
      {'name': 'ago', 'age': 'unknown'}
    ]

    Example:
    name,date
    john,01.01.2020
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': datetime.date(2020, 1, 1)},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    Example:
    name,date
    john,01.01.2020
    mary,late 2021

    Becomes:
    [
      {'name': 'john', 'date': "01.01.2020"},
      {'name': 'mary', 'date': "late 2021"},
    ]

    Value "-" indicates missing value and should be None in the result
    Example:
    name,date
    john,-
    mary,07.09.2021

    Becomes:
    [
      {'name': 'john', 'date': None},
      {'name': 'mary', 'date': datetime.date(2021, 9, 7)},
    ]

    None value also doesn't affect the data type
    (the column will have the type based on the existing values).

    The order of the elements in the list should be the same
    as the lines in the file.

    For date, strptime can be used:
    https://docs.python.org/3/library/datetime.html#examples-of-usage-date
    """
    csv_list = read_csv_file(filename)
    content = read_file_contents(filename)
    categories = content.split("\n")[0].split(",")
    for i in range(len(categories)):
        for line in csv_list[1:]:
            if line[i] == "-":
                line[i] = None
            if are_all_digits(content, i) and line[i] is not None:
                line[i] = int(line[i])
    for i in range(len(categories)):
        for line in csv_list[1:]:
            if are_all_dates(content, i) and line[i] is not None:
                line[i] = datetime.datetime.strptime(line[i], "%d.%m.%Y").date()
    output = []
    for i in range(1, len(csv_list)):
        output.append(dict(zip(csv_list[0], csv_list[i])))
    return output


def read_people_data(directory: str) -> dict:
    """
    Read people data from files.
    Files are inside directory. Read all *.csv files.

    Each file has an int field "id" which should be used to merge information.

    The result should be one dict where the key is id (int) and value is
    a dict of all the different values across the the files.
    Missing keys should be in every dictionary.
    Missing value is represented as None.

    File: a.csv
    id,name
    1,john
    2,mary
    3,john

    File: births.csv
    id,birth
    1,01.01.2001
    2,05.06.1990

    File: deaths.csv
    id,death
    2,01.02.2020
    1,-

    Becomes:
    {
        1: {"id": 1, "name": "john", "birth": datetime.date(2001, 1, 1), "death": None},
        2: {"id": 2, "name": "mary", "birth": datetime.date(1990, 6, 5),
            "death": datetime.date(2020, 2, 1)},
        3: {"id": 3, "name": "john", "birth": None, "death": None},
    }


    :param directory: Directory where the csv files are.
    :return: Dictionary with id as keys and data dictionaries as values.
    """
    files_list = os.listdir(directory)
    dodo = {}
    for file_name in files_list:
        for dictionary in read_csv_file_into_list_of_dicts_using_datatypes(fr"{directory}\{file_name}"):
            if dictionary["id"] not in dodo:
                dodo[dictionary["id"]] = dictionary
            else:
                dodo[dictionary["id"]].update(dictionary)
    datatype_list = []
    for key in dodo.keys():
        for gogo in dodo[key]:
            if gogo not in datatype_list:
                datatype_list.append(gogo)
    for key in dodo.keys():
        for datatype in datatype_list:
            if datatype not in dodo[key]:
                dodo[key].update({datatype: None})
    return dodo


def generate_people_report(person_data_directory: str, report_filename: str) -> None:
    """
    Generate report about people data.

    Data should be read using read_people_data().

    The input files contain fields "birth" and "death" which are dates. Those can be in different files. There are no
    duplicate headers in the files (except for the "id").

    The report is a CSV file where all the fields are written to
    (along with the headers).
    In addition, there should be two fields:
    - "status" this is either "dead" or "alive" depending on whether
    there is a death date
    - "age" - current age or the age when dying.
    The age is calculated as full years.
    Birth 01.01.1940, death 01.01.2020 - age: 80
    Birth 02.01.1940, death 01.01.2020 - age: 79

    If there is no birth date, then the age is -1.

    When calculating age, dates can be compared.

    The lines in the file should be ordered:
    - first by the age ascending (younger before older);
      if the age cannot be calculated, then those lines will come last
    - if the age is the same, then those lines should be ordered
      by birthdate descending (newer birth before older birth)
    - if both the age and birth date are the same,
      then by name ascending (a before b). If name is not available, use "" (people with missing name should be before
      people with  name)
    - if the names are the same or name field is missing,
      order by id ascending.

    Dates in the report should in the format: dd.mm.yyyy
    (2-digit day, 2-digit month, 4-digit year).

    :param person_data_directory: Directory of input data.
    :param report_filename: Output file.
    :return: None
    """
    pass


if __name__ == '__main__':
    print(read_people_data("data"))
