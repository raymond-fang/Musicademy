var numGenres = 8;

function loadAudio() {
    let audio = $(data.embedAudio);
    let audio2 = $(data.embedAudio2);
    $("#audio-wrapper").append(audio);
    $("#audio-wrapper").append(audio2);
}


// load the next question/ prev question  buttons
function loadButtons(){
    numNext = parseInt(data.id) + 1;
    numPrev = parseInt(data.id) - 1;

    prevQuest= $('<a href="/learn/' + numPrev + '" class="btn btn-primary">  < Previous Genre </a>');
    nextQuest= $('<a href="/learn/' + numNext + '" class="btn btn-primary">  Next Genre > </a>');
    if (numPrev <= 0){
        prevQuest.addClass("disabled");
        prevQuest.prop("disabled",true);
    }
    $("#buttons-wrapper").append(prevQuest);
    if (numNext <= numGenres) {
        $("#buttons-wrapper").append(nextQuest);
    }
        if (numNext > numGenres) {
        nextQuiz = $('<a href="/quiz/1' + '" class="btn btn-primary">  Take quiz! > </a>');
        $("#buttons-wrapper").append(nextQuiz);
    }
}

$(document).ready(function(){
    loadAudio();
    loadButtons();
})