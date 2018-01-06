$(document).ready(function(){

  let lazy = lazyload();
      $("img.lazyload").lazyload();
  });

    $(".boring").on("click", function(){
      $(".infoButton").toggleClass("clicked");
      $(".info").toggleClass("clicked");
    });

    //slide toggle for project content
    $(".collab").click(function(){
        $(".content-collab").toggle();
    });

    $(".politicoin").click(function(){
        $(".content-politicoin").toggle();
    });

    $(".muse").click(function(){
        $(".content-muse").toggle();
    });

    $(".evan-roth").click(function(){
        $(".content-evan-roth").toggle();
    });

    $(".flare").click(function(){
        $(".content-flare").toggle();
    });

    $(".shuffle").click(function(){
        $(".content-shuffle").toggle();
    });

    $(".epigenia").click(function(){
        $(".content-epigenia").toggle();
    });

    $(".cscc").click(function(){
        $(".content-cscc").toggle();
    });

    $(".bfc").click(function(){
        $(".content-bfc").toggle();
    });

    $(".streetlight").click(function(){
        $(".content-streetlight").toggle();
    });

    $(".edes").click(function(){
        $(".content-edes").toggle();
    });

    $(".manzanar").click(function(){
        $(".content-manzanar").toggle();
    });

    $(".raid").click(function(){
        $(".content-raid").toggle();
    });

    $(".posters").click(function(){
        $(".content-posters").toggle();
    });

    $(".cornell-dive").click(function(){
        $(".content-cornell-dive").toggle();
    });

$('.owl-carousel').owlCarousel({
    items:1,
    lazyLoad:true,
    margin:10,
    autoplay:false,
    // autoplayTimeout:5000,
    loop:true
});