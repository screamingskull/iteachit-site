document.getElementById("file").addEventListener("change", function() {
    var read = new FileReader();
    read.onload = function() {
        document.getElementById("showFile").textContent = this.result;
    }
    read.readAsText(this.files[0]);
})