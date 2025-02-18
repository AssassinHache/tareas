// Escena, cámara y renderizador
const escena = new THREE.Scene();
const camara = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderizador = new THREE.WebGLRenderer();
renderizador.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderizador.domElement);

// Cargar textura
const loader = new THREE.TextureLoader();
const textura = loader.load('heno.jpg'); // Reemplaza con tu imagen

// Crear un cilindro con textura
const geometría = new THREE.CylinderGeometry(2, 2, 3, 32);
const material = new THREE.MeshBasicMaterial({ map: textura });
const cilindro = new THREE.Mesh(geometría, material);
escena.add(cilindro);

// Posicionar la cámara
camara.position.z = 5;

// Animación del cilindro
function animacion() {
    requestAnimationFrame(animacion);
    cilindro.rotation.x += 0.05;
    cilindro.rotation.y += 0.05;
    renderizador.render(escena, camara);
}

animacion();

// Ajustar el tamaño de la ventana al cambiar su tamaño
window.addEventListener('resize', () => {
    camara.aspect = window.innerWidth / window.innerHeight;
    camara.updateProjectionMatrix();
    renderizador.setSize(window.innerWidth, window.innerHeight);
});
