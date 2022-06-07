window.onscroll = function() {scrollDetect()};

function scrollDetect() {
    if (document.body.scrollTop > 2 || document.documentElement.scrollTop > 2) {
        document.getElementById("shrink-onscroll").className = "small-header";
        document.getElementById("shrink-this-paragraph").className = "p-style-shrunk";
    } else {
        document.getElementById("shrink-onscroll").className = "header";
        document.getElementById("shrink-this-paragraph").className = "p-style-normal";
    }    
}