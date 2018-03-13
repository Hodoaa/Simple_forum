from flask import Flask, render_template


@app.route("/")
@app.route("/index")
def home():
	return render_template("index.html")


