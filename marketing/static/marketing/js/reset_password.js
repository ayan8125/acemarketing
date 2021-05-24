const password = document.getElementById('password')
const reset_pass_form = document.querySelector(".reset-password-form")
const loader = document.getElementById('loader')
let passwordvalid = true

const closebtn = document.querySelector(".close-btn")
const message_modal = document.querySelector(".message-modal")

let passwordStrength = document.getElementById("password-strength");
let lowUpperCasei = document.querySelector("#lowUpperCase i");
let digitsi = document.querySelector("#digits i");
let specialChari = document.querySelector("#specialChar i");
let eightChari = document.querySelector("#eightChar i");

let lowUpperCase = document.querySelector("#lowUpperCase");
let digits = document.querySelector("#digits");
let specialChar = document.querySelector("#specialChar");
let eightChar = document.querySelector("#eightChar");

function submitResetPasswordForm() {
    if(passwordvalid){
        loader.style.display = 'block'
        reset_pass_form.style.filter = 'blur(6px)'
    $.ajax({
            type:'POST',
            url:location.href.pathname,
            dataType: 'json',
            data:{
            password: password.value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(data){
                        loader.style.display = 'none'
                        reset_pass_form.style.filter = 'blur(0px)'
                    if (data.success) {
                        message_modal.classList.add('show-message-modal')
                    }   
                    
   
                }
        });
    }
}



function checkStrength(password) {
    let strength = 0;

    //If password contains both lower and uppercase characters
    if (password.match(/([a-z].*[A-Z])|([A-Z].*[a-z])/)) {
        strength += 1;
        lowUpperCasei.classList.remove('fa-circle');
        lowUpperCasei.classList.add('fa-check-circle');
        lowUpperCase.style.color = 'forestgreen'
    } else {
        lowUpperCasei.classList.add('fa-circle');
        lowUpperCasei.classList.remove('fa-check-circle');
        lowUpperCase.style.color = '#7c8288'
    }
    //If it has numbers and characters
    if (password.match(/([0-9])/)) {
        strength += 1;
        digitsi.classList.remove('fa-circle');
        digitsi.classList.add('fa-check-circle');
        digits.style.color = 'forestgreen'
    } else {
        digitsi.classList.add('fa-circle');
        digitsi.classList.remove('fa-check-circle');
        digits.style.color = '#7c8288'
    }
    //If it has one special character
    if (password.match(/([!,%,&,@,#,$,^,*,?,_,~])/)) {
        strength += 1;
        specialChari.classList.remove('fa-circle');
        specialChari.classList.add('fa-check-circle');
        specialChar.style.color = 'forestgreen'
    } else {
        specialChari.classList.add('fa-circle');
        specialChari.classList.remove('fa-check-circle');
        specialChar.style.color = '#7c8288'
    }
    //If password is greater than 7
    if (password.length > 7) {
        strength += 1;
        eightChari.classList.remove('fa-circle');
        eightChari.classList.add('fa-check-circle');
        eightChar.style.color = 'forestgreen'
    } else {
        eightChari.classList.add('fa-circle');
        eightChari.classList.remove('fa-check-circle');   
        eightChar.style.color = '#7c8288'
    }



    // If value is less than 2
    if (strength < 2) {
        passwordStrength.classList.remove('progress-bar-warning');
        passwordStrength.classList.remove('progress-bar-success');
        passwordStrength.classList.add('progress-bar-danger');
        passwordStrength.style = 'width: 10%';
        passwordValid = false; 
    } else if (strength == 3) {
        passwordStrength.classList.remove('progress-bar-success');
        passwordStrength.classList.remove('progress-bar-danger');
        passwordStrength.classList.add('progress-bar-warning');
        passwordStrength.style = 'width: 60%';
        passwordValid = false; 
    } else if (strength == 4) {
        passwordStrength.classList.remove('progress-bar-warning');
        passwordStrength.classList.remove('progress-bar-danger');
        passwordStrength.classList.add('progress-bar-success');
        passwordStrength.style = 'width: 100%';
        passwordValid = true; 
    }
}


reset_pass_form.addEventListener('submit', function(e){
    e.preventDefault()
    submitResetPasswordForm()

})

password.addEventListener("keyup", function(){
    let pass = document.getElementById("password").value;
    checkStrength(pass);
});



closebtn.addEventListener('click', function(){
     message_modal.classList.remove('show-message-modal')
     location.href = '/joinus'
})