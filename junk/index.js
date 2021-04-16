var req = new XMLHttpRequest();
var key = '';
var site = $('https://api.nasa.gov/planetary/apod?api_key={key}');

req.onreadystatechange = function(){
    if(this.readyState == 4 && this.status == 200){
        response_html = document.getElementById('response-json')
        response_html.innerHTML = req.responseText;
    }
}

req.open("GET", site, true);
req.send(null);

// var xhttp = new XMLHttpRequest();
// xhttp.onreadystatechange = function() {
//     if (this.readyState == 4 && this.status == 200) {
//        // Typical action to be performed when the document is ready:
//        document.getElementById("demo").innerHTML = xhttp.responseText;
//     }
// };

// xhttp.open("GET", "filename", true);
// xhttp.send();