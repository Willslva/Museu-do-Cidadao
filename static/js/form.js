function validar() {
  var form1 = document.getElementById("form");
  console.log(form1);
  return false;
  console.log(form1.username);
  var nome = form1.username.value;
  var firstnome = form1.first_name.value;
  var lastnome = form1.last_name.value;
  var password = form1.password.value;
  var email = form1.email.value;

    if (nome == "") {
        alert('Preencha o campo com seu nome');
        nome.focus();
        return false;
    }
    if (firstnome == "") {
        alert('Preencha o campo com seu primeiro nome');
        firstnome.focus();
        return false;
    }
    if (lastnome == "") {
        alert('Preencha o campo com seu último nome');
        lastnome.focus();
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

    return false;
}