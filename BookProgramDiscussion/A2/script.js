console.log("Hello World");

function myFunction() {
  console.log("myFunction");
}

myFunction();   // Call my function multiple times
myFunction();

const notLoaded = document.getElementById("btn");
console.log(notLoaded);

window.onload = () => {
    var regform = document.getElementById("bookclubrego");
    var modalbtn = document.getElementById("trigger-modal");
    var span = document.getElementsByClassName("close")[0];
    var reg = document.getElementById("reg");

    modalbtn.onclick = function() {
        regform.style.display = "block";
    }
    span.onclick = function() {
        regform.style.display = "none";
    }
      
    window.onclick = function(event) {
        if (event.target == modal) {
            regform.style.display = "none";
        }
    }
    
    function closeModal() {
        document.querySelector(".modal").style.display = "none";
    }   

    reg.onclick = function() {
        alert("Registration form has been submitted!");
        regform.style.display = "none";
    }

};
