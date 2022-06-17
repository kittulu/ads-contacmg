/*-----------------------------------------------------------------------------------

    Template Name:Multikart APP
    Template URI: themes.pixelstrap.com/multikart-app
    Description: This is PWA Html Template
    Author: Pixelstrap
    Author URL: https://themeforest.net/user/pixelstrap

----------------------------------------------------------------------------------- */
// 01.Manifest js
// 02.Loader
// 03.Header sidebar
// 04.Header scroll
// 05.Filter select js
// 06.Quantity js
// 07.wishlist added
// 08.Slick slider
// 09.Image to background
// 10.Payment show more
// 11.Dark local storage
// 12.RTL local storage setting

(function ($) {
  "use strict";

  /*========================
   01. Manifest js
   ==========================*/

  $(window).on('load', function () {
    'use strict';
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker
        .register('/sw.js');
    }
  });


  /*=====================
     02. Loader js 
  ==========================*/
  $(window).on('load', function () {
    setTimeout(function () {
      $('.loader').fadeOut('slow');
    }, 500);
    $('.loader').remove('slow');
  });


  /*=====================
    03.  Header sidebar 
  ==========================*/
  $(".nav-bar").on('click', function () {
    $(".header-sidebar").addClass("show");
    $(".overlay-sidebar").addClass("show");
    $('body').css({
      'overflow': 'hidden'
    });
  });
  $(".overlay-sidebar").on('click', function () {
    $(".header-sidebar").removeClass("show");
    $(".overlay-sidebar").removeClass("show");
    $('body').css({
      'overflow': 'auto'
    });
  });


  /*=====================
     04. Header scroll js
  ==========================*/
  $(window).scroll(function () {
    var scroll = $(window).scrollTop();

    if (scroll >= 15) {
      $("header").addClass("darkHeader");
    } else {
      $("header").removeClass("darkHeader");
    }
  });

  /*=====================
    05. Filter select js
  ==========================*/
  $('.filter-row li, .filter-color li, .size-select li').on('click', function (e) {
    $(this).addClass('active').siblings('.active').removeClass('active');
  });


  /*=====================
   06. Quantity js
  ==========================*/
  var minVal = 1, maxVal = 20; // Set Max and Min values
  // Increase product quantity on cart page
  $(".qty-counter .quantity-right-plus").on('click', function () {
    var $parentElm = $(this).parents(".qty-counter");
    $(this).addClass("clicked");
    setTimeout(function () {
      $(".clicked").removeClass("clicked");
    }, 100);
    var value = $parentElm.find(".input-number").val();
    if (value < maxVal) {
      value++;
    }
    $parentElm.find(".input-number").val(value);
  });
  // Decrease product quantity on cart page
  $(".qty-counter .quantity-left-minus").on('click', function () {
    var $parentElm = $(this).parents(".qty-counter");
    $(this).addClass("clicked");
    setTimeout(function () {
      $(".clicked").removeClass("clicked");
    }, 100);
    var value = $parentElm.find(".input-number").val();
    if (value > 1) {
      value--;
    }
    $parentElm.find(".input-number").val(value);
  });


  /*=====================
    07. wishlist added start
  ==========================*/
  $(".wishlist-btn").on('click', function () {
    if ($(this).hasClass("deactivate")) {
      $(this).removeClass("deactivate")
    }
    if ($(this).hasClass("active")) {
      $(this).addClass("deactivate")
    }
    $(this).toggleClass("animate");
    $(this).toggleClass("active");
    $(this).toggleClass("inactive");
  });

  /*=====================
    08. Slick slider start
  ==========================*/
  $('.category-slider').slick({
    infinite: true,
    slidesToShow: 5,
    slidesToScroll: 5,
    centerMode: true,
    centerPadding: '30px',
    dots: false,
    arrows: false,
  });

  $('.home-slider').slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    centerMode: true,
    centerPadding: '30px',
    dots: true,
    arrows: false,
  });

  $('.brand-slider').slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    centerMode: true,
    centerPadding: '30px',
    dots: false,
    arrows: false,
  });

  $('.product-slider').slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    centerMode: true,
    centerPadding: '60px',
    dots: false,
    arrows: false,
    responsive: [
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 2,
        }
      },
      {
        breakpoint: 365,
        settings: {
          slidesToShow: 2,
          centerPadding: '20px',
        }
      }
    ]
  });

  $('.payment-slider').slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    centerMode: true,
    centerPadding: '40px',
    dots: false,
    arrows: false,
  });

  $('.onboarding-slider').slick({
    centerMode: true,
    centerPadding: '40px',
    slidesToShow: 1,
    infinite: false,
    arrows: false,
    dots: true
  });


  /*=====================
   09. Image to background js
   ==========================*/
  $(".bg-top").parent().addClass('b-top');
  $(".bg-bottom").parent().addClass('b-bottom');
  $(".bg-center").parent().addClass('b-center');
  $(".bg_size_content").parent().addClass('b_size_content');
  $(".bg-img").parent().addClass('bg-size');
  $(".bg-img.blur-up").parent().addClass('blur-up lazyload');

  jQuery('.bg-img').each(function () {

    var el = $(this),
      src = el.attr('src'),
      parent = el.parent();

    parent.css({
      'background-image': 'url(' + src + ')',
      'background-size': 'cover',
      'background-position': 'center',
      'display': 'block'
    });

    el.hide();
  });


  /*========================
    10. Payment show more js
   ==========================*/
  $('.show-more').on('click', function (e) {
    $('.offer-listing').toggleClass("maximized");
    $(this).text(function (i, text) {
      return text === "Show Less" ? "Show More" : "Show Less";
    })
  });


  /*========================
   11. Dark local storage setting js
   ==========================*/
  $('#darkButton').change(function () {
    if ($(this).is(":checked")) {
      $('body').addClass('dark');
      $("#change-link").attr("href", "/assets/css/dark.css");
      localStorage.setItem('body', 'dark');
      localStorage.setItem('layoutcss', '/assets/css/dark.css');
    } else {
      $('body').removeClass('dark');
      $("#change-link").attr("href", "/assets/css/style.css");
      localStorage.setItem('body', '');
      localStorage.setItem('layoutcss', '/assets/css/style.css');
    }
  });

  $("body").attr("class", localStorage.getItem('body'));
  $("#change-link").attr("href", localStorage.getItem('layoutcss') ? localStorage.getItem('layoutcss') : '/assets/css/style.css');
  localStorage.getItem('body') ? $('#darkButton').attr('checked', true) : '';


  /*========================
   12. RTL local storage setting js
   ==========================*/
  $('#rtlButton').change(function () {
    if ($(this).is(":checked")) {
      $("html").attr("dir", "rtl");
      $("#rtl-link").attr("href", "/assets/css/vendors/bootstrap.rtl.css");
      localStorage.setItem('rtlcss', '/assets/css/vendors/bootstrap.rtl.css');
      localStorage.setItem('dir', 'rtl');
    } else {
      $("html").attr("dir", '');
      localStorage.setItem('dir', '');
      $("#rtl-link").attr("href", "/assets/css/vendors/bootstrap.css");
      localStorage.setItem('rtlcss', '/assets/css/vendors/bootstrap.css');
    }
  });
  $("html").attr("dir", localStorage.getItem('dir'));
  $("#rtl-link").attr("href", localStorage.getItem('rtlcss') ? localStorage.getItem('rtlcss') : '/assets/css/vendors/bootstrap.css');
  localStorage.getItem('dir') ? $('#rtlButton').attr('checked', true) : '';


  /*============================
   13. checkbox js
   ==========================*/
  $('.delivery-option-section .form-check input').each(function () {
    if ($(this).is(":checked")) {
      $(this).parents().find(".check-box").parent('li').addClass('red');
    } else {
      $(this).parents().find(".check-box").parent('li').removeClass('red');
    }
  });

})(jQuery);