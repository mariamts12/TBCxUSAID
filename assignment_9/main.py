from assignment_9.score_analyzer import ScoreAnalyzer
FILENAME = "student_scores_random_names.csv"
EXCEL_FILE = "average_class_grade_per_semester.xlsx"


def main() -> None:
    grade_analyzer = ScoreAnalyzer(FILENAME)
    failed = grade_analyzer.failed_one_or_more_class()
    print("Students that failed at least one class:\n", failed)

    average_class_score_per_semester = grade_analyzer.average_class_score_per_semester()
    print("\nAverage score for each class per semester:\n", average_class_score_per_semester)

    highest_scores = grade_analyzer.students_with_highest_average_scores()
    print("\nStudent(s) with highest average scores:\n", highest_scores)

    class_with_lowest_average = grade_analyzer.class_with_lowest_average_score()
    print("\nClass(es) with lowest average scores:")
    for subject, avg in class_with_lowest_average.items():
        print(f"{subject}: {avg}")

    grade_analyzer.to_excel(average_class_score_per_semester, EXCEL_FILE)

    grade_analyzer.average_grade_diagram()
    grade_analyzer.overall_average_linear_diagram()


if __name__ == "__main__":
    main()
