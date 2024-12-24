from flask import Flask, render_template, request, Response, redirect, url_for
import cv2
import time
import os
from detectFace import *
from customImageConcat import custom_concat
from functools import reduce
import json

app = Flask(__name__)
face = FaceDetect()
emotion = EmotionAnalyze()
visualize = emotionVisualize()
# records = []

@app.route('/')
def index():
    return render_template('index.html')



def gen(video_path, width=1200, height=400, data_path='./uploads/data.json'):
    # global records
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file")
        return None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break  
        frame = face.drawBbox(frame)
        frame, emots = emotion.labelEmotion(frame)
        frame = cv2.resize(frame, (700,500))

        if emots:
            graphs = []
            num_persons = len(emots)
            for person,emot in emots.items():
                visualize.visualize(person, emot)
                graph = visualize.plane
                graph_length, graph_width = graph.shape[:2]
                graph = cv2.resize(graph, (int(graph_length/num_persons), int(graph_width/num_persons)))
                graphs.append(graph)

                if not os.path.exists(data_path):
                    json_object = json.dumps({}, indent=4)
                    with open(data_path, "w") as outfile:
                        outfile.write(json_object)
                with open(data_path, "r") as openfile:
                    records = json.load(openfile)
                    if (str(person+1) not in list(records.keys())) or (len(records)==0):
                        records[str(person+1)] = [emot]    
                    else:
                        records[str(person+1)].append(emot)
                json_object = json.dumps(records, indent=4)
                with open(data_path, "w") as outfile:
                    outfile.write(json_object)

            if len(graphs) <= 10:
                emot_graph = custom_concat(*graphs) if num_persons > 1 else graphs[0]
            else:
                emot_graph = custom_concat(*graphs[:10]) if num_persons > 1 else graphs[0]
        else:
            visualize.visualize("unknown", dict(zip(list(visualize.line_angles.keys())[:-1], [0,0,0,0,0,0,0])))
            emot_graph = visualize.plane

        emot_graph = cv2.resize(emot_graph, (500,500))
        frame = np.concatenate((frame, emot_graph), axis=1)
        frame = cv2.resize(frame, (width, height))
        ret, jpeg_data = cv2.imencode('.jpg', frame)
        if ret:
            jpeg_data = jpeg_data.tobytes()

        # time.sleep(0.07)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg_data + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    video_path = request.args.get('video_path')
    return Response(gen(video_path), mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return "No file part", 400
    
    video_file = request.files['video']
    if video_file.filename == '':
        return "No selected file", 400
    
    video_filename = video_file.filename
    video_path = os.path.join('./uploads', video_filename)
    
    if not os.path.exists('./uploads'):
        os.makedirs('./uploads')
    
    # video_file.save(video_path)

    return render_template('index.html', video_path=video_path)



if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)
