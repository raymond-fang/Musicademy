from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)



# ROUTES
@app.route('/')
def start_page():
   return render_template('home.html')   


@app.route('/quiz/<page>')
def load_quiz(page=None):
    return render_template('quiz.html', quizData= quizData[page]) 

@app.route('/learn/<page>')
def learn(page=0):
    return render_template('learn.html') 




# AJAX FUNCTIONS

quizData = {
    "1" : {
        "id":  "1", 
        "question": "Tech-House is the combination between which of these two genres?",
        "choices": ["Techno and Progressive Techno", "House and Pop", "Techno and House", "Country and House"],
        "answer": "3"
    }
}



if __name__ == '__main__':
   app.run(debug = True)




