def pos_or_neg(value: int) -> int:
    """Отрицательное, положительное или ноль?"""
    if value < 0:
        return -1
    if value == 0:
        return 0
    return 1

