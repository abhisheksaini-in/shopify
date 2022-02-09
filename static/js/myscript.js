$('#slider1, #slider2, #slider3, #slider4, #slider5, #slider6, #slider7').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function(){
        var id = $(this).attr("pid").toString();
        var em1 = this.parentNode.children[2]
        
        $.ajax({
            type: "GET",
            url: "/pluscart",
            data: {
                product_id:id
            },
            success: function (data) {
                em1.innerText = data.quantity
                document.getElementById("amount").innerText = data.amount
                document.getElementById("totalamount").innerText = data.totalamount
            }
        })
})


$('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var em1 = this.parentNode.children[2]
    
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data: {
            product_id:id
        },
        success: function (data) {
            em1.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
        }
    })
})


$('.remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var em1 = this
    
    $.ajax({
        type: "GET",
        url: "/removecart",
        data: {
            product_id:id
        },
        success: function (data) {
            console.log("Delete")
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
            em1.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})

