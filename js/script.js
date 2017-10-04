$(document).ready(function(){

  //MAIN DIVS
    $(".cover").on("click", function(){
      $(this).toggleClass("nicked");
      $(".title").toggleClass("nicked");

      $(".infoButton").toggleClass("clicked");
      $(".info").toggleClass("clicked");

    });

    $(".title").on("click", function(){
      $(this).toggleClass("nicked")
      $(".cover").toggleClass("nicked")

      $(".infoButton").toggleClass("clicked");
      $(".info").toggleClass("clicked");

    });

    //slide toggle for project content

    $(".evan-roth").click(function(){
        // $(this).slideToggle()
        $(".content-evan-roth").toggle();
    });


    $(".epigenia").click(function(){
        // $(this).slideToggle()
        $(".content-epigenia").toggle();
    });

    $(".streetlight").click(function(){
        // $(this).slideToggle()
        $(".content-streetlight").toggle();
    });

    $(".edes").click(function(){
        // $(this).slideToggle()
        $(".content-edes").toggle();
    });

    $(".manzanar").click(function(){
        // $(this).slideToggle()
        $(".content-manzanar").toggle();
    });

    $(".raid").click(function(){
        // $(this).slideToggle()
        $(".content-raid").toggle();
    });

    $(".posters").click(function(){
        // $(this).slideToggle()
        $(".content-posters").toggle();
    });

    $(".cornell-dive").click(function(){
        // $(this).slideToggle()
        $(".content-cornell-dive").toggle();
    });


    
let lazy = lazyload();

    $("img.lazyload").lazyload();






});






