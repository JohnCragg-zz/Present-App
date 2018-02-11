function clicked() {
    let email = document.getElementById("email").value;
    let first_name = document.getElementById("first_name").value;
    let second_name  = document.getElementById("second_name").value;
    let url = 'http://127.0.0.1:5000/api/v1/person/' + email + '/' + first_name + '/' + second_name + '/';

    let xhr = new XMLHttpRequest();
    let data = JSON.stringify({id: "200"});

    xhr.open("PUT", url, true);
    xhr.setRequestHeader('Content-type','application/json; charset=utf8');
    xhr.onload = function(){
        let response = JSON.parse(xhr.response);
        if(xhr.readyState === 4 && xhr.status === 200){
            console.log(url);
            console.log('Success ', response);
        }
        else{
            console.log('Error', response);
        }
    };
    xhr.send(data);
};