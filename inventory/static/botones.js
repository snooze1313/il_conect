const miBoton = document.getElementById("mi-boton");

miBoton.addEventListener("click", function() {
  if (miBoton.classList.contains("active")) {
    miBoton.classList.remove("active");
  } else {
    miBoton.classList.add("active");
  }
});