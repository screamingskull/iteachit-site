window.onscroll = function() {scrollDetect()};

function scrollDetect() {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        document.getElementById("shrink-onscroll").className = "small-header";
    } else {
        document.getElementById("shrink-onscroll").className = "header";
    }    
}