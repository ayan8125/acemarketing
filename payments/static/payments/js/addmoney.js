const money = document.getElementById('money')
const addmoneybtn = document.getElementById('addmoneybtn')
const addmoneyform = document.querySelector('.add-money-o-Wallet')
const csrfmiddlewaretoken1 = document.getElementsByName('csrfmiddlewaretoken')[0]
var stripe = Stripe("pk_live_51H6aJHEoanPy9ym03AGyC4SNyuE8XQRg9OX2IAPN3t3MgLCLRyKp13hClNa80crAl1dMAfF2VmzMmVALfCFJ9Ccb00Tht16Ive");
const errmsg = document.querySelector('.money-err-msg')
var amountValid = true;
var addmoney_main_screen = document.getElementsByTagName('main')[0]
var addmoneyloader = document.getElementById('loader')
var p_addmoney = document.querySelector('.p_addmoney')
const acc_wallet = document.querySelector('.acc-wallet')
const close_wall_btn = document.querySelector('.close-wall-btn')

function UpdateTransaction(razorpay_payment_id, razorpay_order_id, razorpay_signature) {
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
    xmlhttp.open("post", "/payments/transaction/", true);
    xmlhttp.setRequestHeader("X-CSRFToken", csrfmiddlewaretoken1.value);
    xmlhttp.setRequestHeader("Content-type", "application/json");
    xmlhttp.send(JSON.stringify(data));
  }

addmoneybtn.addEventListener("click", function (e) {
  e.preventDefault()
  if (amountValid) {
    addmoney_main_screen.style.filter = 'blur(5px)'
    addmoneyloader.style.display = 'block'
    fetch("/payments/transaction/", {
      method: "POST",
      body: JSON.stringify({'amount':money.value}),
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfmiddlewaretoken1.value,
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
    if (parseInt(money.value) < 1000 )
    errmsg.innerHTML = 'You have to add minimum 1k'
  else{
      if (parseInt(money.value) > 7000)
        errmsg.innerHTML = 'You can only add 7k maximum in one transaction'
      else{
        errmsg.innerHTML = '';
        amountValid = true;
      }
    }
})
try {
    p_addmoney.addEventListener('click', function() {
    acc_wallet.classList.toggle('show-add-amoney-form')
  })

  close_wall_btn.addEventListener('click', function() {
    acc_wallet.classList.toggle('show-add-amoney-form')
  })
}

catch {
  
}
