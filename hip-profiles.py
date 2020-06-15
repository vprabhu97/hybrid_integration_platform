from flask import Flask
import json

app = Flask(__name__)
#hello function
@app.route("/")
def hello():
        data = {
                    "profile1": {
                                "name": "Vinayak",
                                "email": "vprabhu97@gmail.com"
                                            },
                        "profile2": {
                                    "name": "Krishna",
                                    "email": "krishna123@gmail.com"
                                                }
                            }   
            return data


        if __name__ == '__main__':
                app.run(debug=True,host='0.0.0.0')
