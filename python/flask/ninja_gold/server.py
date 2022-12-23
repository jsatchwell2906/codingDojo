import random
from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "pizza"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money', methods=['post'])
def add_gold():
    if request.form.get('building') == "farm":
        earnings = random.randrange(10, 20)
        print('farm')
        session['gold'] += earnings
        session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the farm')
    elif request.form.get('building') == "cave":
        earnings = random.randrange(5, 10)
        session['gold'] += earnings
        session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the cave')
    elif request.form.get('building') == "house":
        earnings = random.randrange(2, 5)
        session['gold'] += earnings
        session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the house')
    elif request.form.get('building') == "casino":
        earnings = random.randrange(-50, 50)
        session['gold'] += earnings
        if earnings > 0:
            session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the casino')
        else:
            session['activities'].append(
                'Lost ' + str(earnings) + ' gold from the casino')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
