from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'rock_paper_scissors'

@app.route('/')
def index():
    if 'draws' not in session:
        session['draws'] = 0
        session['losses'] = 0
        session['wins'] = 0
        session['outcome'] = []
    return render_template("index.html")

@app.route('/choice', methods=['post'])
def choice ():
    opp_choices = ['Rock', 'Paper', 'Scissors']
    randoint = random.randint(0,len(opp_choices) - 1)
    session['opp_choice'] = opp_choices[randoint]
    session['our_choice'] = request.form['our_choices']
    
    if session['our_choice'] == session['opp_choice']:
        session['draws'] += 1
        session['result'] = 'Draw'
        color = "blue"


    elif session['our_choice'] == 'Rock' and session['opp_choice'] == 'Paper':
        session['losses'] += 1
        session['result'] = 'Lose'


    elif session['our_choice'] == 'Rock' and session['opp_choice'] == 'Scissors':
        session['wins'] += 1
        session['result'] = 'Win'


    elif session['our_choice'] == 'Paper' and session['opp_choice'] == 'Rock':
        session['wins'] += 1
        session['result'] = 'Win'


    elif session['our_choice'] == 'Paper' and session['opp_choice'] == 'Scissors':
        session['losses'] += 1
        session['result'] = 'Lose'


    elif session['our_choice'] == 'Scissors' and session['opp_choice'] == 'Paper':
        session['wins'] += 1
        session['result'] = 'Win'


    elif session['our_choice'] == 'Scissors' and session['opp_choice'] == 'Rock':
        session['losses'] += 1
        session['result'] = 'Lose'

    if session['result'] == 'Win':
        color = "green"
    elif session['result'] == "Lose":
        color = "red"

    message = (f"Your opponent chose {session['opp_choice']}, You Chose {session['our_choice']}. You {session['result']}")
    session['outcome'].append({'color': color, 'message': message})
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)