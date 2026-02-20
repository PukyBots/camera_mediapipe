import cv2
import mediapipe as mp


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


def count_fingers(landmarks):
   fingers = 0


   # Finger tip indexes
   tips = [8, 12, 16, 20]


   for tip in tips:
       if landmarks[tip].y < landmarks[tip - 2].y:
           fingers += 1


   # Thumb (horizontal check)
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
                   (50, 100),
                   cv2.FONT_HERSHEY_SIMPLEX,
                   2,
                   (0,255,0),
                   3)


   cv2.imshow("Finger Count", frame)


   frame_id += 1


   if cv2.waitKey(1) & 0xFF == ord('q'):
       break


cap.release()
cv2.destroyAllWindows()
