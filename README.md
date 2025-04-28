# emotion_detection_app

Use the following command to pull and run the container locally. A local directory (eg. "${PWD}/my-data") is needed to be mounted to the container to access the video files and return JSON data.

`docker run -d -p 5000:5000 --name emotiondetector2 --mount type=bind,source=${PWD}/my-data,destination=/app/uploads tkdutta/emotiondetector:v1.0-ubuntu22.04`

The application can be accessed in any browser locally through port `5000` in the above case.

Docker image: tkdutta/emotiondetector
