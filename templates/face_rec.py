import cv2
import threading
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

ref_img = cv2.imread("C:\\Users\\sumag\\face_rec\\data\\test\\suma\\suma156.jpg")

def check_face(frame):
  global face_match
  try:
    #to check if the live video matches with the image stored in database
    if DeepFace.verify(frame, ref_img.copy())['verified']:
      face_match = True
    else:
      face_match = False
  except ValueError:
    face_match = False

def video_stream():
  while True:
    ret, frame = cap.read()

    if ret:
      #After 30 frames
      if counter%30 == 0:
        #check if the frame (live) matches the image (ref)
        try:
          threading.Thread(target = check_face, args = (frame.copy(), ) )
        except ValueError:
          #As deepface throws a value error incase the face is not recognised, we are writing a value error block
          pass

      counter+=1

      if face_match:
        cv2.putText(frame, "Face Matched", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
      else:
        cv2.putText(frame, "Face Not Matched", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)

      cv2.imshow("Video", frame)


    key = cv2.waitKey(1)
    if key == ord("q"):
      break
# cv2.destroyAllWindows()
    

from flask import Flask,render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(video_stream(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)