const removeError = (clicked_id) =>{
    
    document.getElementById(clicked_id).style.border = "none";
}

const ValidateSignin = () =>{
    let useremail = document.getElementById("useremail");
    let passwords = document.getElementById("userpassword");
    let rememberme = document.getElementById("rememberme");
    if(useremail.value.trim() === "" || passwords.value.trim() === ""){
        if(useremail.value.trim() === ""){
            useremail.style.border = "1px solid red";
            return false;
        }else{
            passwords.style.border = "1px solid red";
            return false;
        }
    }else{
        if(rememberme.checked){
            alert("checked")
            localStorage.setItem("useremail", useremail);
            localStorage.setItem("passwords", passwords);
        }
    }

}

const getcredentials = () =>{
    document.getElementById("uploadpost").style.display = "block"
}
const getcredential = () =>{
    document.getElementById("uploadpost").style.display = "none"
}

const ValidateSignup = () =>{
    let useremail = document.getElementById("useremail");
    let phonenumber = document.getElementById("phonenumber");
    let userimages = document.getElementById("userimages");
    let userpassword = document.getElementById("userpassword");
    if(useremail.value.trim() === "" || phonenumber.value.trim() === "" || userimages.value.trim() === "" || userpassword.value.trim() === ""){
        if(useremail.value.trim() === ""){
            useremail.style.border = "1px solid red";
            return false;
        }else if(phonenumber.value.trim() === ""){
            phonenumber.style.border = "1px solid red";
            return false;
        }else if(userimages.value.trim() === ""){
            userimages.style.border = "1px solid red";
            return false;
        }else{
            userpassword.style.border = "1px solid red";
            return false;
        }
    }else{
       
    }

}

const ShowAddStory = () =>{
    document.getElementById("").style.display = "block"
}