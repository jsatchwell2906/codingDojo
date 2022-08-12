var animalImg = document.querySelector("#fav-animal");

console.log(animalImg);

function pickCat(element) {
    //element.style.backgroundColor = "goldenrod";
    element.remove();
    animalImg.src = "images/cat.jpg";
}

function pickDog(element) {
    element.classList.add("btn");
    animalImg.src = "images/dog.jpeg";
}