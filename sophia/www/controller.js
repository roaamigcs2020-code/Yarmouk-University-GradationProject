$(document).ready(function(){ // to change hello i am sophia
    eel.expose(DisplayMessage);
    function DisplayMessage(message){ // change text dynamically
        $(".siri-message li:first").text(message); // to change the text 
        $(".siri-message").textillate('start'); // to restart the animation
    }

    //Display hood 
    eel.expose(ShowHood)
    function ShowHood(){
        $("#Oval").attr("hidden",false);
        $("#SiriWave").attr("hidden",true);
    }
});



