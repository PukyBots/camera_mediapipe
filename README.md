# GestureDrive Robot Car

Control a robot car using finger recognition with MediaPipe, Python, and Arduino.

---

## Repository Name

GestureDrive-RobotCar

---

## Project Overview

GestureDrive Robot Car is a computer vision-based robotics project that allows you to control a robot car using hand gestures (finger counting).

<p align="center">
  <img src="images/img1.png" width="400">
</p>


### Technologies Used

- Laptop / Raspberry Pi Camera  
- MediaPipe (Google)  
- Python  
- PySerial  
- Arduino  
- L298N Motor Driver  

---

## Objective

The goal of this project is to:

- Detect human hand gestures  
- Recognize number of fingers  
- Convert gestures into motion commands  
- Control robot motors wirelessly  


<p align="center">
  <img src="images/img4.jpeg" width="400">
</p>



---

## Project Structure

```
GestureDrive-RobotCar/
│
├── simple_cam.py
├── mediapipe_cam.py
├── fingers.py
├── fingers_print.py
├── fingers_motors.py
├── requirements.txt
└── README.md
```

---

## File Description

### simple_cam.py
Opens the camera to test if it is working properly.

### mediapipe_cam.py
Uses MediaPipe to detect hand landmarks and display them.

### fingers.py
Counts the number of fingers shown to the camera.

### fingers_print.py
Converts finger count into motion commands:

| Fingers | Command | Action |
|---------|----------|--------|
| 1 | F | Forward |
| 2 | B | Backward |
| 3 | L | Left |
| 4 | R | Right |
| 5 | S | Stop |

### fingers_motors.py
Sends motion commands to Arduino using Serial communication to move the robot.

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/yourusername/GestureDrive-RobotCar.git
cd GestureDrive-RobotCar
```

### 2. Create Virtual Environment (Recommended)

Linux / Mac:

```
python3 -m venv venv
source venv/bin/activate
```

Windows:

```
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## Required Libraries (requirements.txt)

```
opencv-python
opencv-contrib-python
mediapipe
pyserial
numpy
```

---

## Arduino Setup

1. Upload motor driver code to Arduino  
2. Connect L298N motor driver  
3. Connect DC motors  
4. Check Serial Port:

```
ls /dev/tty*
```

Common ports:

```
/dev/ttyUSB0
/dev/ttyACM0
```

Update inside Python file if needed:

```
serial.Serial('/dev/ttyUSB0', 9600)
```

---

## How to Run

### Step 1: Test Camera

```
python simple_cam.py
```

### Step 2: Test MediaPipe Detection

```
python mediapipe_cam.py
```

### Step 3: Test Finger Counting

```
python fingers.py
```

### Step 4: Print Motion Commands

```
python fingers_print.py
```

### Step 5: Control Motors

```
python fingers_motors.py
```

---

## Distributed System Architecture (Laptop → RPi → Arduino)

This project supports a distributed robotics architecture where heavy computer vision processing runs on a laptop, and the Raspberry Pi handles motor control.

---

## System Flow

Laptop (MediaPipe Processing)  
→ Sends motion commands over WiFi using Flask (HTTP)  
→ Raspberry Pi receives command  
→ Raspberry Pi sends command via USB Serial  
→ Arduino controls motors  

---

## How It Works (Network Mode)

1. MediaPipe runs on the laptop and detects finger gestures.
2. Based on the number of fingers detected, a motion command is generated:

   - F → Forward  
   - B → Backward  
   - L → Left  
   - R → Right  
   - S → Stop  

3. The laptop sends this command to the Raspberry Pi using an HTTP request.
4. The Raspberry Pi receives the command using a Flask server.
5. The Raspberry Pi forwards the command to Arduino via Serial communication.
6. Arduino drives the motors accordingly.

---

## Why This Architecture?

- No need to install MediaPipe on Raspberry Pi  
- Heavy processing handled by laptop  
- Raspberry Pi remains lightweight  
- Clean separation of vision and control  
- Scalable and industry-style robotics setup  

---

## Network Requirement

- Laptop and Raspberry Pi must be connected to the same WiFi network.
- Raspberry Pi runs a Flask server.
- Laptop sends commands using HTTP requests.

---

## How It Works

1. Camera captures live video  
2. MediaPipe detects hand landmarks  
3. Finger counting algorithm runs  
4. Finger count converts to motion command  
5. Command received by Rpi over Web Socket
6. Command sent via Serial  
7. Arduino controls motors  

---

## Learning Outcomes

- Computer Vision  
- Hand Tracking  
- Serial Communication  
- Embedded Systems  
- Robotics Control  
- Human-Robot Interaction  

---

## Future Improvements

- Add PID speed control  
- Add obstacle detection  
- Add WiFi control  
- Add voice control  
- Deploy fully on Raspberry Pi  

---

## Author

Pulkit Garg  
Master’s in Robotics – University of Lille, France  

---

## License

Open-source for educational purposes.