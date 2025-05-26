// FUNCIONALIDAD 1: Cambiar tamaño del texto
function cambiarTamano(factor) {
    const elementos = document.querySelectorAll('h1, h2, h3, h4, p, span, li, a, label, tr, td, th, input, select, textarea, button'
);
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


// FUNCIONALIDAD 3:  Username
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
// FUNCIONALIDAD 4: Generar <select> desde array
function poblarDepartamentos() {
    const departamentos = ['RRHH', 'Marketing', 'IT', 'Contabilidad', 'Ventas'];
    const select = document.getElementById('departamento');
    if (!select) return;

    departamentos.forEach(dep => {
        const option = document.createElement('option');
        option.value = dep.toLowerCase();
        option.textContent = dep;
        select.appendChild(option);
    });
}

// FUNCIONALIDAD 5: Mostrar contenido extra
function activarToggleInformacion() {
    const toggleBtn = document.getElementById('toggleInfo');
    const infoExtra = document.getElementById('infoExtra');

    if (!toggleBtn || !infoExtra) return;

    toggleBtn.addEventListener('click', () => {
        const visible = infoExtra.style.display === 'block';
        infoExtra.style.display = visible ? 'none' : 'block';
        toggleBtn.textContent = visible ? 'Mostrar información adicional' : 'Ocultar información adicional';
    });
}

// Lanzar todas las funciones al cargar
document.addEventListener('DOMContentLoaded', () => {
    // Botones de tamaño
    const btnAumentar = document.getElementById('aumentar');
    const btnDisminuir = document.getElementById('disminuir');

    if (btnAumentar) btnAumentar.addEventListener('click', () => cambiarTamano(2));
    if (btnDisminuir) btnDisminuir.addEventListener('click', () => cambiarTamano(-2));

    validarFormulario();
    autocalcularUsername();
    poblarDepartamentos();
    activarToggleInformacion();
});
