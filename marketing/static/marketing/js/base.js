const hamburgerbtn = document.querySelector('.hamburger-btn')
const mobileNav = document.querySelector('.mobile-nav')
const closeNavbtn = document.querySelector('.close-nav-btn')

hamburgerbtn.addEventListener('click', function(){
	mobileNav.classList.add('show-mobile-nav')
})

closeNavbtn.addEventListener('click', function(){
	mobileNav.classList.remove('show-mobile-nav')
})