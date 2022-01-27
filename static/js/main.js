let btn = document.querySelector(".search-btn");
let movieTitle = document.querySelector("#movie-title");
let releaseDate = document.querySelector("#release-date");
let overview = document.querySelector("#overview");
btn.addEventListener("click", function(event) {
    event.preventDefault();
    let movieTitleValue = movieTitle.value;
    let releaseDateValue = releaseDate.value;
    let overviewValue = overview.value;
    fetch(`http://127.0.0.1:8000/api/search?title=${movieTitleValue}&date=${releaseDateValue}&overview=${overviewValue}`)
        .then(response => response.json())
        .then(data => console.log(data));

});