let timeleft = 30;
let downloadTimer = setInterval(function () {
  document.getElementById("progressBar").value = 30 - --timeleft;
    document.getElementById("timeleft").innerHTML = timeleft;
  if(timeleft <= 0)
    clearInterval(downloadTimer);

},1000);

// Your application has indicated there's an error
window.setTimeout(function(){
    // Move to a new location or you can do something else
    // let xhttp = new XMLHttpRequest();
    // xhttp.onreadystatechange = function() {
    //   if (this.readyState === 4 && this.status === 200) {
    //         if (this.responseText === "[false]"){
    //             window.location.href = "/";
    //         }
    //   }
    // };
    // xhttp.open("GET", "/lock", true);
    // xhttp.send();
    // window.location.href = "/online";
    window.location.href = "/lock";
}, 30000);