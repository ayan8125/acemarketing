const email_error = document.getElementById('err-email')
let emailValid = false
const email = document.getElementById('email')
const req_reset_pass_form = document.querySelector(".req-reset-pass-form")
const loader = document.getElementById('loader')
const closebtn = document.querySelector(".close-btn")
const message_modal = document.querySelector(".message-modal")

function validateEmail(email) {
    if (email.match(/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/))
        return true
    return false
}

function submitReqResetPassForm() {
    if(emailValid){
        loader.style.display = 'block'
        req_reset_pass_form.style.filter = 'blur(6px)'
    $.ajax({
            type:'POST',
            url:'/request-reset-password/',
            dataType: 'json',
            data:{
            email: email.value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(data){
                        loader.style.display = 'none'
                        req_reset_pass_form.style.filter = 'blur(0px)'
                    if (data.success) {
                        message_modal.classList.add('show-message-modal')
                    }   

                    if (data.no_user_exists){
                        email_error.innerHTML = 'No user with this email'
                        // email.classList.add('is-invalid')
                    }
   
                }
        });
    }
}


req_reset_pass_form.addEventListener('submit', function(e){
    e.preventDefault()
    submitReqResetPassForm()

})


email.addEventListener('blur', function(){
    emailValid = validateEmail(email.value)
    if (!emailValid){
        email_error.innerHTML = 'Invalid Email'
        return;
    }
    email_error.innerHTML = ''
})



closebtn.addEventListener('click', function(){
     message_modal.classList.remove('show-message-modal')
     // locatio.href = '/joinus'
})