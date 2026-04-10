import pandas as pd
import numpy as np
import pickle
from flask import Flask, request, render_template
from keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences



app = Flask(__name__)

model=load_model('lstm_reviews.keras')
with open('tokenizer.pkl','rb') as f:
    tokenizer=pickle.load(f)
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['Review']
        text=text.lower().strip()
        s=[text]
        max_len=100
        seq = tokenizer.texts_to_sequences([s])
        padded = pad_sequences(seq, maxlen=max_len)
        pred = model.predict(padded)[0][0]
    
        if pred > 0.5:
            r=f"Positive ({pred:.2f})"
            result=1
        else:
            r=f"Negative ({pred:.2f})"
            result=0
    if result==1:
        return render_template('index.html', prediction_text=f'The review is  {r}')
    else:
        return render_template('index.html', prediction_text=f'The review is {r}')

if __name__ == "__main__":
    app.run(debug=True)