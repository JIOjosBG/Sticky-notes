
#HTML to python
from flask import Flask, render_template,request


#python and json
import os.path
import json


with open("users.json") as file:
    data = json.load(file)


newdata=data
print newdata


#json to python



app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
#html to python
	if request.method=='POST':
		name=request.form['name']
		password=request.form['pass']
		r='id:  0 '+' name: '+name+' pass: '+password;



		with open("users.json", "w") as file:
    				json.dump(newdata+r, file)


		return r;
    	



		#output json to python
		#return str(data['name']);



	return render_template('index.html')


if __name__=='__main__':
	app.run(debug=True)