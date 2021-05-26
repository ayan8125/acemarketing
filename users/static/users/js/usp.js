const description = document.getElementById('id_description')
// const business = document.getElementById('id_business') 
const loader = document.getElementById('loader')
const uspform = document.querySelector('.usp-form')
const submitbtn = document.getElementById('submit-btn')
const usplist = document.getElementById('usplist')

const skipbtn = document.querySelector('.skip-btn')
const nextbtn = document.querySelector('.next-btn')

function submitUspForm() {
    if(description.value != ''){
        loader.style.display = 'block'
        uspform.style.filter = 'blur(6px)'
    $.ajax({
            type:'POST',
            url:'/business/usp/',
            dataType: 'json',
            data:{
            description:description.value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(data){
                    loader.style.display = 'none'
                    uspform.style.filter = 'blur(0px)'
                    if (data.usp_added) {
                        description.value = ''
                        pullusp()
                    }   
                    if (data.invalid_usp) {
       
                    }   

   
                }
        });
    }
}

function pullusp() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        // Typical action to be performed when the document is ready:
        usplist.innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "/business/usp_list/", true);
    xhttp.send(); 
}

function addUsp(usp) {
pass
}

submitbtn.addEventListener('click', function(e) {
    e.preventDefault()
    submitUspForm();
});

skipbtn.addEventListener('click', function(){
    location.href = '/payments/addmoney/'
})

nextbtn.addEventListener('click', function(){
    location.href = '/payments/addmoney/'
})


pullusp()

