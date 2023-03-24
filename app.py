from flask import Flask

app=Flask(__name__)

@app.route("/")

def hello():
    return "Hellow word"



#app.run(debug=True,port=5001)