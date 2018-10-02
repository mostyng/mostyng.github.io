$(document).ready(function(){


    $(".info").click(function(){
      $(".topBar").toggleClass("clicked");
      $(".about").toggle();
      $(".feed").toggleClass("clicked");
    });

    // $(".project").click(function(){
    //   $(this).toggleClass("expanded");
    // });

    // $("section.project").click(function(){
    //     $("section.project").show();
    //     $(".content").hide();
    // });

    $(".indexSwitch").click(function(){
        $("section.project").show();
        $(".about").slideUp();
        $(".feed").removeClass("clicked");
    });

    $(".brandSwitch").click(function(){
        $("section.project").hide();
        $("section.project.branding").show();
        $(".about").slideUp();
        $(".feed").removeClass("clicked");
    });
    $(".userSwitch").click(function(){
        $("section.project").hide();
        $("section.project.user").show();
        $(".about").slideUp();
        $(".feed").removeClass("clicked");
    });
    $(".printSwitch").click(function(){
        $("section.project").hide();
        $("section.project.print").show();
        $(".about").slideUp();
        $(".feed").removeClass("clicked");
    });

    //slide toggle for project content

    $(".hush").click(function(){
        $(".content-hush").slideToggle();
    });

    $(".seniors").click(function(){
        $(".content-seniors").slideToggle();
    });

    $(".flags").click(function(){
        $(".content-flags").slideToggle();
    });

    $(".rhody").click(function(){
        $(".content-rhody").slideToggle();
    });

    $(".collab").click(function(){
        $(".content-collab").slideToggle();
    });

    $(".politicoin").click(function(){
        $(".content-politicoin").slideToggle();
    });

    $(".muse").click(function(){
        $(".content-muse").slideToggle();
    });

    $(".evan-roth").click(function(){
        $(".content-evan-roth").slideToggle();
    });

    $(".flare").click(function(){
        $(".content-flare").slideToggle();
    });

    $(".ihs").click(function(){
        $(".content-ihs").slideToggle();
    });

    $(".shuffle").click(function(){
        $(".content-shuffle").slideToggle();
    });

    $(".epigenia").click(function(){
        $(".content-epigenia").slideToggle();
    });

    $(".cscc").click(function(){
        $(".content-cscc").slideToggle();
    });

    $(".bfc").click(function(){
        $(".content-bfc").slideToggle();
    });

    $(".streetlight").click(function(){
        $(".content-streetlight").slideToggle();
    });

    $(".edes").click(function(){
        $(".content-edes").slideToggle();
    });

    $(".dga").click(function(){
        $(".content-dga").slideToggle();
    });

    $(".manzanar").click(function(){
        $(".content-manzanar").slideToggle();
    });

    $(".raid").click(function(){
        $(".content-raid").slideToggle();
    });

    $(".posters").click(function(){
        $(".content-posters").slideToggle();
    });

    $(".cornell-dive").click(function(){
        $(".content-cornell-dive").slideToggle();
    });

    //Close Button Show/hide itself + content
    $(".project").click(function(){
        $("#close").show();
    });

    $("#close").click(function(){
        $(".content").slideUp();
        $("#close").hide();
    });

    let lazy = lazyload();
        $("img.lazyload").lazyload();
    });

$('.owl-carousel').owlCarousel({
    items:1,
    lazyLoad:true,
    margin:10,
    autoplay:false,
    // autoplayTimeout:5000,
    loop:true,
    nav: true,
    center: true
});