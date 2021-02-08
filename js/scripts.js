$(document).ready(function(){


    // $(".info").click(function(){
    //   $(".about").toggle();
    //   $(".projects").toggle();
    //   $(".project-content").toggle();
    // });

    [].forEach.call(document.querySelectorAll('img[data-src]'), function(img) {
    img.setAttribute('src', img.getAttribute('data-src'));
    img.onload = function() {
        img.removeAttribute('data-src');
    };
    });


    // $(".expand-button").click(function(){
    //   $(".expand-container").addClass("show");
    // });

    // $(".expand-button").click(function(){
    //   $(".expand-container.show").removeClass("show");
    // });


    $( ".expand-button" ).click(function() {     
       $('.expand-container').toggle(0);
    });


     // $(".expand-button").on("click", function() {
     //   var nextdiv = $(this).parent().siblings("div");
     //   nextdiv.is(":visible")?nextdiv.hide():nextdiv.show();
     // });

    // $(".expand-button").click(function(){
    //     $(".expand-container").show();
    //   });
    //   $(".expand-button").click(function(){
    //     $(".expand-container").hide();
    //   });





//     $('video').each(function(){
//     if ($(this).is(":in-viewport")) {
//         $(this)[0].play();
//     } else {
//         $(this)[0].pause();
//     }
// });

});

