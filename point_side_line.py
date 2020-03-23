import numpy as np

def point_side_line(p1, p2, p):
    """
    Computes on which side of the line the point lies.
    :param p1: [numpy ndarray] start of line segment
    :param p2: [numpy ndarray] end of line segment
    :param p: [numpy ndarray] point
    :return: 1 = LEFT side, 0 = ON the line, -1 = RIGHT side
    """

    # Get vector from p1 to p2
    a = p2 - p1
    # Get vector from p1 to q
    b = p - p1
    # The sign of the cross product determines point side
    s = np.sign(np.cross(a,b))

    # s>0 -> LEFT side of the line
    # s=0 -> ON side of the line
    # s<0 -> RIGHT side of the line
    return s