# Score Analyzer

## Overview

**Score Analyzer** is a Python project designed to analyze and visualize student performance data from multiple semesters and subjects. By leveraging the Pandas library, this tool processes student scores to uncover valuable insights, such as overall trends in academic performance, areas where students struggle, and identifying top-performing students.



## Features

- **Student Performance Analysis**: Identifies students who did not pass any subject (score < 50).
- **Average Score Calculation**: Computes average scores for each subject per semester.
- **Top Performers**: Identifies students with the highest average scores across all subjects and semesters.
- **Subject Difficulty Analysis**: Finds the subject where students struggled the most based on the lowest average score.
- **Excel Export**: Generates an Excel file containing average scores per semester for further analysis.
- **Data Cleaning**: Handles missing values and replaces negative scores with NaN for accurate analysis.

## Visualizations

The project includes the following visualizations to represent the data graphically:

- **Bar Chart**: Displays average scores for each subject across all semesters, making it easy to compare performance.
- **Line Graph**: Shows the overall average scores per semester, highlighting trends in student performance over time.

## Dependencies

- **Python 3.11**
- **pandas**: For data manipulation and analysis.
- **openpyxl**: For reading and writing Excel files.
- **matplotlib**: For creating visualizations.

You can install these dependencies using pip:

```bash
pip install pandas openpyxl matplotlib
