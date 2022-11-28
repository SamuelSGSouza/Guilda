function insere_fundo(url){
    var fundo = document.getElementById('sessao-1');
    fundo.style.backgroundImage = "url('"+url+"')";
    fundo.style.backgroundSize = "cover";
    fundo.style.backgroundPosition = "center";
    fundo.style.backgroundRepeat = "no-repeat";
}