function continueToChat() {
    var form = document.getElementById("signupform");
    var formData = new FormData(form);

    console.log("Form data submitted:");
    for (var pair of formData.entries()) {
        console.log(pair[0]+ ', ' + pair[1]);
    }
}