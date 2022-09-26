"""Car inventory."""


def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]
    """
    if all_cars == "":
        return []
    else:
        return all_cars.split(",")


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    if all_cars == "":
        return []
    else:
        all_cars_list = all_cars.split(",")
        list_of_makes = []
        for car in all_cars_list:
            car_make = car.split(" ")
            if car_make[0] not in list_of_makes:
                list_of_makes.append(car_make[0])
        return list_of_makes


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4,Audi A6" => ["A4", "Superb", "A6"]
    """
    if all_cars == "":
        return []
    else:
        all_cars_list = all_cars.split(",")
        list_of_models = []
        for car in all_cars_list:
            car_model = car.split(" ")[1:]
            if " ".join(car_model) not in list_of_models:
                list_of_models.append(" ".join(car_model))
                print(list_of_models)
        return list_of_models


def search_by_make(all_cars: str, make: str):
    """Find all cars of the mentioned make."""
    found_list = []
    if make.lower() not in all_cars.lower():
        return found_list
    else:
        for car in all_cars.split(","):
            all_cars_makes = [car.lower().split(" ")[0]]
            if make.lower() in all_cars_makes:
                found_list.append(car)
        return found_list


def search_by_model(all_cars: str, model: str):
    """Find all cars of the mentioned model."""
    found_list = []
    if model.lower() not in all_cars.lower():  # if model isn't in the string of cars then it returns an empty list
        return found_list
    else:
        for car in all_cars.split(","):  # checks each car's full title in the list with the following code
            all_cars_models = car.lower().split(" ")[1:]  # the new variable is a list with all the models of all_cars
            if model.lower() in all_cars_models:  # if the searched model is in the list mentioned above,...
                found_list.append(car)  # ...then add the car's full title to the found_list
        return found_list


def car_make_and_models(all_cars: str) -> list:
    """
    Create a list of structured information about makes and models.
    For each different car make in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the make (string),
    the second element is a list of models for the given make (list of strings).

    No duplicate makes or models should be in the output.

    The order of the makes and models should be the same os in the input list (first appearance).

    "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5" =>
    [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon Lux']]]
    """
    cars_list = all_cars.split(",")
    final_list = []
    if all_cars == "":
        return final_list
    for car in cars_list:
        car_make = car.split(" ")[0:1]
        car_make = "".join(car_make)
        if [car_make, []] not in final_list:
            final_list.append([car_make, []])
    for car in cars_list:
        for x in range(len(final_list)):
            if car.split(" ")[0] in final_list[x] and " ".join(car.split(" ")[1:]) not in final_list[x][1]:
                final_list[x][1].append("".join(car.split(" ")[1:]))
    return final_list


def add_cars(car_list: list, all_cars: str) -> list:
    """
    Add cars from the list into the existing car list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated cars (as in all the previous functions).
    The task is to add cars from the string into the list.

    Hint: This and car_make_and_models are very similar functions. Try to use one inside another.

    [['Audi', ['A4']], ['Skoda', ['Superb']]]
    and
    "Audi A6,BMW A B C,Audi A4"

    =>

    [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]
    """



print(add_cars([['Audi', ['A4']], ['Skoda', ['Superb']]], "Audi A6,BMW A B C,Audi A4"))
