if ($('.owl-brand').length) {
    $(document).ready(function() {
        var owl = $('.owl-brand');
        $('.owl-brand').owlCarousel({
            items: 10,
            autoplay: true,
            loop: true,
            autoplayHoverPause: true,
            autoplayTimeout: 700,

            rtl: true,
            dots: false,
            nav: false,
            lazyLoad: true,
            responsive: {
                200: {
                    items: 3,
                    dots: false,
                },
                400: {
                    items: 4,
                    dots: false,
                },
                500: {
                    items: 8,
                    dots: false,
                    center: true,
                    margin: 100,

                },
                768: {
                    items: 12,
                    dots: true,
                    center: true,
                    margin: 100,
                },
                1200: {
                    items: 10,
                    touchDrag: false,
                    mouseDrag: false
                }

            }
        });
    });
}
// owl-carousel
if ($('.owl-wnd').length) {
    $(document).ready(function() {
        var owl = $('.owl-wnd');
        $('.owl-wnd').owlCarousel({
            rtl: true,
            margin: 10,
            nav: true,
            // navText: ['<i class="fa fa-angle-right"></i>', '<i class="fa fa-angle-left"></i>'],
            dots: false,
            responsiveClass: true,

            responsive: {
                0: {
                    items: 1,
                    slideBy: 1
                },
                576: {
                    items: 1,
                    slideBy: 1
                },
                768: {
                    items: 3,
                    slideBy: 2
                },
                992: {
                    items: 4,
                    slideBy: 3
                },
                1400: {
                    items: 4,
                    slideBy: 3
                }
            }
        });
    });
}

if ($('.owl-widget').length) {
    $(document).ready(function() {
        var owl = $('.owl-widget');
        $('.owl-widget').owlCarousel({
            rtl: true,
            margin: 10,
            nav: true,
            navText: ['<i class="far fa-chevron-right"></i>', '<i class="far fa-chevron-left"></i>'],
            loop: true,
            responsiveClass: true,

            responsive: {
                0: {
                    items: 1,
                    slideBy: 1
                },
                576: {
                    items: 1,
                    slideBy: 1
                },
                768: {
                    items: 3,
                    slideBy: 2
                },
                992: {
                    items: 3,
                    slideBy: 2
                },
                1400: {
                    items: 4,
                    slideBy: 3
                }
            }
        });
    });
}

if ($('.owl-loaded').length) {
    $(document).ready(function() {
        var owl = $('.owl-loaded');
        $("#suggestion-slider").owlCarousel({
            rtl: true,
            items: 1,
            autoplay: true,
            autoplayTimeout: 3000,
            loop: true,
            dots: false,
            nav: false,
            onInitialized: startProgressBar,
            onTranslate: resetProgressBar,
            onTranslated: startProgressBar
        });

        function startProgressBar() {
            $(".slide-progress").css({
                width: "100%",
                transition: "width 3000ms"
            });
        }

        function resetProgressBar() {
            $(".slide-progress").css({
                width: 0,
                transition: "width 0s"
            });
        }
    });
}

if ($('.owl-blog').length) {
    $(document).ready(function() {
        var owl = $('.owl-blog');
        $('.owl-blog').owlCarousel({
            rtl: true,
            margin: 13,
            nav: true,
            // navText: ['<i class="fa fa-angle-right"></i>', '<i class="fa fa-angle-left"></i>'],
            dots: false,
            responsiveClass: true,

            responsive: {
                0: {
                    items: 1,
                    slideBy: 1
                },
                576: {
                    items: 1,
                    slideBy: 1
                },
                768: {
                    items: 3,
                    slideBy: 2
                },
                992: {
                    items: 4,
                    slideBy: 3
                },
                1400: {
                    items: 4,
                    slideBy: 3
                }
            }
        });
    });
}

$(window).scroll(function() {
    if ($(window).scrollTop() >= 125) {
        $('.menu').addClass('position-fixed');
        $('.menu-section2').addClass('d-none');
        $('.menu-hr').addClass('d-none');
    } else if ($(window).scrollTop() >= 67.5) {
        $('.menu').removeClass('position-fixed');
        $('.menu-section2').removeClass('d-none');
        $('.menu-hr').removeClass('d-none');
    } else {
        $('.menu').removeClass('position-fixed');
    }
});

$(document).ready(function() {
    $('.owl-progallery').owlCarousel({
        rtl: true,
        thumbs: true,
        items: 1,
        // When only using images in your slide (like the demo) use this option to dynamicly create thumbnails without using the attribute data-thumb.
        thumbImage: false,

        // Enable this if you have pre-rendered thumbnails in your html instead of letting this plugin generate them. This is recommended as it will prevent FOUC
        thumbsPrerendered: true,

        // Class that will be used on the thumbnail container
        thumbContainerClass: 'owl-thumbs',

        // Class that will be used on the thumbnail item's
        thumbItemClass: 'owl-thumb-item'
    });
});






if ($('.owl-widget-Similar').length) {
    $(document).ready(function() {
        var owl = $('.owl-widget-Similar');
        $('.owl-widget-Similar').owlCarousel({
            rtl: true,
            margin: 10,
            nav: true,
            navText: ['<i class="far fa-chevron-right"></i>', '<i class="far fa-chevron-left"></i>'],
            loop: true,
            responsiveClass: true,

            responsive: {
                0: {
                    items: 1,
                    slideBy: 1
                },
                576: {
                    items: 1,
                    slideBy: 1
                },
                768: {
                    items: 3,
                    slideBy: 2
                },
                992: {
                    items: 5,
                    slideBy: 2
                },
                1400: {
                    items: 4,
                    slideBy: 3
                }
            }
        });
    });
}