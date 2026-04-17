"""
Program to calculate BMI and Health Status from health data.

Reads data from 'health_data.csv' into a Pandas DataFrame, adds two new
columns: BMI and Health_Status. BMI is calculated as Weight / Height^2.
Health_Status is based on BMI values:
- BMI < 18.5: Underweight
- BMI <= 24.9: Healthy range
- BMI <= 29.9: Overweight risk
- BMI <= 34.9: High risk (diabetes/heart disease)
- BMI >= 40: Critical health condition
"""

import pandas as pd


FILENAME = "health_data.csv"
OUTPUT_FILENAME = "health_data_updated.csv"


def load_health_data(filename):
    df = pd.read_csv(filename)

    required_cols = ["Weight", "Height"]
    missing = [col for col in required_cols if col not in df.columns]

    if missing:
        raise ValueError(f"Missing columns in dataset: {missing}")

    return df


def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)


def classify_health_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Healthy range"
    elif bmi <= 29.9:
        return "Overweight risk"
    elif bmi <= 34.9:
        return "High risk (diabetes/heart disease)"
    elif bmi < 40:
        return "High risk (diabetes/heart disease)"
    else:
        return "Critical health condition"


def add_bmi_and_health_status(df):
    df = df.copy()
    df["BMI"] = df.apply(lambda row: calculate_bmi(row["Weight"], row["Height"]), axis=1)
    df["Health_Status"] = df["BMI"].apply(classify_health_status)
    return df


def display_dataframe(df_original, df_updated):
    print("\n" + "=" * 70)
    print("                   DATA ANALYSIS RESULTS")
    print("=" * 70)
    print()
    print("  Original DataFrame:")
    print("-" * 70)
    print(df_original.to_string(index=False))
    print()
    
    print("  Updated DataFrame with BMI and Health Status:")
    print("-" * 70)
    print(df_updated.to_string(index=False))
    print()
    
    print("=" * 70)
    print("                   STATISTICS")
    print("=" * 70)
    print()
    print("  Health Status Distribution:")
    print("-" * 40)
    status_counts = df_updated["Health_Status"].value_counts()
    for status, count in status_counts.items():
        print(f"    {status:30} : {count}")
    print()
    print("-" * 40)
    print("  BMI Statistics:")
    print("-" * 40)
    print(f"    Minimum BMI : {df_updated['BMI'].min()}")
    print(f"    Maximum BMI : {df_updated['BMI'].max()}")
    print(f"    Mean BMI    : {df_updated['BMI'].mean():.2f}")
    print("=" * 70)


def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"\n  Updated data saved to '{filename}'")


def main():
    print("\n" + "=" * 70)
    print("             BMI & HEALTH STATUS ANALYZER")
    print("=" * 70)
    print()
    
    try:
        df_original = load_health_data(FILENAME)
        df_updated = add_bmi_and_health_status(df_original)
        display_dataframe(df_original, df_updated)
        save_to_csv(df_updated, OUTPUT_FILENAME)
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