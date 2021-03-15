import numpy


def manhattan(rating1, rating2):
    """曼哈顿距离

    Args:
        rating1 (numpy.array): [description]
        rating2 (numpy.array): [description]

    Returns:
        int: [description]
    """
    distance = sum(abs(rating1-rating2))
    return distance


def distEclud(vecA, vecB):
    """欧氏距离

    Args:
        vecA (numpy.array): [description]
        vecB (numpy.array): [description]

    Returns:
        double: [description]
    """
    return numpy.sqrt(sum(pow(vecA-vecB, 2)))


first = numpy.array([1, 1])
second = numpy.array([3, 4])
print(manhattan(first, second))
print(distEclud(first, second))
