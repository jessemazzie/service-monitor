window.onload = init;

//Various tasks performed on page load.
function init() {
    let submitBtn = document.getElementById("add-service-button");

    submitBtn.addEventListener('click', function () {
        alert('test');
    });
}