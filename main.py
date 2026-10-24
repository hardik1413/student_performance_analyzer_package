"""
Driver Application consuming the performance_analyzer Package
"""

import performance_analyzer as pa


def main():
    print(f"=== STUDENT PERFORMANCE ANALYZER (v{pa.__version__}) ===")

    raw_data =  [
    ('Test1', 40.0),
    ('Test2', 39.9),
    ('Test3', 105.0)
]

    processed_records = []

    for name, raw_score in raw_data:
        is_valid, score = pa.validate_score(raw_score)

        if is_valid:
            grade, gpa = pa.compute_grade(score)

            processed_records.append({
                'name': name,
                'score': score,
                'grade': grade,
                'gpa': gpa
            })

            print(
                f"[ACCEPTED] {name:10s} | Score: {score:5.1f} "
                f"| Grade: {grade:2s} | GPA: {gpa:2d}"
            )

        else:
            print(
                f"[REJECTED] {name:10s} | "
                f"Invalid Score Input: {raw_score}"
            )

    avg_score, pass_pct, top_scorer = pa.analyze_class(
        processed_records
    )

    print("\n--- CLASS ANALYTICS SUMMARY ---")
    print(f"Class Average Score: {avg_score}")
    print(f"Class Pass Rate       : {pass_pct}%")
    print(f"Top Performing Student: {top_scorer}")


if __name__ == '__main__':
    main()