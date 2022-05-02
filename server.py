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
        "topic": "Disco",
        "summary": "Disco is a genre of dance music and a subculture that emerged in the 1970s from the United States' urban nightlife scene. Its sound is typified by four-on-the-floor beats, syncopated basslines, string sections, horns, electric piano, synthesizers, and electric rhythm guitars. Most disco songs have a steady four-on-the-floor beat, a quaver or semi-quaver hi-hat pattern with an open hi-hat on the off-beat, and a heavy, syncopated bass line. Other Latin rhythms such as the rhumba, the samba, and the cha-cha-cha are also found in disco recordings, and Latin polyrhythms, such as a rhumba beat layered over a merengue, are commonplace. The quaver pattern is often supported by other instruments such as the rhythm guitar and may be implied rather than explicitly present. Songs often use syncopation, which is the accenting of unexpected beats. In general, the difference between disco, or any dance song, and a rock or popular song is that in dance music the bass drum hits four to the floor, at least once a beat (which in 4/4 time is 4 beats per measure).[citation needed] Disco is further characterized by a 16th note division of the quarter notes as shown in the second drum pattern below, after a typical rock drum pattern.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/6ztstiyZL6FXzh4aG46ZPD?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/3GXo1eWlT2flv4x01l5OTu?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    }, 
    "2" : {
        "id":  "2",
        "topic": "Dubstep",
        "summary": "Dubstep is a genre of electronic dance music that originated in South London in the early 2000s. It is generally characterised by sparse, syncopated rhythmic patterns with prominent sub-bass frequencies. The style emerged as an offshoot of UK garage, drawing on a lineage of related styles such as 2-step and dub reggae, as well as jungle, broken beat, and grime. In the United Kingdom, the origins of the genre can be traced back to the growth of the Jamaican sound system party scene in the early 1980s. Dubstep's early roots are in the more experimental releases of UK garage producers, seeking to incorporate elements of drum and bass into the 2-step garage sound. These experiments often ended up on the B-side of a white label or commercial garage release. Dubstep is generally instrumental. Similar to a vocal garage hybrid grime, the genre's feel is commonly dark; tracks frequently use a minor key or the Phrygian mode, and can feature dissonant harmonies such as the tritone interval within a riff. Compared to other styles of garage music, dubstep tends to be more minimalistic, focusing on prominent sub-bass frequencies.  Some dubstep artists have also incorporated a variety of outside influences, from dub-influenced techno such as Basic Channel to classical music or heavy metal.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/76I3PmbGZazzNlEwlp1y85?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/7ikxeH5UEtVb5okhmgk60g?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    },
    "3" : {
        "id":  "3",
        "topic": "Electro Swing",
        "summary": "Electro swing, or swing house, is an electronic dance music genre that combines the influence of vintage or modern swing and jazz mixed with house and hip hop. Successful examples of the genre create a modern and dance-floor focused sound that is more readily accessible to the modern ear, but that also retains the energetic excitement of live brass and early swing recordings. Electro swing groups typically include singers, musicians playing traditional jazz instruments (e.g. trumpet, trombone, clarinet, saxophone) and at least one DJ. Some notable songs in the electro swing genre include 'We No Speak Americano' by Yolanda Be Cool and DCUP, 'Emergency' by Icona Pop, 'Doop' by Doop, 'A Little Party Never Killed Nobody (All We Got)' by Fergie, Q-Tip and GoonRock and 'Bboom Bboom' by Momoland.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/1Oaq4rq7EBVUiXGh7yxuYL?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/04KsMCb9PZE2S0AtUU8Jhb?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    },
    "4" : {
        "id":  "4",
        "topic": "Electronic Rock",
        "summary": "Electronic rock is a music genre that involves a combination of rock music and electronic music, featuring instruments typically found within both genres. It originates from the late 1960s, when rock bands began incorporating electronic instrumentation into their music. Electronic rock acts usually fuse elements from other music styles, including punk rock, industrial rock, hip hop, techno, and synth-pop, which has helped spur subgenres such as indietronica, dance-punk, and electroclash. Being a fusion of rock and electronic, electronic rock features instruments found in both genres, such as synthesizers, mellotrons, tape music techniques, electric guitars, and drums. Some electronic rock artists, however, often eschew guitar in favor of using technology to emulate a rock sound. Vocals are typically mellow or upbeat, but instrumentals are also common in the genre.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/6O5GkApphr8bRlbA8oehvj?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/6zuHPNE8MyG1wiRlbuTKNf?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    },
    "5" : {
        "id":  "5",
        "topic": "Lofi",
        "summary": "Lofi (also known as chillhop and lofi beats to study to) is a form of downtempo that combines elements of hip hop and chill-out music. It was popularized in the 2010s on YouTube and became an Internet meme. Viewership of lo-fi hip hop streams grew significantly during the COVID-19 pandemic.[10] In April 2020, MTV News noted, 'there might be something to be said for lo-fi hip-hop's composition, and the way its creators mix simplistic melodies with a judicious use of words to create intense memories, feelings, and nostalgia' and stated that the quarantine in place in various countries 'has led people to log more hours online due to boredom or virtual workplaces and schools, and livestreamed music performances are reaching their full potential'.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/6bX6vCqqx7vf2rWh6hcD5b?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/4yeGFmSZor98GSwPSe4uOX?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    },
    "6" : {
        "id":  "6",
        "topic": "House",
        "summary": "House is a genre of electronic dance music characterized by a repetitive four-on-the-floor beat and a typical tempo of 115 to 130 beats per minute. It was created by DJs and music producers from Chicago's underground club culture in the 1980s, as DJs from the subculture began altering disco songs to give them a more mechanical beat and deeper basslines. The genre was pioneered by DJs and producers in Chicago such as Frankie Knuckles, Ron Hardy, Jesse Saunders, Chip E., Steve 'Silk' Hurley, Farley 'Jackmaster' Funk, Marshall Jefferson, Phuture and others. From its beginnings in the Chicago club and local radio scene, house music expanded internationally to London, then to other American cities such as New York City and Detroit and became a worldwide phenomenon. House has had a large impact on the pop music scene, especially dance music. It was incorporated by major international pop artists including Janet Jackson ('Together Again'), Kylie Minogue and Madonna ('Vogue'), but also produced some mainstream hits on its own, such as 'French Kiss' by Lil Louis, 'Show Me Love' by Robin S. or 'Push the Feeling On' by the Nightcrawlers. Many house DJ's also did and continue to do remixes for pop artists. House music has remained popular on radio and in clubs while retaining a foothold on the underground scenes across the globe.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/0bsdfTgzxOPN4RcZcGJJ3t?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/3kyskiCpYM2ALQUSEShFMY?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    },
    "7" : {
        "id":  "7",
        "topic": "Industrial",
        "summary": "Electro-industrial is a music genre that emerged from industrial music in the early 1980s. While EBM (electronic body music) has a minimal structure and clean production, electro-industrial tends to have a grittier, complex and layered sound with a more experimental approach, too. The style was pioneered by Skinny Puppy, Front Line Assembly, Numb, and other groups, either from Canada or the Benelux. In the early 1990s, the style spawned the dark electro genre, and in the mid-/late-1990s, the aggrotech offshoot. The fan base for the style is linked to the rivethead subculture. After the EBM movement faded in the early 1990s, electro-industrial increasingly attained popularity in the international club scene. In contrast to the straight EBM style, electro-industrial groups use harsher beats and raspy, distorted, or digitized vocals. In contrast to industrial rock, electro-industrial groups mostly avoided guitars, other than Skinny Puppy, who used electric guitar elements since the mid-'80s in songs like 'Testure' or 'Dig It', and Numb on songs like 'God Is Dead'.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/6veSZZyiPORN6rGyJn5mS2?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/1nZMBGnMGqEsiiw7EVQdjS?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    },
    "8" : {
        "id":  "8",
        "topic": "Trance",
        "summary": "Trance is a genre of electronic dance music that emerged from the British new-age music scene and the early 1990s German techno and hardcore scenes. Trance music is characterized by a tempo generally lying between 120–150 bpm (BPM), repeating melodic phrases and a musical form that distinctly builds tension and elements throughout a track often culminating in 1 to 2 'peaks' or 'drops'. Although trance is a genre of its own, it liberally incorporates influences from other musical styles such as techno, house, pop, chill-out, classical music, tech house, ambient and film music. A trance is a state of hypnotism and heightened consciousness. This is portrayed in trance music by the mixing of layers with distinctly foreshadowed build-up and release. A common characteristic of trance music is a mid-song climax followed by a soft breakdown disposing of beats and percussion entirely, leaving the melody or atmospherics to stand alone for an extended period before gradually building up again. Trance tracks are often lengthy to allow for such progression and commonly have sufficiently sparse opening and closing sections to facilitate mixing by DJs.",
        "name": "",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/4nM12eRb7k6pylJGGivAQp?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
        "embedAudio2" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/0xCodun2Js9PZZ1XadO9oe?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    },
}


quizData = {
    "1" : {
        "id":  "1", 
        "question": "What genre of music combines the influence of vintage or modern swing and jazz mixed with house and hiphop?",
        "choices": ["Electronic Rock","Lofi", "Electro Swing", "Dubstep" ],
        "answer": "2"
    },

    "2" : {
        "id":  "2", 
        "question": " What music style is generally characterized by sparse, syncopated rhythmic patterns with prominent sub-bass frequencies.",
        "choices": ["House", "Dubstep", "Electronic Rock", "Lofi"], 
        "answer": "1"
    },
    "3" : {
        "id":  "3", 
        "question": "Which Genre is a form of downtempo that combines elements of Hiphop and chill out music?",
        "choices": ["House","Electronic Rock", "Dubstep",  "Lofi"], 
        "answer": "3"
    },
    "4" : {
        "id":  "4", 
        "question": "What Genre was created by DJs and music producers from Chicago's underground club culture in the 1980s, as DJs from the subculture began altering disco songs to give them a more mechanical beat and deeper basslines.",
        "choices": [ "Dubstep", "House", "Industrial", "Lofi"], 
        "answer": "1"
    },
    "5" : {
        "id":  "5", 
        "question": "What Genre spawned the dark electro genre, pioneered by ​​ Skinny Puppy, Front Line Assembly, Numb, and others.",
        "choices": [ "Dubstep", "House", "Industrial", "Lofi"], 
        "answer": "2"
    },
    "6" : {
        "id":  "6", 
        "question": " Listen to this Song. What genre is it?",
        "choices": [ "Dubstep", "House", "Industrial", "Lofi"], 
        "answer": "2",
        "embedAudio" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/1nZMBGnMGqEsiiw7EVQdjS?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
    },

    "7" : {
        "id":  "7", 
        "question": " Listen to this Song. What genre is it?",
        "choices": ["House", "Dubstep", "Electronic Rock", "Lofi"], 
        "answer": "2",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/1wKy1UGBNH8B7lTfxX4wm0?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
      },
    
    "8" : {
        "id":  "8", 
        "question": "True or False: This Song is an example of Electro Swing",
        "choices": ["True", "False"],
        "answer": "0",
        "embedAudio" : '<iframe class="right-align" style="border-radius:12px" src="https://open.spotify.com/embed/track/04KsMCb9PZE2S0AtUU8Jhb?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
      },

    "9" : {
        "id":  "9", 
        "question": " True or False: This song is an example of Dubstep",
        "choices": ["True", "False"],
        "answer": "1",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/0bsdfTgzxOPN4RcZcGJJ3t?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',
      },
    "10" : {
        "id":  "10", 
        "question": " Listen to this Song. What genre is it?",
        "choices": ["Trance", "Lofi", "House", "Electro-rock"],
        "answer": "0",
        "embedAudio" : '<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/4nM12eRb7k6pylJGGivAQp?utm_source=generator" width="47%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>',

      }
}



if __name__ == '__main__':
   app.run(debug = True)




