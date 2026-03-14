from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = ""

    if request.method == 'POST':
        weight = float(request.form['weight'])
        height_cm = float(request.form['height'])

        height = height_cm / 100  # convert cm to meters
        bmi = round(weight / (height ** 2), 2)

        if bmi < 20:
            category = "Underweight"
        elif 20 <= bmi < 25:
            category = "Normal"
        else:
            category = "Overweight"

    return render_template('index.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)
