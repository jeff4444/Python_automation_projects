#!/usr/bin/python3
import forex
from forex_python.bitcoin import BtcConverter
import datetime

main = __import__('main').main

# For Bitcoin exchanges (Submain function in this file)
def btc_exchange():
    print("Select Option:\n[1] See price of 1BTC\n[2] Convert to BTC\n[3] Convert from BTC")
    ans = int(forex.get_valid_response("Enter response: ", "123"))
    if ans == 1:
        see_prices()
    elif ans == 2:
        convert_to()
    else:
        convert_from()


# Get latest/recent BTC prices
def see_prices():
    btc = BtcConverter()
    currency = forex.input_currency("Enter currency: ")
    print("[1] Get price as of now, [2] Get price at a specified date and time: ")
    ans = int(forex.get_valid_response("Enter response: ", "12"))
    if ans == 1:
        print_price(1, currency, btc.get_latest_price(currency))
    else:
        y, m, d, h, mi, s, ms = forex.get_valid_date()
        date_obj = datetime.datetime(y, m, d, h, mi, s, ms)
        print_price(currency, btc.get_latest_price(currency, date_obj))
    forex.menu("See prices again", see_prices)


# Convert from Bitcoin to Fiat
def convert_from():
    btc = BtcConverter()
    currency = forex.input_currency("Enter currency: ")
    coins = forex.input_float("Enter number of BTC coins: ")
    print("[1] Get conversion as of now, [2] Get conversion at a specified date and time: ")
    ans = int(forex.get_valid_response("Enter response: ", "12"))
    if ans == 1:
        print_price(coins, currency, btc.convert_btc_to_cur(coins, currency))
    else:
        y, m, d, h, mi, s, ms = forex.get_valid_date()
        date_obj = datetime.datetime(y, m, d, h, mi, s, ms)
        print_price(coins, currency, btc.convert_btc_to_cur_on(coins, currency, date_obj))
    forex.menu("Convert from BTC again", convert_from)


# Convert from Fiat to Bitcoin
def convert_to():
    btc = BtcConverter()
    currency = forex.input_currency("Enter currency: ")
    amount = forex.input_float("Enter amount: ")
    print("[1] Get conversion as of now, [2] Get conversion at a specified date and time: ")
    ans = int(forex.get_valid_response("Enter response: ", "12"))
    if ans == 1:
        print_price_to(amount, currency, btc.convert_to_btc(amount, currency))
    else:
        y, m, d, h, mi, s, ms = forex.get_valid_date()
        date_obj = datetime.datetime(y, m, d, h, mi, s, ms)
        print_price_to(amount, currency, btc.convert_to_btc_on(amount, currency, date_obj))
    forex.menu("Convert to BTC again", convert_to)



''' Helper functions '''

def print_price_to(amt, cur, res):
    print(f'{amt} {cur} = {res} BTC')


def print_price(coin, cur, pr):
    print(f'{coin} BTC = {pr} {cur}')
