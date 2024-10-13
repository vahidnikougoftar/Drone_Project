from djitellopy import Tello
import cv2
import pyttsx3

class FaceDetectionDrone:
    def __init__(self):
        self.tello = Tello()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.engine = pyttsx3.init()
        self.hello_said = False

    def connect(self):
        self.tello.connect()
        print(f"Battery level: {self.tello.get_battery()}%")
        self.tello.streamon()

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return self.face_cascade.detectMultiScale(gray, 1.1, 4)

    def process_frame(self, frame):
        faces = self.detect_faces(frame)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            if not self.hello_said:
                self.engine.say("hello world")
                self.engine.runAndWait()
                self.hello_said = True
        return frame

    def run(self):
        self.connect()
        while True:
            frame = self.tello.get_frame_read().frame
            frame = cv2.resize(frame, (640, 480))
            frame = self.process_frame(frame)
            cv2.imshow("Tello Video Stream", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cleanup()

    def cleanup(self):
        self.tello.streamoff()
        cv2.destroyAllWindows()
        self.tello.end()

if __name__ == "__main__":
    drone = FaceDetectionDrone()
    drone.run()
