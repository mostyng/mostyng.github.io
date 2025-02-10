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


    const video = document.querySelector('#custom-video');
    if(video) {
      video.playbackRate = 1.5;
      video.play();
      setTimeout(() => {
        console.log('\nvideo.currentTime = ', video.currentTime);
        // console.log('video.durationTime = ', video.durationTime);
        console.log('video.duration = ', video.duration);
        console.log('\nvideo.playbackRate = ', video.playbackRate);
        console.log('video.volume = ', video.volume);
      }, 500);
      setTimeout(() => {
        video.pause();
      }, 1000);
    }

    // <script type="application/javascript">

    // function resizeIFrameToFitContent( iFrame ) {

    //     iFrame.width  = iFrame.contentWindow.document.body.scrollWidth;
    //     iFrame.height = iFrame.contentWindow.document.body.scrollHeight;
    // }

    // window.addEventListener('DOMContentLoaded', function(e) {

    //     var iFrame = document.getElementById( 'iFrame1' );
    //     resizeIFrameToFitContent( iFrame );

    //     // or, to resize all iframes:
    //     var iframes = document.querySelectorAll("iframe");
    //     for( var i = 0; i < iframes.length; i++) {
    //         resizeIFrameToFitContent( iframes[i] );
    //     }
    // } );

    // </script>





//     $('video').each(function(){
//     if ($(this).is(":in-viewport")) {
//         $(this)[0].play();
//     } else {
//         $(this)[0].pause();
//     }
// });

});

