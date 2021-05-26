const GetIntouchform = document.querySelector('.get-in-touch-form')
const email = document.getElementById('email')
const csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0]
const contactusArea = document.querySelector('.contactus-section')
const closebtn = document.querySelector('.close-btn-mini-modal')
const minimodal = document.querySelector('.mini-modal')

function submitGetInTouchForm() {
	contactusArea.classList.toggle('blur-5px')
    if (window.XMLHttpRequest) {
        // code for modern browsers
        xmlhttp = new XMLHttpRequest();
    } else {
        // code for old IE browsers
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    } 
    xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) { 
        contactusArea.classList.toggle('blur-5px')
        minimodal.classList.add('show-mini-modal')
        email.value = '';
    }
    };
    const data = {'email': email.value}
    xmlhttp.open("post", "/getIntouch/add/", true);
    xmlhttp.setRequestHeader("X-CSRFToken", csrfmiddlewaretoken.value);
    xmlhttp.setRequestHeader("Content-type", "application/json");
    xmlhttp.send(JSON.stringify(data));
}

try {
    GetIntouchform.addEventListener('submit', function(e) {
        e.preventDefault();
        submitGetInTouchForm();

    })  
}

catch (err) {
    console.log('')
}


try {
   closebtn.addEventListener('click', function(){
    minimodal.classList.remove('show-mini-modal')
    }) 
}

catch (err) {

}
