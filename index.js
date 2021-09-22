const params = new URLSearchParams(window.location.search);

const diff = params.get("diff");
const height = parseInt(params.get("height"));
const width = parseInt(params.get("width"));

document.body.style.height = height + "px";
document.body.style.width = width + "px";

document.body.style.backgroundImage = "url(" + diff + ".jpg)"

// document.getElementById("img").src = diff + ".jpg"

function timeRefresh(time) {
    setTimeout("location.reload(true);", time);
}
