class Smoother:
    """
    Smooths mouse movement to avoid jitter
    using exponential moving average
    """
    def __init__(self, smoothing_factor=7):
        self.smoothing_factor = smoothing_factor
        self.prev_x = 0
        self.prev_y = 0

    def smooth(self, x, y):
        smooth_x = self.prev_x + (x - self.prev_x) / self.smoothing_factor
        smooth_y = self.prev_y + (y - self.prev_y) / self.smoothing_factor

        self.prev_x = smooth_x
        self.prev_y = smooth_y

        return smooth_x, smooth_y
