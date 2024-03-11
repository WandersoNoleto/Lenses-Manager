def is_positive_number(value):
    try:
        number_value = float(value)
        return number_value > 0
    except (ValueError, TypeError):
        return False
