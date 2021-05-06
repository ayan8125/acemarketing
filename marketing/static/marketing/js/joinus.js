const signup_toggle_btn = document.getElementById('sign-up-toggle-btn')
const signin_toggle_btn = document.getElementById('sign-in-toggle-btn')
const signupform = document.getElementById('signupform')
const signinform = document.getElementById('signinform')

const signupbtn = document.getElementById('signup-btn')
const signinbtn = document.getElementById('signin-btn')

const firstname = document.getElementById('first-name')
const lastname = document.getElementById('last-name')
const email = document.getElementById('email')
const phonenumber = document.getElementById('phone-number')
const password = document.getElementById('password')

const sin_email = document.getElementById('sinemail')
const sin_password = document.getElementById('sinpassword')


let firstnameValid = false
let lastnameValid = false
let emailValid = false
let phonenumberValid = false
let passwordValid = false

let sinemailValid = false

let fname_error = document.getElementById('err-fname')
let lname_error = document.getElementById('err-lname')
let email_error = document.getElementById('err-email')
let phnumber_error = document.getElementById('err-phno')

let sinmessage = document.getElementById('err-sinmessage')

let passwordStrength = document.getElementById("password-strength");
let lowUpperCasei = document.querySelector("#lowUpperCase i");
let digitsi = document.querySelector("#digits i");
let specialChari = document.querySelector("#specialChar i");
let eightChari = document.querySelector("#eightChar i");

let lowUpperCase = document.querySelector("#lowUpperCase");
let digits = document.querySelector("#digits");
let specialChar = document.querySelector("#specialChar");
let eightChar = document.querySelector("#eightChar");

const okbtn = document.getElementById('okbtn')
const success_modal_signup = document.querySelector('.success-modal-signup') 


function  makeactive(btn1, btn2) {
    btn2.classList.remove('active-btn')
    btn1.classList.add('active-btn')
    if (signupform.classList.contains('hide-signup')) {
        signupform.classList.remove('hide-signup')
        signinform.classList.add('hide-signin')
        signinform.classList.remove('show-sign-in-form')
    }
    else{
        signinform.classList.remove('hide-signin')
        signinform.classList.add('show-sign-in-form')
        signupform.classList.add('hide-signup')
    }

}

function validateEmail(email) {
    if (email.match(/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/))
        return true
    return false
}


function validateName(name) {
    if (name.match(/([a-zA-Z]{3,})|([A-Za-z]{3,})/)) 
        return true
    return false
}

function validateUkNumber(number) {
    if (number.match(/((\+44))7\d{3}(\s)?\d{6}/))
        return true
    return false
}

function toggle(){
    if(state){
        document.getElementById("password").setAttribute("type","password");
        state = false;
    }else{
        document.getElementById("password").setAttribute("type","text")
        state = true;
    }
}

function myFunction(show){
    show.classList.toggle("fa-eye-slash");
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


function submitSignupForm() {
    if(firstnameValid && lastnameValid && emailValid && phonenumberValid && passwordValid){
        let signupform = document.getElementById('signupform')
        let loader = document.getElementById('loader')
        loader.style.display = 'block'
        signupform.style.filter = 'blur(6px)'
    $.ajax({
            type:'POST',
            url:'/signup/',
            dataType: 'json',
            data:{
            first_name:firstname.value,
            last_name: lastname.value,
            email: email.value,
            phone_number: phonenumber.value.includes('+44') ? phonenumber.value : '+44'+phonenumber.value ,
            password: password.value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(data){
                        loader.style.display = 'none'
                        signupform.style.filter = 'blur(0px)'

                    if (data.success) {
                        success_modal_signup.classList.add('show-success-modal')
                        signupform.reset();
                    }   

                    if (data.email_exists){
                        email_error.innerHTML = 'User with this  Email, already exists'
                        // email.classList.add('is-invalid')
                    }
                    if (data.phone_number_exists){
                        phnumber_error.innerHTML = 'User with this  number, already exists'
                        // pnumber.classList.add('is-invalid')

                    }
   
                }
        });
    }
}


function submitSigninForm() {
    if(sin_email.value != '' && sin_password != ''){
        let signinform = document.getElementById('signinform')
        let loader = document.getElementById('loader')
        loader.style.display = 'block'
        signinform.style.filter = 'blur(6px)'
    $.ajax({
            type:'POST',
            url:'/signin/',
            dataType: 'json',
            data:{
            email: sin_email.value,
            password: sin_password.value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(data){
                    if (data.success) {
                        location.href = '/user/dashboard/'
                    }   

                    if (data.user_does_not_exists){
                        loader.style.display = 'none'
                        signinform.style.filter = 'blur(0px)'
                        sinmessage.innerHTML = 'Incorrect Email Paswword'
                        // email.classList.add('is-invalid')
                    }
                }
        });
    }
}


firstname.addEventListener("blur", function() {
    if (firstname.value != ''){
       firstnameValid = validateName(firstname.value)
        if (!firstnameValid) 
            fname_error.innerHTML = 'InValid FirstName!';
        else 
            fname_error.innerHTML = '';
       
    }
})


lastname.addEventListener("blur", function() {
    if (lastname.value != ''){
       lastnameValid = validateName(lastname.value)
        if (!lastnameValid)
            lname_error.innerHTML = 'InValid LastName!';
        else 
            lname_error.innerHTML = '';
    }
})

email.addEventListener("blur", function() {
    if (email.value != ''){
       emailValid = validateEmail(email.value)
       if (!emailValid) 
            email_error.innerHTML = 'InValid Email!';
        else 
            email_error.innerHTML = '';
    }
})



phonenumber.addEventListener("blur", function() {
    if (phonenumber.value != ''){
        let number = ''
        if (!phonenumber.value.includes("+44"))
            number = '+44' + phonenumber.value;
        else
            number = phonenumber.value;
       phonenumberValid = validateUkNumber(number);
        if (!phonenumberValid) 
            phnumber_error.innerHTML = 'InValid PhoneNumber';
        else 
            phnumber_error.innerHTML = '';
    }
})


password.addEventListener("keyup", function(){
    let pass = document.getElementById("password").value;
    checkStrength(pass);
});

signup_toggle_btn.addEventListener('click', function() {
    makeactive(signup_toggle_btn,signin_toggle_btn)
})

signin_toggle_btn.addEventListener('click', function() {
    makeactive(signin_toggle_btn,signup_toggle_btn)
})



signupbtn.addEventListener('click', function(e) {
    e.preventDefault()
    submitSignupForm()
})

signinbtn.addEventListener('click', function(e) {
    e.preventDefault()
    submitSigninForm()
})


okbtn.addEventListener('click', function() {
    success_modal_signup.classList.remove('show-success-modal')
    makeactive(signin_toggle_btn,signup_toggle_btn)
})