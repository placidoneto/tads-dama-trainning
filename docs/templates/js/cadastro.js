// dados do form
function removePlaceholder(id){
    var input = document.getElementById(id)
    input.removeAttribute('placeholder')

}

function addPlaceholder(id){
    var input = document.getElementById(id)
    if (id == 'nome') var place = "Crie seu nome no DAMA"
    else if (id == 'senha') var place = "Digite sua senha"
    else if (id == 'conf-senha') var place = "Confirme sua senha"
    else if(id === 'cnpj-input')  var place = "XX.XXX.XXX/XXXX-XX"
    else if(id === 'email') var place = "exemplo@email.com"
    else if(id === 'contato') var place = "84 9XXXX-XXXX"
    if (input && input.value == '')
        input.setAttribute('placeholder', place); 
}

function visibilidadeSenha(id){
    const input = document.getElementById(id)

    if (input.type == 'password') {
        input.type = 'text';
    } else {
        input.type = 'password';
    }
}

function mostrarCampos(value){

    if (value !== 'anom'){
        var elementos = document.querySelectorAll('.hidden')
         
        elementos.forEach(function(elemento){
            elemento.classList.remove('hidden');

            elemento.classList.add('visivel');
        });
        
        var nome_usuario = document.getElementById('nome-usuario-label')
        var nome_usuario_input = document.getElementById('nome-usuario-input')

        var cadastro_label = document.getElementById('numero-cadastro-label')
        var cadastro_input = document.getElementById('numero-cadastro-input')

        if (value === 'pro'){
            cadastro_label.innerText = 'CRP'
            cadastro_input.name = 'crp'
            cadastro_input.placeholder = ''
            nome_usuario.innerHTML = "Nome completo"
            nome_usuario_input.name = "nome_completo" 
        }
        else if (value === 'ong'){
            cadastro_label.innerText = 'CNPJ'
            cadastro_input.name = 'cnpj'
            cadastro_input.placeholder = "XX.XXX.XXX/XXXX-XX" 
            nome_usuario.innerHTML = "Razão social"
            nome_usuario_input.name = "razao_social"
        }
        
    }

    else{
        var elementos = document.querySelectorAll('.visivel')
        elementos.forEach(function(elemento){
            elemento.classList.remove('visivel');
            elemento.classList.add('hidden');
        });

    }
    
}
// dados do form

// Adiciona um event listener para o evento de clique no documento
// Manipulação do evento de clique no documento
document.addEventListener('click', function(event) {
    if (event.target.id === 'confirmar-button') {
        // Prevenir a submissão imediata do formulário
        event.preventDefault();

        // Exibir a janela de confirmação após 1s
        setTimeout(function(){
            var janela = document.getElementById('cadastrado');
            if (janela.classList.contains('oculto')) {
                janela.classList.remove('oculto');
                janela.classList.add('cadastrado');
                var main = document.getElementById('main');
                main.classList.add('embassado');
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
    else if(event.target.id === 'login'){
        window.location.href = "login.html"
    }
    else if(event.target.id === 'home'){
        window.location.href = "index.html"
    }
    else if(event.target.id === 'mural-forca'){
        window.location.href = "mural.html"
    }
    else if (event.target.id === 'logo-img')
        window.location.href = 'index.html'
    else {
        // Fechar a janela de confirmação se clicar fora dela
        var janela = document.getElementById('cadastrado');
        if (janela.classList.contains('cadastrado')) {
            janela.classList.remove('cadastrado');
            janela.classList.add('oculto');
            var main = document.getElementById('main');
            main.classList.remove('embassado');
        }
    }
});



