window.addEventListener('load', function () {
    let carouselList = document.querySelector('.carousel__list');
    if (carouselList) {
      new Glider(carouselList, {
        slidesToShow: 1,
        slidesToScroll: 1,
        draggable: true,
        arrows: {
            prev: '.carousel__anterior',
            next: '.carousel__siguiente'
        },
        responsive: [
            {
              // screens greater than >= 450px
              breakpoint: 450,
              settings: {
                // Set to `auto` and provide item width to adjust to viewport
                slidesToShow: 2,
                slidesToScroll: 2,
                draggable: true
              }
            },{
              // screens greater than >= 800px
              breakpoint: 800,
              settings: {
                slidesToShow: 4,
                slidesToScroll: 4,
                draggable: true
              }
            },{
              // screens greater than >= 1024px
              breakpoint: 1024,
              settings: {
                slidesToShow: 5,
                slidesToScroll: 5,
                draggable: true
              }
            }
          ]
      })
    }
});