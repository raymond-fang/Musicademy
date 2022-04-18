function loadAudio() {
    let audio = $(data.embedAudio);
    $("#audio-wrapper").append(audio);
}


$(document).ready(function(){
    loadAudio();
})