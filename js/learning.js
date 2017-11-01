document.addEventListener("DOMContentLoaded", function (event) {
  var languageSelectors = document.getElementsByClassName("logo-wrapper");
  var clicked = function () {
    var h4 = this.getElementsByTagName("h4")[0];
    var moduleDisplay;
    if (this.style.backgroundColor == "") {
      this.style.backgroundColor = "rgba(45, 255, 45, 0.5)";
      h4.style.visibility = "visible";
      moduleDisplay = "block";
    } else {
      this.style.backgroundColor = null;
      h4.style.visibility = null;
      moduleDisplay = null;
    }
    var modules = document.getElementsByClassName(h4.innerHTML.toLowerCase().concat("-module"));
    for (var i = 0; i < modules.length; i++) {
      modules[i].style.display = moduleDisplay;
    }
  };
  for (var i = 0; i < languageSelectors.length; i++) {
    languageSelectors[i].addEventListener("click", clicked, false);
  }
});
