from flask import Flask,render_template
import json
#test comment added
app = Flask(__name__)
data = {
        "profile1": {
                "name": "John",
                "email": "john123@gmail.com"
                },
        "profile2": {
                "name": "Matthew",
                "email": "matthew123@gmail.com"
                }
                }  
#hello function
@app.route("/")
def hello():	
    return render_template('index.html', message=data)

@app.route('/getdata')
def hello_name():
    return data


if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0',port=5000)
