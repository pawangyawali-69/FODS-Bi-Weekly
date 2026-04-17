"""
Program to create Dish and Cookbook classes for recipe management.

Creates a Dish class with attributes: dish_id, dish_name, ingredients,
and instructions. Creates a Cookbook class to manage a collection of dishes
with functionalities to add, remove, search, and display dishes.
Dishes are persisted to 'cookbook.txt' file.
"""

import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


FILENAME = "cookbook.txt"


class Dish:
    def __init__(self, dish_id, dish_name, ingredients, instructions):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.instructions = instructions

    def display(self):
        print("\n" + "  " + "-" * 40)
        print(f"  Dish ID     : {self.dish_id}")
        print(f"  Name        : {self.dish_name}")
        print("  Ingredients :")
        for item in self.ingredients:
            print(f"    - {item}")
        print("  Instructions:")
        print(f"    {self.instructions}")
        print("  " + "-" * 40 + "\n")


class Cookbook:
    def __init__(self):
        self.dishes = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(FILENAME, mode="r", encoding="utf-8") as f:
                lines = f.readlines()
            
            i = 0
            while i < len(lines):
                dish_id = lines[i].strip()
                dish_name = lines[i + 1].strip()
                ingredients = [x.strip() for x in lines[i + 2].split(",")]
                instructions = lines[i + 3].strip()
                dish = Dish(dish_id, dish_name, ingredients, instructions)
                self.dishes.append(dish)
                i += 4
        except FileNotFoundError:
            pass
        except Exception as e:
            pass

    def save_to_file(self):
        with open(FILENAME, mode="w", encoding="utf-8") as f:
            for dish in self.dishes:
                f.write(f"{dish.dish_id}\n")
                f.write(f"{dish.dish_name}\n")
                f.write(f"{','.join(dish.ingredients)}\n")
                f.write(f"{dish.instructions}\n")

    def add_dish(self, dish):
        self.dishes.append(dish)
        self.save_to_file()

    def remove_dish(self, dish_id):
        for dish in self.dishes:
            if dish.dish_id == dish_id:
                self.dishes.remove(dish)
                self.save_to_file()
                print("\n" + "=" * 40)
                print("  Dish removed successfully.")
                print("=" * 40)
                return
        print("\n" + "=" * 40)
        print("  Dish not found.")
        print("=" * 40)

    def search_dish(self, name):
        found = False
        for dish in self.dishes:
            if name.lower() in dish.dish_name.lower():
                dish.display()
                found = True
        if not found:
            print("\n" + "=" * 40)
            print("  No matching dish found.")
            print("=" * 40)

    def display_all(self):
        if not self.dishes:
            print("\n" + "=" * 40)
            print("  Cookbook is empty.")
            print("=" * 40)
            return

        print("\n" + "=" * 50)
        print("           COOKBOOK CONTENTS")
        print("=" * 50)
        print(f"  Total Dishes: {len(self.dishes)}")
        print("=" * 50)
        
        for dish in self.dishes:
            dish.display()


def get_dish_input():
    print("  Enter dish details:")
    print("  " + "-" * 35)
    dish_id = input("  Dish ID     : ").strip()
    name = input("  Dish Name   : ").strip()
    ingredients = input("  Ingredients (comma separated) : ").split(",")
    instructions = input("  Instructions : ").strip()

    return Dish(dish_id, name, [i.strip() for i in ingredients], instructions)


def display_menu():
    clear_screen()
    print("\n" + "=" * 40)
    print("           MENU")
    print("=" * 40)
    print("  1. Add Dish")
    print("  2. Remove Dish")
    print("  3. Search Dish")
    print("  4. Display All Dishes")
    print("  5. Exit")
    print("=" * 40)


def get_menu_choice():
    return input("  Enter your choice : ").strip()


def process_menu_choice(choice, cookbook):
    if choice == "1":
        clear_screen()
        dish = get_dish_input()
        cookbook.add_dish(dish)
        print("\n" + "=" * 40)
        print("  Dish added and saved successfully.")
        print("=" * 40)
    elif choice == "2":
        clear_screen()
        dish_id = input("  Enter Dish ID to remove : ").strip()
        cookbook.remove_dish(dish_id)
    elif choice == "3":
        clear_screen()
        name = input("  Enter dish name to search : ").strip()
        cookbook.search_dish(name)
    elif choice == "4":
        clear_screen()
        cookbook.display_all()
    elif choice == "5":
        clear_screen()
        print("\n" + "=" * 40)
        print("  Exiting program... Thank you!")
        print("=" * 40)
        return True
    else:
        clear_screen()
        print("\n" + "=" * 40)
        print("  Invalid choice!")
        print("=" * 40)
    return False


def main():
    clear_screen()
    print("\n" + "=" * 40)
    print("       COOKBOOK MANAGEMENT PROGRAM")
    print("=" * 40)
    
    cookbook = Cookbook()
    if cookbook.dishes:
        print(f"\n  Loaded {len(cookbook.dishes)} dish(es) from file.")

    while True:
        display_menu()
        choice = get_menu_choice()
        if process_menu_choice(choice, cookbook):
            input("\n  Press Enter to exit...")
            break
        input("\n  Press Enter to continue...")


if __name__ == "__main__":
    main()