document.addEventListener("DOMContentLoaded", function(event) {
var thumbnailElement = document.getElementById("smart_thumbnail","smart_thumbnail_1");

thumbnailElement.addEventListener("click", function() {

if (thumbnailElement.className == "small") {
thumbnailElement.className = "";
} else {
thumbnailElement.className = "small";
}
// write here
});
});
