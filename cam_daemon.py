from flask import Flask, render_template, Response
from picamera2 import Picamera2
import cv2
import numpy as np
import time

app = Flask(__name__)

# Initialize the camera using picamera2 (proper for Raspberry Pi Camera Module v3)
picam2 = Picamera2()

# Configure the camera for Full HD
camera_config = picam2.create_still_configuration(
    main={"size": (1920, 1080), "format": "RGB888"},
    lores={"size": (640, 480), "format": "YUV420"}
)
picam2.configure(camera_config)
picam2.start()

# Allow camera to warm up
time.sleep(2)

def generate_frames():
    while True:
        # Get frame from picamera2
        frame = picam2.capture_array()
        
        # Convert from BGR to RGB if needed (depends on your picamera2 output)
        if frame is not None:
            frame = frame[100:,450:-500,:]
            # Add text overlay
            cv2.putText(frame, '|---|', (860, 900), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.putText(frame, '122,84um', (790, 950), cv2.FONT_HERSHEY_SIMPLEX, 
                        1, (255, 255, 255), 2, cv2.LINE_AA)
            #add "+" on the center
            cv2.putText(frame, '+', (470,550), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255,255,255), 3, cv2.LINE_AA)
            
            # Encode frame to JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            
            # Yield the frame in the format expected by Flask's Response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        
        # Small delay to control frame rate
        time.sleep(0.03)  # ~30fps

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True)
