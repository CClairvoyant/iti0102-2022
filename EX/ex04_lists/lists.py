"""Car inventory."""


def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]
    """
    return [all_cars.split(",")]


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
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
    all_cars_list = all_cars.split(",")
    list_of_models = []
    for car in all_cars_list:
        car_model = car.split(" ")
        if car_model[-1] not in list_of_models:
            list_of_models.append(car_model[-1])
    return list_of_models
