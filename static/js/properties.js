var count = 0;
var $j = jQuery.noConflict();

//jquery objects reference

//1st page 
var $propertypage_title = $j("h1");
var $all_properties = $j(".all_properties");
var $add_button = $j("button.add-properties-btn");

//2nd page
var $add_property_form = $j(".add-property-form");
var $add_sigleunit_form = $j(".add-single-unit-form");

var $add_property_div = $j("div.add-property-div");
var $add_singleunit_div = $j("div.add-singleunit-div");

var $back_button = $j("button.go-back");

//3rd page (after submit properties)
var $next_button = $j("button.next");
var $finish_upload = $j(".finish-upload");
var $skip = $j(".skip");
var $skip_all = $j(".skip-all");


//helper functions
function add_properties_click(){
    $add_button.on("click", function(){
        console.log("add properties clicked")
        $j(this).hide(); 
        $all_properties.hide();
        $add_property_div.show();
        $back_button.show()
        }
        )};


function go_back_click(){
    $back_button.on("click", function(){
        $back_button.hide();
        $add_property_div.hide();

        $add_button.show();
        $all_properties.show()
    })
}




$j( document ).ready(function(){
    //initially hide property form, single rental form, and back button
    $add_property_div.hide();
    $add_singleunit_div.hide();
    $back_button.hide();




    //when add property is clicked 
    add_properties_click();
    //when back buttoni is clicked
    go_back_click();
    //when property form submit button is clicked 
    //property_submit_click();
    })


    