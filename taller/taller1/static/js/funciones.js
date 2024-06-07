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

const header = document.querySelector("header");
const footer = document.querySelector("footer");

header.innerHTML = `
<div class="contenedor">
    <nav class="navbar navbar-expand-lg barra">
        <a class="navbar-brand logo" href="index.html">
            <h1 class="tamano__logo logo__bold no-margin centrar-texto">TM-RM</h1>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto navegacion">
                <li class="nav-item">
                    <a class="nav-link navegacion__enlace buttonNav" href="noticias.html">Noticias</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link navegacion__enlace buttonNav" href="contacto.html">Contacto</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link navegacion__enlace buttonNav" href="catalogo.html">Galería</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle navegacion__enlace buttonNav" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Perfil
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <li><a class="dropdown-item navegacion__enlace" href="#">Iniciar Sesión</a></li>
                        <li><a class="dropdown-item navegacion__enlace" href="#">Cuenta</a></li>
                        <li><a class="dropdown-item navegacion__enlace" href="#">Citas</a></li>
                        <li><a class="dropdown-item navegacion__enlace" href="#">Correo</a></li>
                    </ul>
                </li>
                <li class="nav-item">
                <button class="btn carrito navegacion__enlace" type="button" data-toggle="popover" data-placement="bottom" title="Por el momento la sección de carrito se encuentra en mantenimiento" data-content="Por el momento la sección de carrito se encuentra en mantenimiento" onclick="window.location.href = 'carrito.html';">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cart-fill" viewBox="0 0 16 16">
                    <path d="M0 1.5A.5.5 0 0 1 .5 1H2a.5.5 0 0 1 .485.379L2.89 3H14.5a.5.5 0 0 1 .491.592l-1.5 8A.5.5 0 0 1 13 12H4a.5.5 0 0 1-.491-.408L2.01 3.607 1.61 2H.5a.5.5 0 0 1-.5-.5M5 12a2 2 0 1 0 0 4 2 2 0 0 0 0-4m7 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4m-7 1a1 1 0 1 1 0 2 1 1 0 0 1 0-2m7 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2"/>
                </svg>
            </button>            
                </li>
                <li class="nav-item barra__busqueda">
                    <form class="d-flex" role="search" id="searchForm">
                        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" required>
                        <button class="btn btn-outline-success" type="submit">Buscar</button>
                    </form>
                </li>
            </ul>
        </div>
    </nav>
</div>
`;

footer.innerHTML = `
<div class="contenedor">
    <div class="barra">
        <a class="logo" href="contacto.html">
            <button class="btn carrito navegacion__enlace" type="button" data-placement="bottom">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cart-fill" viewBox="0 0 16 16">
                    <path d="M8 1a5 5 0 0 0-5 5v1h1a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a6 6 0 1 1 12 0v6a2.5 2.5 0 0 1-2.5 2.5H9.366a1 1 0 0 1-.866.5h-1a1 1 0 1 1 0-2h1a1 1 0 0 1 .866.5H11.5A1.5 1.5 0 0 0 13 12h-1a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1h1V6a5 5 0 0 0-5-5"/>
                </svg>
            </button>
        </a>
        <nav class="navegacion">
            <a href="noticias.html" class="navegacion__enlace buttonNav">Noticias</a>
            <a href="contacto.html" class="navegacion__enlace buttonNav">Contacto</a>
            <a href="catalogo.html" class="navegacion__enlace buttonNav">Galería</a>
        </nav>
    </div>
</div>
`;

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

