<!DOCTYPE html>
<html lang="pt-br">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> <!--controlar as ações do browser a respeito do formato de codificação de caracteres utilizado-->
  <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Define em qual versão do Internet Explorer a página deve ser renderizada, evitando falhas devido ao html5.-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!--define o nível de zoom inicial.-->
  <meta name="description" content="Autonomos"> <!--descreve o conteúdo de uma página da web. Os mecanismos de pesquisa mostram isso nos resultados da pesquisa quando a meta descrição também inclui as palavras-chave pesquisadas. -->
  <meta name="keywords" content="ContaComigo"> <!--palavras-chave-->
  <meta name="author" content="Conta Comigo!"> <!--autor-->
  <link rel="manifest" href="manifest.json"> <!--indica que o recurso de destino é um manifesto de aplicativo Web-->
  <link rel="icon" href="assets/images/icon.png" type="image/x-icon" /> <!--icone da página-->
  <title>Conta Comigo!</title>
  <link rel="apple-touch-icon" href="assets/images/favicon.png"> <!--icone da página para app apple-->
  <meta name="theme-color" content="#ff4c3b" /> <!--tema de cor-->
  <meta name="apple-mobile-web-app-capable" content="yes"> <!-- -->
  <meta name="apple-mobile-web-app-status-bar-style" content="black"> <!-- -->
  <meta name="apple-mobile-web-app-title" content="Conta Comigo!"> <!-- -->
  <meta name="msapplication-TileImage" content="assets/images/favicon.png"> <!-- -->
  <meta name="msapplication-TileColor" content="#FFFFFF"> <!-- -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge" /> <!-- -->

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
  <div class="nav-bar">
    <img src="assets/svg/bar.svg" class="img-fluid" alt="">
  </div>
  <a href="index.php" class="brand-logo">
    <img src="assets/images/logomain.png" class="img-fluid main-logo" alt="">
  </a>
  <div class="header-option">
    <ul>
      <li>
        <a href="search.html"><i class="iconly-Search icli"></i></a>
      </li>
      <li>
        <a href="notification.html"><i class="iconly-Notification icli"></i></a>
      </li>
      <li>
        <a href="wishlist.html"><i class="iconly-Heart icli"></i></a>
      </li>
      <li>
        <a href="cart.html"><i class="iconly-Buy icli"></i></a>
      </li>
    </ul>
  </div>
</header>
<a href="javascript:void(0)" class="overlay-sidebar"></a>
<div class="header-sidebar">
  <a href="profile-setting.html" class="user-panel">
    <img src="assets/images/user/1.png" class="img-fluid user-img" alt="">
    <span>Hello, Paige Turner</span>
    <i class="iconly-Arrow-Right-2 icli"></i>
  </a>
  <div class="sidebar-content">
    <ul class="link-section">
      <li>
        <div>
          <i class="iconly-Setting icli"></i>
          <div class="content toggle-sec w-100">
            <div>
              <h4 class="mb-0">Dark Mode</h4>
            </div>
            <div class="button toggle-btn ms-auto">
              <input id="darkButton" type="checkbox" class="checkbox">
              <div class="knobs">
                <span></span>
              </div>
              <div class="layer"></div>
            </div>
          </div>
        </div>
      </li>
      <li>
        <div>
          <i class="iconly-Setting icli"></i>
          <div class="content toggle-sec w-100">
            <div>
              <h4 class="mb-0">RTL</h4>
            </div>
            <div class="button toggle-btn ms-auto">
              <input id="rtlButton" type="checkbox" class="checkbox">
              <div class="knobs">
                <span></span>
              </div>
              <div class="layer"></div>
            </div>
          </div>
        </div>
      </li>
      <li>
        <a href="index.php">
          <i class="iconly-Home icli"></i>
          <div class="content">
            <h4>Home</h4>
            <h6>Offers, Top Deals, Top Brands</h6>
          </div>
        </a>
      </li>
      <li>
        <a href="category.html">
          <i class="iconly-Category icli"></i>
          <div class="content">
            <h4>Shop by Category</h4>
            <h6>Men, Women, Kids, Beauty.. </h6>
          </div>
        </a>
      </li>
      <li>
        <a href="order-history.html">
          <i class="iconly-Document icli"></i>
          <div class="content">
            <h4>Orders</h4>
            <h6>Ongoing Orders, Recent Orders..</h6>
          </div>
        </a>
      </li>
      <li>
        <a href="wishlist.html">
          <i class="iconly-Heart icli"></i>
          <div class="content">
            <h4>Your Wishlist</h4>
            <h6>Your Save Products</h6>
          </div>
        </a>
      </li>
      <li>
        <a href="profile.html">
          <i class="iconly-Profile icli"></i>
          <div class="content">
            <h4>Your Account</h4>
            <h6>Profile, Settings, Saved Cards...</h6>
          </div>
        </a>
      </li>
      <li>
        <a href="#">
          <img src="assets/images/flag.png" class="img-fluid" alt="">
          <div class="content">
            <h4>Langauge</h4>
            <h6>Select your Language here..</h6>
          </div>
        </a>
      </li>
      <li>
        <a href="notification.html">
          <i class="iconly-Notification icli"></i>
          <div class="content">
            <h4>Notification</h4>
            <h6>Offers, Order tracking messages..</h6>
          </div>
        </a>
      </li>
      <li>
        <a href="settings.html">
          <i class="iconly-Setting icli"></i>
          <div class="content">
            <h4>Settings</h4>
            <h6>Dark mode, RTL, Notification</h6>
          </div>
        </a>
      </li>
    </ul>
    <div class="divider"></div>
    <ul class="link-section">
      <li>
        <a href="about-us.html">
          <i class="iconly-Info-Square icli"></i>
          <div class="content">
            <h4>About us</h4>
            <h6>About Multikart</h6>
          </div>
        </a>
      </li>
      <li>
        <a href="help.html">
          <i class="iconly-Call icli"></i>
          <div class="content">
            <h4>Help/Customer Care</h4>
            <h6>Customer Support, FAQs</h6>
          </div>
        </a>
      </li>
    </ul>
  </div>
</div>
<!-- header end -->



  <!-- category start -->
  <section class="category-section top-space">
    <ul class="category-slide">
      <li>
        <a href="#" class="category-box">
          <img src="assets/images/top-category/limpeza.png" class="img-fluid" alt="">
          <h4>Limpeza</h4>
        </a>
      </li>
      <li>
        <a href="#" class="category-box">
          <img src="assets/images/top-category/beleza.png" class="img-fluid" alt="">
          <h4>Beleza</h4>
        </a>
      </li>
      <li>
        <a href="#" class="category-box">
          <img src="assets/images/top-category/manutencao.png" class="img-fluid" alt="">
          <h4>Manutenção</h4>
        </a>
      </li> 
      <li>
        <a href="#" class="category-box">
          <img src="assets/images/top-category/midia.png" class="img-fluid" alt="">
          <h4>Mídia</h4>
        </a>
      </li>
      <li>
        <a href="#" class="category-box">
          <img src="assets/images/top-category/confeitaria.png" class="img-fluid" alt="">
          <h4>Confeitaria</h4>
        </a>
      </li>
      <li>
        <a href="#" class="category-box">
          <img src="assets/images/top-category/gerais.png" class="img-fluid" alt="">
          <h4>Gerais</h4>
        </a>
      </li>
    </ul>
  </section>
  <div class="divider t-12 b-20"></div>
  <!-- category end -->


  <!-- home slider start -->
  <section class="pt-0 home-section ratio_55">
    <div class="home-slider slick-default theme-dots">
      <div>
        <div class="slider-box">
          <img src="assets/images/home-slider/slide1.jpg" class="img-fluid bg-img" alt="">
          <div class="slider-content">
            <div>
              <h2>MELHORES AVALIAÇÕES</h2>
              <a href="#" class="btn btn-solid">Contrate agora!</a>
            </div>
          </div>
        </div>
      </div>
      <div>
        <div class="slider-box">
          <img src="assets/images/home-slider/slide2.jpg" class="img-fluid bg-img" alt="">
          <div class="slider-content">
            <div>
              <h2>SUA CASA LIMPA</h2>
              <a href="#" class="btn btn-solid">Contrate agora!</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- home slider end -->


  <!-- Serviços populares start -->
  <section class="deals-section px-15 pt-0">
    <div class="title-part">
      <h2>Serviços Populares</h2>
      <a href="#">Ver tudo</a>
    </div>
    <div class="product-section">
      <div class="row gy-3">
        <div class="col-12">
          <div class="product-inline">
            <a href="#">
              <img src="assets/images/products/01.jpg" class="img-fluid" alt="">
            </a>
            <div class="product-inline-content">
              <div>
                <a href="#">
                  <h4>Confeitaria</h4>
                </a>
                <h5>Luana Silva</h5>
                <div class="price">
                  <h4>R$55.00 <del>$45.00</del><span>-R$10</span></h4>
                </div>
              </div>
            </div>
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
        </div>
        <div class="col-12">
          <div class="product-inline">
            <a href="#">
              <img src="assets/images/products/02.png" class="img-fluid" alt="">
            </a>
            <div class="product-inline-content">
              <div>
                <a href="#">
                  <h4>Eletricista</h4>
                </a>
                <h5>José Antônio</h5>
                <div class="price">
                  <h4>R$80.00<span>Boas avaliações</span></h4>
                </div>
              </div>
            </div>
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
        </div>
        <div class="col-12">
          <div class="product-inline">
            <a href="#">
              <img src="assets/images/products/3.jpg" class="img-fluid" alt="">
            </a>
            <div class="product-inline-content">
              <div>
                <a href="#">
                  <h4>Consultora de moda</h4>
                </a>
                <h5>Camilla Lima</h5>
                <div class="price">
                  <h4>$120.00 <del>$150.00</del><span>20%</span></h4>
                </div>
              </div>
            </div>
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
        </div>
      </div>
    </div>
  </section>
  <div class="divider"></div>
  <!-- deals section end -->


  <!-- kids corner section start -->
  <section class="pt-0 product-slider-section overflow-hidden">
    <div class="title-section px-15">
      <h2>Melhores avaliações</h2>
      <h3>Profissionais verificados </h3>
    </div>
    <div class="product-slider slick-default pl-15">
      <div>
        <div class="product-box ratio_square">
          <div class="img-part">
            <a href="#"><img src="assets/images/products/03.jpg" alt="" class="img-fluid bg-img"></a>
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
              <li><i class="iconly-Star icbo"></i></li>
            </ul>
            <a href="#">
              <h4>Cabeleireiro Silva</h4>
            </a>
            <div class="price">
              <h4>54 serviços contratados
            </div>
          </div>
        </div>
      </div>
      <div>
        <div class="product-box ratio_square">
          <div class="img-part">
            <a href="#"><img src="assets/images/products/05.png" alt="" class="img-fluid bg-img"></a>
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
              <li><i class="iconly-Star icbo"></i></li>
            </ul>
            <a href="#">
              <h4>Doces da Graça</h4>
            </a>
            <div class="price">
              <h4>32 serviços contratados
            </div>
          </div>
        </div>
      </div>
      <div>
        <div class="product-box ratio_square">
          <div class="img-part">
            <a href="#"><img src="assets/images/products/04.png" alt="" class="img-fluid bg-img"></a>
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
              <li><i class="iconly-Star icbo"></i></li>
            </ul>
            <a href="#">
              <h4>Marcia Bolos e CIA</h4>
            </a>
            <div class="price">
              <h4>28 serviços contratados
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- section end -->

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

  <!-- Slick js-->
  <script src="assets/js/homescreen-popup.js"></script>

  <!-- timer js-->
  <script src="assets/js/timer.js"></script>

  <!-- offcanvas modal js -->
  <script src="assets/js/offcanvas-popup.js"></script>

  <!-- script js -->
  <script src="assets/js/script.js"></script>

</body>

</html>