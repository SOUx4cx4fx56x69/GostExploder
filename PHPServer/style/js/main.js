var cX,cY,MenuClosed=true;
document.onmousemove = function(x){
    cX = x.pageX;
    cY = x.pageY;
}

function turnmenu() {
    //alert("In future");
    var menu = document.getElementsByClassName("menu");
    if(MenuClosed){
	menu[1].style.display="block";
	MenuClosed=false;
    }else{
	menu[1].style.display="none";
	MenuClosed=true;
    }
}
window.onload = function(){
    console.log("...WOOF-WOOF...");
    console.log("...Maybe it social engenering? Just don't it!...");
}
function deleteLoader(){
    var loader = document.getElementById("loader");
    loader.innerHTML="";
    loader.style.display="none";
}
function changecaptcha(){
    var captcha = document.getElementById("captcha");
    captcha.src="/drive/get_captcha.php";
}
document.addEventListener("DOMContentLoaded", function(event) {
    setTimeout(deleteLoader, 5000);
});
/*
function eyes(){
  this.left=document.getElementsByClassName("owleyeleft");
  this.right=document.getElementsByClassName("owleyeright");
};
*/
