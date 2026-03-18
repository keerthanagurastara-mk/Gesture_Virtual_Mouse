# 🖱️ Gesture Virtual Mouse

A real-time gesture-controlled virtual mouse built using **OpenCV** and **MediaPipe**, allowing users to control the system cursor using hand movements captured via webcam.

![Demo](assets/demo.gif)

---

## 🚀 Overview

This project uses computer vision techniques to detect and track hand movements in real-time. By interpreting specific gestures, it enables users to perform mouse operations such as moving the cursor, clicking, and controlling the system without physical input devices.

---

## ✨ Features

* 🎯 Real-time hand tracking using OpenCV & MediaPipe
* 🖐️ Gesture-based mouse control
* ⚡ Smooth and responsive cursor movement
* 🧩 Modular and scalable architecture
* 🎤 Optional voice control integration

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* PyAutoGUI (for mouse control)

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/keerthanagurastara-mk/Gesture_Virtual_Mouse.git
cd Gesture_Virtual_Mouse
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Make sure your webcam is enabled.

---

## 📁 Project Structure

```
Gesture_Virtual_Mouse/
│
├── main.py                # Entry point
├── requirements.txt      # Dependencies
├── README.md
│
├── assets/               # Demo and media files
│   └── demo.gif
│
├── config/               # Configuration settings
│   └── settings.py
│
├── modules/              # Core functionalities
│   ├── hand_tracking.py
│   ├── gesture_recognition.py
│   ├── mouse_controller.py
│   └── voice_control.py
│
├── utils/                # Helper functions
│   ├── helpers.py
│   ├── smoothing.py
│   └── shared_state.py
│
└── tests/                # Test cases
    └── test_gestures.py
```

---

## 🧠 How It Works

1. Captures video from webcam
2. Detects hand landmarks using MediaPipe
3. Interprets gestures based on finger positions
4. Maps gestures to mouse actions
5. Executes actions using system control

---

## 🚧 Future Improvements

* 🤖 Machine Learning-based gesture classification
* 🖥️ GUI interface for better usability
* 🎯 Improved accuracy and performance optimization
* 📱 Cross-platform compatibility

---

## 📌 Use Cases

* Touchless computer interaction
* Accessibility for physically challenged users
* Interactive presentations
* Smart environments

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
