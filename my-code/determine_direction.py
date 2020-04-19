
# determine the direction between two-points in 2D
def determine_direction(pt1,pt0):
    x1_0 = pt1[0] - pt0[0]
    y1_0 = pt1[1] - pt0[1]
    segLen = (x1_0**2 + y1_0**2)**0.5
    cosTheta = x1_0/segLen
    sinTheta = y1_0/segLen
    return (cosTheta,sinTheta)