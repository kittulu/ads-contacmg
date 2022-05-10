<?php 
    include("conexao.php");

//STRING    
    $titulo=$_POST['titulo'];
    $genero=$_POST['genero'];
    $descricao=$_POST['descricao'];
    $condicao=$_POST['condicao'];
    $tamanho=$_POST['tamanho'];
    $cor = $_POST['cor'];
//INT
    $tipo=$_POST['tipo'];
    $marca=$_POST['marca'];
    $material=$_POST['material'];
//FLOAT
    $preco=$_POST['preco'];
//DIMENSÃO / STRING
    $busto=$_POST['busto'];
    $cintura=$_POST['cintura'];
    $comprimento=$_POST['comprimento'];
    $largura=$_POST['largura'];
    $ombros=$_POST['ombros'];
    $quadril=$_POST['quadril'];
//IMAGEM/MEDIUMBLOB
    $imagem1=$_FILES['imagem1']['name'];
    $imagem2=$_FILES['imagem2']['name'];
    $imagem3=$_FILES['imagem3']['name'];
    $imagetmp1=addslashes (file_get_contents($_FILES['imagem1']['tmp_name']));
    $imagetmp2=addslashes (file_get_contents($_FILES['imagem2']['tmp_name']));
    $imagetmp3=addslashes (file_get_contents($_FILES['imagem3']['tmp_name']));
    
        
    //ENVIANDO INFORMAÇÕES DO PRODUTO PARA O BANCO DE DADOS
    $sql1 = "INSERT INTO produto (  
            descricao_produto, preco_produto, tamanho_produto, condicao_produto,
            fk_Tipo_cod_tipo, fk_Marca_cod_Marca, fk_Material_cod_Material, imagem_produto, imagem_produto2, imagem_produto3,
            nome_produto, cor_produto)
            VALUES 
            ('$descricao', $preco, '$tamanho', '$condicao', '$tipo', '$marca', '$material',  '$imagetmp1', '$imagetmp2','$imagetmp3','$titulo', '$cor')";
 
    //ENVIANDO DIMENSÃO PARA O BANCO DE DADOS
    $sql2="INSERT INTO dimensao (
            comprimento_dimensao, busto_dimensao, quadril_dimensao, cintura_dimensao,
            ombros_dimensao, largura_dimensao) 
            VALUES (
                '$comprimento', '$busto', '$quadril', '$cintura', '$ombros', '$largura'
                );
    ";

    //ENVIANDO A IMAGEM DO PRODUTO PARA O BANCO DE DADOS
   

    if ((mysqli_query($conexao, $sql1)) && (mysqli_query($conexao, $sql2))){
        
        header('location: produto_cad.php');
    } else {
        echo "Erro:" . $sql1 . mysqli_error($conexao);
        echo "Erro:" . $sql2 . mysqli_error($conexao);
    }


    mysqli_close($conexao);
?>
