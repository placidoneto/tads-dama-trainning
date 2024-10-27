function visibilidadeSenha(id){
    const input = document.getElementById(id)

    if (input.type == 'password') {
        input.type = 'text';
    } else {
        input.type = 'password';
    }
}

function removePlaceholder(id){
    var input = document.getElementById(id)
    input.removeAttribute('placeholder')

}

function addPlaceholder(id){
    var input = document.getElementById(id)
    if (id == 'nome'){
        var place = "Nome de usuário no DAMA"
    } 
    else if (id == 'senha'){
        var place = "Digite sua senha"
    } 
   
    if (input && input.value == ''){
        input.setAttribute('placeholder', place);
    }
}


document.addEventListener('click', function(event) {
    if (event.target.id === 'entrar') {
        // Prevenir a submissão imediata do formulário
        event.preventDefault();

        var nome = document.getElementById('nome').value
        // Exibir a janela de confirmação após 1s
        setTimeout(function(){
            var janela = document.getElementById('logado');
            if (janela.classList.contains('oculto')) {
                janela.classList.remove('oculto');
                janela.classList.add('logado');
                var main = document.getElementById('main');
                main.classList.add('embassado');
                document.getElementById('nome-usuario').textContent = nome
            }
    
        },1000)

        // Submeter o formulário após 7s
        setTimeout(function() {
            event.target.closest('form').submit();
        }, 7000); 

    } 
    else if(event.target.id === 'denuncia' || event.target.id === 'bttdenuncia'){
        window.location.href = "denuncia.html"
    }
    else if(event.target.id === 'bttcadastro'){
        window.location.href = "cadastro.html"
    }
    else if(event.target.id === 'home' || event.target.id === 'logo-img'){
        window.location.href = "index.html"
    }
    else {
        // Fechar a janela de confirmação se clicar fora dela
        var janela = document.getElementById('logado');
        if (janela.classList.contains('logado')) {
            janela.classList.remove('logado');
            janela.classList.add('oculto');
            var main = document.getElementById('main');
            main.classList.remove('embassado');
        }
    }
});


function criarConta(){
    window.location.href = "cadastro.html"
}