function read() {
    jQuery.get("files/12monkeys.txt", function(txt) {
               $("#showFile").text(txt);
               });
}