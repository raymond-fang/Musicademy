from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


score = 0

# ROUTES
@app.route('/')
def start_page():
   return render_template('welcome.html')   


@app.route('/quiz/<page>')
def load_quiz(page=None):
    return render_template('quiz.html', quizData= quizData[page], score=score) 

@app.route('/learn/<page>')
def learn(page=None):
    return render_template('learn.html', data = learnData[page])

@app.route('/updateScore', methods=['POST'])
def add():
    global score
    data = request.get_json()
    print(data)
    score += data["result"]
    print(score)
    return jsonify(url="quiz/1")




# AJAX FUNCTIONS

learnData = {
    "1" : {
        "topic": "Techno",
        "summary": "Techno is a genre of electronic dance music (EDM) characterized by a repetitive four on the floor beat which is generally produced for use in a continuous DJ set. The central rhythm is often in common time (4/4), while the tempo typically varies between 120 and 150 beats per minute (bpm). Artists may use electronic instruments such as drum machines, sequencers, and synthesizers, as well as digital audio workstations. Drum machines from the 1980s such as Roland's TR-808 and TR-909 are highly prized, and software emulations of such retro instruments are popular.",
        "name": "5 Meter Mauern by Actek",
        "embedAudio" : '<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1085049022&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/actek44" title="ACTEK [E•F•N]" target="_blank" style="color: #cccccc; text-decoration: none;">ACTEK [E•F•N]</a> · <a href="https://soundcloud.com/actek44/actek-5-meter-mauern-reupload" title="Actek - 5 Meter Mauern (REUPLOAD)" target="_blank" style="color: #cccccc; text-decoration: none;">Actek - 5 Meter Mauern (REUPLOAD)</a></div>'
    }, 

    "2" : {
        "topic": "House",
        "summary": "House is a genre of electronic dance music characterized by a repetitive four-on-the-floor beat and a typical tempo of 115 to 130 beats per minute. It was created by DJs and music producers from Chicago's underground club culture in the 1980s, as DJs from the subculture began altering disco songs to give them a more mechanical beat and deeper basslines. The genre was pioneered by DJs and producers in Chicago such as Frankie Knuckles, Ron Hardy, Jesse Saunders, Chip E., Steve Hurley, Farley Funk, Marshall Jefferson, Phuture and others. From its beginnings in the Chicago club and local radio scene, house music expanded internationally to London, then to other American cities such as New York City and Detroit and became a worldwide phenomenon.",
        "name": "Don't You Worry Child by Swedish House Mafia",
        "embedAudio" : '<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/60140066&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/stelarwarrior" title="stelarwarrior" target="_blank" style="color: #cccccc; text-decoration: none;">stelarwarrior</a> · <a href="https://soundcloud.com/stelarwarrior/dont-you-worry-child-swedish" title="Don&#x27;t You Worry Child - Swedish House Mafia (ft. John Martin)" target="_blank" style="color: #cccccc; text-decoration: none;">Don&#x27;t You Worry Child - Swedish House Mafia (ft. John Martin)</a></div>',
    },
}


quizData = {
    "1" : {
        "id":  "1", 
        "question": "Tech-House is the combination between which of these two genres?",
        "choices": ["Techno and Progressive Techno", "House and Pop", "Techno and House", "Country and House"],
        "answer": "2"
    },

    "2" : {
        "id":  "2", 
        "question": "Which of the following genres tends to use acoustic guitars?",
        "choices": ["Techno", "Pop", "House", "Country"],
        "answer": "3"
    },
    "3" : {
        "id":  "3", 
        "question": "Which of the following genres is known for its heavy reliance on a 4/4 rhythm?",
        "choices": ["Techno", "Pop", "House", "Country"],
        "answer": "0"
    },
    "4" : {
        "id":  "4", 
        "question": "Which of the following genres makes up the majority of mainstream music consumption?",
        "choices": ["Techno", "Pop", "House", "Country"],
        "answer": "1"
    },
      "5" : {
        "id":  "5", 
        "question": "Which of the following pairs contains the most similar genres?",
        "choices": ["Techno and House", "Pop and Techno", "House and Country", "Country and Techno"],
        "answer": "0"
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
   app.run(debug = True)




