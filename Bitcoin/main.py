#!/usr/bin/python3
import forex
import btc


def main():
    print("Looking for:")
    ans = input("[1] Fiat exchange rates or [2] Bitcoin exchanges rates?(1/2) ").strip()
    while ans not in "12":
        print("Invalid choice: Enter 1 or 2")
        ans = input("[1] Fiat exchange rates or [2] Bitcoin exchanges rates?(1/2) ").strip()
    ans = int(ans)
    if ans == 1:
        forex.fiat_exchange()
    else:
        btc.btc_exchange()


if __name__ == "__main__":
    main()
    print("Thank you for using Jeff.co :)")
