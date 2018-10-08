$(document).ready(function(){

	$('.previous').click(function(event) {
		$("body").addClass("slideOutLeft");
	});

	var distance = $('.footer').offset().top,
	$window = $(window);

	$window.scroll(function() {
		if ( $window.scrollTop() >= (distance) ) {
			// var scroll = $(window).scrollTop();
			$(".landing_img_hero").hide();
			$(".nav").hide();
			// $(".footer_wrapper").css("position","fixed");
			// $(".footer_wrapper").css("top","-15px");
			// $(".footer_wrapper").css("margin","0 30px");
			// $(".footer_wrapper").css("width","calc(100% - 60px)");
			$(".footer").css("background","white");
			$(".footer_wrapper").attr('id', 'scrolled_footer');

			$(".footer_up").show();
		}
		else{
			$(".footer_up").hide();

			$(".landing_img_hero").show();
			$(".nav").show();
			$(".footer_wrapper").removeAttr('id', "scrolled_footer");
		}
	});


	$('.footer_up').each(function(){
    $(this).click(function(){ 
        $('html,body').animate({ scrollTop: 0 }, 'slow');
        return false; 
    });
});
});
