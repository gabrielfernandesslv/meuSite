function egt() {
    

    if (document.form.nome.value == "") {
        alert ("Diga o nome completo");
        document.form.nome.focus();
        return false;

    }

    if (document.form.idade.value < 18) {
         alert("São para maiores de idade"); 
     return false; 
    }

    if (document.form.cartaosus.value == "") {
        alert ("Insira o número do cartão do sus");
        document.form.cartaosus.focus();
        return false;
    }

    if (document.form.endereco.value == "") {
        alert ("Insira o endereço");
        document.form.endereco.focus();
        return false;
    }


    if (document.form.telefone.value == "") {
        alert ("Insira o número de telefone");
        document.form.telefone.focus();
        return false;
    }

    if (document.form.cidest.value == "") {
        alert ("Insira a cidade e o Estado");
        document.form.cidest.focus();
        return false;
    }
    if (document.form.email.value == "" || document.form.email.value.indexOf('@')==-1 || document.form.email.value.indexOf('.')==-1){ 
            alert("Insira um email válido"); document.formlogin.usuario.focus(); 
            return false; 
        }
        if (document.form.senha.value == "") {
        alert ("Insira a senha");
        document.form.cidest.focus();
        return false;
    }
        if (document.form.confirmarsenha.value != document.form.senha.value ) {
        alert ("As senhas não condizem");
        document.form.cidest.focus();
        return false;
    }

    alert("O cadastro foi enviado com sucesso");
}

function eeggtt() {

       if (document.formlogin.usuario.value == "" || document.formlogin.usuario.value.indexOf('@')==-1 || document.formlogin.usuario.value.indexOf('.')==-1){ 
            alert("Insira um email"); document.formlogin.usuario.focus(); 
            return false; 
        }

        if (document.formlogin.senha.value == "") {
        alert ("Digite a senha");
        document.formlogin.senha.focus();
        return false;
        }

        alert ("Entrando..."); 
}