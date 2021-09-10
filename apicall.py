from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
@app.route("/home")
def Hello():
	return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():    
    return request.form.get('name')

if __name__=='__main__':
	app.run(debug=True,host='127.0.0.1',port=5000)