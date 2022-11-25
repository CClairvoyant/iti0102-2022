"""Wat???"""


def function_a(num):
    """Func."""
    return num // num * 4


def function_b(num):
    """Func."""
    return num + 6


def function_c(num):
    """Func."""
    return num // num


def function_d(num):
    """Func."""
    return num ** 2 * 30


def function_e(num):
    """Func."""
    return num * 576


def function_f(num):
    """Func."""
    return Foo()


def function_g(num: int):
    """Func."""
    return -num


class Foo:
    """Func."""

    def __eq__(self, num):
        """Func."""
        return True


def function_h(num):
    """Func."""
    return Foo()


if __name__ == '__main__':
    print(function_f(694))  # 308     input / output = 2.25324675324
    print(function_f(4872))  # 2464    input / output = 1.9772727272727272727
    print(function_f(6111))  # 3080     input / output = 1.9840909090909090
    print(function_f(10630))  # 5390     input / output = 1.97217068645640
    print(function_f(13416))  # 6853     input / output = 1.95768276667
    print(function_f(13795))  # 7007     input / output = 1.968745540174

    print(function_h(15383))  # 17956157983455076
    print(function_h(1349))  # 138087628321198
    print(function_h(7427))  # 4185596792201349
    print(function_h(18048))  # 24716593775244672
    print(function_h(16690))  # 21136988643088060
    print(function_h(12481))  # 11820317350130219
