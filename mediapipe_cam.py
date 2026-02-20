import cv2
import mediapipe as mp
import numpy as np


# --- MediaPipe setup ---
BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


options = PoseLandmarkerOptions(
   base_options=BaseOptions(model_asset_path="pose_landmarker.task"),
   running_mode=VisionRunningMode.VIDEO
)


pose = PoseLandmarker.create_from_options(options)


# --- Camera ---
cap = cv2.VideoCapture(0)


frame_id = 0


while True:
   ret, frame = cap.read()
   if not ret:
       break


   # Convert BGR → RGB
   rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


   # Convert to MediaPipe Image
   mp_image = mp.Image(
       image_format=mp.ImageFormat.SRGB,
       data=rgb
   )


   # Detect pose
   result = pose.detect_for_video(mp_image, frame_id)


   # Draw landmarks if detected
   if result.pose_landmarks:
       for landmark in result.pose_landmarks[0]:
           h, w, _ = frame.shape
           cx = int(landmark.x * w)
           cy = int(landmark.y * h)
           cv2.circle(frame, (cx, cy), 5, (0,255,0), -1)


   cv2.imshow("Pose Detection", frame)


   frame_id += 1


   if cv2.waitKey(1) & 0xFF == ord('q'):
       break


cap.release()
cv2.destroyAllWindows()
