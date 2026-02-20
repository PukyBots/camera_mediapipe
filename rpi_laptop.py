import cv2
import mediapipe as mp
import serial
import time
import requests



RPI_IP = "172.21.7.4"  # Change this

def send_to_rpi(cmd):
    try:
        requests.get(f"http://{RPI_IP}:5000/cmd/{cmd}")
    except:
        print("RPi not reachable")


# MediaPipe setup
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


options = HandLandmarkerOptions(
   base_options=BaseOptions(model_asset_path="hand_landmarker.task"),
   running_mode=VisionRunningMode.VIDEO,
   num_hands=1
)


hand_detector = HandLandmarker.create_from_options(options)


cap = cv2.VideoCapture(0)
frame_id = 0
last_command = ""


def count_fingers(landmarks):
   fingers = 0
   tips = [8, 12, 16, 20]


   for tip in tips:
       if landmarks[tip].y < landmarks[tip - 2].y:
           fingers += 1


   # Thumb
   if landmarks[4].x > landmarks[3].x:
       fingers += 1


   return fingers




while True:
   ret, frame = cap.read()
   if not ret:
       break


   rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


   mp_image = mp.Image(
       image_format=mp.ImageFormat.SRGB,
       data=rgb
   )


   result = hand_detector.detect_for_video(mp_image, frame_id)


   if result.hand_landmarks:
       landmarks = result.hand_landmarks[0]
       finger_count = count_fingers(landmarks)


       cv2.putText(frame, f'Fingers: {finger_count}',
                   (50,100),
                   cv2.FONT_HERSHEY_SIMPLEX,
                   2,
                   (0,255,0),
                   3)


       # Robot Control Logic
       if finger_count == 2 and last_command != "F":
           send_to_rpi('F')
           print("Sent: F")
           last_command = "F"

       elif finger_count == 1 and last_command != "B":
           send_to_rpi('B')
           print("Sent: B")
           last_command = "B"

       elif finger_count == 5 and last_command != "S":
           send_to_rpi('S')
           print("Sent: S")
           last_command = "S"

       elif finger_count == 3 and last_command != "R":
           send_to_rpi('R')
           print("Sent: R")
           last_command = "R"

       elif finger_count == 4 and last_command != "L":
           send_to_rpi('L')
           print("Sent: L")
           last_command = "L"



   cv2.imshow("Finger Count", frame)
   frame_id += 1


   if cv2.waitKey(1) & 0xFF == ord('q'):
       break


cap.release()
cv2.destroyAllWindows()


