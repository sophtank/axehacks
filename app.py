from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.get('/about')
def about():
    return render_template('about_us.html')

@app.get('/definitions')
def roadmap():
    return render_template('definitions.html')

@app.get('/2000s')
def year2000():
    return render_template('2000.html')

@app.get('/2010s')
def year2010():
    return render_template('2010.html')

@app.get('/all')
def year2024():
    return render_template('all.html')