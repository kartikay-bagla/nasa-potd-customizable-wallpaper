var diff = parseInt(document.querySelector('title').text);

var prevDate = null;

function updateImage() {
    var currDate = new Date();
    currDate.setDate(currDate.getDate() - diff);

    if (currDate != prevDate) {
        prevDate = currDate;
        var dd = String(currDate.getDate()).padStart(2, '0');
        var mm = String(currDate.getMonth() + 1).padStart(2, '0');
        var yyyy = String(currDate.getFullYear());

        currDate = yyyy + "-" + mm + "-" + dd;

        var url = "http://apodapi.herokuapp.com/api?date=" + currDate;

        fetch(url)
            .then(resp => resp.json())
            .then(jsonObj => {
                document.body.style.backgroundImage = "url(" + jsonObj["url"] + ")";
                console.log(jsonObj["url"]);
            });
    }
}

updateImage();
setTimeout(updateImage, 5000);