def evaluate_p_value(p_value: float, alpha: float = 0.05) -> str:
    """
    Return 'reject' if p_value <= alpha, else return 'fail to reject'.
    """
    if p_value <= alpha:
        return "reject"
    return "fail to reject"