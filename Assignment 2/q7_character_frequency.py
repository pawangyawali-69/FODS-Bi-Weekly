"""
Program to count character frequency in a sentence.

This module provides a function that takes a sentence as input and
returns a dictionary showing how many times each character
(excluding spaces) occurs in the sentence.
"""


def key_value(sentence):
    freq = {}
    for char in sentence.lower().replace(" ", ""):
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


def get_sentence_input(prompt):
    return input(prompt)


def display_result(sentence, result):
    print("\n" + "=" * 50)
    print("        CHARACTER FREQUENCY RESULT")
    print("=" * 50)
    print()
    print(f"  Input Sentence : {sentence}")
    print("-" * 50)
    print("  Character Frequency:")
    for char, count in sorted(result.items()):
        print(f"    '{char}' : {count}")
    print("=" * 50)


def main():
    print("\n" + "=" * 50)
    print("       CHARACTER FREQUENCY PROGRAM")
    print("=" * 50)
    print()
    
    sentence = get_sentence_input("  Enter a sentence : ")
    print()
    
    result = key_value(sentence)
    display_result(sentence, result)


if __name__ == "__main__":
    main()