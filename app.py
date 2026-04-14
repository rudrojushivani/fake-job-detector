from flask import Flask, render_template, request

app = Flask(__name__)

# Simple fake job logic (you can replace with ML model later)
def predict_job(text):
    text = text.lower()

    fake_words = [
        "urgent", 
        "earn money fast", 
        "no experience", 
        "work from home easy money",
        "register fee"
    ]

    for word in fake_words:
        if word in text:
            return "⚠️ Fake Job Detected"

    return "✅ Genuine Job"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # MUST MATCH HTML name="text"
    text = request.form.get('text')

    if not text:
        return render_template('index.html', prediction="❌ No job description provided!")

    result = predict_job(text)

    return render_template('index.html', prediction=result)


if __name__ == "__main__":
    app.run(debug=True)