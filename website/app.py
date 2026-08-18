import os
from flask import Flask, request, jsonify, render_template
from ultralytics import YOLO
import time
import uuid
import cv2

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'best.pt')
try:
    model = YOLO(MODEL_PATH)
    print("Model YOLO loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model not loaded.'}), 500

    if 'image' not in request.files:
        return jsonify({'error': 'No image provided.'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'Empty filename.'}), 400

    filename = f"{time.strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}.jpg"
    uploads_dir = os.path.join(os.path.dirname(__file__), 'uploads')
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)
        
    save_path = os.path.join(uploads_dir, filename)
    file.save(save_path)

    try:
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        img = cv2.imread(save_path)
        if img is None:
            return jsonify({'error': 'Gambar gagal diproses'}), 400
            
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        if len(faces) == 0:
            return jsonify({'error': 'Objek bukan wajah manusia (gagal dideteksi oleh OpenCV)'}), 400

        results = model.predict(source=save_path, conf=0.25)

        if len(results) == 0 or len(results[0].boxes) == 0:
            return jsonify({'error': 'Emosi tidak dapat diprediksi oleh YOLO'}), 400

        box = results[0].boxes[0]
        class_id = int(box.cls[0].item())
        confidence = box.conf[0].item()
        class_names = model.names

        scores = {
            'angry': confidence if class_names[class_id] in ['anger', 'angry'] else (1-confidence)/2,
            'happy': confidence if class_names[class_id] == 'happy' else (1-confidence)/2,
            'sad': confidence if class_names[class_id] == 'sad' else (1-confidence)/2,
        }

        return jsonify({'scores': scores})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)
