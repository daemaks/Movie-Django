//Footage aroow

const arrows = document.querySelectorAll(".arrow");
const movieFootage = document.querySelectorAll(".movie-detail-footage");

arrows. forEach((arrow,i)=>{
    const itemNumber = movieFootage[i].querySelectorAll("img").length;
    let clickCounter = 0;
    arrow.addEventListener("click", ()=>{
        clickCounter++;
        if(itemNumber - (1 + clickCounter) > 0){
            movieFootage[i].style.transform = `translateX(${
                movieFootage[i].computedStyleMap().get("transform")[0].x.value-300
            }px)`;
        } else{
            movieFootage[i].style.transform = "translateX(0)";
            clickCounter = 0;
        }

    });
});


//Start rating

const rating = document.querySelector('form[name=rating]');

rating.addEventListener("change", function() {

    let data = new FormData(this)
    fetch(`${this.action}`, {
        method: 'POST',
        body: data
    })
})