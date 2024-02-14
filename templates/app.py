import os
import datetime
import cv2
from flask import Flask,jsonify,render_template,request
import face_recognition
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register', methods = ["POST"])
def register():
  start = request.form.get("Start")
  photo = request.files['photo']

  uploads_folder = os.path.join(os.getcwd(),"static","uploads")
  if not os.path.exists(uploads_folder):
    os.makedirs(uploads_folder)

  photo.save(os.path.join(uploads_folder, ))

  return render_template()
print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True,port=8080)