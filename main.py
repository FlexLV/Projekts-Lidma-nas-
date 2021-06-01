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
  return render_template("ParLidmasinu.html")

@app.route('/Lidojumi')
def Lidojumi():
  return render_template("Lidojumi.html") 

@app.route('/Register')
def Register():
  return render_template("Register.html")

  @app.route('/ForgotPass')
  def ForgotPass():
    return render_template("ForgotPass.html")
  
app.run(host='0.0.0.0', port=8080)