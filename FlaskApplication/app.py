from flask import Flask, render_template
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


@app.route("/trade")
def trade():
    return render_template('trade.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/tracsaction")
def tracsaction():
    return render_template('tracsaction.html')







# @app.route('/read-form', methods=['POST']) 
# def read_form(): 
  
#     # Get the form data as Python ImmutableDict datatype  
#     data = request.form 
  
#     ## Return the extracted information  
#     return { 
#         'emailId'     : data['userEmail'], 
#         'phoneNumber' : data['userContact'], 
#         'password'    : data['userPassword'], 
#         'gender'      : 'Male' if data['genderMale'] else 'Female', 
#     } 

if(__name__ == "__main__"): 
    app.run(debug=True) 