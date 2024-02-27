from flask import Flask, render_template, request
import datetime
app = Flask(__name__)
app.debug = True


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/contact")
def contact():
    tickers = ['This is apple.',
            'This is microsoft',
            'This is google',
            'This is facebook',
            ]
    return render_template('contact.html', tickers=tickers)


@app.route("/trade", methods=['GET', 'POST'])
def trade():
    if request.method == 'POST':
        for key, value in request.form.items():
            print(f'{key}: {value}')
    return render_template('trade.html')


@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/tracsaction")
def tracsaction():
    return render_template('tracsaction.html')

if(__name__ == "__main__"): 
    app.run(debug=True) 