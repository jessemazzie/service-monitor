window.onload = init;
/*
Various tasks performed on page load.
 */
function init() {
    let submitBtn = document.getElementById("add-service-button");

    submitBtn.addEventListener('click', function () {
        let server = document.getElementById("server").value;
        let port = document.getElementById("port").value;
        //TODO: Validate server/port

        getStatus(server, port).then(data => console.log(data));
    });
}

/*
Gets status of a given service.
*/
function getStatus(server, port) {
    return fetch('http://localhost:5000/status/' + server + "/" + port, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => response.json()
            addToDashBoard(server, port);
    );
}

/*
Adds a service to the dashboard.
 */
function addToDashBoard(server, port) {

}