import speech_recognition as sr
import pyautogui
import threading
import time
from utils import shared_state


class VoiceController:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.running = True

        threading.Thread(target=self.listen, daemon=True).start()

    def listen(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("🎤 Voice control started")

            # Words that Google often confuses with "click"
            CLICK_ALIASES = [
                "click", "quick", "clique", "cleek", "collect",
                "clicked", "open", "select"
            ]

            while self.running:
                try:
                    audio = self.recognizer.listen(source, timeout=5)
                    command = self.recognizer.recognize_google(audio).lower()
                    print(f"Voice command: {command}")

                    # 🛑 Freeze gesture movement
                    shared_state.voice_action_active = True
                    time.sleep(0.15)  # allow cursor to settle

                    # 🔴 RIGHT CLICK
                    if "right click" in command:
                        pyautogui.rightClick()
                        print("🖱️ Right click")

                    # 🔵 SCROLL
                    elif "scroll down" in command:
                        pyautogui.scroll(-300)
                        print("⬇️ Scroll down")

                    elif "scroll up" in command:
                        pyautogui.scroll(300)
                        print("⬆️ Scroll up")

                    # 🟢 LEFT CLICK (OPEN FILE)
                    elif any(word in command for word in CLICK_ALIASES):
                        pyautogui.click()
                        print("🖱️ Left click (OPEN)")

                    time.sleep(0.6)

                    # ▶️ Resume gesture movement
                    shared_state.voice_action_active = False

                except sr.WaitTimeoutError:
                    continue
                except sr.UnknownValueError:
                    pass
                except Exception as e:
                    print("Voice error:", e)
