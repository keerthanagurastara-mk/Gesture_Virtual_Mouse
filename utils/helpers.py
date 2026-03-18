# utils/helpers.py

def clamp(value, min_value, max_value):
    """
    Restrict a value between min_value and max_value
    """
    return max(min_value, min(value, max_value))
