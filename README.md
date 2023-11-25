# Emotify

Emotify is a unique "Music Recommendation System” that seamlessly integrates emotion detection through facial recognition. The model used in this project achieves an accuracy of approximately 72% on the provided dataset.

Click on the image to see the demo video:
[![Emotify Prototype Demo](https://img.youtube.com/vi/qTglMz0Ef_w/maxresdefault.jpg)](https://youtu.be/qTglMz0Ef_w)

The system adapts music recommendations from Spotify based on users’ emotions, identified from 7 distinctive moods:

- Angry
- Disgust
- Fear
- Happy
- Neutral
- Sad
- Surprise

And provides playlists such as:

- Happy
- Sad
- Calm
- Energetic

based on your mood

## Features

- **Facial Emotion Detection**: Utilize OpenCV and Keras for real-time emotion detection through webcam input.
- **Music Recommendation**: Uses KMeans for clustering and song recommendation based on detected emotions.
- **Integration with Spotify**: Integration with Spotify API to play the recommended songs.
- **Frontend**: React app that initiates the process.

## Folder Structure

- `frontend`: Contains the React frontend code.
- `emotionDetection`: Backend 1 responsible for facial emotion detection.
- `songRecommender`: Backend 2 that interacts with Spotify for song recommendations.

## Instructions to run the App

1. Clone the repository:

   ```
   git clone https://github.com/daspragya/Emotify.git
   ```

2. Set your enviornment variables as given in the .env.example file and rename it to .env

3. Install backend packages using:

   ```
   npm i
   ```

4. Install frontend packages using:

   ```
   cd frontend
   npm i
   ```

5. Install requirements for backend:

   ```
   cd emotionDetection
   pip install -r requirements.txt
   ```

6. Start backend:

   ```
   cd emotionDetection
   python main.py
   ```

7. Start frontend:
   ```
   cd frontend
   npm start
   ```
