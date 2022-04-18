from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


# ROUTES
@app.route('/')
def start_page():
    return render_template('welcome.html')


@app.route('/quiz/<page>')
def load_quiz(page=None):
    return render_template('quiz.html', quizData=quizData[page])


@app.route('/learn/<page>')
def learn(page=0):
    return render_template('learn.html')


# AJAX FUNCTIONS
quizData = {
    "1": {
        "id":  "1",
        "question": "Tech-House is the combination between which of these two genres?",
        "choices": ["Techno and Progressive Techno", "House and Pop", "Techno and House", "Country and House"],
        "answer": "2"
    },

    "2": {
        "id":  "2",
        "question": "*Filler Question* ",
        "choices": ["Techno and Progressive Techno", "House and Pop", "Techno and House", "Country and House"],
        "answer": "2"
    },
    "3": {
        "id":  "3",
        "question": "*Filler Question* ",
        "choices": ["Techno and Progressive Techno", "House and Pop", "Techno and House", "Country and House"],
        "answer": "2"
    },
    "4": {
        "id":  "4",
        "question": "*Filler Question* ",
        "choices": ["Techno and Progressive Techno", "House and Pop", "Techno and House", "Country and House"],
        "answer": "2"
    },
    "5": {
        "id":  "5",
        "question": "*Filler Question* ",
        "choices": ["Techno and Progressive Techno", "House and Pop", "Techno and House", "Country and House"],
        "answer": "2"
    },
    "6" : {
        "id":  "6", 
        "question": " Listen to this Song. What genre is it?",
        "choices": ["Progressive Techno", "Deep House", "Techno House", "Minimal"],
        "answer": "2",
        "embedAudio" : '<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/259022901&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/livealok" title="Alok" target="_blank" style="color: #cccccc; text-decoration: none;">Alok</a> · <a href="https://soundcloud.com/livealok/alok-liu-bolum-back" title="ALOK &amp; LIU - BOLUMBACK [ FREE DOWNLOAD ]" target="_blank" style="color: #cccccc; text-decoration: none;">ALOK &amp; LIU - BOLUMBACK [ FREE DOWNLOAD ]</a></div>'
    },
      "7" : {
        "id":  "7", 
        "question": " Listen to this Song. What genre is it?",
        "choices": ["Progressive Techno", "House", "Techno House", "Minimal"],
        "answer": "0",
        "embedAudio" : '<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/629240799&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/joris-voorn" title="Joris Voorn" target="_blank" style="color: #cccccc; text-decoration: none;">Joris Voorn</a> · <a href="https://soundcloud.com/joris-voorn/antigone-2" title="Antigone" target="_blank" style="color: #cccccc; text-decoration: none;">Antigone</a></div>'
    }

}


if __name__ == '__main__':
    app.run(debug=True)
