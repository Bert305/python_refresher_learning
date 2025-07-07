import cv2
import mediapipe as mp

# Initialize MediaPipe Hands.
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Start webcam.
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for a later selfie-view display.
        frame = cv2.flip(frame, 1)
        h, w, c = frame.shape

        # Convert the BGR image to RGB.
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        finger_count = 0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # List of tip landmarks for each finger.
                finger_tips = [8, 12, 16, 20]
                thumb_tip = 4

                # Get landmark positions.
                landmarks = hand_landmarks.landmark

                # Check fingers (excluding thumb).
                for tip in finger_tips:
                    if landmarks[tip].y < landmarks[tip - 2].y:
                        finger_count += 1

                # Check thumb (compare x for right hand, y for left hand).
                if landmarks[thumb_tip].x > landmarks[thumb_tip - 1].x:
                    finger_count += 1

                # Draw hand landmarks.
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display finger count.
        cv2.putText(frame, f'Fingers: {finger_count}', (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

        cv2.imshow('Finger Counter', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()