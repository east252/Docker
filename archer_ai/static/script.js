/*
    This Javascript is a part of the Reggie Program.
    Javascript comments are // or /* until */
/*

    Javascript is linked to HTML, by the HTML href.


*/
function sendData() {
  var value = document.getElementById("input").value;
  $.ajax({
    url: "/process",
    type: "POST",
    data: { data: value },
    success: function (response) {
      document.getElementById("output").innerHTML = response;
    },
    error: function (error) {
      console.log(error);
    },
  });
}

function clearData() {
  document.getElementById("input").value = "";
}

function thinking() {
  document.getElementById("output").textContent = "Thinking . . .";
}

function hello() {
  console.log("Hello World!");
}
