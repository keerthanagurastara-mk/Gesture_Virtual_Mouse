# tests/test_gestures.py

from modules.gesture_recognition import distance

def test_distance():
    assert distance((0, 0), (3, 4)) == 5
