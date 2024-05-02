/* Signup password funtion */

// function togglePassword(fieldId, eyeIconId)

function togglePassword(fieldId, eyeIconId) {
  var passwordField = document.getElementById(fieldId);
  var eyeIcon = document.getElementById(eyeIconId);

  if (passwordField.type === "password") {
      passwordField.type = "text";
      eyeIcon.className = "bx bx-show";
  } else {
      passwordField.type = "password";
      eyeIcon.className = "bx bx-show";
  }
}






/// Login eye controler



const forms = document.querySelector(".forms"),
      pwShowHide = document.querySelectorAll(".eye-icon"),
      links = document.querySelectorAll(".link");

pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", () => {
        let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password");
        
        pwFields.forEach(password => {
            if(password.type === "password"){
                password.type = "text";
                password.type = "text";
                eyeIcon.classList.replace("bx-hide", "bx-show");
                return;
            }
            password.type = "password";
            eyeIcon.classList.replace("bx-show", "bx-hide");
        })
        
    })
})  

links.forEach(link => {
    link.addEventListener("click", e => {
       e.preventDefault(); //preventing form submit
       forms.classList.toggle("show-signup");
    })
})







