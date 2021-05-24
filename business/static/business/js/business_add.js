const submitbtn = document.querySelector('.submit-business-btn')
const businessform = document.getElementById('business-address-form')
const loader1 = document.getElementById('loader')
const business_name = document.getElementById('id_name')
const website = document.getElementById('id_website')
const address = document.getElementById('id_address')
const city = document.getElementById('id_city')
const postcode = document.getElementById('id_postcode')
const runs_online = document.getElementById('id_runs_online')
const runs_locally = document.getElementById('id_runs_locally')
const sectorfield = document.getElementById('id_sector')
const countryfield = document.getElementById('id_country')
const err_name = document.getElementById('err-business-name')
const err_address = document.getElementById('err-address')
const err_city = document.getElementById('err-city')
const err_postcode = document.getElementById('err-postcode')
const err_website = document.getElementById('err-website')
const business_detail_form = document.getElementById('business-detail-form')
const buiness_content_area = document.querySelector('.business-details-form')
const UserBusinessstatusMsg = document.getElementById('user-business-detail-status-msg')
const user_business_status_div = document.querySelector('.user-business-detail-status')
const close_btn_user_business_status = document.querySelector('.close-btn-user-business-detail-status')
const prev_btn = document.querySelector('.prev-btn')
const sector_list = document.getElementById('sector-list')
const country_list = document.getElementById('country-list')

let sector = 1
let country = 0


let validName = false
let validWebsite = false
let validAddress = false
let validCity = false
let validPostCode = false


function submitBusinessForm() {
    // console.log(validName, validWebsite, validAddress, validCity, validPostCode)
    if(validName && validWebsite && validAddress && validCity && validPostCode){
        loader1.style.display = 'block'
        businessform.style.filter = 'blur(6px)'
    $.ajax({
            type:'POST',
            url:'/business/add/',
            dataType: 'json',
            data:{
            name:business_name.value,
            runs_online: runs_online.value,
            runs_locally: runs_locally.value,
            sector: sector,
            website: website.value,
            country: country,
            address: address.value,
            city: city.value,
            postcode: postcode.value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(data){
                        loader1.style.display = 'none'
                        businessform.style.filter = 'blur(0px)'
                        if (data.business_addedd) {
                            if (location.href.includes('/business/add/')) {
                                location.href = '/business/goals/'
                            }
                        user_business_status_div.classList.add('show-status-div')
                        UserBusinessstatusMsg.innerHTML = 'Your Business Details Updated sucessfully'
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


function changecountry(key, name) {
    countryfield.value = name
    country= key
    country_list.style.height = '0';
    country_list.style.visibility = 'hidden';
    country_list.style.pointerEvents = 'none';
}


function changesector(id, name) {
    sectorfield.value = name
    sector = id
    sector_list.style.height = '0';
    sector_list.style.visibility = 'hidden';
    sector_list.style.pointerEvents = 'none';
}


business_name.addEventListener('blur', function() {
    if (business_name.value.match(/([a-zA-Z0-9]{3,})|([A-Za-z0-9]{3,})/) ){
        validName = true
        err_name.innerHTML = ''
    }
    else{
        validName = false 
        err_name.innerHTML = 'Invalid Business Name'
    }
})

website.addEventListener('blur', function() {
    if (website.value.match(/[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?/ig) ){
        validWebsite = true
        err_website.innerHTML = ''
    }
    else{
        validWebsite = false 
        err_website.innerHTML = 'Invalid website address'
    }
})

address.addEventListener('blur', function() {
    if (address.value.match(/^[a-zA-Z0-9\s,'-]*$/)){
        validAddress = true
        err_address.innerHTML = ''
    }
    else{
        validAddress = false 
        err_address.innerHTML = 'Invalid address'
    }
})

city.addEventListener('blur', function() {
    if (city.value.match(/[a-zA-Z]/)){
        err_city.innerHTML = ''
        validCity = true
    }
    else{
        err_city.innerHTML = 'Invalid city'
        validCity = false 
    }
})

postcode.addEventListener('blur', function() {

    if (postcode.value.match(/([a-zA-Z0-9])/g)){
        err_postcode.innerHTML = ''
        validPostCode = true
    }
    else{
        err_postcode.innerHTML = 'Invalid postcode'
        validPostCode = false 
    }
        
})

submitbtn.addEventListener('click', function(e) {
    e.preventDefault();
    submitBusinessForm()
})


runs_locally.addEventListener('click', function() {
    runs_locally.value == 'True' ? runs_locally.value = 'False' : runs_locally.value = 'True' 
})

runs_online.addEventListener('click', function(){
    runs_online.value == 'True' ? runs_online.value = 'False' : runs_online.value = 'True' 
})

close_btn_user_business_status.addEventListener('click', function(e){
    e.preventDefault()
    user_business_status_div.classList.remove('show-status-div')
})


business_detail_form.addEventListener('submit', function(e){
    e.preventDefault()
    if (validName && validWebsite){
        
        buiness_content_area.classList.remove('show-business-detail-form')
        buiness_content_area.classList.add('show-business-address-form')
    }
})

prev_btn.addEventListener('click', function(e){
    e.preventDefault()
    buiness_content_area.classList.remove('show-business-address-form')
    buiness_content_area.classList.add('show-business-detail-form')
    

})





pullList('/business/sector-list/', 'sector-list')
pullList('/business/country-list/', 'country-list')