

var ourRequest = new XMLHttpRequest();
ourRequest.open('GET', 'http://127.0.0.1:8000/comment/');
ourRequest.onload = function() {

if (ourRequest.status >= 200 && ourRequest.status < 400) {

	var data = JSON.parse(ourRequest.responseText);
	createHTML(data);
	console.log("We are connected to the server");
} 

else {
console.log("We are connected to the server, but it returned an error.");
}
};

ourRequest.onerror = function() {
	// var data = JSON.parse(ourRequest.responseText);
	// createHTML(data);
	console.log("We are connected to the server");
console.log("Connection error");
};


ourRequest.send();


function createHTML(petsData) {
    var rawtemplate = document.getElementById("mycmttemplate").innerHTML
    var compiledTemp = Handlebars.compile(rawtemplate)
    var generatedHTML = compiledTemp(petsData)
    var petsContainer = document.getElementById("mydata_container");
    petsContainer.innerHTML = generatedHTML
}