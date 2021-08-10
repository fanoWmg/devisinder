/*document.getElementsByClassName("act").style.background_color = "red"
tablinks = document.getElementsByClassName("tablinks");*/

/*document.getElementById('individual').style.display = "block";*/
/*event.currentTarget.className += " active";*/

function openCity(evt, cityName) {
    console.log("mande v")
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