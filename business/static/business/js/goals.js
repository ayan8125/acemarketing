const goals = document.getElementsByClassName('goal')
const csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0]
const nextbtn = document.getElementById('next')
const main = document.getElementsByTagName('main')[0]
const loader2 = document.getElementById('loader')
var UserGoals = []

for (var goalindex=0;goalindex<goals.length;goalindex++){
    addevent(goals[goalindex])
}

function addevent(elemt) {
    const input = elemt.getElementsByTagName('input')[0]
    elemt.addEventListener('click', function() {
        console.log(input)
        if (elemt.classList.contains('selected')) {
            removeA(UserGoals, input.value)
            UserGoals = UserGoals.filter(function(e) { return e !==  input.value})
        }
        else
            UserGoals.push(input.value)
        elemt.classList.toggle('selected')
    })
}

function PostGoals() {
    loader2.style.display = 'block';
    main.style.filter = 'blur(5px)';
    if (window.XMLHttpRequest) {
        // code for modern browsers
        xmlhttp = new XMLHttpRequest();
    } else {
        // code for old IE browsers
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    } 
    xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) { 
        loader2.style.display = 'none';
        main.style.filter = 'none';
        if (location.href.includes('/business/goals/')){
            location.href = '/business/usp/'
        }

    }
    };
    const data = {'goals': UserGoals}
    xmlhttp.open("post", "/business/goals/", true);
    xmlhttp.setRequestHeader("X-CSRFToken", csrfmiddlewaretoken.value);
    xmlhttp.setRequestHeader("Content-type", "application/json");
    xmlhttp.send(JSON.stringify(data));
}

nextbtn.addEventListener('click', PostGoals)