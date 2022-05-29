<?php
session_start();

require_once("dbcontroller.php");
$db_handle = new DBController();
if (!empty($_GET["action"])) {

  switch ($_GET["action"]) {
    case "add":

      if (!empty($_POST["quantity"])) {
        $productBycod_produto = $db_handle->runQuery("SELECT cod_produto, nome_produto, preco_produto, imagem_produto, imagem_produto2, imagem_produto3 FROM produto WHERE cod_produto='" . $_GET["cod_produto"] . "'");
        $itemArray = array($productBycod_produto[0]["cod_produto"] => array('nome_produto' => $productBycod_produto[0]["nome_produto"], 'cod_produto' => $productBycod_produto[0]["cod_produto"], 'quantity' => $_POST["quantity"], 'preco_produto' => $productBycod_produto[0]["preco_produto"], 'imagem_produto' => $productBycod_produto[0]["imagem_produto"], 'imagem_produto2' => $productBycod_produto[0]["imagem_produto2"], 'imagem_produto3' => $productBycod_produto[0]["imagem_produto3"]));

        if (!empty($_SESSION["cart_item"])) {
          if (in_array($productBycod_produto[0]["cod_produto"], array_keys($_SESSION["cart_item"]))) {
            foreach ($_SESSION["cart_item"] as $k => $v) {
              if ($productBycod_produto[0]["cod_produto"] == $k) {
                if (empty($_SESSION["cart_item"][$k]["quantity"])) {
                  $_SESSION["cart_item"][$k]["quantity"] = 0;
                }
                $_SESSION["cart_item"][$k]["quantity"] += $_POST["quantity"];
              }
            }
          } else {
            $_SESSION["cart_item"] = array_merge($_SESSION["cart_item"], $itemArray);
          }
        } else {
          $_SESSION["cart_item"] = $itemArray;
        }
      }
      break;
    case "remove":
      if (!empty($_SESSION["cart_item"])) {
        foreach ($_SESSION["cart_item"] as $k => $v) {
          if ($_GET["cod_produto"] == $k)
            unset($_SESSION["cart_item"][$k]);
          if (empty($_SESSION["cart_item"]))
            unset($_SESSION["cart_item"]);
        }
      }
      break;
    case "empty":
      unset($_SESSION["cart_item"]);
      break;
  }
}


?>


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
  <link rel="icon" href="assets/images/favicon.png" type="image/x-icon" /> <!--icone da página-->
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


  <body class="animsition">
    <!-- Header -->
    <header class="header1">
      <!-- Header desktop -->
      <div class="container-menu-header">
        <div class="topbar">
          <div class="topbar-social">
            <a href="https://www.facebook.com/alugueaq" class="topbar-social-item fa fa-facebook  text-dark"></a>
            <a href="https://www.instagram.com/alugueaq" class="topbar-social-item fa fa-instagram  text-dark"></a>

          </div>

          <span class="topbar-child1 text-dark">
           Cadastro de Serviços
          </span>


        </div>

        <div class="wrap_header ">
          <!-- Logo -->
          <a href="index.php" class="logo">

            <h4>AlugueAq</h4>
          </a>

    

          <!-- Header Icon -->
          <div class="header-icons">

            <?php

            if (isset($login)) :  
              

              echo '<div class="dropdown">';
              echo ' <a class="dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">';

              echo ($login);

              echo " </a>";

              echo '<div class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenuLink">';
              echo '<a class="dropdown-item" href="adicionar_prod.php">Adicionar Produto</a>';
              echo '<div class="dropdown-divider"></div>';
              echo '<a class="dropdown-item" href="logout.php">Sair</a>';
              echo '</div>';
              echo '</div>';

            else :

              echo "<a href='login.php' class='header-wrapicon1 dis-block'>";
              echo "Login";
              echo "</a>";
              echo "<span class='linedivide1'></span>";
              echo "<a href='cad_cliente.php' class='header-wrapicon1 dis-block'>";
              echo "Cadastre-se";
              echo "</a>";


            endif;

            ?>

            <span class="linedivide1"></span>

           
          </div>
        </div>
      </div>

      <!-- Header Mobile -->
      <div class="wrap_header_mobile">

        <!-- Arrumar a parte Mobile!!! -->

        <!-- Logo moblie -->
        <a href="index.php" class="logo-mobile">
          <h4>AlugueAq</h4>
        </a>

        <!-- Button show menu -->
        <div class="btn-show-menu">
          <!-- Header Icon mobile -->
          <div class="header-icons-mobile">
            <?php

            if (isset($login)) :

              echo '<div class="dropdown">';
              echo ' <a class="dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">';

              echo ($login);

              echo " </a>";

              echo '<div class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenuLink">';
              echo '<a class="dropdown-item" href="adicionar_prod.php">Adicionar Produto</a>';
              echo '<div class="dropdown-divider"></div>';
              echo '<a class="dropdown-item" href="logout.php">Sair</a>';
              echo '</div>';
              echo '</div>';

            else :

              echo "<a href='login.php' class='header-wrapicon1 dis-block'>";
              echo "Login";
              echo "</a>";
              echo "<span class='linedivide1'></span>";
              echo "<a href='cad_cliente.php' class='header-wrapicon1 dis-block'>";
              echo "Cadastre-se";
              echo "</a>";

            endif;
            ?>
            <span class="linedivide2"></span>

            
          </div>

          <div class="btn-show-menu-mobile hamburger hamburger--squeeze">
            <span class="hamburger-box">
              <span class="hamburger-inner"></span>
            </span>
          </div>
        </div>
      </div>




    <!-- Title Page -->
    <section class="bg-title-page p-t-40 p-b-50 flex-col-c-m" style="background-image: url(images/banner_fundo.jpg);">
      <h2 class="l-text2 t-center">
        Adicione seu Produto
      </h2>
    </section>

    <br />

    <section class="bgwhite p-t-66 p-b-60">
      <h4 class="m-text26 p-b-36 p-t-15 text-center mb-5">
        Preenha os campos abaixo para cadastrar o produto
      </h4>
      <div class="card card-register mx-auto col-8 px-0 mb-5">

        <!-- Add produto -->

        <div class="col-md-12 p-b-30 ">
          <div class="form-row">

            <div class="container col-10 p-b-30 mt-5">

              <form class="addProd form-group " action="add_prod.php" method="POST" enctype="multipart/form-data">
               
                <!-- Nome Produto -->
                <div class="input-group mb-4">
                  <div class="input-group-prepend">
                    <span class="input-group-text">Nome Produto</span>
                  </div>
                  <input type="text" class="form-control  border border-secondary" name="titulo" />
                </div>


                <!-- descricao -->
                <div class="input-group mb-4">
                  <div class="input-group-prepend">
                    <span class="input-group-text">Descrição</span>
                  </div>
                  <textarea class="form-control about input-textoo  border border-secondary" aria-label="Descrição" name="descricao"></textarea>
                </div>

                <!-- Cor do Produto -->

                <!-- descricao -->
                <div class="input-group mb-4">
                  <div class="input-group-prepend">
                    <span class="input-group-text">Cor</span>
                  </div>
                  <input type="text" class="form-control about input-textoo  border border-secondary" aria-label="Cor" name="cor">
                </div>

                <!-- tipo produto -->
                <div class="input-group mb-4">
                  <div class="input-group-prepend">
                    <label class="input-group-text label-input" for="tipo">Tipo</label>
                  </div>
                  <select class="custom-select input-textoo  border border-secondary" id="tipo" name="tipo">
                    <option disabled selected>Escolha...</option>
                    <option value="1"> Blusa</option>
                    <option value="2"> Boné</option>
                    <option value="3"> Calça</option>
                    <option value="4"> Camisa</option>
                    <option value="5"> Camiseta</option>
                    <option value="6"> Casaco</option>
                    <option value="7"> Chapéu</option>
                    <option value="8"> Gravata</option>
                    <option value="9"> Jaqueta</option>
                    <option value="10"> Meia-calça</option>
                    <option value="11"> Saia</option>
                    <option value="12"> Shorts</option>
                    <option value="13"> Sweater</option>
                    <option value="14"> Terno</option>
                    <option value="15"> Vestido</option>
                  </select>
                </div>

                <!-- genero -->
                <div class="input-group mb-4">
                  <div class="input-group-prepend">
                    <label class="input-group-text label-input" for="genero">Gênero</label>
                  </div>
                  <select class="custom-select input-textoo  border border-secondary" id="genero" name="genero">
                    <option disabled selected>Escolha...</option>
                    <option value="feminino"> Feminino</option>
                    <option value="masculino"> Masculino</option>
                    <option value="indeterminado"> Indeterminado</option>
                  </select>
                </div>

                <!-- marca -->
                <div class="input-group mb-4">
                  <div class="input-group-prepend">
                    <label class="input-group-text label-input" for="marca">Marca</label>
                  </div>
                  <select class="custom-select input-textoo  border border-secondary" id="marca" name="marca">
                    <option disabled selected>Escolha...</option>
                    <option disabled>A</option>

                    <option disabled>B</option>

                    <option disabled>C</option>
                    <option value="3"> Calvin Klein </option>
                    <option disabled>D</option>

                    <option disabled>E</option>

                    <option disabled>F</option>

                    <option disabled>G</option>

                    <option disabled>H</option>

                    <option disabled>I</option>

                    <option disabled>J</option>

                    <option disabled>K</option>

                    <option disabled>L</option>

                    <option disabled>M</option>

                    <option disabled>N</option>

                    <option disabled>O</option>

                    <option disabled>P</option>

                    <option disabled>Q</option>

                    <option disabled>R</option>

                    <option disabled>S</option>

                    <option disabled>T</option>

                    <option disabled>U</option>

                    <option disabled>V</option>

                    <option disabled>W</option>

                    <option disabled>X</option>

                    <option disabled>Y</option>

                    <option disabled>Z</option>
                  </select>
                </div>

                <!-- condição -->
                <div class="input-group mb-4">
                  <div class="input-group-prepend">
                    <label class="input-group-text label-input" for="condicao">Condição</label>
                  </div>
                  <select class="custom-select input-textoo  border border-secondary" id="condicao" name="condicao">
                    <option disabled selected>Escolha...</option>
                    <option value="novo">Novo</option>
                    <option value="semiUsado">Semi-usado</option>
                    <option value="usado">Usado</option>
                  </select>
                </div>

                <!-- material -->
                <div class="input-group mb-4">
                  <div class="input-group-prepend">
                    <label class="input-group-text label-input" for="material">Material</label>
                  </div>
                  <select class="custom-select input-textoo  border border-secondary" id="material" name="material">
                    <option disabled selected>Escolha...</option>
                    <option disabled>A</option>
                    <option value="1">Acrílico</option>
                    <option value="2">Alpaca</option>
                    <option disabled>C</option>
                    <option value="3">Chambre</option>
                    <option value="4">Chamois</option>
                    <option value="5">Couro</option>
                    <option value="6">Camurça</option>
                    <option value="7">Couro falso</option>
                    <option value="8">Cotelê</option>
                    <option disabled>D</option>
                    <option value="9">Drill</option>
                    <option disabled>E</option>
                    <option value="10">Elastano</option>
                    <option disabled>F</option>
                    <option value="11">Feltro</option>
                    <option value="12">Fleece</option>
                    <option value="13">Full Grain</option>
                    <option disabled>G</option>
                    <option value="14">Gabardina</option>
                    <option disabled>L</option>
                    <option value="15">Lã</option>
                    <option disabled>M</option>
                    <option value="16">Malha</option>
                    <option value="17">Moletom</option>
                    <option disabled>N</option>
                    <option value="18">Nylon</option>
                    <option disabled>P</option>
                    <option value="19">Paina</option>
                    <option value="20">Piquê</option>
                    <option value="21">Poliéster</option>
                    <option disabled>R</option>
                    <option value="22">Renda</option>
                    <option disabled>S</option>
                    <option value="23">Sarja</option>
                    <option value="24">Scrim</option>
                    <option value="25">Seda</option>
                    <option disabled>T</option>
                    <option value="26">Tafetá</option>
                    <option value="27">Tela</option>
                    <option value="28">Tricô</option>
                    <option value="29">Tule</option>
                    <option disabled>V</option>
                    <option value="30">Veludo</option>
                    <option value="31">Vinil</option>
                  </select>
                </div>

                <!-- tamanho -->
                <div class="input-group mb-4">
                  <div class="input-group-prepend">
                    <label class="input-group-text label-input " for="tamanho">Tamanho</label>
                  </div>
                  <select class="custom-select input-textoo  border border-secondary" id="tamanho" name="tamanho">
                    <option disabled selected>Escolha...</option>
                    <option value="pp">PP</option>
                    <option value="p">P</option>
                    <option value="m">M</option>
                    <option value="g">G</option>
                    <option value="GG">GG</option>
                    <option value="xgg">XGG</option>
                  </select>
                </div>

                <!-- dimensao -->
                <span class="flex-c-m size2 bg1 bo-rad-23 hov1 m-text3 trans-0-4 border" data-toggle="collapse" href="#collapsedimensao" role="button" aria-expanded="false" aria-controls="collapsedimensao">
                  DIMENSÃO DO PRODUTO
                </span>

                <br /><br />

                <div class="collapse" id="collapsedimensao">
                  <input type="text" class="input-texto  border border-secondary mb-3" name="comprimento" placeholder="Comprimento" />
                  <br>
                  <input type="text" class="input-texto  border border-secondary mb-3" name="busto" placeholder="Busto" />

                  <input type="text" class="input-texto border border-secondary mb-3" name="quadril" placeholder="Quadril" />
                  <br>
                  <input type="text" class="input-texto  border border-secondary mb-3" name="cintura" placeholder="Cintura" />
                  <br>
                  <input type="text" class="input-texto  border border-secondary mb-3" name="ombros" placeholder="Ombros" />
                  <br>
                  <input type="text" class="input-texto  border border-secondary mb-3" name="largura" placeholder="Largura" />
             
                </div>

               
                <!--add imagem 1 -->
                <div>Imagem 1</div>
                <div class="input-group mb-4  border border-secondary">
                  <div class="">
                    <input type="file" id="fileImg" name="imagem1" class="" />
                  </div>
                </div>
                <!--<label for="fileImg">INSIRA UMA IMAGEM DO PRODUTO</label>-->

                <!--add imagem 2 -->
                <div>Imagem 2</div>
                <div class="input-group mb-4  border border-secondary">
                  <div class="">
                    <input type="file" id="fileImg" name="imagem2" />
                  </div>
                </div>

                <!--add imagem 3 -->
                <div>Imagem 3</div>
                <div class="input-group mb-4  border border-secondary">
                  <div class="">
                    <input type="file" id="fileImg" name="imagem3" />
                  </div>
                </div>

                <div class="input-group mb-4">
                  <div class="input-group-prepend">
                    <span class="input-group-text">Preço (R$)</span>
                  </div>
                  <input type="text" class="form-control  border border-secondary" name="preco" />
                </div>

                <!-- Button ADD PROD -->
                <button type="submit" class="flex-c-m size2 bg1 bo-rad-23 hov1 m-text3 trans-0-4 ">
                  Adicionar
                </button>
              </form>
            </div>
          </div>

        </div>



      </div>
    </section>

   
    <!-- Back to top -->
    <div class="btn-back-to-top bg0-hov" id="myBtn">
      <span class="symbol-btn-back-to-top">
        <i class="fa fa-angle-double-up" aria-hidden="true"></i>
      </span>
    </div>

    <!-- Container Selection -->
    <div id="dropDownSelect1"></div>
    <div id="dropDownSelect2"></div>

    <!--===============================================================================================-->
    <script type="text/javascript" src="vendor/jquery/jquery-3.2.1.min.js"></script>
    <!--===============================================================================================-->
    <script type="text/javascript" src="vendor/animsition/js/animsition.min.js"></script>
    <!--===============================================================================================-->
    <script type="text/javascript" src="vendor/bootstrap/js/popper.js"></script>
    <script type="text/javascript" src="vendor/bootstrap/js/bootstrap.min.js"></script>
    <!--===============================================================================================-->
    <script type="text/javascript" src="vendor/select2/select2.min.js"></script>
    <script type="text/javascript">
      $(".selection-1").select2({
        minimumResultsForSearch: 20,
        dropdownParent: $('#dropDownSelect1')
      });

      $(".selection-2").select2({
        minimumResultsForSearch: 20,
        dropdownParent: $('#dropDownSelect2')
      });
    </script>
    <!--===============================================================================================-->
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAKFWBqlKAGCeS1rMVoaNlwyayu0e0YRes"></script>
    <script src="js/map-custom.js"></script>
    <!--===============================================================================================-->
    <script src="js/main.js"></script>

  </body>

  </html>