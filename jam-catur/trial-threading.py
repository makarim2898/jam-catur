import cv2
import threading

def camera(camindex, window):
    cap = cv2.VideoCapture(camindex)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow(window, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

thread1 = threading.Thread(target=camera, args=(0, 'Camera 1'), daemon=True)
thread2 = threading.Thread(target=camera, args=(1, 'Camera 2'), daemon=True)
thread1.start()
thread2.start()