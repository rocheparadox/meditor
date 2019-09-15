function populateOptions() {
    var portalsJsonObject = {
        "patient_details": {
            "display_name": "Patient Details",
            "display_picture": "",
            "redirect_link": "/utils/patients_details"
        },
        "add_patient": {
            "display_name": "Add Patient",
            "display_picture": "",
            "redirect_link": "/utils/add_patient"
        },
        "add_pill": {
            "display_name": "Add New Pill Details",
            "display_picture": "",
            "redirect_link": "/utils/add_pill"
        },
        "change_pill": {
            "display_name": "Change Pill Details",
            "display_picture": "",
            "redirect_link": "/utils/change_pill"
        },
        "pill_to_patients": {
            "display_name": "Pill To Patients",
            "display_picture": "",
            "redirect_link": "/utils/pill_to_patients"
        }
    }

    var keys = getJsonKeys(portalsJsonObject);
    //console.log(keys)

    var portalsSpan = document.getElementById("portalsDiv");
    var portalsSpanHtml = "";
    for (i in keys) {
        var key = keys[i];
        var portalJsonObj = portalsJsonObject[key];
        var displayName = portalJsonObj["display_name"];
        var redirect_link = portalJsonObj["redirect_link"];

        var temp = "<a href='";
        temp = temp + redirect_link + "'>" + displayName + "</a>";
        //console.log(temp);

        portalsSpanHtml = portalsSpanHtml + temp;
    }
    //console.log(portalsSpanHtml);
    portalsSpan.innerHTML = portalsSpanHtml;
}