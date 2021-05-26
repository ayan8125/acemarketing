const mob_sigin_toggle_btn = document.querySelector('.mob-signin-make-active')
const mob_sigup_toggle_btn = document.querySelector('.mob-signup-make-active')
const form_area = document.querySelector('.mob-forms-area')

const mob_sign_in_form = document.querySelector('.mob-sign-in')
const mob_sign_up_form = document.querySelector('.mob-sign-up')

const mob_firstname = document.getElementById('mob-first-name')
const mob_lastname = document.getElementById('mob-last-name')
const mob_email = document.getElementById('mob-email')
const mob_phonenumber = document.getElementById('mob-phone-number')
const mob_password = document.getElementById('mob-password')

const mob_sin_email = document.getElementById('mob-sinemail')
const mob_sin_password = document.getElementById('mob-sinpassword')


let mob_firstnameValid = false
let mob_lastnameValid = false
let mob_emailValid = false
let mob_phonenumberValid = false
let mob_passwordValid = false

let mob_sinemailValid = false

let mob_fname_error = document.getElementById('mob-err-fname')
let mob_lname_error = document.getElementById('mob-err-lname')
let mob_email_error = document.getElementById('mob-err-email')
let mob_phnumber_error = document.getElementById('mob-err-phno')
let mob_password_error = document.getElementById('mob-err-pass')

let mob_sinmessage = document.getElementById('mob-err-sinmessage')


const okbtn = document.getElementById('okbtn')
const success_modal_signup = document.querySelector('.success-modal-signup') 




function MobsubmitSignupForm() {
    if(mob_firstnameValid && mob_lastnameValid && mob_emailValid && mob_phonenumberValid && mob_passwordValid){
        let signupform = document.querySelector('.mob-sign-up')
        let loader = document.getElementById('mob-loader')
        loader.style.display = 'block'
        signupform.style.filter = 'blur(6px)'
    $.ajax({
            type:'POST',
            url:'/signup/',
            dataType: 'json',
            data:{
            first_name:mob_firstname.value,
            last_name: mob_lastname.value,
            email: mob_email.value,
            phone_number: mob_phonenumber.value.includes('+44') ? mob_phonenumber.value : '+44'+mob_phonenumber.value ,
            password: mob_password.value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(data){
                        loader.style.display = 'none'
                        signupform.style.filter = 'blur(0px)'

                    if (data.success) {
                        success_modal_signup.classList.add('show-success-modal')
                 
                    }   

                    if (data.email_exists){
                        mob_email_error.innerHTML = 'User with this  Email, already exists'
                        // email.classList.add('is-invalid')
                    }
                    if (data.phone_number_exists){
                        mob_phnumber_error.innerHTML = 'User with this  number, already exists'
                        // pnumber.classList.add('is-invalid')

                    }
   
                }
        });
    }
}


function MobsubmitSigninForm() {
    if(mob_sin_email.value != '' && mob_sin_password != ''){
        let signinform = document.querySelector('.mob-sign-in')
        let loader = document.getElementById('mob-loader')
        loader.style.display = 'block'
        signinform.style.filter = 'blur(6px)'
    $.ajax({
            type:'POST',
            url:'/signin/',
            dataType: 'json',
            data:{
            email: mob_sin_email.value,
            password: mob_sin_password.value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(data){
                console.log(data)
                    if (data.success) {
                        if(data.is_new_user) {
                            location.href = '/business/add/'
                            return
                        }
                        if (queryString.has('next')){
                            location.href = queryString.get('next')
                            return
                        }
                        else{
                            location.href = '/user/dashboard/'
                        }
                        
                    }   

                    if (data.user_does_not_exists){
                        loader.style.display = 'none'
                        signinform.style.filter = 'blur(0px)'
                        mob_sinmessage.innerHTML = 'Incorrect Email or Paswword'
                        // email.classList.add('is-invalid')
                    }
                }
        });
    }
}


mob_sigup_toggle_btn.addEventListener('click', function() {
    if (form_area.classList.contains('mob-sign-in-mode')){
        form_area.classList.remove('mob-sign-in-mode')
        form_area.classList.add('mob-sign-up-mode')
    }
})

mob_sigin_toggle_btn.addEventListener('click',function(){
    if (form_area.classList.contains('mob-sign-up-mode')){
        form_area.classList.remove('mob-sign-up-mode')
        form_area.classList.add('mob-sign-in-mode')
    }
})



mob_sign_in_form.addEventListener('submit',function(e){
    e.preventDefault()
    MobsubmitSigninForm()
})


mob_sign_up_form.addEventListener('submit',function(e){
    e.preventDefault()
    MobsubmitSignupForm()
})



mob_firstname.addEventListener("blur", function() {
    if (mob_firstname.value != ''){
       mob_firstnameValid = validateName(mob_firstname.value)
        if (!mob_firstnameValid) 
            mob_fname_error.innerHTML = 'InValid FirstName!';
        else 
            mob_fname_error.innerHTML = '';
       
    }
})


mob_lastname.addEventListener("blur", function() {
    if (mob_lastname.value != ''){
       mob_lastnameValid = validateName(mob_lastname.value)
        if (!mob_lastnameValid)
            mob_lname_error.innerHTML = 'InValid LastName!';
        else 
            mob_lname_error.innerHTML = '';
    }
})

mob_email.addEventListener("blur", function() {
    if (mob_email.value != ''){
       mob_emailValid = validateEmail(mob_email.value)
       if (!mob_emailValid) 
            mob_email_error.innerHTML = 'InValid Email!';
        else 
            mob_email_error.innerHTML = '';
    }
})


mob_password.addEventListener("blur", function() {
    if (mob_password.value != ''){
        if (mob_password.value.length >= 8){
            mob_password_error.innerHTML = '';
            mob_passwordValid = true
            
        }
        else{
            
             mob_passwordValid = false
             mob_password_error.innerHTML = 'Password should be atleast 8 character long';
        } 
           
    }
})



mob_phonenumber.addEventListener("blur", function() {
    if (mob_phonenumber.value != ''){
        let number = ''
        if (!mob_phonenumber.value.includes("+44"))
            number = '+44' + mob_phonenumber.value;
        else
            number = mob_phonenumber.value;
       mob_phonenumberValid = validateUkNumber(number);
        if (!mob_phonenumberValid) 
            mob_phnumber_error.innerHTML = 'InValid PhoneNumber';
        else 
            mob_phnumber_error.innerHTML = '';
    }
})


okbtn.addEventListener('click', function() {
    const media = window.matchMedia('(max-width: 600px)');
    console.log(media)
    success_modal_signup.classList.remove('show-success-modal')
    if (media.matches==true){
        form_area.classList.remove('mob-sign-up-mode')
        form_area.classList.add('mob-sign-in-mode')
        return
    }
    makeactive(signin_toggle_btn,signup_toggle_btn)
})

