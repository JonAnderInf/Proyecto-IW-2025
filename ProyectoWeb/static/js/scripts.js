

// ----------------------------------------------------------------FUNCIONALIDAD 1: Validación del formulario ----------------------------------------------------------------------------
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


// -----------------------------------------------------------------------FUNCIONALIDAD 2:  Username-----------------------------------------------------------------------------------
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
// --------------------------------------------------FUNCIONALIDAD 3: Generar <select> desde array--------------------------------------------------------------------------------------
function TipoDepartamentos() {
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

// ------------------------------------------------------FUNCIONALIDAD 4: Mostrar contenido extra-------------------------------------------------------------------------------------------
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

// ------------------------------------------------------FUNCIONALIDAD 5: Mostrar mensaje emergente enviar formulario-------------------------------------------------------------------------------------------

// ----------------------------------------------------------Lanzar todas las funciones al cargar-----------------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
    validarFormulario();
    autocalcularUsername();
    TipoDepartamentos();
    activarToggleInformacion();
});



// -------------------------------------------------------------NO VISTO EN LA TEORIA / USO DE FETCH/POST PARA EL ESTADO--------------------------------------------------------------------

function cambiarEstado(ticketId) {
  const url = `/Aerotech/tickets/${ticketId}/cambiar_estado/`; 

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken') 
    },
    body: JSON.stringify({})  
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      const fila = document.getElementById(`ticket-${ticketId}`);
      fila.querySelector('.estado').textContent = data.nuevo_estado;
    } else {
      alert('Error al cambiar estado');
    }
  })
  .catch(error => console.error('Error:', error));
}

// -------------------------------------------------------Función para obtener el CSRF token de las cookies ----------------------------------------------------------------------------
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
