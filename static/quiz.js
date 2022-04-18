function loadChoices() {
    $("#question-wrapper").append($('<p> ' + quizData.question + '</p>'));
    for(let i=0; i< 4; i++) {
        let choice = $('<button type="button" class="btn btn-outline-secondary row d-block">' + quizData.choices[i] + '</button>');
        $("#choices-wrapper").append(choice);
    }
}


$(document).ready(function(){
    loadChoices();

 

  

    
})
