/*========================
 password show hide js
 ==========================*/
 let passwordInput = document.getElementById('txtPassword'),
 toggle = document.getElementById('btnToggle'),
 icon =  document.getElementById('eyeIcon');

function togglePassword() {
if (passwordInput.type === 'password') {
 passwordInput.type = 'text';
 icon.classList.add("iconly-Show");
} else {
 passwordInput.type = 'password';
 icon.classList.remove("iconly-Show");
}
}
toggle.addEventListener('click', togglePassword, false);