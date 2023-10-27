const btnBorrar = document.querySelector("#btn-borrar");
const spanInvisible = document.querySelector("#span-id");
const spanCsrf = document.querySelector("#span-csrf");

function eliminar() {
  fetch(
    `http://localhost:8000/proyectos/borrar-proyecto/${spanInvisible.textContent}`,
    {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": `${spanCsrf.textContent}`,
        credentials: "same-origin",
      },
    }
  );
}

btnBorrar.addEventListener("click", eliminar);
