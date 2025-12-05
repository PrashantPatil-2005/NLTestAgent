from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        return f"Logged in as {username}"
    return render_template("login.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        return f"Search result for {query}"
    return render_template("search.html")

@app.route("/form-step-1", methods=["GET", "POST"])
def step1():
    if request.method == "POST":
        return redirect("/form-step-2")
    return render_template("multistep_step1.html")

@app.route("/form-step-2")
def step2():
    return render_template("multistep_step2.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
