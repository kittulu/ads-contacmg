<!DOCTYPE html>
<html lang="en">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Multikart">
    <meta name="keywords" content="Multikart">
    <meta name="author" content="Multikart">
    <link rel="manifest" href="manifest.json">
    <link rel="icon" href="assets/images/favicon.png" type="image/x-icon" />
    <title>Multikart PWA App</title>
    <link rel="icon" href="assets/images/favicon.png" type="image/x-icon" />
    <link rel="apple-touch-icon" href="assets/images/favicon.png">
    <meta name="theme-color" content="#ff4c3b" />
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="apple-mobile-web-app-title" content="multikart">
    <meta name="msapplication-TileImage" content="assets/images/favicon.png">
    <meta name="msapplication-TileColor" content="#FFFFFF">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />

    <!--Google font-->
    <link href="https://fonts.googleapis.com/css?family=Lato:300,400,700,900" rel="stylesheet">

    <!-- bootstrap css -->
    <link rel="stylesheet" id="rtl-link" type="text/css" href="assets/css/vendors/bootstrap.css">

    <!-- slick css -->
    <link rel="stylesheet" type="text/css" href="assets/css/vendors/slick-theme.css">
    <link rel="stylesheet" type="text/css" href="assets/css/vendors/slick.css">

    <!-- iconly css -->
    <link rel="stylesheet" type="text/css" href="assets/css/vendors/iconly.css">

    <!-- Theme css -->
    <link rel="stylesheet" id="change-link" type="text/css" href="assets/css/style.css">

</head>

<body>

    <!-- loader strat -->
    <div class="loader">
        <span></span>
        <span></span>
    </div>
    <!-- loader end -->



    <!-- header start -->
    <header>
        <div class="back-links">
            <a href="index.php">
                <i class="iconly-Arrow-Left icli"></i>
                <div class="content">
                    <h2>Shopping Cart</h2>
                    <h6>Step 1 of 3</h6>
                </div>
            </a>
        </div>
        <div class="header-option">
            <ul>
                <li>
                    <a href="wishlist.html"><i class="iconly-Heart icli"></i></a>
                </li>
            </ul>
        </div>
    </header>
    <!-- header end -->


    <!-- cart items start -->
    <section class="cart-section pt-0 top-space xl-space">
        <div class="cart-box px-15">
            <a href="product.html" class="cart-img">
                <img src="assets/images/products/1.jpg" class="img-fluid" alt="">
            </a>
            <div class="cart-content">
                <a href="product.html">
                    <h4>Pink Hoodie t-shirt full </h4>
                </a>
                <h5 class="content-color">by Mango</h5>
                <div class="price">
                    <h4>$32.00 <del>$35.00</del><span>20%</span></h4>
                </div>
                <div class="select-size-sec">
                    <a href="javascript:void(0)" data-bs-toggle="offcanvas" data-bs-target="#selectQty" class="opion">
                        <h6>Qty: 1</h6><i class="iconly-Arrow-Down-2 icli"></i>
                    </a>
                    <a href="javascript:void(0)" data-bs-toggle="offcanvas" data-bs-target="#selectSize" class="opion">
                        <h6>Size: S</h6><i class="iconly-Arrow-Down-2 icli"></i>
                    </a>
                </div>
                <div class="cart-option">
                    <h5 data-bs-toggle="offcanvas" data-bs-target="#removecart"><i class="iconly-Heart icli"></i> Move
                        to
                        wishlist</h5>
                    <span class="divider-cls">|</span>
                    <h5 data-bs-toggle="offcanvas" data-bs-target="#removecart"><i class="iconly-Delete icli"></i>
                        Remove
                    </h5>
                </div>
            </div>
        </div>
        <div class="divider"></div>
        <div class="cart-box px-15">
            <a href="product.html" class="cart-img">
                <img src="assets/images/products/2.jpg" class="img-fluid" alt="">
            </a>
            <div class="cart-content">
                <a href="product.html">
                    <h4>Pink Hoodie t-shirt full </h4>
                </a>
                <h5 class="content-color">by Mango</h5>
                <div class="price">
                    <h4>$32.00 <del>$35.00</del><span>20%</span></h4>
                </div>
                <div class="select-size-sec">
                    <a href="javascript:void(0)" data-bs-toggle="offcanvas" data-bs-target="#selectQty" class="opion">
                        <h6>Qty: 1</h6><i class="iconly-Arrow-Down-2 icli"></i>
                    </a>
                    <a href="javascript:void(0)" data-bs-toggle="offcanvas" data-bs-target="#selectSize" class="opion">
                        <h6>Size: S</h6><i class="iconly-Arrow-Down-2 icli"></i>
                    </a>
                </div>
                <div class="cart-option">
                    <h5 data-bs-toggle="offcanvas" data-bs-target="#removecart"><i class="iconly-Heart icli"></i> Move
                        to
                        wishlist</h5>
                    <span class="divider-cls">|</span>
                    <h5 data-bs-toggle="offcanvas" data-bs-target="#removecart"><i class="iconly-Delete icli"></i>
                        Remove
                    </h5>
                </div>
            </div>
        </div>
        <div class="divider"></div>
        <div class="cart-box px-15">
            <a href="product.html" class="cart-img">
                <img src="assets/images/products/3.jpg" class="img-fluid" alt="">
            </a>
            <div class="cart-content">
                <a href="product.html">
                    <h4>Pink Hoodie t-shirt full </h4>
                </a>
                <h5 class="content-color">by Mango</h5>
                <div class="price">
                    <h4>$32.00 <del>$35.00</del><span>20%</span></h4>
                </div>
                <div class="select-size-sec">
                    <a href="javascript:void(0)" data-bs-toggle="offcanvas" data-bs-target="#selectQty" class="opion">
                        <h6>Qty: 1</h6><i class="iconly-Arrow-Down-2 icli"></i>
                    </a>
                    <a href="javascript:void(0)" data-bs-toggle="offcanvas" data-bs-target="#selectSize" class="opion">
                        <h6>Size: S</h6><i class="iconly-Arrow-Down-2 icli"></i>
                    </a>
                </div>
                <div class="cart-option">
                    <h5 data-bs-toggle="offcanvas" data-bs-target="#removecart"><i class="iconly-Heart icli"></i> Move
                        to
                        wishlist</h5>
                    <span class="divider-cls">|</span>
                    <h5 data-bs-toggle="offcanvas" data-bs-target="#removecart"><i class="iconly-Delete icli"></i>
                        Remove
                    </h5>
                </div>
            </div>
        </div>
        <div class="divider"></div>
    </section>
    <!-- cart items end -->


    <!-- you may also like section start -->
    <section class="pt-0 product-slider-section overflow-hidden">
        <div class="title-section px-15">
            <h2>You May also Like</h2>
        </div>
        <div class="product-slider slick-default pl-15">
            <div>
                <div class="product-box ratio_square">
                    <div class="img-part">
                        <a href="product.html"><img src="assets/images/products/9.jpg" alt="" class="img-fluid bg-img"></a>
                        <div class="wishlist-btn">
                            <i class="iconly-Heart icli"></i>
                            <i class="iconly-Heart icbo"></i>
                            <div class="effect-group">
                                <span class="effect"></span>
                                <span class="effect"></span>
                                <span class="effect"></span>
                                <span class="effect"></span>
                                <span class="effect"></span>
                            </div>
                        </div>
                    </div>
                    <div class="product-content">
                        <ul class="ratings">
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo empty"></i></li>
                        </ul>
                        <a href="product.html">
                            <h4>Blue Denim Jacket</h4>
                        </a>
                        <div class="price">
                            <h4>$32.00 <del>$35.00</del><span>20%</span></h4>
                        </div>
                    </div>
                </div>
            </div>
            <div>
                <div class="product-box ratio_square">
                    <div class="img-part">
                        <a href="product.html"><img src="assets/images/products/10.jpg" alt="" class="img-fluid bg-img"></a>
                        <div class="wishlist-btn">
                            <i class="iconly-Heart icli"></i>
                            <i class="iconly-Heart icbo"></i>
                            <div class="effect-group">
                                <span class="effect"></span>
                                <span class="effect"></span>
                                <span class="effect"></span>
                                <span class="effect"></span>
                                <span class="effect"></span>
                            </div>
                        </div>
                    </div>
                    <div class="product-content">
                        <ul class="ratings">
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo empty"></i></li>
                        </ul>
                        <a href="product.html">
                            <h4>Blue Denim Jacket</h4>
                        </a>
                        <div class="price">
                            <h4>$32.00 <del>$35.00</del><span>20%</span></h4>
                        </div>
                    </div>
                </div>
            </div>
            <div>
                <div class="product-box ratio_square">
                    <div class="img-part">
                        <a href="product.html"><img src="assets/images/products/8.jpg" alt="" class="img-fluid bg-img"></a>
                        <div class="wishlist-btn">
                            <i class="iconly-Heart icli"></i>
                            <i class="iconly-Heart icbo"></i>
                            <div class="effect-group">
                                <span class="effect"></span>
                                <span class="effect"></span>
                                <span class="effect"></span>
                                <span class="effect"></span>
                                <span class="effect"></span>
                            </div>
                        </div>
                    </div>
                    <div class="product-content">
                        <ul class="ratings">
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo empty"></i></li>
                        </ul>
                        <a href="product.html">
                            <h4>Blue Denim Jacket</h4>
                        </a>
                        <div class="price">
                            <h4>$32.00 <del>$35.00</del><span>20%</span></h4>
                        </div>
                    </div>
                </div>
            </div>
            <div>
                <div class="product-box ratio_square">
                    <div class="img-part">
                        <a href="product.html"><img src="assets/images/products/2.jpg" alt="" class="img-fluid bg-img"></a>
                        <div class="wishlist-btn">
                            <i class="iconly-Heart icli"></i>
                            <i class="iconly-Heart icbo"></i>
                            <div class="effect-group">
                                <span class="effect"></span>
                                <span class="effect"></span>
                                <span class="effect"></span>
                                <span class="effect"></span>
                                <span class="effect"></span>
                            </div>
                        </div>
                    </div>
                    <div class="product-content">
                        <ul class="ratings">
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo"></i></li>
                            <li><i class="iconly-Star icbo empty"></i></li>
                        </ul>
                        <a href="product.html">
                            <h4>Blue Denim Jacket</h4>
                        </a>
                        <div class="price">
                            <h4>$32.00 <del>$35.00</del><span>20%</span></h4>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <div class="divider"></div>
    <!-- you may also like section end -->


    <!-- order details start -->
    <section id="order-details" class="px-15 pt-0">
        <h2 class="title">Order Details:</h2>
        <div class="order-details">
            <ul>
                <li>
                    <h4>Bag total <span>$220.00</span></h4>
                </li>
                <li>
                    <h4>Bag savings <span class="text-green">-$20.00</span></h4>
                </li>
                <li>
                    <h4>Delivery <span>$50.00</span></h4>
                </li>
            </ul>
            <div class="total-amount">
                <h4>Total Amount <span>$270.00</span></h4>
            </div>
            <div class="delivery-info">
                <img src="assets/images/truck.gif" class="img-fluid" alt="">
                <h4>No Delivery Charges applied on this order </h4>
            </div>
        </div>
    </section>
    <div class="divider"></div>
    <!-- order details end -->


    <!-- service section start -->
    <section class="service-wrapper px-15 pt-0">
        <div class="row">
            <div class="col-4">
                <div class="service-wrap">
                    <div class="icon-box">
                        <img src="assets/svg/returning.svg" class="img-fluid" alt="">
                    </div>
                    <span>7 Day Return</span>
                </div>
            </div>
            <div class="col-4">
                <div class="service-wrap">
                    <div class="icon-box">
                        <img src="assets/svg/24-hours.svg" class="img-fluid" alt="">
                    </div>
                    <span>24/7 Support</span>
                </div>
            </div>
            <div class="col-4">
                <div class="service-wrap">
                    <div class="icon-box">
                        <img src="assets/svg/wallet.svg" class="img-fluid" alt="">
                    </div>
                    <span>Secure Payment</span>
                </div>
            </div>
        </div>
    </section>
    <!-- service section end -->


    <!-- panel space start -->
    <section class="panel-space"></section>
    <!-- panel space end -->


    <!-- bottom panel start -->
    <div class="cart-bottom">
        <div>
            <div class="left-content">
                <h4>$270.00</h4>
                <a href="#order-details" class="theme-color">View details</a>
            </div>
            <a href="delivery.html" class="btn btn-solid">Place Order</a>
        </div>
    </div>
    <!-- bottom panel end -->


    <!-- select qty offcanvas start -->
    <div class="offcanvas offcanvas-bottom h-auto qty-canvas" id="selectQty">
        <div class="offcanvas-body small">
            <h4>Select Quanity:</h4>
            <div class="qty-counter">
                <div class="input-group">
                    <button type="button" class="btn quantity-left-minus" data-type="minus" data-field="">
                        <img src="assets/svg/minus-square.svg" class="img-fluid" alt="">
                    </button>
                    <input type="text" name="quantity" class="form-control form-theme qty-input input-number" value="1">
                    <button type="button" class="btn quantity-right-plus" data-type="plus" data-field="">
                        <img src="assets/svg/plus-square.svg" class="img-fluid" alt="">
                    </button>
                </div>
            </div>
            <a href="delivery.html" class="btn btn-solid w-100" data-bs-dismiss="offcanvas">Add to Bag</a>
        </div>
    </div>
    <!-- select qty offcanvas end -->


    <!-- select size offcanvas start -->
    <div class="offcanvas offcanvas-bottom h-auto qty-canvas" id="selectSize">
        <div class="offcanvas-body small">
            <h4>Select Size:</h4>
            <div class="size-detail mb-2 mt-2">
                <ul class="size-select">
                    <li>S</li>
                    <li>M</li>
                    <li>L</li>
                    <li class="disable">XL</li>
                </ul>
            </div>
            <div class="price mb-3">
                <h4>$32.00 <del>$35.00</del><span>20%</span></h4>
            </div>
            <a href="javascript:void(0)" class="btn btn-solid w-100" data-bs-dismiss="offcanvas">DONE</a>
        </div>
    </div>
    <!-- select size offcanvas end -->


    <!-- remove item canvas start -->
    <div class="offcanvas offcanvas-bottom h-auto removecart-canvas" id="removecart">
        <div class="offcanvas-body small">
            <div class="content">
                <h4>Remove Item:</h4>
                <p>Are you sure you want to remove or move this item from the cart?</p>
            </div>
            <div class="bottom-cart-panel">
                <div class="row">
                    <div class="col-7">
                        <a href="wishlist.html" class="title-color">MOVE TO WISHLIST</a>
                    </div>
                    <div class="col-5">
                        <a href="#" class="theme-color">REMOVE</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- remove item canvas end -->


    <!-- latest jquery-->
    <script src="assets/js/jquery-3.3.1.min.js"></script>

    <!-- Bootstrap js-->
    <script src="assets/js/bootstrap.bundle.min.js"></script>

    <!-- Slick js-->
    <script src="assets/js/slick.js"></script>

    <!-- script js -->
    <script src="assets/js/script.js"></script>

</body>

</html>