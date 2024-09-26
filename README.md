# SpotifyRecommender

_A web-based music recommender system built with Flask. This system allows users to input a song ID and get recommendations for similar songs based on a KMeans clustering model._

## Overview

This project provides a simple way to recommend songs to users based on the song they input. Using KMeans clustering and TF-IDF vectorization on song data, the system suggests songs with similar characteristics. The application is deployed as a web app using Flask.

The project involves:

- Data preprocessing and feature extraction using TF-IDF.
- Training a KMeans model for song recommendation.
- Developing a Flask web application for user interaction.

## Features

- Uses a pre-trained KMeans clustering model to recommend similar songs.
- A simple web interface where users can input a song ID to receive recommendations.
- The model and application can be easily extended with additional features or improved models.

![image](https://github.com/user-attachments/assets/70f31e9c-7bee-4178-b706-b75091c215db)
![image](https://github.com/user-attachments/assets/4b0c68c2-f1e8-48ce-974a-6fd5b1b8a864)


## Project Structure

```plaintext
.
├── app.py
├── cleaned_data.csv
├── kmeans_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── templates
│   ├── index.html
├── static
│   ├── style.css
│   ├── app.js
└── README.md
```

## Project Structure

- `app.py`: Main Flask application file.
- `cleaned_data.csv`: Preprocessed dataset containing song features.
- `kmeans_model.pkl`: Pre-trained KMeans clustering model.
- `tfidf_vectorizer.pkl`: Vectorizer used for feature extraction from song data.
- `requirements.txt`: Python dependencies.
- `templates/`: HTML template for the web interface.
- `static/`: Static files like CSS and JavaScript.
- `README.md`: Project documentation.

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)
- Git (optional)

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/stutterk1d/SpotifyRecommender.git
    cd SpotifyRecommender
    ```

2. **Create a Virtual Environment**

    It's recommended to use a virtual environment to manage dependencies.

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Place Model Files**

    Ensure `kmeans_model.pkl` and `tfidf_vectorizer.pkl` are in the project root directory.

## Usage

1. **Run the Flask Application**

    ```bash
    python app.py
    ```

2. **Access the Application**

    Open your web browser and navigate to:

    [http://localhost:5000](http://localhost:5000)

3. **Get Song Recommendations**

    - Enter a song ID into the input field.
    - Click the "Get Recommendations" button.
    - View the recommended songs displayed on the page.

## Dataset

The dataset used for training the model is from [this Kaggle project](https://www.kaggle.com/code/vatsalmavani/music-recommendation-system-using-spotify-dataset). It has been cleaned and processed for use in this recommender system.

- `cleaned_data.csv`: Contains preprocessed song data for model training and recommendations.

## Model Training

The system uses a KMeans clustering model to recommend songs.

### Steps

1. **Data Preprocessing**

    - Song data is cleaned and vectorized using TF-IDF to extract meaningful features.

2. **Model Architecture**

    - **KMeans Clustering**: Songs are grouped into clusters based on similarity in their features.

3. **Training**

    - The KMeans model is trained on the vectorized song data.
    - Model is saved as `kmeans_model.pkl` for future use.

4. **Saving the Model**

    - KMeans model saved as `kmeans_model.pkl`.
    - TF-IDF vectorizer saved as `tfidf_vectorizer.pkl`.

_For detailed code and steps, refer to the model training script (not included in this repository)._

## Web Application

The Flask web application provides a user interface for the Spotify Song Recommender.

### Key Files

- `app.py`: Contains the Flask application code.
- `templates/index.html`: Home page with a form to input song ID.
- `static/style.css`: Contains styles for the web pages.
- `static/app.js`: Handles the form submission and renders recommendations dynamically.

### Routes

- `/`: Renders the home page.
- `/recommend`: Handles form submission and returns song recommendations.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
    - Flask
    - scikit-learn
    - NumPy
    - Pandas
- **Frontend**:
    - HTML
    - CSS
    - JavaScript

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

- **Name**: Ethan Tran
- **Email**: [ethantran03@gmail.com](mailto:ethantran03@gmail.com)
- **GitHub**: [stutterk1d](https://github.com/stutterk1d)

_Feel free to reach out if you have any questions or suggestions!_
