// FUNCIONALIDAD 1: Cambiar tamaño del texto
function cambiarTamano(factor) {
    const elementos = document.querySelectorAll('h1, h2, h3, h4, h5, h6, p, span, li, a');
    elementos.forEach(el => {
        const actual = parseFloat(window.getComputedStyle(el).fontSize);
        el.style.fontSize = (actual + factor) + 'px';
    });
}

// FUNCIONALIDAD 2: Validación del formulario 
function validarFormulario() {
    const form = document.querySelector('form');
    if (!form) return;

    const dniInput = document.getElementById('id_dni');
    const nombreInput = document.getElementById('id_nombre');
    const erroresDiv = document.createElement('div');
    erroresDiv.id = 'errores';
    erroresDiv.style.color = 'red';
    form.appendChild(erroresDiv);

    const nombresProhibidos = ['admin', 'root', 'usuario'];

    form.addEventListener('submit', (e) => {
        let errores = [];

        if (dniInput && !/^\d{8}[A-Z]$/.test(dniInput.value)) {
            errores.push('El DNI debe tener 8 números seguidos de una letra mayúscula. Ej: 12345678Z');
        }

        if (nombreInput && nombresProhibidos.includes(nombreInput.value.toLowerCase())) {
            errores.push('El nombre no puede ser una palabra reservada.');
        }

        if (errores.length > 0) {
            e.preventDefault();
            erroresDiv.innerHTML = errores.join('<br>');
        } else {
            erroresDiv.innerHTML = '';
        }
    });
}


// FUNCIONALIDAD 3: Autocalcular username a partir de nombre y apellidos
function autocalcularUsername() {
    const nombreInput = document.getElementById('id_nombre');
    const apellidosInput = document.getElementById('id_apellidos');
    const usernameInput = document.getElementById('id_username');

    if (nombreInput && apellidosInput && usernameInput) {
        function actualizarUsername() {
            const nombre = nombreInput.value.trim().toLowerCase();
            const apellidos = apellidosInput.value.trim().toLowerCase();

            if (nombre && apellidos) {
                const primerNombre = nombre.split(' ')[0];
                const primerApellido = apellidos.split(' ')[0];
                usernameInput.value = `${primerNombre}.${primerApellido}`;
            } else {
                usernameInput.value = '';
            }
        }

        nombreInput.addEventListener('input', actualizarUsername);
        apellidosInput.addEventListener('input', actualizarUsername);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Botones de tamaño
    const btnAumentar = document.getElementById('aumentar');
    const btnDisminuir = document.getElementById('disminuir');

    if (btnAumentar) btnAumentar.addEventListener('click', () => cambiarTamano(2));
    if (btnDisminuir) btnDisminuir.addEventListener('click', () => cambiarTamano(-2));

    // Validar formulario
    validarFormulario();

    // Autocalcular username
    autocalcularUsername();
});
