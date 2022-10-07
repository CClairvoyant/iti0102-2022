"""Regex, I think."""
import re


class Entry:
    """Entry class."""

    def __init__(self, first_name: str, last_name: str, id_code: str, phone_number: str, date_of_birth: str,
                 address: str):
        """Init."""
        self.first_name = first_name
        self.last_name = last_name
        self.id_code = id_code
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.address = address

    def format_date(self):
        """
        Return the date in the following format: 'Day: {day}, Month: {month}, Year: {year}'.

        Just for fun, no points gained or lost from this.

        Example: 'Day: 06, Month: 11, Year: 1995'
        If the object doesn't have date of birth given, return None.
        :return:
        """
        pass

    def __repr__(self) -> str:
        """
        Object representation.

        This method makes printing the object actually readable in the console.
        This method is perfect. It's not necessary to edit.
        """
        return f"Name: {self.first_name} {self.last_name}\n" \
               f"ID code: {self.id_code}\n" \
               f"Phone number: {self.phone_number}\n" \
               f"Date of birth: {self.date_of_birth}\n" \
               f"Address: {self.address}"

    def __eq__(self, other) -> bool:
        """
        Compare two Entry objects.

        This method assists in comparing two different objects.
        This method is perfect. Don't touch it.
        """
        return self.first_name == other.first_name and self.last_name == other.last_name and \
            self.id_code == other.id_code and self.phone_number == other.phone_number and \
            self.date_of_birth == other.date_of_birth and self.address == other.address


def parse(row: str) -> Entry:
    """
    Parse data from input string.

    :param row: String representation of the data.
    :return: Entry object with filled values
    """
    data = ""
    for match in re.finditer(r"([A-ZÕÄÖÜŽŠ][a-zõäöüžš]+)?([A-ZÕÄÖÜŽŠ][a-zõäöüžš]+)?(\d{11})((\+\d{3})? ?(\d{7,8}))?(\d{2}-\d{2}-\d{4})?(.+)?", row):
        data = Entry(match.group(1), match.group(2), match.group(3), match.group(4), match.group(7), match.group(8))
    return data


if __name__ == '__main__':
    print(parse('PriitPann39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    """
    Name: Priit Pann
    ID code: 39712047623
    Phone number: +372 56887364
    Date of birth: Day: 02, Month: 12, Year: 1998
    Address: Oja 18-2,Pärnumaa,Are
    """
    print()
    print(parse('39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    """
    Name: None None
    ID code: 39712047623
    Phone number: +372 56887364
    Date of birth: Day: 02, Month: 12, Year: 1998
    Address: Oja 18-2,Pärnumaa,Are
    """
    print()
    print(parse('PriitPann3971204762302-12-1998Oja 18-2,Pärnumaa,Are'))
    """
    Name: Priit Pann
    ID code: 39712047623
    Phone number: None
    Date of birth: Day: 02, Month: 12, Year: 1998
    Address: Oja 18-2,Pärnumaa,Are
    """
    print()
    print(parse('PriitPann39712047623+372 56887364Oja 18-2,Pärnumaa,Are'))
    """
    Name: Priit Pann
    ID code: 39712047623
    Phone number: +372 56887364
    Date of birth: None
    Address: Oja 18-2,Pärnumaa,Are
    """
    print()
    print(parse('PriitPann39712047623+372 5688736402-12-1998'))
    """Name: Priit Pann
    ID code: 39712047623
    Phone number: +372 56887364
    Date of birth: Day: 02, Month: 12, Year: 1998
    Address: None
    """
