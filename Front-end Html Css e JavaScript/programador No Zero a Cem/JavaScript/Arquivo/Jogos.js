var numeroSecreto = 0;
var tentativas = 0;
var maxTentativas =10;

function atualizar(){
numeroSecreto=parseInt(Math.random() * 100) +1 ;
console.log(numeroSecreto)
}
function verificarNumero(){
var palpite = document.getElementById("palpite").value;
var mensagem = document.getElementById("mensagem");

if (isNaN(palpite) || palpite > 100 || palpite < 1) {

mensagem.textContent = "Numero Invalida!!";
return;

}
mensagem.textContent = "numero valida"

if (palpite > numeroSecreto){
tentativas ++;
mensagem.textContent = "O numero secreto e Menor!!";

}
else if (palpite < numeroSecreto) {

tentativas ++
mensagem.textContent = "O numero secreto e Maior"

}
else{
mensagem.textContent = "Voce Acertou!! Com" +tentativas+ "tentativas"; 
desativarJogo();
return;
}
var tentativasRestantes = maxTentativas - tentativas;
document.getElementById("tentativas").textContent = "tentativas restantes" + tentativasRestantes;

if (tentativasRestantes <= 0) {
mensagem.textContent = "Voce perdeu! O numero secreto era" + numeroSecreto + ".";
desativarJogo()

}

}
function desativarJogo(){
document.getElementById("btnChutar").disabled =true;
document.getElementById("palpite").disabled = true;

}
atualizar();
