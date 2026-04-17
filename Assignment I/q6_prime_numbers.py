"""
Program to find and display all prime numbers within a user-defined range.

Prompts the user for the start and end of the range, then displays:
- All prime numbers in that range
- Count of prime numbers
- Sum of all prime numbers
"""


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]


def display_results(start, end, primes):
    print("\n" + "=" * 55)
    print("            PRIME NUMBERS IN RANGE")
    print("=" * 55)
    print()
    print(f"  Range           : {start} to {end}")
    print(f"  Prime Numbers  : {primes}")
    print("-" * 55)
    print(f"  Count           : {len(primes)}")
    print(f"  Sum             : {sum(primes)}")
    print("=" * 55)


def get_range_input():
    print("\n  Enter the range limits:")
    start = int(input("  Start of range  : "))
    end = int(input("  End of range    : "))
    return start, end


def main():
    print("\n" + "=" * 55)
    print("         PRIME NUMBERS FINDER PROGRAM")
    print("=" * 55)
    
    start, end = get_range_input()
    primes = find_primes_in_range(start, end)
    display_results(start, end, primes)


if __name__ == "__main__":
    main()