function validar() {
  form1 = document.getElementById("form");
  var nome = form1.username.value;
  var first_name = form1.first_name.value;
  var last_name = form1.last_name.value;
  var email = form1.email.value;
  var password = form1.password.value;

    if (nome == "") {
alert('Preencha o campo com seu nome');
nome.focus();
return false;
}
if (first_name == "") {
alert('Preencha o campo com seu primeiro nome');
first_name.focus();
return false;
}
if (last_name == "") {
alert('Preencha o campo com seu último nome');
last_name.focus();
return false;
}
if (password.length < 8) {
    alert('Preencha o campo com sua senha com no mímino 8 caracteres');
    password.focus();
    return false;
  }

if(email.indexOf("@") == -1 ||
      email.indexOf(".") == -1 ||
      email == "" ||
      email == null) {
        alert("Por favor, indique um e-mail válido.");
        email.focus();
        return false;
    }
}

function auth() {
  form1 = document.getElementById("formauth");
  var nome = form1.username.value;
  var password = form1.password.value;

    if (nome == "") {
      alert('Preencha o campo com seu nome');
      nome.focus();
      return false;
}

if (password.length < 8) {
    alert('Preencha o campo com sua senha com no mímino 8 caracteres');
    password.focus();
    return false;
  }

}

function exposicao() {
  form1 = document.getElementById("formexposicao");
  var titulo = form1.titulo.value;
  var assunto = form1.assunto.value;
  var original = form1.original.value;

    if (titulo == "") {
      alert('Preencha o campo com o titulo de sua exposição');
      titulo.focus();
      return false;
}

 if (assunto == "") {
      alert('Preencha o campo com o assunto da sua exposição');
      assunto.focus();
      return false;
}

if (original == "") {
    alert('Adicione alguma foto na sua exposição');
    original.focus();
    return false;
  }

}