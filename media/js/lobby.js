var timeleft = 30;
var downloadTimer = setInterval(function(){
  document.getElementById("progressBar").value = 30 - --timeleft;
  document.getElementById("timeleft").innerHTML = timeleft
  if(timeleft <= 0)
    clearInterval(downloadTimer);

},1000);

// Your application has indicated there's an error
window.setTimeout(function(){
    // Move to a new location or you can do something else
    window.location.href = "/online";
}, 30000);