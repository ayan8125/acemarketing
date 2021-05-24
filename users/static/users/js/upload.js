const profile_field = document.getElementById('profile-field')
const statusMsg = document.getElementById('user-detail-status-msg')
const status_div = document.querySelector('.status-div')
const close_btn_status = document.querySelector('.close-btn-status')
const avatar = document.getElementById('user-profile-img')

function uploadProfileImage(event) {
        event.preventDefault();
                // Get the files from the input
        var files = profile_field.files;
        var file = files[0]; 
        //Check the file type.
        if (!file.type.match('image.*')) {
            status_div.classList.contains('show-status-div') == false ? status_div.classList.add('show-status-div') : console.log('')
            statusMsg.innerHTML = 'You cannot upload this file because it’s not an image.';
            return;
        }

        if (file.size >= 2000000 ) {
            status_div.classList.contains('show-status-div') == false ? status_div.classList.add('show-status-div') : console.log('')
            statusMsg.innerHTML = 'You cannot upload this file because its size exceeds the maximum limit of 2 MB.';
            return;
        }

        loader.style.display = 'block'
        main.style.filter = 'blur(6px)'

        // Create a FormData object.
        var formData = new FormData();

        //Grab only one file since this script disallows multiple file uploads.
        
         // Add the file to the AJAX request.
        formData.append('avatar', file, file.name);

        // Set up the request.
        var xhr = new XMLHttpRequest();

        // Open the connection.
        xhr.open('POST', '/user/edit-user-avatar/', true);
        xhr.setRequestHeader("X-CSRFToken", csrfmiddlewaretoken1.value);



        // Set up a handler for when the task for the request is complete.
        xhr.onload = function () {
            loader.style.display = 'none'
            main.style.filter = 'blur(0px)'
          if (xhr.status === 200) {
            status_div.classList.contains('show-status-div') == false ? status_div.classList.add('show-status-div') : console.log('')
            statusMsg.innerHTML = 'Your upload is successful..';
            const reader = new FileReader();
            reader.addEventListener('load', function(){
                avatar.setAttribute("src", this.result)
            })
            reader.readAsDataURL(file)
          } else {
            status_div.classList.contains('show-status-div') == false ? status_div.classList.add('show-status-div') : console.log('')
            statusMsg.innerHTML = 'An error occurred during the upload. Try again.';
          }
        };

        // Send the data.
        xhr.send(formData);
}

profile_field.addEventListener('change', function(e){
    uploadProfileImage(e)
})


close_btn_status.addEventListener('click', function(){
    status_div.classList.remove('show-status-div')
})