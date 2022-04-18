//max # of questions in quiz
var maxQuestions= 6;

function loadChoices() {
    $("#question-wrapper").append($('<p> ' + quizData.id + ") " + quizData.question + '</p>'));
    for(let i=0; i< 4; i++) {
        let choice = $('<button type="button" data-numchoice="' + i + '" class="btn btn-outline-secondary row d-block multChoice">' + quizData.choices[i] + '</button>');
        $("#choices-wrapper").append(choice);
    }
    if(quizData.id > 5) {
        let embedAudio = $(quizData.embedAudio);
        $("#question-wrapper").append(embedAudio);
    }
}

// load the next question/ prev question  buttons
function loadButtons(){
    numNext = parseInt(quizData.id) +1;
    numPrev = parseInt(quizData.id) - 1;


    prevQuest= $('<a href="/quiz/' + numPrev + '" class="btn-link">  < Prev. Question </a>');
    nextQuest= $('<a href="/quiz/' + numNext + '" class="btn-link">  Next Question > </a>');
    if (numPrev <= 0){
        prevQuest.addClass("disabled");
        prevQuest.prop("disabled",true);
    }
    if (numNext > maxQuestions) {
        nextQuest.addClass("disabled");
        nextQuest.prop("disabled",true);
    }
    $("#buttons-wrapper").append(prevQuest);
    $("#buttons-wrapper").append(nextQuest);
}



$(document).ready(function(){
    loadChoices();
    loadButtons();
    // handle user clicking on choice
    $('#choices-wrapper').on('click', '.multChoice', function(){    
        let choice = $(this).data("numchoice")
        $("#inline-msg").remove();

        if (choice == quizData.answer){
            // add success msg if correct
            $(this).addClass("bg-success")
            $("<span id='inline-msg' class='text-success'>Correct Answer! </span>").insertAfter("#question-wrapper")
        
        } else {
            // add err msg if incorrect
            $(this).addClass("bg-danger")
            $("<span  id='inline-msg' class='text-danger'>Incorrect Answer </span>").insertAfter("#question-wrapper")
        }
        // disable buttons after answer chosen
        $('.multChoice').each(function(i, obj) {
            $(this).prop("disabled",true);
        });
      
    
        
    });

  

    
})
