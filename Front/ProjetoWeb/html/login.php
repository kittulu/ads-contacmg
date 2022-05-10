<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="ContaComigo">
    <meta name="keywords" content="ContaComigo">
    <meta name="author" content="ContaComigo">
    <link rel="manifest" href="manifest.json">
    <link rel="icon" href="assets/images/icon.png" type="image/x-icon" />
    <title>ContaComigo!</title>
    <link rel="apple-touch-icon" href="assets/images/favicon.png">
    <meta name="theme-color" content="#ff4c3b" />
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="apple-mobile-web-app-title" content="ContaComigo">
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
<?php
$value = 'alguma coisa de algum lugar';

setcookie("CookieTeste", $value);
setcookie("CookieTeste", $value, time()+3600);  /* expira em 1 hora */
setcookie("CookieTeste", $value, time()+3600, "/~rasmus/", ".example.com", 1);
?>
    <!-- loader strat -->
    <div class="loader">
        <span></span>
        <span></span>
    </div>
    <!-- loader end -->

    <!-- top bar start -->
    <div class="topbar-section">
        <a href="index.php"><img src="assets/images/logomain.png" class="img-fluid main-logo" alt=""></a>
    </div>
    <!-- top bar end -->


    <!-- login section start -->
    <section class="form-section px-15 top-space section-b-space">
        <h1>Ei, <br>faça seu login</h1>
        <form>
            <div class="form-floating mb-4">
                <input type="text" class="form-control" id="one" placeholder="Email">
                <label for="one">E-mail</label>
            </div>  
            <div class="form-floating mb-2">
                <input type="password" class="form-control" id="two" placeholder="Senha">
                <label for="two">Senha</label>
            </div>
            <div class="text-end mb-4">
                <a href="#" class="theme-color">Esqueceu sua senha?</a>
            </div>
            <a href="index.php" class="btn btn-solid w-100">Login</a>
        </form>
        <div class="or-divider">
            <span>Ou faça login com</span>
        </div>
        <div class="social-auth">
            <ul>
                <li>
                    <a href="#"><img src="assets/images/social/google.png" class="img-fluid" alt=""></a>
                </li>
                <li>
                    <a href="#"><img src="assets/images/social/fb.png" class="img-fluid" alt=""></a>
                </li>
                <li class="apple-icon">
                    <a href="#"><img src="assets/images/social/apple.png" class="img-fluid" alt=""></a>
                </li>
            </ul>
        </div>
        <div class="bottom-detail text-center mt-3">
            <h4 class="content-color">Se você é novo, <a class="title-color text-decoration-underline"
                    href="register.html">Crie uma conta</a></h4>
        </div>
    </section>
    <!-- login section end -->


    <!-- panel space start -->
    <section class="panel-space"></section>
    <!-- panel space end -->



    <!-- latest jquery-->
    <script src="assets/js/jquery-3.3.1.min.js"></script>

    <!-- Bootstrap js-->
    <script src="assets/js/bootstrap.bundle.min.js"></script>

    <!-- Slick js-->
    <script src="assets/js/slick.js"></script>

    <!-- Filter js -->
    <script src="assets/js/filter.js"></script>

    <!-- script js -->
    <script src="assets/js/script.js"></script>

</body>

</html>
