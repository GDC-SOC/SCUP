/**
 * This scripts contains helper functions for the data page on the SCUP.
 */

const API_URL = "https://5puisoo9r8.execute-api.us-east-1.amazonaws.com";

/**
 * Retrieves a presigned url for the given item using the API.
 * @param {str} item 
 */
function generatePresignedURL(item) {
    console.log("Starting generatePresignedURL...");
    try {
        fetch(API_URL + "/prod/generatepresignedurl?key=" + item, {method: "GET"})
        .then((response) => { return response.json() })
        .then((data) => {console.log(data); window.location.replace(data); });
    } catch (error) {
        alert(error); // TODO - Change this to a Bootstarp notif/toast
    }
}

/**
 * Retrieves all data stored in the S3 bucket using the API.
 */
function getData() {
    console.log("Starting getData...");
    try {
        fetch(API_URL + "/prod/listgdcdata", {method: "GET"})
        .then((response) => { return response.json() })
        .then((data) => { return JSON.parse(data.body); })
        .then((parsedData) => {
            $("#data-list").empty();
            $("#data-loading").remove();
            parsedData.forEach((item, index) => {
                $("#data-list").append('<li class="list-group-item"><a href="#" onclick="generatePresignedURL(\''+item+'\')">'+item+'</a></li>');
            })
        })
    } catch (error) {
        alert(error); // TODO - Change this to a Bootstrap notif/toast
    }
}