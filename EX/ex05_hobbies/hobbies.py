"""EX05 - Hobbies."""


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param data: given string from database
    :return: dictionary where keys are people and values are lists of hobbies
    """
    data_list = data.split("\n")
    unique_hobbies = {}
    for person in data_list:
        if person.split(":")[0] not in unique_hobbies:
            unique_hobbies[person.split(":")[0]] = [person.split(":")[1]]
        else:
            unique_hobbies.get(person.split(":")[0]).append(person.split(":")[1])
    for hobbies in unique_hobbies.keys():
        unique_hobbies[hobbies] = list(set(unique_hobbies.get(hobbies)))
    return unique_hobbies


def sort_dictionary(dic: dict) -> dict:
    """
    Sort dictionary values alphabetically.

    The order of keys is not important.

    sort_dictionary({"b":[], "a":[], "c": []})  => {"b":[], "a":[], "c": []}
    sort_dictionary({"": ["a", "f", "d"]})  => {"": ["a", "d", "f"]}
    sort_dictionary({"b":["d", "a"], "a":["c", "f"]})  => {"b":["a", "d"], "a":["c", "f"]}
    sort_dictionary({"Jack": ["swimming", "hiking"], "Charlie": ["games", "yoga"]})
        => {"Jack": ["hiking", "swimming"], "Charlie": ["games", "yoga"]}

    :param dic: dictionary to sort
    :return: sorted dictionary
    """
    for key in dic:
        dic[key] = sorted(dic.get(key))
    return dic


def create_dictionary_with_hobbies(data: str) -> dict:
    """
    Create dictionary about hobbies and their hobbyists ie. {hobby1: [name1, name2, ...], hobby2: [...]}.
    :param data: given string from database
    :return: dictionary, where keys are hobbies and values are lists of people. Values are sorted alphabetically
    """
    data_list = data.split("\n")
    people_hobbies = {}
    for person in data_list:
        if person.split(":")[1] not in people_hobbies:
            people_hobbies[person.split(":")[1]] = [person.split(":")[0]]
        else:
            people_hobbies.get(person.split(":")[1]).append(person.split(":")[0])
    for hobbies in people_hobbies.keys():
        people_hobbies[hobbies] = list(set(people_hobbies.get(hobbies)))
    for key in people_hobbies:
        people_hobbies[key] = sorted(people_hobbies.get(key))
    return people_hobbies


def find_people_with_most_hobbies(data: str) -> list:
    """
    Find the people who have the most hobbies.
    :param data: given string from database
    :return: list of people with most hobbies. Sorted alphabetically.
    """
    people_with_hobbies = create_dictionary(data)
    counts_of_hobbies = []
    people_with_most_hobbies = []
    for person in people_with_hobbies:
        counts_of_hobbies.append(len(people_with_hobbies.get(person)))
    max_count_of_hobbies = max(counts_of_hobbies)
    for person in people_with_hobbies:
        if len(people_with_hobbies.get(person)) == max_count_of_hobbies:
            people_with_most_hobbies.append(person)
    return sorted(people_with_most_hobbies)


def find_least_popular_hobbies(data: str) -> list:
    """
    Find the least popular hobbies.

    :param data: given string from database
    :return: list of least popular hobbies. Sorted alphabetically.
    """
    hobby_list = create_dictionary_with_hobbies(data)
    counts_of_people = []
    hobbies_with_least_people = []
    for hobby in hobby_list:
        counts_of_people.append(len(hobby_list.get(hobby)))
    min_count_of_people = min(counts_of_people)
    for hobby in hobby_list:
        if len(hobby_list.get(hobby)) == min_count_of_people:
            hobbies_with_least_people.append(hobby)
    return sorted(hobbies_with_least_people)
