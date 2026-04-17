"""
Program to copy content from one file to another.

Reads from an input file and copies the content into an output file.
The input and output file names are entered by the user. Uses try/except
to handle exceptions: displays error if input file does not exist,
and if output file already exists.
"""


def get_filename(prompt):
    return input(prompt)


def copy_file_content(src, dst):
    try:
        with open(src, "r", encoding="utf-8") as fin:
            content = fin.read()

        try:
            with open(dst, "x", encoding="utf-8") as fout:
                fout.write(content)
            
            print("\n" + "=" * 50)
            print("         FILE COPIED SUCCESSFULLY")
            print("=" * 50)
            print()
            print(f"  Source File      : {src}")
            print(f"  Destination File  : {dst}")
            print(f"  Characters copied : {len(content)}")
            print("=" * 50)

        except FileExistsError:
            print("\n----------------------------------------------------")
            print(f"  ERROR: Output file '{dst}' already exists.")
            print("----------------------------------------------------")

    except FileNotFoundError:
        print("\n----------------------------------------------------")
        print(f"  ERROR: Input file '{src}' does not exist.")
        print("----------------------------------------------------")

    except Exception as e:
        print("\n----------------------------------------------------")
        print(f"  ERROR: Unexpected error occurred - {e}")
        print("----------------------------------------------------")


def main():
    print("\n" + "=" * 50)
    print("       FILE COPY PROGRAM")
    print("=" * 50)
    print()
    
    src = get_filename("  Enter input file name  : ")
    print()
    dst = get_filename("  Enter output file name : ")
    
    copy_file_content(src, dst)


if __name__ == "__main__":
    main()