const toggleButton=document.querySelector(".userProfileButton");
const profilePopUp=document.querySelector(".userDisplay");
let scrolledUp=true;
toggleButton.addEventListener("click",()=>{
    if(scrolledUp){
        profilePopUp.classList.remove("scrollUp");
        profilePopUp.classList.add("scrollDown");
        scrolledUp=false;
    }
    else{
        profilePopUp.classList.remove("scrollDown");
        profilePopUp.classList.add("scrollUp");
        scrolledUp=true;
    }
})