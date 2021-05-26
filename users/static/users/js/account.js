const uploadbtn = document.querySelector('.upload-btn')
const profileImgField = document.getElementById('profile-field')
const userDetailArea = document.querySelector(".user-basic-details")
const changeContent = document.querySelector(".change-content-btn")
const EditBack = document.getElementById('edit-back')
const loader = document.getElementById('loader')
const main = document.getElementsByTagName('main')[0]
const editform = document.getElementById('edit-form')
const businessgoals = document.getElementById('business-goals')
const csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0]


const goal = document.getElementById('id_goal')
const goalsubmitbtn = document.querySelector('.add-goal-btn')
const goalarea = document.querySelector('.business-goals')


const usp = document.getElementById('id_usp')
const uspsubmitbtn = document.querySelector('.add-usp-btn')
const usparea = document.querySelector('.business-usp')


const businessDetailArea = document.querySelector(".business-basic-details")
const changebusinessContent = document.getElementById("busines-content-tog")
const businessEditBack = document.getElementById('edit-back-business')

const user_details = document.querySelector(".user-detail")

const UserstatusMsg = document.getElementById('user-detail-status-msg')
const user_status_div = document.querySelector('.user-detail-status')
const close_btn_user_status = document.querySelector('.close-btn-user-detail-status')
const verifyEmailbtn = document.querySelector('.verify-emai-btn')


firstnameValid = true
lastnameValid = true
emailValid = true
phonenumberValid = true

validName = true
validWebsite = true
validAddress = true
validCity = true
validPostCode = true

const closebtn = document.querySelector(".close-btn")
const message_modal = document.querySelector(".message-modal")


function submitEditForm() {
    if(firstnameValid && lastnameValid && emailValid && phonenumberValid){
        loader.style.display = 'block'
        main.style.filter = 'blur(6px)'
    $.ajax({
            type:'POST',
            url:'/user/edit-user/',
            dataType: 'json',
            data:{
            first_name:firstname.value,
            last_name: lastname.value,
            email: email.value,
            phone_number: phonenumber.value.includes('+44') ? phonenumber.value : '+44'+phonenumber.value ,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(data){
                        loader.style.display = 'none'
                        main.style.filter = 'blur(0px)'
                    if (data.success) {
                        user_status_div.classList.add('show-status-div')
                        UserstatusMsg.innerHTML = 'Your Profile Updated sucessfully'
                        // success_modal_signup.classList.add('show-success-modal')
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


function AddUsp() {
    if(usp.value != ''){
        loader.style.display = 'block'
        usparea.style.filter = 'blur(6px)'
    $.ajax({
            type:'POST',
            url:'/business/usp/',
            dataType: 'json',
            data:{
            description:usp.value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(data){
                    loader.style.display = 'none'
                    usparea.style.filter = 'blur(0px)'
                    if (data.usp_added) {
                    	usp.value = ''
                    	pullList('/business/usp_list/', 'business-usp')
                    }   
                    if (data.invalid_usp) {
                        console.log('Invlaid usp')
                    }   

   
                }
        });
    }
}


function pullList(url, drop_id) {
	if (window.XMLHttpRequest)
    // code for modern browsers
    xhttp = new XMLHttpRequest();
	else
    // code for old IE browsers
    xhttp = new ActiveXObject("Microsoft.XMLHTTP");

    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
       document.getElementById(drop_id).innerHTML = xhttp.responseText;
	    }
	};
	xhttp.open("GET", url, false);
	xhttp.send();
}




function PostGoal() {
    loader.style.display = 'block';
    goalarea.style.filter = 'blur(5px)';
    if (window.XMLHttpRequest) {
        // code for modern browsers
        xmlhttp = new XMLHttpRequest();
    } else {
        // code for old IE browsers
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    } 
    xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) { 
    	pullList('/business/goals-list/', 'business-goals')
        goal.value = ''
        loader.style.display = 'none';
        goalarea.style.filter = 'none';



    }
    };
    const data = {'goals': [goal.value]}
    xmlhttp.open("post", "/business/goals/", true);
    xmlhttp.setRequestHeader("X-CSRFToken", csrfmiddlewaretoken.value);
    xmlhttp.setRequestHeader("Content-type", "application/json");
    xmlhttp.send(JSON.stringify(data));
}



function SendEmailVerificationlink() {
    loader.style.display = 'block';
    user_details.style.filter = 'blur(5px)';
    if (window.XMLHttpRequest)
    // code for modern browsers
    xhttp = new XMLHttpRequest();
    else
    // code for old IE browsers
    xhttp = new ActiveXObject("Microsoft.XMLHTTP");

    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
            const data = JSON.parse(this.response)
            loader.style.display = 'none';
            user_details.style.filter = 'blur(0px)';
            if (data.success) {
                message_modal.classList.add('show-message-modal')            
            }
            else{
                user_status_div.classList.add('show-status-div')
                UserstatusMsg.innerHTML = 'Some error has occured , please try again.'
            }
            
        }
    };
    xhttp.open("GET", '/user/email-verification/', true);
    xhttp.send();
}





uploadbtn.addEventListener('click', function(e) {
	e.preventDefault();
	profileImgField.click();
})


changeContent.addEventListener('click', function() {
	userDetailArea.classList.toggle('show-info')
	userDetailArea.classList.toggle('show-edit-info-form')
	EditBack.classList.toggle('fa-pen')
	EditBack.classList.toggle('fa-arrow-left')
})


changebusinessContent.addEventListener('click', function() {
	businessDetailArea.classList.toggle('show-business-info')
	businessDetailArea.classList.toggle('show-business-edit-form')
	businessEditBack.classList.toggle('fa-pen')
	businessEditBack.classList.toggle('fa-arrow-left')
})



editform.addEventListener('submit', function(e){
	e.preventDefault()
	submitEditForm()
})

goalsubmitbtn.addEventListener('click',function(){
	PostGoal()
})

uspsubmitbtn.addEventListener('click',function(){
	AddUsp()
})

close_btn_user_status.addEventListener('click', function(){
    user_status_div.classList.remove('show-status-div')
})

try {
     verifyEmailbtn.addEventListener('click', function(e){
        e.preventDefault()
        SendEmailVerificationlink();
    })   
}
catch {
    
}


closebtn.addEventListener('click', function(){
     message_modal.classList.remove('show-message-modal')
})


pullList('/business/sector-list/', 'sector-list')
pullList('/business/country-list/', 'country-list')
pullList('/business/goals-list/', 'business-goals')
pullList('/business/usp_list/', 'business-usp')