from utils import shared_state
import cv2
import numpy as np
import pyautogui

from modules.hand_tracking import HandTracker
from modules.gesture_recognition import is_click
from modules.mouse_controller import MouseController
from modules.voice_control import VoiceController
from utils.smoothing import Smoother
from config.settings import *

print("MAIN.PY IS RUNNING")

# Camera setup
cap = cv2.VideoCapture(0)
cap.set(3, CAMERA_WIDTH)
cap.set(4, CAMERA_HEIGHT)

screen_w, screen_h = pyautogui.size()

# Initialize modules
tracker = HandTracker()
mouse = MouseController(screen_w, screen_h)
smoother = Smoother(SMOOTHING_FACTOR)

# 🔊 Start voice control
voice = VoiceController()

try:
    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        results = tracker.find_hands(frame)

        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]
            h, w, _ = frame.shape

            index_tip = hand.landmark[8]
            thumb_tip = hand.landmark[4]

            ix, iy = int(index_tip.x * w), int(index_tip.y * h)
            tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)

            screen_x = np.interp(
                ix, (SCREEN_PADDING, w - SCREEN_PADDING), (0, screen_w)
            )
            screen_y = np.interp(
                iy, (SCREEN_PADDING, h - SCREEN_PADDING), (0, screen_h)
            )

            smooth_x, smooth_y = smoother.smooth(screen_x, screen_y)

            # 🟢 MOVE ONLY WHEN NO VOICE COMMAND
            if not shared_state.voice_action_active:
                mouse.move(smooth_x, smooth_y)

                # 🟢 Gesture click ONLY when voice inactive
                if is_click((ix, iy), (tx, ty), CLICK_DISTANCE):
                    mouse.click()

        tracker.draw_hands(frame, results)
        cv2.imshow("Gesture Virtual Mouse", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

except KeyboardInterrupt:
    print("Exiting gracefully")

finally:
    cap.release()
    cv2.destroyAllWindows()
