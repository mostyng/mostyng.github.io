$(document).ready(function(){


    $(".info").click(function(){
      $(".about").toggle();
      $(".projects").toggle();
      $(".project-content").toggle();

    });

    [].forEach.call(document.querySelectorAll('img[data-src]'), function(img) {
    img.setAttribute('src', img.getAttribute('data-src'));
    img.onload = function() {
        img.removeAttribute('data-src');
    };
    });

//     $('video').each(function(){
//     if ($(this).is(":in-viewport")) {
//         $(this)[0].play();
//     } else {
//         $(this)[0].pause();
//     }
// });

});

