from myutils.l2_norm import l2_norm
import warnings

def dist_point_to_line(p1, p2, p, seg=0):
    """
    Computes the distance between a line segment and a point.
    :param p1: [numpy ndarray] start of line segment
    :param p2: [numpy ndarray] end of line segment
    :param p: [numpy ndarray] point
    :param seg: [0 = distance to line (default), 1 = distance to segment]
    :return: distance between p and line or segment p1p2 and projection point q
    """

    # Check if p1 and p2 are the same
    if l2_norm(p1,p2) == 0:
        warnings.warn("No segment, p1 and p2 are one and the same point!")

    # Get vector from p1 to p2
    a = p2 - p1
    # Get vector from p1 to q
    b = p - p1
    # Get projection scalar
    u = a.dot(b) / l2_norm(p2,p1)**2

    # Check if point lies within segment
    if seg==1 and u<0: return l2_norm(p1,p), p1
    if seg==1 and u>1: return l2_norm(p2,p), p2

    # Point of tangent intersection
    q = p1 + u*a
    # Get distance from p to q
    d = l2_norm(p,q)

    """
    plt.figure()
    plt.plot([p1[0],p2[0]],[p1[1],p2[1]],'b-')
    plt.plot(p[0],p[1],'bo')
    plt.plot(q[0],q[1],'mo')
    """

    return d, q