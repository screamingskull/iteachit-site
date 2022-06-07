window.onscroll = function() {scrollDetect()};

function scrollDetect() {
    if (document.body.scrollTop > 2 || document.documentElement.scrollTop > 2) {
        document.getElementById("shadow-onscroll").className = "shadow-header";
    } else {
        document.getElementById("shadow-onscroll").className = "header";
    }    
}