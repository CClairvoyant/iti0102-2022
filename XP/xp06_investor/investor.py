"""Investor helper."""


def get_currency_rates_from_file(filename: str) -> tuple:
    """
    Read and return the currency and exchange rate history from file.

    See web page:
    https://www.eestipank.ee/valuutakursside-ajalugu

    Note that the return value is tuple, that consists of two things:
    1) currency name given in the file.
    2) exchange rate history for the given currency.
        Note that history is returned using dictionary where keys represent dates
        and values represent exchange rates for the dates.

    :param filename: file name to read CSV data from
    :return: Tuple that consists of currency name and dict with exchange rate history
    """
    values = {}

    with open(filename) as f:
        content = f.read().split("\n")
    currency = content[0].split(" ")[-1][:-1]
    lines = content[:2:-1]

    if not lines[0]:
        lines.pop(0)

    for line in lines:
        date, value = line.split(",")
        values[date] = float(value)

    return currency, values


def exchange_money(exchange_rates: dict) -> list:
    """
    Find best dates to exchange money for maximum profit.

    You are given a dictionary where keys represent dates and values represent exchange
    rates for the dates. The amount you initially have is 1000 and you always use the
    maximum amount during the exchange.
    Be aware that there is 1% of service fee for every exchange. You only need to return
    the dates where you take action. That means the first action is always to buy the
    second currency and the second action is to sell it back. Repeat the sequence as
    many times as you need for maximum profit. You should always end up having the
    initial currency. That means there should always be an even number of actions. You can
    also decide that the best decision is to not make any transactions at all, if
    for example the rate is always dropping. In that case just return an empty list.

    :param exchange_rates: dictionary of dates and exchange rates
    :return: list of dates
    """
    drops, dates = [], []

    exchange_rates = dict(reversed(list(exchange_rates.items())))

    for i in range(1, len(exchange_rates)):
        temp_dates = list(exchange_rates)
        if exchange_rates[temp_dates[i - 1]] >= exchange_rates[temp_dates[i]]:
            drops.append({
                "start_date": temp_dates[i - 1],
                "end_date": temp_dates[i],
                "start_value": exchange_rates[temp_dates[i - 1]],
                "end_value": exchange_rates[temp_dates[i]]
            })

    while len(drops) > len(optimal_merge(drops)):
        drops = optimal_merge(drops)

    for drop in remove_bad_drops(drops):
        dates.append(drop["start_date"])
        dates.append(drop["end_date"])

    return dates


def optimal_merge(drops: list[dict]) -> list[dict]:
    """Find points where it isn't optimal to cash out and eliminate them from the dictionary."""
    for i in range(1, len(drops)):
        if drops[i]["end_value"] < drops[i - 1]["end_value"] and \
                drops[i]["start_value"] < drops[i - 1]["start_value"]:
            drops[i]["start_date"] = drops[i - 1]["start_date"]
            drops[i]["start_value"] = drops[i - 1]["start_value"]
            drops[i - 1] = {}
            break

    if {} in drops:
        drops.remove({})

    return drops


def remove_bad_drops(drops: list[dict]) -> list[dict]:
    """Remove points, where investing would lose you money, due to bank's cut."""
    for i in range(len(drops)):
        if drops[i]["start_value"] * 99 / 100 / drops[i]["end_value"] * 99 / 100 < 1:
            drops[i] = {}

    while {} in drops:
        drops.remove({})

    return drops


if __name__ == '__main__':
    result = get_currency_rates_from_file("article-report.csv")
    # test_data = {
    #     '31-10-2016': 1.0946,
    #     '28-10-2016': 1.0922,
    #     '27-10-2016': 1.0927,
    #     '26-10-2016': 1.0925,
    #     '25-10-2016': 1.0872,
    #     '24-10-2016': 1.0891,
    #     '21-10-2016': 1.0886,
    #     '20-10-2016': 1.0980,
    #     '19-10-2016': 1.0979,
    #     '18-10-2016': 1.0993,
    #     '17-10-2016': 1.0994,
    #     '14-10-2016': 1.1002,
    #     '13-10-2016': 1.1038,
    #     '12-10-2016': 1.1020,
    #     '11-10-2016': 1.1079,
    #     '10-10-2016': 1.1160,
    #     '07-10-2016': 1.1140,
    #     '06-10-2016': 1.1185,
    #     '05-10-2016': 1.1211,
    #     '04-10-2016': 1.1161,
    #     '03-10-2016': 1.1236
    # }
    print(exchange_money(result[1]))
    # 03 10 2016
    # 25 10 2016
