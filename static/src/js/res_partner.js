/*document.getElementsByClassName("act").style.background_color = "red"
tablinks = document.getElementsByClassName("tablinks");*/

/*document.getElementById('individual').style.display = "block";*/

/*event.currentTarget.className += " active";*/

function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}

function type_display_div(display, tab) {
    if (tab != "mirror") {
        if (display == "none") {
            document.getElementById("minus").style.display = "none";
            document.getElementById("plus").style.display = "block";
            document.getElementById("cadre_").style.height = "57px";
        }
        if (display == "block") {
            document.getElementById("plus").style.display = "none";
            document.getElementById("minus").style.display = "block";
            document.getElementById("cadre_").style.height = "auto";
        }
        document.getElementById("display_cadre").style.display = display;
    } else {
        if (display == "none") {
            document.getElementById("minus_mir").style.display = "none";
            document.getElementById("plus_mir").style.display = "block";
            document.getElementById("cadre_mir").style.height = "57px";
        }
        if (display == "block") {
            document.getElementById("plus_mir").style.display = "none";
            document.getElementById("minus_mir").style.display = "block";
            document.getElementById("cadre_mir").style.height = "auto";
        }
        document.getElementById("display_cadre_mir").style.display = display;
    }
}
