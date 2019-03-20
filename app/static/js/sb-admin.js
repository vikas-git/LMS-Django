$(function () {
    /* set active nav link */
    var setActiveNav = function (url) {
        $('ul.nav a').filter(function () {
            
            return (this.href == url || url.href.indexOf(this.href) == 0);
            
        }).addClass('active').parent().addClass('active').parent().addClass('in').parent('li').addClass('active');
    };
    setActiveNav(window.location);
    
    /* optimize style on load and resize */
    $(window).bind('load resize', function () {
        var top_offset = parseInt($('body').css('margin-top')) || 42;
        var offset = top_offset + parseInt($('#page-footer').outerHeight());
        var height = ((this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height) - offset;
        if (height < 1) {
            height = 1;
        }
        if (height > offset) {
            $('#page-wrapper').css('min-height', (height) + 'px');
        }
        
        /*var width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            $('div.navbar-collapse').removeClass('in');
        }*/
    });
});

/*custom js add by rahul 10-oct-2018 start here */
$(document).ready(function(e){
   var  isMobile = ($(window).width() <= 768) ? true : false ; // to check small mobile screen size
   var  isTablet = ($(window).width() <= 991 && $(window).width() > 991)  ? true : false ; // to check tablet screen size

$(window).resize(function(e){
    isMobile = ($(window).width() <= 768) ? true : false ;
    isTablet = ($(window).width() <= 991 && $(window).width() > 768)  ? true : false ;
    // console.log("does Mobile : "+isMobile);
    if(isMobile){
        $(".side-nav").removeClass("slide-left");
        $("#wrapper").removeClass("sidebar-close");
    }
});
    $(".close-sidebar , html , body").click(function(e){
        (isMobile) ? $(".side-nav").removeClass("slide-left") : null;  
    });
    $(".toggle_sidebar").click(function(e){
        e.stopPropagation();
       $(".side-nav").toggleClass("slide-left");
       if(!isMobile) {$("#wrapper").toggleClass("sidebar-close");}
    });
    $(".side-nav").click(function(e){
        e.stopPropagation();
    })

    
})
/*custom js add by rahul 10-oct-2018 end here */
