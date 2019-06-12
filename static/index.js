window.onload = init;

//Various tasks performed on page load.
function init() {
    let submitBtn = document.getElementById("add-service-button");

    submitBtn.addEventListener('click', function () {
        let server = document.getElementById("server");
        let port = document.getElementById("port");
        //TODO: Validate server/port
    });
}


//Gets status of a given service.
function getStatus(server, port) {

}