
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"


#add anather line   
if __name__ == '__main__':
    app.run()       
    
    