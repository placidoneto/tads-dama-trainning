document.addEventListener('DOMContentLoaded', function() {
    const atualizarDados = document.getElementById('atualizar-dados');
    const atualizarContaButton = document.getElementById('atualizar-conta');

    atualizarContaButton.addEventListener('click', function() {
      atualizarDados.style.display = 'block'; 
    });

    const cancelarButton = document.getElementById('cancelar');
    cancelarButton.addEventListener('click', function() {
      atualizarDados.style.display = 'none'; 
    });
  });