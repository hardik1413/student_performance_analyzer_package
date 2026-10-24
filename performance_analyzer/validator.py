"""
Sub-Module 1: Score Input Validation Engine
"""


def validate_score(score_input):
    """Validates if score is numeric and within bounds [0, 100]."""

    try:
        val = float(score_input)

        if 0.0 <= val <= 100.0:
            return True, val

        return False, 0.0

    except (ValueError, TypeError):
        return False, 0.0