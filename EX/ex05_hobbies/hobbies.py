"""EX05 - Hobbies."""


def create_dictionary(data: str) -> dict:
    """
    Create dictionary about people and their hobbies ie. {name1: [hobby1, hobby2, ...], name2: [...]}.

    There should be no duplicate hobbies on 1 person.

    :param: data: given string from database
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
    :param: data: given string from database
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

    :param: data: given string from database
    :return: list of the least popular hobbies. Sorted alphabetically.
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


def sort_names_and_hobbies(data: str) -> tuple:
    """
    Create a tuple of sorted names and their hobbies.

    The structure of the tuple is as follows:
    (
        (name1, (hobby1, hobby2)),
        (name2, (hobby1, hobby2)),
         ...
    )

    For each person, there is a tuple, where the first element is the name (string)
    and the second element is an ordered tuple of hobbies (ordered alphabetically).
    All those person-tuples are ordered by the name of the person and are inside a tuple.
    """
    hobbies_list = data.split("\n")
    final_list = []
    if data == "":
        return tuple(final_list)
    for person_hobby in hobbies_list:
        person = person_hobby.split(":")[0:1]
        person = "".join(person)
        if [person, []] not in final_list:
            final_list.append([person, []])
    for person_hobby in hobbies_list:
        for x in range(len(final_list)):
            if person_hobby.split(":")[0] in final_list[x] and\
                    " ".join(person_hobby.split(":")[1:]) not in final_list[x][1]:
                final_list[x][1].append(" ".join(person_hobby.split(":")[1:]))
    for n in range(len(final_list)):
        # noinspection PyTypeChecker
        final_list[n][1] = tuple(sorted(final_list[n][1]))
        final_list[n] = tuple(final_list[n])
    final_list = tuple(sorted(final_list))
    return final_list


def find_people_with_hobbies(data: str, hobbies: list) -> set:
    """
    Find all the different people with certain hobbies.

    It is recommended to use set here.

    Example:
        data="John:running\nMary:running\nJohn:dancing\nJack:dancing\nJack:painting\nSmith:painting"
        hobbies=["running", "dancing"]
    Result:
        {"John", "Mary", "Jack"}
    """
    people_set = set()
    list_people_hobbies = data.split("\n")
    for i in list_people_hobbies:
        if i.split(":")[1] in hobbies:
            people_set.add(i.split(":")[0])
    return people_set


def find_two_people_with_most_common_hobbies(data: str) -> tuple | None:
    """
    Find the pair of people who have the highest ratio of common hobbies to different hobbies.

    Common hobbies are the ones which both people have.
    Different hobbies are the ones, which only one person has.

    Example:
    John has:
        running
        walking
    Mary has:
        dancing
        running
    Nora has:
        running
        singing
        dancing

    Pairs and corresponding common and different hobbies, ratio
    John and Mary; common: running; diff: walking, dancing; ratio: 1/2
    John and Nora; common: running; diff: walking, singing, dancing; ratio: 1/3
    Mary and Nora; common: running, dancing; diff: singing; ratio: 2/1

    So the best result is Mary and Nora. It doesn't matter in which order the names are returned.

    If multiple pairs have the same best ratio, it doesn't matter which pair (and in which order) is returned.

    If there are less than 2 people in the input, return None.
    """
    ratios = []
    d = create_dictionary(data)
    if len(d) >= 2:
        for i in range(len(list(d))):
            p1_hobbies = list(d.values())[i]
            p2_hobbies = list(d.values())[i-1]
            hobbies = p1_hobbies + p2_hobbies
            s = set(hobbies)
            common_hobbies = len(hobbies) - len(s)
            different_hobbies = len(s) - common_hobbies
            ratios.append((common_hobbies + 1) / (different_hobbies + 1))
        for i in range(len(list(d))):
            p1_hobbies = list(d.values())[i]
            p2_hobbies = list(d.values())[i-1]
            hobbies = p1_hobbies + p2_hobbies
            s = set(hobbies)
            common_hobbies = len(hobbies) - len(s) + 1
            different_hobbies = len(s) - common_hobbies + 1
            if max(ratios) == (common_hobbies + 1) / (different_hobbies + 1):
                return list(d)[i-1], list(d)[i]
    else:
        return None
