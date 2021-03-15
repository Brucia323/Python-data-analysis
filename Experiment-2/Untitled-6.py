def CalculationOfInterest(principal, rate, year):
    """计算利息

    Args:
        principal (int): 本金
        rate (float): 年利率
        year (int): 存款年限

    Returns:
        float: 利息
    """
    return principal*rate*year


print(CalculationOfInterest(10000, 0.055, 5))
print(CalculationOfInterest(10000, 0.035, 3))
