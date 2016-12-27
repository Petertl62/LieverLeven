(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.parallax').parallax();
    $('.carousel.carousel-slider').carousel({full_width: true});

  }); // end of document ready
  $(function nextSlide() {
    setTimeout(function () {
      $('.carousel').carousel('next');
      nextSlide();
    }, 10000);
  })
})(jQuery); // end of jQuery name space
