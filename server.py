from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


# ROUTES
@app.route('/')
def start_page():
   return render_template('home.html')   


@app.route('/quiz/<page>')
def hello_name(page=None):
    return render_template('quiz.html') 

@app.route('/learn/<page>')
def hello_name(page=0):
    return render_template('learn.html') 




# AJAX FUNCTIONS



if __name__ == '__main__':
   app.run(debug = True)




