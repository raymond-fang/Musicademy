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
        "id":  "1",
        "topic": "Jazz",
        "summary": "Jazz is a music genre that originated in the African-American communities of New Orleans, Louisiana in the late 19th and early 20th centuries, with its roots in blues and ragtime. Since the 1920s Jazz Age, it has been recognized as a major form of musical expression in traditional and popular music, linked by the common bonds of African-American and European-American musical parentage. Jazz is characterized by swing and blue notes, complex chords, call and response vocals, polyrhythms and improvisation. Jazz has roots in European harmony and African rhythmic rituals. Although jazz is considered difficult to define, in part because it contains many subgenres, improvisation is one of its defining elements.",
        "name": "Take Five by Dave Brubeck",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/1YQWosTIljIvxAgHWTp7KP?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/19vVghIuHm3IAfN4xpRF3q?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    }, 
    "2" : {
        "id":  "2",
        "topic": "Pop",
        "summary": "Pop is a genre of popular music that originated in its modern form during the mid-1950s in the United States and the United Kingdom. The terms popular music and pop music are often used interchangeably, although the former describes all music that is popular and includes many disparate styles. During the 1950s and 1960s, pop music encompassed rock and roll and the youth-oriented styles it influenced. Rock and pop music remained roughly synonymous until the late 1960s, after which pop became associated with music that was more commercial, ephemeral, and accessible. Although much of the music that appears on record charts is seen as pop music, the genre is distinguished from chart music. Identifying factors usually include repeated choruses and hooks, short to medium-length songs written in a basic format (often the verse-chorus structure), and rhythms or tempos that can be easily danced to. Much pop music also borrows elements from other styles such as rock, urban, dance, Latin, and country.",
        "name": "Levitating by Dua Lipa",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/39LLxExYz6ewLAcYrzQQyP?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/5pD9x23lsoQr464mlmaKNJ?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    },
    "3" : {
        "id":  "3",
        "topic": "EDM",
        "summary": "Rather than designating a single genre, electronic dance music (EDM) encompasses styles ranging from beatless ambient music to 200-beats-per-minute hardcore, with house music, techno, drum and bass, dubstep, and trance among the most-notable examples. Considered as a whole, electronic dance music is characterized by several defining features. It is typified by deliberately inorganic sounds and timbres, frequently produced by cheap early-1980s gear—such as the 303 bass synthesizer and the 808 drum machine, both made by Japanese electronics firm Roland—or built from samples of previous recordings. Live instrumentation and singing are often featured but usually as a garnish rather than the main dish. Most important, the music is created specifically for the social function of dancing all night. A strong emphasis on rhythm is therefore common to most styles of EDM, while ambient music, which is less focused on maintaining a beat, provides an aural cushion for settling down at the end of the night.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/0DiWol3AO6WpXZgp0goxAV?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/60wwxj6Dd9NJlirf84wr2c?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    },
    "4" : {
        "id":  "4",
        "topic": "Classical",
        "summary": "Classical music generally refers to the formal musical tradition of the Western world, considered to be distinct from Western folk music or popular music traditions. It is sometimes distinguished as Western classical music, as the term 'classical music' may also refer to non-Western traditions which exhibit similar formal qualities. In addition to formality, classical music is often characterized by complexity in its musical form and harmonic organization, particularly with the use of polyphony. Since at least the 9th-century it has been primarily a written tradition, spawning a sophisticated notational system, as well as accompanying literature in analytical, critical, historiographical, musicological and philosophical practices. A foundational component of Western Culture, classical music is frequently seen from the perspective of individual or groups of composers, whose compositions, personalities and beliefs have fundamentally shaped its history.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/5u5aVJKjSMJr4zesMPz7bL?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/0nF5aQoLs2YtbWwClXvumL?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    },
    "5" : {
        "id":  "5",
        "topic": "Rock",
        "summary": "Rock music is a broad genre of popular music that originated as 'rock and roll' in the United States in the late 1940s and early 1950s, developing into a range of different styles in the mid-1960s and later, particularly in the United States and the United Kingdom. It has its roots in 1940s and 1950s rock and roll, a style that drew directly from the blues and rhythm and blues genres of African-American music and from country music. Rock music also drew strongly from a number of other genres such as electric blues and folk, and incorporated influences from jazz, classical, and other musical styles. For instrumentation, rock has centered on the electric guitar, usually as part of a rock group with electric bass, drums, and one or more singers. Usually, rock is song-based music with a 4/4 time signature using a verse–chorus form, but the genre has become extremely diverse. Like pop music, lyrics often stress romantic love but also address a wide variety of other themes that are frequently social or political.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/3KYiA4vq6RPO1dE2XROXd8?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/0o4e5Tt4vorx2012FrGIjV?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    },
    "6" : {
        "id":  "6",
        "topic": "Hip Hop",
        "summary": "Hip hop music or hip-hop music, also known as rap music, is a genre of popular music developed in the United States by inner-city African Americans, Latino Americans and Caribbean Americans in the Bronx borough of New York City in the 1970s. It consists of a stylized rhythmic music that commonly accompanies rapping, a rhythmic and rhyming speech that is chanted. It developed as part of hip hop culture, a subculture defined by four key stylistic elements: MCing/rapping, DJing/scratching with turntables, break dancing, and graffiti writing. Other elements include sampling beats or bass lines from records (or synthesized beats and sounds), and rhythmic beatboxing. While often used to refer solely to rapping, 'hip hop' more properly denotes the practice of the entire subculture.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/3PdiRnD8aIC3ljfqMhq93B?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/0j2T0R9dR9qdJYsB7ciXhf?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    },
    "7" : {
        "id":  "7",
        "topic": "Country",
        "summary": "Country (also called country and western) is a genre of popular music that originated with blues, church music such as Southern gospel and spirituals, old-time, and American folk music forms including Appalachian, Cajun, Creole, and the cowboy Western music styles of New Mexico, Red Dirt, Tejano, and Texas country. Its popularized roots originate in the Southern and Southwestern United States of the early 1920s. Country music often consists of ballads and dance tunes (most commonly known as 'Honky Tonk music') with generally simple forms, folk lyrics, and harmonies often accompanied by string instruments such as banjos, electric and acoustic guitars, steel guitars (such as pedal steels and dobros), and fiddles as well as harmonicas. Blues modes have been used extensively throughout its recorded history. The term country music gained popularity in the 1940s in preference to hillbilly music; it came to encompass Western music, which evolved parallel to hillbilly music from similar roots, in the mid-20th century. In 2009, in the United States, country music was the most listened to rush hour radio genre during the evening commute, and second most popular in the morning commute.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/3fqwjXwUGN6vbzIwvyFMhx?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/5gVCfYmQRPy1QJifP8f5gg?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    },
    "8" : {
        "id":  "8",
        "topic": "Indie Pop",
        "summary": "Indie pop (also typeset as indie-pop or indiepop) is a music genre and subculture that combines guitar pop with DIY ethic in opposition to the style and tone of mainstream pop music. It originated from British post-punk in the late 1970s and subsequently generated a thriving fanzine, label, and club and gig circuit. Compared to its counterpart, indie rock, the genre is more melodic, less abrasive, and relatively angst-free. In later years, the definition of indie pop has bifurcated to also mean bands from unrelated DIY scenes/movements with pop leanings. Subgenres include chamber pop and twee pop.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/1ZseaIKt19broBzze3F8hz?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/5OUTFH5acycdnf8OVo21Gv?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
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




