function validar() {
  var nome = form1.nome.value;
  var assunto = form1.assunto.value;
  var mensagem = form1.mensagem.value;
  var email = form1.email.value;

    if (nome == "") {
alert('Preencha o campo com seu nome');
nome.focus();
return false;
}
if (assunto == "") {
alert('Preencha o campo com seu primeiro nome');
assunto.focus();
return false;
}
if (mensagem == "") {
alert('Preencha o campo com seu último nome');
mensagem.focus();
return false;
}
// if (password.length < 8) {
// alert('Preencha o campo com sua senha com no mímino 8 caracteres');
// password.focus();
// return false;
// }

if(email.indexOf("@") == -1 ||
      email.indexOf(".") == -1 ||
      email == "" ||
      email == null) {
        alert("Por favor, indique um e-mail válido.");
        email.focus();
        return false;
    }
}