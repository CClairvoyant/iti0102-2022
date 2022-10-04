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
    d = create_dictionary(data)
    l = []
    for p1 in d:
        for p2 in d:
            if p1 != p2:
                hobby_list = d[p1] + d[p2]
                common_hobbies = len(hobby_list) - len(set(hobby_list))
                different_hobbies = len(set(hobby_list)) - common_hobbies
                if different_hobbies == 0:
                    different_hobbies += 0.000000000000000000000000000000001
                l.append(common_hobbies / different_hobbies)
    for p1 in d:
        for p2 in d:
            if p1 != p2:
                hobby_list = d[p1] + d[p2]
                common_hobbies = len(hobby_list) - len(set(hobby_list))
                different_hobbies = len(set(hobby_list)) - common_hobbies
                if different_hobbies == 0:
                    different_hobbies += 0.000000000000000000000000000000001
                if common_hobbies / different_hobbies == max(l):
                    return p1, p2



print(find_two_people_with_most_common_hobbies("John:running\nJohn:walking\nMary:dancing\nMary:running\nNora:running\nNora:singing\nNora:dancing"))  # ('Mary', 'Nora')
# print(find_two_people_with_most_common_hobbies("name8:hobby1\nname13:hobby6\nname3:hobby1\nname10:hobby9\nname2:hobby9\nname14:hobby5\nname12:hobby0\nname5:hobby6\nname8:hobby4\nname11:hobby2"))      # [{'name5', 'name13'}, {'name10', 'name2'}, {'name10', 'name2'}, {'name5', 'name13'}]
# print(find_two_people_with_most_common_hobbies("name3:hobby10\nname3:hobby11\nname0:hobby1\nname10:hobby8\nname10:hobby0\nname2:hobby1\nname12:hobby8\nname1:hobby5\nname1:hobby5\nname8:hobby8"))      # [{'name2', 'name0'}, {'name2', 'name0'}, {'name8', 'name12'}, {'name8', 'name12'}]
# print(find_two_people_with_most_common_hobbies("name12:hobby3\nname11:hobby1\nname9:hobby6\nname1:hobby3\nname12:hobby5\nname3:hobby0\nname7:hobby5\nname0:hobby6\nname8:hobby3\nname9:hobby6\nname11:hobby3\nname8:hobby0\nname11:hobby1\nname3:hobby3"))      # [{'name8', 'name3'}, {'name8', 'name3'}]
# print(find_two_people_with_most_common_hobbies("name0:hobby8\nname2:hobby1\nname2:hobby2\nname4:hobby10\nname0:hobby9\nname1:hobby4\nname0:hobby4\nname0:hobby6\nname2:hobby2\nname4:hobby2"))      # [{'name2', 'name4'}, {'name2', 'name4'}]
# print(find_two_people_with_most_common_hobbies("name0:hobby1\nname2:hobby5\nname2:hobby6\nname2:hobby5\nname5:hobby3\nname5:hobby4\nname0:hobby5\nname2:hobby6\nname5:hobby1\nname5:hobby1\nname4:hobby1"))     # [{'name0', 'name4'}, {'name0', 'name4'}]
# print(find_two_people_with_most_common_hobbies("name5:hobby2\nname0:hobby0\nname4:hobby9\nname4:hobby10\nname5:hobby10\nname2:hobby2\nname3:hobby0\nname4:hobby2\nname2:hobby0\nname4:hobby5\nname5:hobby2\nname2:hobby10"))        #[{'name0', 'name3'}, {'name0', 'name3'}]
# print(find_two_people_with_most_common_hobbies("name4:hobby0\nname2:hobby2\nname1:hobby2\nname5:hobby2\nname3:hobby1\nname1:hobby5\nname2:hobby1\nname0:hobby4\nname3:hobby3\nname4:hobby0"))       # [{'name5', 'name2'}, {'name5', 'name1'}, {'name5', 'name2'}, {'name5', 'name1'}]
# print(find_two_people_with_most_common_hobbies("name9:hobby3\nname9:hobby4name7:hobby6\nname9:hobby10\nname12:hobby9\nname13:hobby9\nname7:hobby8\nname8:hobby3\nname0:hobby3\nname8:hobby4"))      # [{'name13', 'name12'}, {'name13', 'name12'}]
# print(find_two_people_with_most_common_hobbies("name3:hobby3\nname9:hobby4\nname13:hobby7\nname5:hobby6\nname4:hobby6\nname4:hobby5\nname9:hobby0\nname0:hobby2\nname10:hobby6\nname3:hobby7"))     # [{'name10', 'name5'}, {'name10', 'name5'}]
# print(find_two_people_with_most_common_hobbies("name3:hobby0\nname5:hobby4\nname3:hobby0\nname4:hobby8\nname3:hobby4\nname3:hobby9\nname4:hobby6\nname3:hobby3\nname5:hobby7\nname0:hobby10\nname1:hobby3"))        # [{'name1', 'name3'}, {'name1', 'name3'}]
# print(find_two_people_with_most_common_hobbies("name3:hobby4\nname1:hobby1\nname5:hobby0\nname5:hobby2\nname5:hobby4\nname4:hobby0\nname6:hobby0\nname3:hobby1\nname3:hobby1\nname7:hobby2\nname3:hobby3\nname3:hobby3\nname6:hobby0\nname7:hobby0\nname7:hobby1\nname1:hobby0"))       # [{'name4', 'name6'}, {'name4', 'name6'}]