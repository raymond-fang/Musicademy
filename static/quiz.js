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

function loadResults() {
    results = quizData.results
    for (const n in results){
        let result = $('<div class="res-item my-4"> <div>');
    
        let question = $('<div class="result-question h5 mt-2 mb-0" > <strong> Question ' + results[n].id + ':</strong> '  + results[n].question + ' </div>');
        let answer = $('<hr/><div class="result-answer px-2" >  Your answer: <span class="text-danger">' + results[n].choice +'</span> <br> <span class="font-weight-bold"> Correct Answer: </span> <span class="text-success" ">'+ results[n].answer +   '</span>   </div>');
        let learn = $('<div class="result-learn px-4 py-2"> <a href="/learn/' + results[n].learn + '" class="link-primary result-link" > Click here to review ' + results[n].topic + '  </a> ')
        result.append(question);
        result.append(answer);
        result.append(learn);
        $("#results-wrapper").append(result);
    }
}

// load the next question/ prev question  buttons
function loadButtons(){
    numNext = parseInt(quizData.id) +1;
    if (numNext == 11) {
        nextQuest= $('<a href="/quiz/results" id="next-button" class="btn-link pull-right"><button class="btn quizz-btns"> Results > </button></a>');


    } else {
        nextQuest= $('<a href="/quiz/' + numNext + '" id="next-button" class="btn-link pull-right"><button class="btn quizz-btns"> Next Question > </button></a>');
    }
    nextQuest.addClass("disabled");
    nextQuest.prop("disabled",true);
    $("#buttons-wrapper").append(nextQuest);
}



$(document).ready(function(){
    console.log(quizData)

    if(quizData.id == "result"){
        console.log("results")
        loadResults()

    } else {
        loadChoices();
        loadButtons();
    }

    // handle user clicking on choice
    $('#choices-wrapper').on('click', '.multChoice', function(){    
        let choice = $(this).data("numchoice")
        $("#inline-msg").remove();
        nextQuest.removeClass("disabled");
        nextQuest.prop("disabled",false);


        if (choice == quizData.answer){
            // add success msg if correct
            $(this).addClass("bg-success");
            var item = {"id": quizData.id, "result" : 1, "choice":choice};
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
            $("<span id='inline-msg' class='text-success correct'>Correct Answer! </span>").insertAfter("#question-wrapper")
        
        } else {
            // add err msg if incorrect
            $(this).addClass("bg-danger")
            var item = {"id": quizData.id, "result" : 0, "choice":choice};
            $.ajax({
                type: "POST",
                url: "/updateScore",
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(item),
                success: function (response) {
                }
            });
            $("<span id='inline-msg' class='text-danger' incorrect>Incorrect Answer </span>").insertAfter("#question-wrapper")
        }
        if (quizData.id == maxQuestions){
            $("<span id='inline-msg' class='correct'>Final Score: " + score + " </span> <br> <br>").insertAfter("#question-wrapper")
        }
        // disable buttons after answer chosen
        $('.multChoice').each(function(i, obj) {
            $(this).prop("disabled",true);
        });
        $('#nextButton').removeClass('disabled');
    });

  

    
})
