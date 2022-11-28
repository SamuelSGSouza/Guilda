function esconde_tela_detalhes_sites() {
    var tela_lateral = document.getElementById("area-detalhes");
    tela_lateral.style.left = "200vw";
}

function exibe_tela_lateral_sites() {
    var tela_lateral = document.getElementById("area-detalhes");
    tela_lateral.style.left = "0vw";
}

function exibe_tela_detalhes_sites(url) {
    console.log(url);
    $( "#area-detalhes-wrap" ).load( url, function(responseTxt, statusTxt, xhr){
        if(statusTxt == "success")
            exibe_tela_lateral_sites();
        else
            alert("Error: " + xhr.status + ": " + xhr.statusText);
    });
}

function envia_dados_ajax(url) {
    var nome = document.getElementById("contato_nome").value;
    var email = document.getElementById("contato_email").value;
    var assunto = document.getElementById("contato_assunto").value;
    var mensagem = document.getElementById("contato_mensagem").value;
    console.log(nome);
    var dados = {
        nome: nome,
        email: email,
        assunto: assunto,
        mensagem: mensagem
    };
    $.ajax({
        url: url,
        type: 'GET',
        data: dados,
        success: function (data) {
            alert("Mensagem Enviada com Sucesso!");
        },
        error: function (data) {
            alert("Houve um erro no envio de sua mensagem!");
        }
    });
}


