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
    """Find all cars of the mentioned make"""
    found_list = []
    if make.lower() not in all_cars.lower():
        return found_list
    else:
        all_cars_list = all_cars.split(",")
        for n in all_cars_list:
            if make.lower() in n.lower():
                found_list.append(n)
        return found_list


def search_by_model(all_cars: str, model: str):
    found_list = []
    if model.lower() not in all_cars.lower():
        return found_list
    else:
        all_cars_list = all_cars.split(",")
        for n in all_cars_list:
            f = n.lower().split(" ")
            if model.lower() in f:
                found_list.append(n)
        return found_list
