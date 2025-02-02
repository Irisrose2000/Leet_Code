"""
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.
"""






import sys

def create_phone_book(n):
    phone_book = {}
    for _ in range(n):
        name, number = sys.stdin.readline().strip().split()
        phone_book[name] = number
    return phone_book

def query_phone_book(phone_book):
    for line in sys.stdin:
        name = line.strip()
        if name in phone_book:
            print(f"{name}={phone_book[name]}")
        else:
            print("Not found")

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    phone_book = create_phone_book(n)
    query_phone_book(phone_book)
