"""
Program to manage and display movie details.

Prompts the user to enter details for multiple movies (title, director,
release year, rating), stores them in a dictionary, and displays the
information in a well-formatted manner.
"""


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("\n  ERROR: Please enter a positive number.")
        except ValueError:
            print("\n  ERROR: Invalid input. Please enter a valid number.")


def get_valid_year(prompt):
    while True:
        year_str = input(prompt).strip()
        if year_str.isdigit():
            return int(year_str)
        print("\n  ERROR: Please enter a valid year.")


def get_valid_rating(prompt):
    while True:
        rating_str = input(prompt).strip()
        try:
            rating = float(rating_str)
        except ValueError:
            print("\n  ERROR: Please enter a numeric rating.")
            continue
        if 0 <= rating <= 10:
            return rating
        print("\n  ERROR: Rating must be between 0 and 10.")


def get_movie_details(num):
    movies = []
    print()
    for i in range(1, num + 1):
        print(f"  Enter details for movie {i}:")
        print("  " + "-" * 30)
        title = input("  Title         : ").strip()
        director = input("  Director      : ").strip()
        year = get_valid_year("  Release Year  : ")
        rating = get_valid_rating("  Rating (0-10) : ")
        
        movies.append({
            "title": title,
            "director": director,
            "year": year,
            "rating": rating,
        })
        print()
    return movies


def display_movies(movies):
    print("\n" + "=" * 50)
    print("           MOVIE DETAILS")
    print("=" * 50)
    print()
    
    for idx, m in enumerate(movies, start=1):
        print(f"  Movie {idx}")
        print(f"  " + "-" * 35)
        print(f"  Title         : {m['title']}")
        print(f"  Director      : {m['director']}")
        print(f"  Release Year  : {m['year']}")
        print(f"  Rating        : {m['rating']:.1f}")
        print("  " + "-" * 35)
        print()


def main():
    print("\n" + "=" * 50)
    print("       MOVIE DETAILS MANAGER")
    print("=" * 50)
    print()
    
    while True:
        try:
            num_movies = get_positive_integer("  How many movies would you like to add? ")
            if num_movies > 0:
                break
            print("\n  ERROR: Please enter a positive number.")
        except ValueError:
            print("\n  ERROR: Please enter a valid number.")

    movies = get_movie_details(num_movies)
    display_movies(movies)


if __name__ == "__main__":
    main()