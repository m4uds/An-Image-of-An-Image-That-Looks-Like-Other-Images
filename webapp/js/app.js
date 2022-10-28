function blinkNextChar(){
    
    setInterval(function (){
    
        if ($("#next-char").css('opacity') == '1'){
            $("#next-char").css('opacity', '0');
        }
        else {
            
            $("#next-char").css('opacity', '1');}
        }, 1000);
}
blinkNextChar()

function addBinary(newBinary){
    
    //get len of string in #binary
    //if 8 delete
    
    if ($("#binary").text().length == 8){
        $("#binary").html("");
    }

    //add binary to #binary
    
    var existingBinary = $("#binary").text();
    $("#binary").html(existingBinary + newBinary)

    




    //check if 8chars
    //if so add char to decoded text

    if ($("#binary").text().length == 8){
        
        //decode binary to char
        var newChar = String.fromCharCode(parseInt($("#binary").text(), 2)).toLowerCase(); 
        
        //insert decoded char
        $("#decoded").html($("#decoded").text() + newChar)
        
     
    }}

$( "#beep" ).click(function() {
        navigator.vibrate(200)
        addBinary(0);
      });
$( "#bop" ).click(function() {
        navigator.vibrate(200)
        addBinary(1);
      });

//animate drop shadows
$( "#beep" ).mouseover(function() {
    $( "#beep" ).css('transition', "all 100ms")
    $( "#beep" ).css('box-shadow', 'grey 0.1px 0.1px 1px');
});

$( "#beep" ).mouseleave(function() {
    $( "#beep" ).css('transition', "all 2s")
    $( "#beep" ).css('box-shadow', 'grey 2px 2px 5px');
});

//animate drop shadows
$( "#bop" ).mouseover(function() {
    $( "#bop" ).css('transition', "all 100ms" )
    $( "#bop" ).css('box-shadow', 'grey 0.1px 0.1px 1px');
});

$( "#bop" ).mouseleave(function() {
    $( "#bop" ).css('transition', "all 2s")
    $( "#bop" ).css('box-shadow', 'grey 2px 2px 5px');
});