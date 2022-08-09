// Get the modal
 

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
 function popup() {
    document.getElementById("myModal").style.display = "block";
}

// When the user clicks on <span> (x), close the modal
function done() {
    document.getElementById("myModal").style.display = "none";
}

window.addEventListener("mouseup", function(event){
    var box = document.getElementById("myModal")
    if(event.target == box){
        box.style.display = "none"
    }
})




