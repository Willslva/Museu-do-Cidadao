adicionar = document.getElementById("adicionar");
adicionar.onclick = criarCampo
i += 1

interesses = document.getElementById("interesses");

function criarCampo() {
  
  //interesses.innerHTML += "<input type='text' name='interesse' /><br /> ";

  //Criando um label:
  novoLabel = document.createElement("label");
  novoLabel.innerHTML = 'Interesse:'
  //Criando um Input:
  novoInput = document.createElement("input");
  novoInput.type = 'text';
  novoInput.name = 'interesse';

  //Criando uma div:
  novoDiv = document.createElement("div");
  novoDiv.setAttribute("class","bloco_formulario");
  novoDiv.id = 'elemento-' + i++;
  //Adicionando elementos à div
  novoDiv.append(novoLabel);
  novoDiv.append(novoInput);
  //Adicionando div ao bloco maior (interesses)
  interesses.append(novoDiv);

}