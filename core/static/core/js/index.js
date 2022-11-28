function esconde_tela_lateral() {
    var tela_lateral = document.getElementById("tela-lateral-sessao-2");
    tela_lateral.style.left = "-100vw";
}

function exibe_tela_lateral() {
    var tela_lateral = document.getElementById("tela-lateral-sessao-2");
    tela_lateral.style.left = "10vw";
}

function exibe_tela_sites(url) {
    console.log(url);
    $( "#bloco-conteudo-lateral" ).load( url, function(responseTxt, statusTxt, xhr){
        if(statusTxt == "success")
            exibe_tela_lateral();
        else
            alert("Error: " + xhr.status + ": " + xhr.statusText);
    });
}
function carrega_slick(){
    var teste = document.getElementById("bloco-conteudo-lateral");
    console.log(teste);
}

