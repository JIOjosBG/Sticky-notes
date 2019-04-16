
from flask import Flask, render_template,request

import os.path
import json
from pprint import pprint

import ast




app = Flask(__name__)



if os.path.exists("users.json"):
    with open("users.json") as file:
        newdata = json.load(file)
newdata=ast.literal_eval(newdata)


@app.route('/',methods=['GET','POST'])
def index():



	r=newdata
	for i in range(len(r)):
		if i==0:
			r[i]=0;
		else:
			r[i]={
				'name':'None',
				'pass':'None',
				'id':r[0]
			}



	if request.method=='POST':
		name=request.form['name']
		password=request.form['pass']
		for i in range(len(r)):
			if i>=r[0]+1:
				r[i]['name']=name
				r[i]['pass']=password
				r[0]=r[0]+1
				break



		with open("users.json", "w") as file:
    				r = json.dumps(r)
    				json.dump(r, file)


		return r;
    	





	return render_template('index.html')


if __name__=='__main__':
	app.run(debug=True)