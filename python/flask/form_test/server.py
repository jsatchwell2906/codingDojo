from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)
app.secret_key = "pizza"

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/success")
def success():
    if "name" not in session:
        return redirect("/")
    print(request.form)
    return render_template("success.html")
            
@app.route("/create_user", methods=["post"])
def create_user():
    print(request.form)    # Never render a template on a POST request.
    session['name'] = request.form['name']
    return redirect("/success")    # Instead we will redirect to our index route.

@app.route("/clear_name")
def clear_name():
    session.pop("name")
    return redirect("/")

@app.route("/clear_session")
def clear():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)