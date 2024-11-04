import tensorflow as tf
from flask import Flask, request, jsonify, render_template
import numpy as np

# Load the trained CNN model
model = tf.keras.models.load_model('model.h5')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['pixels']
    # Convert the data to the appropriate format
    data = np.array(data).reshape(1, 28, 28, 1) / 255.0  # Normalize and reshape for CNN
    prediction = model.predict(data)
    predicted_class = np.argmax(prediction)
    probabilities = prediction.tolist()[0]  # Convert probabilities to a list

    # Return both the predicted class and all probabilities
    return jsonify({'prediction': int(predicted_class), 'probabilities': probabilities})

if __name__ == '__main__':
    app.run(debug=True)
