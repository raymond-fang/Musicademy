//max # of questions in quiz
var maxQuestions= 10;

function loadChoices() {
    $("#question-wrapper").append($('<p> ' + quizData.id + ") " + quizData.question + '</p>'));
    for(let i=0; i< quizData.choices.length; i++) {
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


    prevQuest= $('<a href="/quiz/' + numPrev + '" class="btn-link"><button class="btn quizz-btns">  < Prev. Question </button></a>');
    nextQuest= $('<a href="/quiz/' + numNext + '" class="btn-link"><button class="btn quizz-btns"> Next Question > </button></a>');
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
            $(this).addClass("bg-success");
            var item = {"result" : 1};
            score++;
            $.ajax({
                type: "POST",
                url: "/updateScore",
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(item),
                success: function (response) {
                }
            });
            $("<span id='inline-msg' class='text-success'>Correct Answer! </span>").insertAfter("#question-wrapper")
        
        } else {
            // add err msg if incorrect
            $(this).addClass("bg-danger")
            var item = {"result" : 0};
            $.ajax({
                type: "POST",
                url: "/updateScore",
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(item),
                success: function (response) {
                }
            });
            $("<span id='inline-msg' class='text-danger'>Incorrect Answer </span>").insertAfter("#question-wrapper")
        }
        if (quizData.id == maxQuestions){
            $("<span id='inline-msg'>Final Score: " + score + " </span> <br>").insertAfter("#question-wrapper")
        }
        // disable buttons after answer chosen
        $('.multChoice').each(function(i, obj) {
            $(this).prop("disabled",true);
        });
      
    
        
    });

  

    
})
