document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('formulario');

    form.addEventListener('submit', function(evt) {
        evt.preventDefault();

        // Obtener los valores de los campos
        const rut = document.getElementById("rut").value;
        const nombre = document.getElementById("nombre").value;
        const apPaterno = document.getElementById("apPaterno").value;
        const apMaterno = document.getElementById("apMaterno").value;
        const edad = document.getElementById("edad").value;
        const genero = document.getElementById("genero").value;
        const celular = document.getElementById("celular").value;
        const comentario = document.getElementById("comentario").value;

        // Validaciones
        if (rut.length < 9 || rut.length > 10) {
            alert("El rut debe tener entre 9 y 10 caracteres.");
            return false;
        }

        if (nombre.length < 3 || nombre.length > 20) {
            alert("El nombre debe tener entre 3 y 20 caracteres.");
            return false;
        }

        if (apPaterno.length < 3 || apPaterno.length > 20) {
            alert("El apellido paterno debe tener entre 3 y 20 caracteres.");
            return false;
        }

        if (apMaterno.length < 3 || apMaterno.length > 20) {
            alert("El apellido materno debe tener entre 3 y 20 caracteres.");
            return false;
        }

        if (edad < 18 || edad > 35) {
            alert("La edad debe estar entre 18 y 35 años.");
            return false;
        }

        if (genero === "") {
            alert("Debe seleccionar un género.");
            return false;
        }

        if (celular.length < 9 || celular.length > 12) {
            alert("El celular debe tener entre 9 y 12 caracteres.");
            return false;
        }

        if (comentario.trim() === "") {
            alert("Debe ingresar un comentario.");
            return false;
        }

        // Generar contenido del archivo
        const contenidoArchivo = `Nombre: ${nombre}\nRUT: ${rut}\nApellido Paterno: ${apPaterno}\nApellido Materno: ${apMaterno}\nEdad: ${edad}\nGénero: ${genero}\nCelular: ${celular}\nComentario: ${comentario}`;
        const blob = new Blob([contenidoArchivo], { type: "text/plain;charset=utf-8" });
        const urlArchivo = URL.createObjectURL(blob);
        const linkDescarga = document.createElement('a');

        linkDescarga.href = urlArchivo;
        linkDescarga.download = 'formulario.txt'; 
        document.body.appendChild(linkDescarga);

        linkDescarga.click();

        document.body.removeChild(linkDescarga);
    });
});


$(document).ready(function() {
    $('#searchForm').submit(function(event) {
        event.preventDefault();

        var searchTerm = $(this).find('input').val().trim().toLowerCase();

        var servicios = {
            'carrito': '{% url "carrito" %}',
            'catalogo': '{% url "catalogo" %}',
            'contacto': '{% url "contacto" %}',
            'menu': '{% url "index" %}',
            'noticias': '{% url "noticias" %}',
            'servivio1': '{% url "servicio" %}'
        };

        if (servicios[searchTerm]) {
            window.location.href = servicios[searchTerm];
        } else {
            alert('Servicio no encontrado');
        }
    });
});


// Generar api fecha y hora actual
function fetchDateTime() {
    const url = 'http://worldtimeapi.org/api/ip';

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('No se pudo obtener la fecha y hora');
            }
            return response.json();
        })
        .then(data => {
            const datetime = new Date(data.utc_datetime);

            const options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric'};
            const formattedDateTime = datetime.toLocaleDateString('es-ES', options);

            document.getElementById('datetime').textContent = formattedDateTime;
        })
        .catch(error => {
            console.error('Error al obtener la fecha y hora:', error);
        });
}

// Llama a la función para mostrar la fecha y hora actual cuando se carga la página
window.onload = function() {
    fetchDateTime(); // Llamada inicial para mostrar la hora y fecha actual
    setInterval(fetchDateTime, 1000); // Actualizar cada segundo
};


$(document).ready(function(){
    $("#idMensajes").delay(2000).fadeOut("slow");
});


