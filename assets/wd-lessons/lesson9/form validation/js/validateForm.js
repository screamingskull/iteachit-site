function formError() {
	var name = document.forms["testForm"]["name"].value;
	var age = document.forms["testForm"]["age"].value;
    var email = document.forms["testForm"]["email"].value;
    var atpos = email.indexOf("@");
    var dotpos = email.lastIndexOf(".");
    
    if (name == "") {
      	document.getElementById("error-box").textContent = "Please enter name";
        return false;
		}
    
    if (age == "" || age < 1) {
      	document.getElementById("error-box").textContent = "Please enter age";
      	return false;
		}
    if (atpos<1 || dotpos<atpos+2 || dotpos+2>=email.length) {
      	document.getElementById("error-box").textContent = "Please enter a valid email address";
        return false;
    }
}