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
        
        addBinary(0);

        $( "#beep" ).css('transition', "all 100ms" )
        $( "#beep" ).css('box-shadow', 'grey 0.1px 0.1px 1px');
        const myTimeout = setTimeout(function(){
            $( "#beep" ).css('transition', "all 5s ease-out" );
            $( "#beep" ).css('box-shadow', 'grey 2px 2px 5px');
            clearTimeout(myTimeout)
        }, 150);


    


      });
$( "#bop" ).click(function() {
        
        addBinary(1);

        $( "#bop" ).css('transition', "all 100ms" )
        $( "#bop" ).css('box-shadow', 'grey 0.1px 0.1px 1px');
        const myTimeout = setTimeout(function(){
            $( "#bop" ).css('transition', "all 5s ease-out" );
            $( "#bop" ).css('box-shadow', 'grey 2px 2px 5px');
            clearTimeout(myTimeout)
        }, 150);

      });

    
$("#clear").click(function() {
    $("#decoded").html("An image of an image that looks like ");
    $("#binary").html("")
    $( "#clear" ).css('transition', "all 100ms" )
        $( "#clear" ).css('box-shadow', 'grey 0.1px 0.1px 1px');
        const myTimeout = setTimeout(function(){
            $( "#clear" ).css('transition', "all 5s ease-out" );
            $( "#clear" ).css('box-shadow', 'grey 1px 1px 2px');
            clearTimeout(myTimeout)
        }, 150);
 
    });

