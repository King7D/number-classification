# 28x28 Digit Recognizer with Neural Network Visualization

This project is a **handwritten digit recognizer** built using a **28x28 grid drawing interface**. It uses a **Convolutional Neural Network (CNN)** to predict which digit (0-9) is drawn by the user and also displays the **likelihood of each digit**. When the model's confidence is less than 50%, the result is displayed as **"Unknown"**.

## Features
- **Interactive Drawing Grid**: Users can draw digits (0-9) on a 28x28 grid by holding down the mouse button.
- **Real-Time Prediction**: After drawing, users can click the **Predict** button to see the predicted digit.
- **Probability Visualization**: Displays the likelihood of each possible digit as a percentage, using a horizontal bar to represent confidence.
- **Prediction Threshold**: If none of the digit probabilities exceed 50%, the prediction is displayed as **"Unknown"**.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Machine Learning Model**: TensorFlow (Convolutional Neural Network)

## Getting Started

### Prerequisites
Make sure you have the following installed:
- **Python 3.7+**
- **Pip** (Python package installer)

### Usage
1. **Drawing a Digit**
- Click and hold the mouse button to draw on the 28x28 grid. You can draw any digit from 0-9.
2. **Making a Prediction**
- Once you finish drawing, click the Predict button.
- The application will display the predicted digit and the likelihood of each digit (0-9).
- If no digit has a probability greater than 50%, the prediction will be "Unknown".
3. **Clearing the Grid**
- Click the Clear button to reset the grid and draw a new digit.

## Project Structure

- app.py: The Flask backend that serves the application and handles digit predictions.
- templates/index.html: The frontend HTML page containing the 28x28 grid and UI.
- static/: Contains CSS and JavaScript files used for the frontend.
- model training.ipynb: Script to train the CNN model using the MNIST dataset.
- model.h5: The trained model used for making predictions.
