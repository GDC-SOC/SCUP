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
    <button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">EPHEM</button>`
const DATA_LEVEL_LIST = `
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">QL</button>
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">L0</button>
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">L1</button>
<button type="button" class="list-group-item list-group-item-action" onclick="stepThrough(this)">L2</button>`
const GDC_REGEX = /^GDC-\d$/;
const SUBTYPE_REGEX = /^(CAPE|AETHER|MoSAIC|EPHEM)$/;
const DATA_LEVEL_REGEX = /^(QL|L0|L1|L2|)$/;
const SPINNER = `<div class="spinner-border text-primary" role="status">
<span class="visually-hidden">Loading...</span>
</div>`

function convertMonth(monthInt) {
    switch(monthInt) {
        case "01":
            return "JAN";
        case "02":
            return "FEB";
        case "03":
            return "MAR";
        case "04":
            return "APR";
        case "05":
            return "MAY";
        case "06":
            return "JUN";
        case "07":
            return "JUL";
        case "08":
            return "AUG";
        case "09":
            return "SEP";
        case "10":
            return "OCT";
        case "11":
            return "NOV";
        case "12":
            return "DEC";
    }
}

/**
 * Retrieves a presigned url for the given item using the API.
 * @param {str} item 
 */
function generatePresignedURL(item) {
    $("#alerts").empty();
    $("#alerts").append(SPINNER);
    try {
        fetch(API_URL + "/prod/generatepresignedurl?key=" + item, {method: "GET"})
        .then((response) => { return response.json() })
        .then((data) => {console.log(data); window.location.replace(data); });
    } catch (error) {
        alert(error); // TODO - Change this to a Bootstarp notif/toast
    }
}

/**
 * Retrieves all the data contained in the S3 bucket, using the given request parameters. Specifically grabs the files and ignores any subdirectories.
 * requestParams is an array of strings, expected as [gdc, subtype, data level], for example ['GDC-1', 'CAPE', 'L2'].
 * @param {element} parentElement 
 * @param {Array[str]} requestParams 
 */
function getFiles(parentElement, requestParams) {
    console.log("Sending request...");
    let gdc = requestParams.shift();
    let subtype = requestParams.shift();
    let datalevel = requestParams.shift();
    let year = requestParams.shift();
    let month = requestParams.shift();
    let day = requestParams.shift();
    try {
        fetch(API_URL + "/prod/listgdcdata?gdc=" + gdc + "&subtype=" + subtype + "&datalevel=" + datalevel + "&year=" + year + "&month=" + month + "&day=" + day + "&type=f", {method: "GET"})
        .then((response) => { return response.json(); })
        .then((data) => { 
            parentElement.empty();
            if (data.length > 0) {
                data.forEach((item, index) => {
                    let itemFilename = item.split("/").pop();
                    parentElement.append('<li class="list-group-item"><a href="#" onclick="generatePresignedURL(\''+item+'\')">'+itemFilename+'</a></li>');
                });
            } else {
                parentElement.append(`<div class="alert alert-warning" role="alert">
                No data was found for the given request!
                </div>`);
            }
        })
    } catch (error) {
        alert(error); // TODO - Change this to a Bootstrap notif/toast
    }
}

function dataSubmit() {
    // Retrieve values
    let selectGDC = $("#selectGDC").find(":selected").text();
    let selectDataType = $("#selectDataType").find(":selected").text();
    let selectDataLevel = $("#selectDataLevel").find(":selected").text();
    let selectDate = $("#selectDate").val();
    let invalidForms = [];
    // Validate
    if (selectGDC == "") { invalidForms.push("GDC"); }
    if (selectDataType == "") { invalidForms.push("Data Type"); }
    if (selectDataLevel == "") { invalidForms.push("Data Level"); }
    if (selectDate == "") { invalidForms.push("Date"); }
    // If there were invalid forms, create an alert
    if (invalidForms.length > 0) {
        $("#alerts").empty();
        $("#alerts").append(`<div class="alert alert-danger" role="alert">
        The following values were invalid: ${invalidForms.join(", ")}
      </div>`)
        return;
    }
    $("#dataList").append(SPINNER);
    selectDate = selectDate.split("-");
    let selectYear = selectDate.shift();
    let selectMonth = convertMonth(selectDate.shift());
    let selectDay = selectDate.shift();
    let requestParams = [selectGDC, selectDataType, selectDataLevel, selectYear, selectMonth, selectDay];
    getFiles($("#dataList"), requestParams);
}