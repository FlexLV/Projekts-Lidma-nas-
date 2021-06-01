from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def main():
  return render_template("Main.html")


@app.route('/Covid_19')
def Covid_19():
  return render_template("Covid_19.html")

@app.route('/ParLidmasinam')
def Par_lidmasinu():
  return render_template("Parlidmasinu.html")


app.run(host='0.0.0.0', port=8080)