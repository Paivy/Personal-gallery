function copy() {
  var copyText = document.getElementById("imagedirectlink");

  copyText.select();
  copyText.setSelectionRange(0, 99999);

  document.execCommand("copy");
  alert("Copied!");
}

