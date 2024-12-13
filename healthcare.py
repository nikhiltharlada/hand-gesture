import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import sys

dataset = None

def choice(n):
    if n == 1:
        load_dataset()
        print("\n")
    elif n == 2:
        convert_into_df()
        print("\n")
    elif n == 3:
        data_cleaning()
        print("\n")
    elif n == 4:
        overview()
        print("\n")
    elif n == 5:
        feature_engineering()
        print("\n")
    elif n == 6:
        graphs()
        print("\n")
    elif n == 0:
        sys.exit("Exiting the program........!")
    else:
        print("Invalid Choice")
        choice(int(input("Enter your choice again: ")))

def load_dataset():
    global dataset
    dataset = pd.read_csv(input("Enter the path of the file: "))
    print(dataset.head(30))

def convert_into_df():
    global dataset
    if dataset is not None:
        dataset = pd.DataFrame(dataset)
        print("Converted into Data Frame.......")
    else:
        print("Dataset not loaded. Please load the dataset first.")

def data_cleaning():
    global dataset
    if dataset is not None:
        cleaned_dataset = dataset.dropna(inplace=False)
        print("Dataset is cleaned......")
    else:
        print("Dataset not loaded. Please load the dataset first.")

def overview():
    global dataset
    if dataset is not None:
        cleaned_dataset = dataset.dropna(inplace=False)
        print(cleaned_dataset.info())
        print(cleaned_dataset.describe())
    else:
        print("Dataset not loaded. Please load the dataset first.")

def feature_engineering():
    global dataset
    if dataset is not None:
        def calculate_days_between_dates(start_date, end_date):
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            return (end_date - start_date).days

        dataset = dataset.dropna(subset=['Date of Admission', 'Discharge Date'], inplace=False)
        dataset['Treatment Days'] = dataset.apply(
            lambda row: calculate_days_between_dates(row['Date of Admission'], row['Discharge Date']), axis=1
        )
        print("Treatment Days feature created using cleaned_dataset.")
    else:
        print("Dataset not loaded. Please load the dataset first.")

def graphs():
    global dataset
    if dataset is not None:
        dataset = dataset.dropna(inplace=False)
        plt.figure(figsize=(10, 6))
        sns.histplot(dataset['Age'], bins=30, kde=True)
        plt.title('Age Distribution of Patients')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.show()

        plt.figure(figsize=(10, 6))
        sns.histplot(dataset['Treatment Days'], bins=5, kde=True)
        plt.title('Distribution of Treatment Days')
        plt.xlabel('Treatment Days')
        plt.ylabel('Frequency')
        plt.show()

        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='Age', y='Treatment Days', data=dataset, hue='Medical Condition')
        plt.title('Age vs. Treatment Days')
        plt.xlabel('Age')
        plt.ylabel('Treatment Days')
        plt.legend(title='Medical Condition', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.show()

        dataset['Date of Admission'] = pd.to_datetime(dataset['Date of Admission'])
        avg_age_per_day = dataset.groupby(dataset['Date of Admission'].dt.date)['Age'].mean()
        plt.figure(figsize=(10, 6))
        plt.plot(avg_age_per_day.index, avg_age_per_day.values)
        plt.title('Average Age of Patients Over Time')
        plt.xlabel('Date')
        plt.ylabel('Average Age')
        plt.xticks(rotation=45)
        plt.show()

        plt.figure(figsize=(14, 7))
        sns.plot(x='Medical Condition', y='Age', data=dataset, inner='quartile')
        plt.title('Age Distribution by Medical Condition')
        plt.xlabel('Medical Condition')
        plt.ylabel('Age')
        plt.xticks(rotation=90)
        plt.show()

        plt.figure(figsize=(10, 6))
        sns.histplot(dataset['Medical Condition'], discrete=True)
        plt.title('Medical Condition Count')
        plt.xlabel('Medical Condition')
        plt.ylabel('Count')
        plt.show()

        plt.figure(figsize=(14, 7))
        sns.histplot(data=dataset, x='Age', hue='Medical Condition', multiple='stack', bins=20, kde=True)
        plt.title('Age Distribution by Medical Condition')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print("Dataset not loaded. Please load the dataset first.")

if __name__ == "__main__":
    print("Welcome to Healthcare Analysis")
    while True:
        choice(int(input("Enter your choice:\n"
                          "1. Load Dataset\n"
                          "2. Convert into Data Frame\n"
                          "3. Data Cleaning\n"
                          "4. Overview\n"
                          "5. Feature Engineering\n"
                          "6. Graphs\n"
                          "0. Exit\n")))

