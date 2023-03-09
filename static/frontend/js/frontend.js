$(function () {
  "use strict";
  if ($("#scrool-top").length) {
    const scrollTrigger = 100,
        backToTop = function () {
          const scrollTop = $(window).scrollTop();
          if (scrollTop > scrollTrigger) {
            $("#scrool-top").addClass("show");
          } else {
            $("#scrool-top").removeClass("show");
          }
        };
    backToTop();
    $(window).on("scroll", function () {
      backToTop();
    });
    $("#scrool-top").on("click", function (e) {
      e.preventDefault();
      $("html,body").animate({ scrollTop: 0 }, 700);
    });
  }
  $(document).ready(function () {
    $(".page-scroll a").on("click", function (event) {
      const $anchor = $(this);
      $("html, body")
        .stop()
        .animate(
          { scrollTop: $($anchor.attr("href")).offset().top - 60 },
          1250,
          "easeInOutExpo"
        );
      event.preventDefault();
    });
  });
  $("body").scrollspy({ target: ".navbar-default", offset: 70 });
  $(".navbar-collapse ul li a:not(.dropdown-toggle)").on("click", function () {
    $(".navbar-toggle:visible").click();
  });
});


window.onscroll = function() {myFunction()};
const header = document.getElementById("mainHeader");
const sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}