#!/usr/bin/python3

from forex_python.converter import CurrencyRates
import datetime

def get_valid_response(text, options):
    response = input(text).strip()
    while response not in options:
        response = input(f'Invalid choice, {text}').strip()
    return response

def get_valid_date():
    year = int(get_valid_response("Enter year: ", list(map((lambda x: str(x)), list(range(1, 10000))))))
    month = int(get_valid_response("Enter month: ", list(map((lambda x: str(x)), list(range(1, 13))))))
    day = int(get_valid_response("Enter day: ", list(map((lambda x: str(x)), list(range(1, 32))))))
    hour = int(get_valid_response("Enter hour: ", list(map((lambda x: str(x)), list(range(0, 24))))))
    minute = int(get_valid_response("Enter minute: ", list(map((lambda x: str(x)), list(range(0, 60))))))
    second = int(get_valid_response("Enter second: ", list(map((lambda x: str(x)), list(range(0, 60))))))
    return year, month, day, hour, minute, second, 0

def print_rates(dictionary, c):
    for key, val in dictionary.items():
        print(f'1 {c} -> {val} {key}')

def menu(text, fnc):
    option = int(get_valid_response(f"Select Option:\n[1] Return To main\n[2] {text}\n[3] Quit\nEnter response: ", "123"))
    if option == 1:
        main()
    elif option == 2:
        fnc()


def latest_currencies():
    rate = CurrencyRates()
    currency = input_currency("Enter currency: ")
    option = int(get_valid_response("Select option:\n[1] View Rates as of now\n[2] View Rates at a user specified date and time: ", "12"))

    if option == 2:
        y, m, d, h, mi, s, ms = get_valid_date()
        date_obj = datetime.datetime(y, m, d, h, mi, s, ms)
        try:
            print_rates(rate.get_rates(currency, date_obj), currency)
        except:
            print(f'{currency} could not be found')
    else:
        try:
            print_rates(rate.get_rates(currency), currency)
        except:
            print(f'{currency} could not be found')
    menu("Check rates again", latest_currencies)

def print_conversion(base, dest, amt, res):
    print(f'{amt} {base} = {res} {dest}')

def print_pair_rate(base, dest, res):
    print(f'1 {base} = {res} {dest}')


def convert_amount():
    rate = CurrencyRates()
    base_cur = input_currency("Enter base currency: ")
    dest_cur = input_currency("Enter destination currency: ")
    amount = input_float("Enter amount: ")
    option = int(get_valid_response("Select option:\n[1] View coversion as of now\n[2] View conversion at a user specified date and time: ", "12"))
    if option == 2:
        y, m, d, h, mi, s, ms = get_valid_date()
        date_obj = datetime.datetime(y, m, d, h, mi, s, ms)
        try:
            print_conversion(base_cur, dest_cur, amount, rate.convert(base_cur, dest_cur, amount, date_obj))
        except:
            print("An error occured")
    else:
        try:
            print_conversion(base_cur, dest_cur, amount, rate.convert(base_cur, dest_cur, amount))
        except:
            print("An error occured")
    menu("Convert again", convert_amount)



def two_pairs_exchange():
    rate = CurrencyRates()
    base_cur = input_currency("Enter base currency: ")
    dest_cur = input_currency("Enter destination currency: ")
    option = int(get_valid_response("Select option:\n[1] View Rates as of now\n[2] View Rates at a user specified date and time: ", "12"))
    if option == 2:
        y, m, d, h, mi, s, ms = get_valid_date()
        date_obj = datetime.datetime(y, m, d, h, mi, s, ms)
        try:
            print_pair_rate(base_cur, dest_cur, rate.get_rate(base_cur, dest_cur, date_obj))
        except:
            print("An error occured")
    else:
        try:
            print_pair_rate(base_cur, dest_cur, rate.get_rate(base_cur, dest_cur))
        except:
            print("An error occured")
    menu("Check exchange rate again", two_pairs_exchange)


def fiat_exchange():
    print("Select Option: \n \
            [1] See all latest currency rates for one currency\n \
            [2] Check exchange rate between two pairs\n \
            [3] Convert an amount in one currency to another")
    ans = int(get_valid_response("Enter response: ", "123"))

    if ans == 1:
        latest_currencies()
    elif ans == 2:
        two_pairs_exchange()
    else:
        convert_amount()

def input_currency(text):
    code = CurrencyRates()
    cur = input(text).strip().upper()
    try:
        c = code.get_rates(cur)
        return cur
    except:
        print(f'{cur} not found. Try again')
        cur = input_currency(text)
        return cur

def input_float(text):
    try:
        amount = float(input(text).strip())
        return amount
    except:
        print("The amount you entered isn't valid! Try again")
        amount = input_float(text)
        return amount
