<!DOCTYPE html>
<html lang="pt-br">

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
                    <h2>Categories</h2>
                </div>
            </a>
        </div>
        <div class="header-option">
            <ul>
                <li>
                    <a href="wishlist.html"><i class="iconly-Heart icli"></i></a>
                </li>
                <li class="nav-bar">
                    <a href="cadservice.php">       
                    <img src="assets/svg/plus-square.svg" class="img-fluid" alt="">
                    </a>
                </li>
            </ul>
        </div>
    </header>
    <!-- header end -->


    <!-- category start -->
    <section class="category-listing px-15 xl-space top-space pt-0">
        <a href="shop.php" class="category-wrap">
            <div class="content-part">
                <img src="assets/images/maos.gif" class="img-fluid sale-gif" alt="">
                <h4>POPULARES</h4>
            </div>
            <div class="img-part">
                <img src="assets/images/category/sale.png" class="img-fluid" alt="">
            </div>
        </a>
        <a href="shop.php.html" class="category-wrap">
            <div class="content-part">
                <h2>BELEZA</h2>
                <h4>Cabeleireiro, manicure, maquiadora...</h4>
            </div>
            <div class="img-part">
                <img src="assets/images/category/beleza.png" class="img-fluid" alt="">
            </div>
        </a>
        <a href="shop.php.html" class="category-wrap">
            <div class="content-part">
                <h2>CASA</h2>
                <h4>Eletricista, jardineiro, faxineira...</h4>
            </div>
            <div class="img-part">
                <img src="assets/images/category/casa.png" class="img-fluid" alt="">
            </div>
        </a>
        <a href="shop.php.html" class="category-wrap">
            <div class="content-part">
                <h2>CONFEITARIA</h2>
                <h4>Boleira, doceira...</h4>
            </div>
            <div class="img-part">
                <img src="assets/images/category/confeitaria.png" class="img-fluid" alt="">
            </div>
        </a>
        <a href="shop.php.html" class="category-wrap">
            <div class="content-part">
                <h2>TECNOLOGIA</h2>
                <h4>TI, design</h4>
            </div>
            <div class="img-part">
                <img src="assets/images/category/tecnologia.png" class="img-fluid" alt="">
            </div>
        </a>
        <a href="shop.php.html" class="category-wrap">
            <div class="content-part">
                <h2>EVENTOS</h2>
                <h4>Buffet...</h4>
            </div>
            <div class="img-part">
                <img src="assets/images/category/eventos.png" class="img-fluid" alt="">
            </div>
        </a>
        
    </section>
    <!-- category end -->


    <!-- panel space start -->
    <section class="panel-space"></section>
    <!-- panel space end -->

    <!-- importa o menu -->
    <?php include "menupages.php" ?>

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
