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
    return render_template("index.html")

@app.route('/choice', methods=['post'])
def choice ():
    opp_choices = ['Rock', 'Paper', 'Scissors']
    randoint = random.randint(0,len(opp_choices) - 1)
    session['opp_choice'] = opp_choices[randoint]
    session['our_choice'] = request.form['our_choices']
    print(session)
    if session['our_choice'] == session['opp_choice']:
        session('draws')
        session['result'] = 'draw'
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)