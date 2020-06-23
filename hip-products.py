from flask import Flask, render_template
import json

app = Flask(__name__)
#hello function
@app.route("/")
def hello():
        data = {
                    "product1": {
                                "name": "Washing machine",
                                        "species": "Germany"
                                            },
                        "product2": {
                                    "name": "Kite",
                                            "species": "India"
                                                }
                            }   
            return render_template('index.html', message=data)


        if __name__ == '__main__':
                app.run(debug=True,host='0.0.0.0',port=5000)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)


