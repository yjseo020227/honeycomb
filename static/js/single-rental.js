var $j = jQuery.noConflict();

var $next_button = $j("button.next");
var $finish_upload = $j(".finish-upload");
var $skip = $j(".skip");
var $skip_all = $j(".skip-all");

$j("#singleunit-form").on('submit', function(event){
    console.log("single unit added")
    event.preventDefault();
    url = $j("form").attr("data-url")
    var serializedData = $j(this).serialize();
    $j.ajax({
        type:'POST',
        url : url,
        data: serializedData, 

        success: function(response){
            console.log("it is a success!")
            $j("#singleunit-form").trigger('reset')
        },
        error: function(response){
            alert(response["responseJson"]["error"])
        } 
    })
})

$j("")


$j(".next").on("click", function(){


})