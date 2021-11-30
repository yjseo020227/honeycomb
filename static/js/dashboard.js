$( "button" ).on("click", function() {
    var button_text = $( this ).html('button is clicked');
    console.log(button_text)
});


$("#user_select").on('change', function(){
    console.log("option is clicked");
    console.log($(this).val());
    var $selected_user = $(this).val();

    $.ajax({
        url:'api/data/',
        data:{'user': $selected_user},
        dataType: 'json',
        success: function(data){
            properties_list= data['properties'];

            //get the container for all_property
            var $all_property_container = $('div.all_properties');

            //empty all of the all_property_container
            $all_property_container.empty();

            for (const property of properties_list){
                //get all values necessary 
                const property_name = property['name'];
                var price = property['recent_price'];
                var price = add_commas(String(price));
                const photo_url = property['photos'];

                //create a new list element 
                var $property_unique_div = $('<div class = "unique_property"></div>');
                var $property_name_tag = $('<p>' + property_name + '</p>');
                var $property_price_tag = $('<p> <strong> Property Price: </strong>'+ String(price) + '</p>' );            
                var $property_image_tag = $('<img class = "property_image">')
                $property_image_tag.attr("src" , photo_url)
                
                //finally, append it to the container
                $property_unique_div.appendTo($all_property_container);
                $property_name_tag.appendTo($property_unique_div);
                $property_price_tag.appendTo($property_unique_div);
                $property_image_tag.appendTo($property_unique_div);
                
            }
                

            //loop through the properties data, get each of their photo, most recent price data, and name
        },
        error: function(error_data){
            console.log(error_data)
            console.log('there is an error')
        }

    })
})
/** 
 * const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
*/


/** Place commas to the left of every 3 digits starting from the right and place a currency value on the leftmost side
 * @param {*} str1 
 * @returns A string with commas appropriately placed
 */
function add_commas(str1){
    if (str1.length<=3){
        return "₩"+str1;
    }
    else{
        return add_commas(str1.slice(0,-3))+','+str1.slice(-3)
    }
}
