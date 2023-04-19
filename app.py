from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/shortenedurl.html', methods=['GET','POST'])
def shortenedurl():
    return render_template('shortenedurl.html', shortcode=request.form['shortcode'])

