const cancelbtn = document.querySelector('.btn-cancel')
const signoutbtn = document.querySelector('.signout-btn')
const signoutmodal = document.querySelector('.signout-modal')

cancelbtn.addEventListener('click',function(){
	signoutmodal.classList.toggle('show-sign-out-modal')
})

signoutbtn.addEventListener('click',function(){
	signoutmodal.classList.toggle('show-sign-out-modal')
})
