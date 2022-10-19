/**
 * This scripts contains helper functions for the data page on the SCUP.
 */

const API_URL = "https://5puisoo9r8.execute-api.us-east-1.amazonaws.com";
const GDC_LIST = `
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">GDC-1</button>
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">GDC-2</button>
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">GDC-3</button>
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">GDC-4</button>
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">GDC-5</button>
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">GDC-6</button>`
const SUBTYPE_LIST = `
    <button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">CAPE</button>
    <button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">AETHER</button>
    <button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">MoSAIC</button>
    <button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">Ephem</button>`
const DATA_LEVEL_LIST = `
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">QL</button>
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">L0</button>
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">L1</button>
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">L2</button>`
const GDC_REGEX = /^GDC-\d$/;
const SUBTYPE_REGEX = /^(CAPE|AETHER|MoSAIC|EPHEM)$/;
const DATA_LEVEL_REGEX = /^(QL|L0|L1|L2|)$/;

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

function stepThrough(currentElement) {
    let wasContentUpdated = false;
    let currentElementText = currentElement.innerText;
    let parentElement = $(currentElement.parentElement);
    if (currentElementText.match(GDC_REGEX)) {
        // Update the list group
        parentElement.empty();
        parentElement.append(SUBTYPE_LIST);
        wasContentUpdated = true;
        // Update the breadcrumb view
    } else if (currentElementText.match(SUBTYPE_REGEX)) {
        parentElement.empty();
        parentElement.append(DATA_LEVEL_LIST);
        wasContentUpdated = true;
    } else if (currentElementText.match(DATA_LEVEL_REGEX)) {
        parentElement.empty();
        // Actuall start loading data from the API
        wasContentUpdated = true;
    }

    if (wasContentUpdated === true) {
        let lastBreadcrumbText = $("#data-breadcrumbs").children().last()[0].innerHTML;
        $("#data-breadcrumbs").children().last().removeClass('active');
        $("#data-breadcrumbs").children().last().replaceWith(`<li class="breadcrumb-item"><a href="">` + lastBreadcrumbText + `</a></li>`);
        $("#data-breadcrumbs").append(`<li class="breadcrumb-item active" aria-current="page">` + currentElementText + `</li>`);
    }
}

function stepBack(currentElement) {
    /** TODO */
    let currentElementText = currentElement.innerText;
    $("#data-breadcrumbs").children().last().remove();
    $("#data-breadcrumbs").children().last().addClass("active");
    $("#data-breadcrumbs").children().last().replaceWith(`<li class="breadcrumb-item">` + lastBreadcrumbText + `</li>`);
}