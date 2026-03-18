import math


def is_click(index_tip, thumb_tip, threshold):
    """
    Detect click gesture based on distance
    between index finger tip and thumb tip
    """
    x1, y1 = index_tip
    x2, y2 = thumb_tip

    distance = math.hypot(x2 - x1, y2 - y1)

    return distance < threshold
