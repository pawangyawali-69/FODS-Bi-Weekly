"""
Program to read health data from CSV and create scatter plots.

Reads data from 'health_data.csv' using Pandas and creates scatter plots
for the following relationships:
- weight vs height
- age vs weight
- height vs age
- gender vs height
- gender vs weight
"""

import pandas as pd
import matplotlib.pyplot as plt


FILENAME = "health_data.csv"
REQUIRED_COLUMNS = ['Weight', 'Height', 'Age', 'Gender']


def load_health_data(filename):
    df = pd.read_csv(filename)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in CSV file: {missing}")

    return df


def prepare_gender_encoding(df):
    df = df.copy()
    df['Gender_Encoded'] = df['Gender'].astype('category').cat.codes
    return df


def create_scatter_plots(df):
    gender_map = dict(enumerate(df['Gender'].astype('category').cat.categories))

    print("\n" + "=" * 50)
    print("       CREATING SCATTER PLOTS...")
    print("=" * 50)
    print()
    print("  Generating plots for:")
    print("    1. Weight vs Height")
    print("    2. Age vs Weight")
    print("    3. Height vs Age")
    print("    4. Gender vs Height")
    print("    5. Gender vs Weight")
    print()

    plt.figure(figsize=(18, 10))

    plt.subplot(2, 3, 1)
    plt.scatter(df['Weight'], df['Height'], alpha=0.7, color='blue')
    plt.xlabel("Weight (kg)")
    plt.ylabel("Height (cm)")
    plt.title("Weight vs Height")

    plt.subplot(2, 3, 2)
    plt.scatter(df['Age'], df['Weight'], alpha=0.7, color='green')
    plt.xlabel("Age")
    plt.ylabel("Weight (kg)")
    plt.title("Age vs Weight")

    plt.subplot(2, 3, 3)
    plt.scatter(df['Height'], df['Age'], alpha=0.7, color='red')
    plt.xlabel("Height (cm)")
    plt.ylabel("Age")
    plt.title("Height vs Age")

    plt.subplot(2, 3, 4)
    plt.scatter(df['Gender_Encoded'], df['Height'], alpha=0.7, color='purple')
    plt.xlabel(f"Gender (0={gender_map[0]}, 1={gender_map[1]})")
    plt.ylabel("Height (cm)")
    plt.title("Gender vs Height")

    plt.subplot(2, 3, 5)
    plt.scatter(df['Gender_Encoded'], df['Weight'], alpha=0.7, color='orange')
    plt.xlabel(f"Gender (0={gender_map[0]}, 1={gender_map[1]})")
    plt.ylabel("Weight (kg)")
    plt.title("Gender vs Weight")

    plt.tight_layout()
    plt.show()
    
    print("  Plots displayed successfully!")
    print("=" * 50)


def main():
    print("\n" + "=" * 50)
    print("       HEALTH DATA VISUALIZATION PROGRAM")
    print("=" * 50)
    print()
    
    try:
        df = load_health_data(FILENAME)
        df = prepare_gender_encoding(df)
        create_scatter_plots(df)
    except FileNotFoundError:
        print("\n----------------------------------------------------")
        print(f"  ERROR: File '{FILENAME}' not found.")
        print("----------------------------------------------------")
    except ValueError as e:
        print("\n----------------------------------------------------")
        print(f"  ERROR: {e}")
        print("----------------------------------------------------")
    except Exception as e:
        print("\n----------------------------------------------------")
        print(f"  ERROR: {e}")
        print("----------------------------------------------------")


if __name__ == "__main__":
    main()