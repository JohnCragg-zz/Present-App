function clicked() {

 var email = document.getElementById("email").value;
 var first_name = document.getElementById("first_name").value;
 var second_name  = document.getElementById("second_name").value;
 var url = 'http://127.0.0.1:5000/api/v1/person/' + email + '/' + first_name + '/' + second_name + '/';

 console.log(url);

 var xhr = new XMLHttpRequest();
 xhr.open('POST', url, false);
 xhr.send();

}