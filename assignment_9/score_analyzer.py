from dataclasses import dataclass
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


@dataclass
class ScoreAnalyzer:
    filename: str

    def __post_init__(self) -> None:
        self.df = pd.read_csv(self.filename)
        self.clean_data()
        # pd.set_option('display.max_rows', None)
        # pd.set_option('display.max_columns', None)

    def clean_data(self) -> None:
        numeric_cols = self.df.select_dtypes(include=['number'])
        self.df[numeric_cols.columns] = numeric_cols.where(numeric_cols >= 0, np.nan)
        self.df.dropna(how='all', inplace=True)

    def failed_one_or_more_class(self) -> list:
        result = self.df.loc[(self.df.iloc[:, 2:] < 50).any(axis=1), ['Student']]
        return result

    def average_class_score_per_semester(self):
        return self.df.groupby("Semester").mean(numeric_only=True).round(2)

    def students_with_highest_average_scores(self) -> dict:
        temp = self.df.groupby("Student").mean(numeric_only=True).round(2)
        temp['average'] = temp.mean(axis=1).round(2)
        max_average = temp['average'].max()
        students_with_max_average = temp[temp['average'] == max_average]
        return students_with_max_average

    def class_with_lowest_average_score(self) -> dict:
        temp = self.df.groupby("Semester").mean(numeric_only=True).round(2)
        average = temp.mean(axis=0).round(2)
        min_avg = average.min()
        return average[average == min_avg]

    def overall_average(self):
        temp = self.df.groupby("Semester").mean(numeric_only=True).round(2)
        return temp.mean(axis=1).round(2)

    def average_grade_diagram(self) -> None:
        average = self.average_class_score_per_semester()
        average.index = range(1, len(average) + 1)
        average.plot(kind='bar', figsize=(10, 6))
        plt.ylim(0, 100)
        plt.title('Average Scores for each Subject per Semester')
        plt.ylabel('Average Score')
        plt.xlabel('Semester')
        plt.show()

    def overall_average_linear_diagram(self) -> None:
        overall_avg = self.overall_average()
        overall_avg.index = range(1, len(overall_avg) + 1)
        overall_avg.plot(kind='line', marker='o')
        plt.title('Overall Average Score per Semester')
        plt.ylabel('Average Score')
        plt.xlabel('Semester')
        plt.show()

    @staticmethod
    def to_excel(df, filename) -> None:
        try:
            df_reset = df.reset_index()
            df_reset.to_excel(filename, index=False)
            print(f"\nDataFrame successfully saved to {filename}")
        except Exception as e:
            print(f"\nAn error occurred while saving to Excel: {e}")
