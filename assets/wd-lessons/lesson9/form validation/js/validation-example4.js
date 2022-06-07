function formError() {
	var name = document.forms["testForm"]["name"].value;
	var age = document.forms["testForm"]["age"].value;   

    if (name == "") {
      	document.getElementById("error-box").textContent = "Please enter name";
        return false;
		}
}