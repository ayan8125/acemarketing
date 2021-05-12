const money = document.getElementById('money')
const addmoneybtn = document.getElementById('addmoneybtn')
const addmoneyform = document.querySelector('.add-money-o-Wallet')
const csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0]
var stripe = Stripe("pk_test_51H6aJHEoanPy9ym0YhsVmX6Nz24wbDv0i2HygIRLBt1BllWmPKE71Nrlv16luAYTwAgmdfqkdiWb411cUpGqGH5N00rePP7L1m");
const errmsg = document.querySelector('.err-msg')
var amountValid = false;
var main = document.getElementsByTagName('main')[0]
var loader = document.getElementById('loader')


function UpdateTransaction(razorpay_payment_id, razorpay_order_id, razorpay_signature) {
  console.log('came in loaddoc')
    if (window.XMLHttpRequest) {
        // code for modern browsers
        xmlhttp = new XMLHttpRequest();
     } else {
        // code for old IE browsers
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    } 
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        console.log(this)
        var options = JSON.parse(this.response)  
        console.log(options)
      }
    };
    const data = {'razorpay_payment_id':razorpay_payment_id,'razorpay_order_id':razorpay_order_id, 'razorpay_signature': razorpay_signature}
    console.log(data)
    xmlhttp.open("post", "/payments/transaction/", true);
    xmlhttp.setRequestHeader("X-CSRFToken", csrfmiddlewaretoken.value);
    xmlhttp.setRequestHeader("Content-type", "application/json");
    xmlhttp.send(JSON.stringify(data));
  }

addmoneybtn.addEventListener("click", function (e) {
  e.preventDefault()
  if (amountValid) {
    main.style.filter = 'blur(5px)'
    loader.style.display = 'block'
    fetch("/payments/transaction/", {
      method: "POST",
      body: JSON.stringify({'amount':money.value}),
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfmiddlewaretoken.value,
      },
    }).then(function (response) {

        return response.json();

      }).then(function (session) {

        return stripe.redirectToCheckout({ sessionId: session.id });

      })

      .then(function (result) {

        // If redirectToCheckout fails due to a browser or network

        // error, you should display the localized error message to your

        // customer using error.message.

        if (result.error) {

          alert(result.error.message);

        }

      })

      .catch(function (error) {

        console.error("Error:", error);

      });
}
else{
  console.log('invalid amount')
}

});


money.addEventListener('blur', function(){
    if (parseInt(money.value) < 2000 )
    errmsg.innerHTML = 'You have to add minimum 2k'
  else{
      if (parseInt(money.value) > 7000)
        errmsg.innerHTML = 'You can only add 7k maximum in one transaction'
      else{
        errmsg.innerHTML = '';
        amountValid = true;
      }
    }
})