/* Función para mostrar la contraseña */
window.addEventListener("load", function() {

    // icono para mostrar contraseña
    showPassword = document.querySelector('.show-password');
    showPassword.addEventListener('click', () => {

        // elementos input de tipo clave
        password1 = document.querySelector('#password');
        password2 = document.querySelector('#password2');

        if ( password1.type === "text" ) {
            password1.type = "password"
            password2.type = "password"
            showPassword.classList.remove('fa-eye-slash');
        } else {
            password1.type = "text"
            password2.type = "text"
            showPassword.classList.toggle("fa-eye-slash");
        }

    })

});