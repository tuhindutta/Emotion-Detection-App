# 🎭 Emotion Detection App
A real-time emotion analysis application that detects human faces in a video and visualizes their emotional states through live graphs.

## 📌 Overview
Emotion Detection App is a Flask-based web application that processes user-uploaded video files to:
- Detect faces in each frame.
- Analyze the emotions of detected faces.
- Render the results as live emotion-labeled video frames.
- Display accompanying emotion probability graphs for each person.
- This project is ideal for experimenting with real-time video analytics, emotion recognition, and basic data visualization in computer vision pipelines.

## 🚀 Features
- 🎥 Upload and analyze any .mp4 video.
- 🤖 Detect multiple faces using MediaPipe.
- 😄 Identify emotions (e.g., happy, sad, angry, surprised, etc.) using deep learning.
- 📊 Real-time emotion graph generation per individual.
- 📁 Store emotion trends as JSON logs.
- 📡 Stream analyzed video with emotion graphs in-browser.

## 🧰 Technologies Used
<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>Tech Stack</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Language</td>
      <td>Python</td>
    </tr>
    <tr>
      <td>Backend</td>
      <td>Flask 3.1.0</td>
    </tr>
    <tr>
      <td>Computer Vision</td>
      <td>OpenCV, MediaPipe</td>
    </tr>
    <tr>
      <td>Emotion Detection</td>
      <td>DeepFace</td>
    </tr>
    <tr>
      <td>Visualization</td>
      <td>Custom OpenCV drawing and Matplotlib graphs</td>
    </tr>
    <tr>
      <td>Packaging</td>
      <td>Docker</td>
    </tr>
  </tbody>
</table>



## 🗂️ Project Structure
```env
emotion_detection_app/
│
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── uploads/
│   │   └── test.mp4
│   ├── customImageConcat.py
│   ├── detectFace.py
│   ├── main.py
│   └── requirements.txt
│
├── Dockerfile
├── README.md
```

## ⚙️ Setup Instructions
### 🐳 Dockerized Deployment (Docker Image: tkdutta/emotiondetector)
1. Run the container
  ```bash
  docker run -d -p 5000:5000 --name emotiondetector2 --mount type=bind,source=${PWD}/my-data,destination=/app/uploads tkdutta/emotiondetector:v1.0-ubuntu22.04
  ```
2. Open your browser and go to:
   ```url
   http://localhost:5000
   ```

## 🧠 Core Logic Explained
- Face Detection: Uses MediaPipe to detect faces frame-by-frame.
- Emotion Analysis: For each detected face, the DeepFace model predicts emotions.
- Visualization: Live graph generation using OpenCV's custom rendering based on emotion probabilities.
- Data Persistence: Saves per-frame emotion probability for each person into a data.json file inside /uploads.

## 🚧 Limitations
- Works best on clear, front-facing video footage.
- Limited to predefined emotion categories.
- Assumes moderate lighting and stable camera conditions.

## 🌐 Future Improvements
- Integrate audio sentiment analysis.
- Add login and emotion history dashboard.
- Expand emotion categories using transformers.
- Support webcam-based live stream input.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes. For more details and updates, visit the [GitHub Repository](https://github.com/tuhindutta/Emotion-Detection-App).
