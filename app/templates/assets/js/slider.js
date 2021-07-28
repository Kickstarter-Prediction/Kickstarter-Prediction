var slider1 = document.getElementById("goal");
var output1 = document.getElementById("display1");
output1.innerHTML = slider1.value; // Display the default slider value
// Update the current slider value (each time you drag the slider handle)
slider1.oninput = function() {
  output1.innerHTML = this.value;
}


var slider2 = document.getElementById("duration_days");
var output2 = document.getElementById("display2");
output2.innerHTML = slider2.value;
slider2.oninput = function() {
    output2.innerHTML = this.value;
  }

