$(document).ready(function () {
    $(".main-banner-slider").slick({
            autoplay: true,
            speed: 2000,
            slidesToShow: 1,
            arrows: true,
            infinite: true,
            lazyLoad: "ondemand",
            dots: true,
        }
    );
    $(".event-slider-interior").slick({
        autoplay: true,
        speed: 500,
        slidesToShow: 1,
        vertical: true,
        lazyLoad: "ondemand",
        nextArrow: ".event-interior-down",
        prevArrow: ".event-interior-up",
    });

    $(".event-slider-fashion").slick({
        autoplay: true,
        speed: 500,
        slidesToShow: 1,
        vertical: true,
        lazyLoad: "ondemand",
        nextArrow: ".event-fashion-down",
        prevArrow: ".event-fashion-up",
    });

    $(".media-coverage-slider").slick({
        autoplay: true,
        arrows: true,
        infinite: true,
        lazyLoad: "ondemand",
        slidesToShow: 1,
        nextArrow: ".media-slider-next",
        prevArrow: ".media-slider-prev",
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                }
            }
        ]
    });

    $(".inhouse-mentor-slider").slick({
        centerMode: false,
        autoplay: true,
        slidesToShow: 7,
        arrows: true,
        infinite: true,
        lazyLoad: "ondemand",
        responsive: [
            {
                breakpoint: 1080,
                settings: {
                    arrows: false,
                    centerMode: false,
                    slidesToShow: 5
                }
            },
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: false,
                    slidesToShow: 3
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: false,
                    // centerPadding: '40px',
                    slidesToShow: 2
                }
            }
        ]
    });

    $(".placement-slider").slick({
        autoplay: true,
        speed: 500,
        slidesToShow: 4,
        arrows: true,
        infinite: true,
        lazyLoad: "ondemand",
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: false,
                    slidesToShow: 3
                }
            },
            {
                breakpoint: 550,
                settings: {
                    arrows: false,
                    centerMode: false,
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 1
                }
            }
        ]
    });
    $(".academic-tour-slider").slick({
        autoplay: true,
        speed: 500,
        slidesToShow: 4,
        arrows: true,
        infinite: true,
        height: 400,
        lazyLoad: "ondemand",
        centerMode: true,
        centerPadding: "30px",
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: false,
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 550,
                settings: {
                    arrows: false,
                    centerMode: false,
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 1
                }
            }
        ]
    });
    $(".collaboration-with-slider-fashion").slick({
        autoplay: true,
        speed: 500,
        slidesToShow: 4,
        arrows: true,
        infinite: true,
        lazyLoad: "ondemand",
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 3
                }
            },
            {
                breakpoint: 550,
                settings: {
                    arrows: false,
                    centerMode: false,
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 1
                }
            }
        ]
    });
    $(".collaboration-with-slider-interior").slick({
        autoplay: true,
        speed: 500,
        slidesToShow: 5,
        arrows: true,
        infinite: true,
        lazyLoad: "ondemand",
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 3
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 1
                }
            }
        ]
    });
    $(".exhibitions-slider-fashion").slick({
        autoplay: true,
        speed: 500,
        slidesToShow: 4,
        arrows: true,
        infinite: true,
        lazyLoad: "ondemand",
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 3
                }
            },
            {
                breakpoint: 550,
                settings: {
                    arrows: false,
                    centerMode: false,
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 1
                }
            }
        ]
    });
    $(".exhibitions-slider-interior").slick({
        autoplay: true,
        speed: 500,
        slidesToShow: 4,
        arrows: true,
        infinite: true,
        lazyLoad: "ondemand",
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 3
                }
            },
            {
                breakpoint: 550,
                settings: {
                    arrows: false,
                    centerMode: false,
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 1
                }
            }
        ]
    });
    $(".my_slider_two").slick({
        padding: 10,
        centerPadding: "80px",
        vertical: true,
        centerMode: true,
        slidesToShow: 1,
        arrows: true,
        autoplay: false,
        nextArrow: ".ms-up",
        prevArrow: ".ms-down",
        lazyLoad: "ondemand",
        responsive: [
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 3,
                    vertical: false,
                    arrows: false,
                }
            },
            {
                breakpoint: 680,
                settings: {
                    slidesToShow: 3,
                    vertical: false,
                    arrows: false,
                    centerMode: false,
                    centerPadding: "0px"
                }
            },
            {
                breakpoint: 550,
                settings: {
                    slidesToShow: 2,
                    vertical: false,
                    arrows: false,
                    centerMode: false,
                    centerPadding: "0px"
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 2,
                    vertical: false,
                    arrows: false,
                    centerMode: false,
                    centerPadding: "0px"
                }
            }
        ]
    });

    $(".my_slider_one").slick({
        padding: 10,
        centerPadding: "80px",
        vertical: true,
        centerMode: true,
        slidesToShow: 1,
        arrows: true,
        autoplay: false,
        lazyLoad: "ondemand",
        nextArrow: ".ms-up_one",
        prevArrow: ".ms-down_one",
        responsive: [
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 3,
                    vertical: false,
                    arrows: false,
                }
            },
            {
                breakpoint: 680,
                settings: {
                    slidesToShow: 3,
                    vertical: false,
                    arrows: false,
                    centerMode: false,
                    centerPadding: "0px"
                }
            },
            {
                breakpoint: 550,
                settings: {
                    slidesToShow: 2,
                    vertical: false,
                    arrows: false,
                    centerMode: false,
                    centerPadding: "0px"
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 2,
                    vertical: false,
                    arrows: false,
                    centerMode: false,
                    centerPadding: "0px"
                }
            }
        ]
    });

    $(".my_slider_one").on("beforeChange", function (
        event,
        slick,
        currentSlide,
        nextSlide
    ) {
        let elSlide = $(slick.$slides[nextSlide]);
        let name = elSlide.data("name");
        let content = elSlide.data("content");
        $("#testimony-name").text(name);
        $("#testimony-content").text(content);
    });

    $(".my_slider_two").on("beforeChange", function (
        event,
        slick,
        currentSlide,
        nextSlide,
    ) {
        let elSlide = $(slick.$slides[nextSlide]);
        let name = elSlide.data("name");
        let content = elSlide.data("content");
        $("#testimony-name").text(name);
        $("#testimony-content").text(content);
    });

    $(".placement-partner-fashion-slider").slick({
        autoplay: true,
        speed: 500,
        slidesToShow: 5,
        centerMode: true,
        arrows: true,
        infinite: true,
        lazyLoad: "ondemand",
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 4
                }
            },
            {
                breakpoint: 550,
                settings: {
                    arrows: false,
                    centerMode: false,
                    centerPadding: "40px",
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 1
                }
            }
        ]
    });
    $(".placement-partner-interior-slider").slick({
        autoplay: true,
        speed: 500,
        slidesToShow: 5,
        centerMode: true,
        arrows: true,
        infinite: true,
        lazyLoad: "ondemand",
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 4
                }
            },
            {
                breakpoint: 550,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: "40px",
                    slidesToShow: 1
                }
            }
        ]
    });

    $(".jury-members-slider").slick({
        centerMode: false,
        autoplay: true,
        slidesToShow: 7,
        arrows: true,
        infinite: true,
        lazyLoad: "ondemand",
        responsive: [
            {
                breakpoint: 1080,
                settings: {
                    arrows: false,
                    centerMode: false,
                    slidesToShow: 5
                }
            },
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: false,
                    slidesToShow: 5
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: false,
                    // centerPadding: '40px',
                    slidesToShow: 3
                }
            }
        ]
    });

    $('a[data-bs-toggle="tab"]').on("shown.bs.tab", function (e) {
        $(".collaboration-with-slider-fashion").slick("setPosition");
        $(".collaboration-with-slider-interior").slick("setPosition");
        $(".placement-partner-fashion-slider").slick("setPosition");
        $(".placement-partner-interior-slider").slick("setPosition");
        $(".exhibitions-slider-fashion").slick("setPosition");
        $(".exhibitions-slider-interior").slick("setPosition");
    });
});
