from flask import render_template, request
from flaskapp import app

@app.route("/", methods=['GET', 'POST'])
def testing():
    text = ""
    if request.method == 'POST':
        text = request.form['input_text']
        text = text.upper()

    return render_template('bot.html', generated_response=text)




