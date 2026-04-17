"""
Program to search for a country in a list and return its index.

Prompts the user to enter a list of countries and a country to search.
Returns the index of the country if found, or a message if not found.
"""

NOT_FOUND_MESSAGE = "Not Found in List"


def search_country(countries, country):
    if country in countries:
        return countries.index(country)
    return NOT_FOUND_MESSAGE


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("\n  ERROR: Please enter a positive number.")
        except ValueError:
            print("\n  ERROR: Invalid input. Please enter a valid number.")


def get_country_list(n):
    countries = []
    print()
    for i in range(n):
        c = input(f"  Enter country {i + 1} : ")
        countries.append(c)
    return countries


def display_result(search, result):
    print("\n" + "=" * 50)
    print("           COUNTRY SEARCH RESULT")
    print("=" * 50)
    print()
    print(f"  Searching for : {search}")
    print("-" * 50)
    print(f"  Result        : {result}")
    print("=" * 50)


def main():
    print("\n" + "=" * 50)
    print("       COUNTRY SEARCH PROGRAM")
    print("=" * 50)
    print()
    
    n = get_positive_integer("  Enter number of countries : ")
    countries = get_country_list(n)
    
    print()
    search = input("  Enter country to search : ")
    print()
    
    result = search_country(countries, search)
    display_result(search, result)


if __name__ == "__main__":
    main()