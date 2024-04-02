from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import datetime
import os
app = Flask(__name__)
app.debug = True

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/stocks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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
    stock = Stock.query.all()
    return render_template('tracsaction.html', stock=stock)



#Models 
class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10))
    price = db.Column(db.Float)
    date = db.Column(db.DateTime, default=func.now())

    def __init__(self, ticker, price):
        self.ticker = ticker
        self.price = price
    
    def __repr__(self):
        return f'{self.ticker} at {self.price}'


if(__name__ == "__main__"): 
    app.run(debug=True)