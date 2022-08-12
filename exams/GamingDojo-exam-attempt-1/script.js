console.log("page loaded...");

function message() {
    alert("This game is supported on Linux");
}

var cartCount = 0;
var buySpan = document.querySelector("#buy");

function buy() {
    cartCount++;
    buySpan.innerText = cartCount;
}

var gameImg = document.querySelector("#cafe-neko")

function scrollGameleft() {
    gameImg.src = "images/cafe-neko.png";
}

function scrollGameright() {
    gameImg.src = "images/pixel-ninjas-2.png"
}
