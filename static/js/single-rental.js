var $j = jQuery.noConflict();

var $next_button = $j("button.next");
var $finish_upload = $j(".finish-upload");
var $skip = $j(".skip");
var $skip_all = $j(".skip-all");

$j("#singleunit-form").on('submit', function(event){
    event.preventDefault();
    url = $j("form").attr("data-url")
    url_redirect = $j("form").attr("data-url-redirect")
    var serializedData = $j(this).serialize();
    $j.ajax({
        type:'POST',
        url : url,
        data: serializedData, 

        success: function(response){
            console.log(response)
            //response_instance = JSON.parse(response)
            //if the json is True, do the reset because this means more needs to be done
            if (response["add_more"] == true){
                console.log('need to add more')
                $j("#singleunit-form").trigger('reset');
                number = response['left_to_register']
                $j("b").html(number)
            }
            else{
                // show done 
                window.location.href = url_redirect;
            }
            
        },
        error: function(response){
            alert(response["responseJson"]["error"])
        } 
    })
})

$j("")


$j(".next").on("click", function(){


})