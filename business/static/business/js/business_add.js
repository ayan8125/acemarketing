const submitbtn = document.querySelector('.submit-btn')
const businessform = document.getElementById('business-address-form')
const loader = document.getElementById('loader')
const business_name = document.getElementById('id_name')
const website = document.getElementById('id_website')
const address = document.getElementById('id_address')
const city = document.getElementById('id_city')
const postcode = document.getElementById('id_postcode')
const runs_online = document.getElementById('id_runs_online')
const runs_locally = document.getElementById('id_runs_locally')
const sector = document.getElementById('id_sector')


let validName = false
let validWebsite = false
let validAddress = false
let validCity = false
let validPostCode = false


function submitBusinessForm() {
    console.log(validName, validWebsite, validAddress, validCity, validPostCode)
    if(validName && validWebsite && validAddress && validCity && validPostCode){
        console.log('came')
        loader.style.display = 'block'
        businessform.style.filter = 'blur(6px)'
    $.ajax({
            type:'POST',
            url:'/business/add/',
            dataType: 'json',
            data:{
            name:business_name.value,
            runs_online: runs_online.value,
            runs_locally: runs_locally.value,
            sector: sector.value,
            website: website.value,
            address: address.value,
            city: city.value,
            postcode: postcode.value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(data){
                        loader.style.display = 'none'
                        businessform.style.filter = 'blur(0px)'
                        if (data.business_addedd) {
                            console.log('adddres submited')
                        }
                }
        });
    }
}

business_name.addEventListener('blur', function() {
    if (business_name.value.match(/([a-zA-Z0-9]{3,})|([A-Za-z0-9]{3,})/) )
        validName = true
    else
        validName = false 
})

website.addEventListener('blur', function() {
    if (website.value.match(/[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?/ig) )
        validWebsite = true
    else
        validWebsite = false 
})

address.addEventListener('blur', function() {
    if (address.value.match(/^[a-zA-Z0-9\s,'-]*$/))
        validAddress = true
    else
        validAddress = false 
})

city.addEventListener('blur', function() {
    if (city.value.match(/[a-zA-Z]/))
        validCity = true
    else
        validCity = false 
})

postcode.addEventListener('blur', function() {

    if (postcode.value.match(/([a-zA-Z0-9])/g)){
        console.log('match')
        validPostCode = true
    }
    else{
       console.log('NOTmatch')
        validPostCode = false 
    }
        
})

submitbtn.addEventListener('click', function(e) {
    e.preventDefault();
    console.log('came in submit')
    submitBusinessForm()
})



