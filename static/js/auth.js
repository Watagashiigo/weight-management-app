const loginTab = document.getElementById("loginTab");
const registerTab = document.getElementById("registerTab");
const showRegister = document.getElementById("showRegister");
const showLogin = document.getElementById("showLogin");

const loginSection = document.querySelector(".login-section");
const registerSection = document.querySelector(".register-section");

function activateLogin() {
  loginTab.classList.add("active");
  registerTab.classList.remove("active");

  loginSection.classList.add("active");
  registerSection.classList.remove("active");
}

function activateRegister() {
  registerTab.classList.add("active");
  loginTab.classList.remove("active");

  registerSection.classList.add("active");
  loginSection.classList.remove("active");
}

loginTab.addEventListener("click", activateLogin);
registerTab.addEventListener("click", activateRegister);
showRegister.addEventListener("click", activateRegister);
showLogin.addEventListener("click", activateLogin);

activateLogin();