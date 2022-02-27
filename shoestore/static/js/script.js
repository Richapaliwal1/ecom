$(document).ready(function(){
    $('#submit').on('click', function(){
        $product_name = $('#product_name').val();
        $price = $('#price').val();
        $image = $('#image').val();
 
        if($product_name == "" || $price == "" || $image == ""){
            alert("Please complete field");
        }else{
            $.ajax({
                type: "POST",
                url: "checkout",
                data:{
                    product_name: $product_name,
                    price: $price,
                    image: $image,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    alert('Save Data');
                    $('#product_name').val('');
                    $('#price').val('');
                    $('#image').val('');
                    window.location = "checkout";
                }
            });
        }
    });
});