window.onload = () => {

    //HOMEPAGE
    var home = document.getElementById("home");
    home.onclick = function(){ //close all modals
        document.getElementById("instituteshop-page").style.display = "none";
        document.getElementById("login-page").style.display = "none";
        document.getElementById("signup-page").style.display = "none";
        document.getElementById("comment-page").style.display = "none";
        document.getElementById("staff-page").style.display = "none"
    }

    document.getElementById("version").innerText = fetch('http://localhost:5000/api/GetVersion',
    {
        headers : {
        "Accept" : "application/json", },
    }).then((response) => response.json()).then((data) => document.getElementById("version").innerText =data);
    
    
    //STAFFS
    var staff_modal = document.getElementById("staff-page")
    var staffbtn = document.getElementById("staff")
    var staff_lst = [];
    var vcard_info;

    staffbtn.onclick = function(){
        document.getElementById("instituteshop-page").style.display = "none";
        document.getElementById("login-page").style.display = "none";
        document.getElementById("signup-page").style.display = "none";
        document.getElementById("comment-page").style.display = "none";
        
        if (staff_modal.style.display == "none" || staff_modal.style.display == ""){
            staff_modal.style.display = "block";
            fetch('http://localhost:5000/api/GetAllStaff',
            {
                headers : {
                "Accept" : "application/json", },
            }).then((response) => response.json()).then(data => {
                staff_lst = data;
                staff_lst.sort();
                console.log(staff_lst)
                for (let i=0; i<staff_lst.length; i++){
                    var staff_name, staff_mail, staff_tel , staff_res;
                    let li = document.createElement("li");
                    
                    var vcard = fetch('http://localhost:5000/api/GetCard/' + staff_lst[i].id,
                    {
                        headers : {
                        "Accept" : "text/vcard", },
                    }).then((response) => response.text()).then(data =>{
                        var fn = /FN:(.*)/g;
                        var tel = /TEL:(.*)/g;
                        var mail = /EMAIL;[^:]*:(.*)/g;
                        var research = /CATEGORIES:(.*)/g;

                        staff_name = fn.exec(data)[1];
                        staff_tel = tel.exec(data)[1];
                        staff_mail = mail.exec(data)[1];
                        staff_res = research.exec(data)[1];

                        var pname = document.createElement("a");
                        // pname.style.cssText = "cursor:pointer;"
                        pname.appendChild(document.createTextNode("Name: " + staff_name))
                        // pname.onclick = function(){location.href = 'http://localhost:5000/api/GetCard/' + staff_lst[i].id;}

                        var ptel = document.createElement("a");
                        ptel.style.cssText = "cursor:pointer; color:blue; text-decoration:underline;"
                        ptel.title = "tel:" + staff_tel
                        ptel.onclick = function(){
                            var index = ptel.firstChild.nodeValue.indexOf("+")
                            staff_tel = ptel.firstChild.nodeValue.slice(index);
                            // console.log(staff_tel)
                            window.open('tel:' + staff_tel);
                            ptel.style.cssText = "cursor:pointer; color:blue; text-decoration:underline;"
                        }
                        ptel.appendChild(document.createTextNode("Tel: " + staff_tel))
                        
                        var pmail = document.createElement("a");
                        pmail.style.cssText = "cursor:pointer; color:#63c5da; text-decoration: underline"
                        pmail.title = "mailto:" + staff_mail
                        pmail.onclick = function() {
                            var index = pmail.firstChild.nodeValue.indexOf(" ")
                            staff_mail = pmail.firstChild.nodeValue.slice(index);
                            console.log(staff_mail)
                            window.open('mailto:' + staff_mail);
                        }
                        pmail.appendChild(document.createTextNode("Email: " + staff_mail))

                        var pres = document.createElement("a");
                        pres.appendChild(document.createTextNode("Research: "+ staff_res))
                    
                        // let li = document.createElement("li");
                        var hr = document.createElement('hr');
                        
                        var img = document.createElement('img');
                        img.src = 'http://localhost:5000/api/GetStaffPhoto/' + staff_lst[i].id;
                        img.title = "Get vCard of " + staff_name
                        img.style.cssText = "width: 200px;height:200px; display: inline-block; background-color: white; position:relative; cursor: pointer"
                        img.onclick = function(){location.href = 'http://localhost:5000/api/GetCard/' + staff_lst[i].id;}

                        var div = document.createElement("div");
                        div.appendChild(pname);
                        div.appendChild(document.createElement("br"))
                        div.appendChild(ptel);
                        div.appendChild(document.createElement("br"))
                        div.appendChild(pmail);
                        div.appendChild(document.createElement("br"))
                        div.appendChild(pres);

                        li.appendChild(img);
                        li.appendChild(div)
                        li.appendChild(hr);
                        hr.style.cssText = "border: 1px solid #f1f1f1;margin-left: 50px; width: 90%; position:relative"
                        li.style.cssText = 'list-style-type: none;display: inline-block;padding: 5px 15px;width:100%';
                        
                        // document.getElementById("staff-content").appendChild(li);
                        // console.log(staff_name[1]);
                        // console.log(staff_tel[1]);
                        // console.log(staff_mail[1]);
                        // console.log(staff_res[1]);
                    });
                    document.getElementById("staff-content").appendChild(li);
                }
            });

        }else{staff_modal.style.display = "none"}
    }


    //INSTITUTE SHOP
    var content = document.getElementById("content");
    var instituteshop_modal = document.getElementById("instituteshop-page");
    var instituteshopbtn = document.getElementById("instituteshop");
    var success_purchase = document.getElementById("purchased")
    var lst = [];

    instituteshopbtn.onclick = function() {
        document.getElementById("login-page").style.display = "none";
        document.getElementById("signup-page").style.display = "none";
        document.getElementById("comment-page").style.display = "none";
        document.getElementById("staff-page").style.display = "none"

        if (instituteshop_modal.style.display == "none" || instituteshop_modal.style.display == ""){
            instituteshop_modal.style.display = "block";
            fetch('http://localhost:5000/api/GetItems',
            {
                headers : {
                "Accept" : "application/json", },
            }).then((response) => response.json()).then(data => {
                lst = data;
                for (let i=0; i<lst.length; i++) {
                    let li = document.createElement("li");
                    var hr = document.createElement('hr');
                    let buy_now = document.createElement("button");
                    buy_now.setAttribute("id", "buy_button"+lst[i].id);
                    buy_now.innerHTML = "Buy Now";
                    buy_now.style.cssText = "cursor: pointer"
                    
                    let name = document.createTextNode(lst[i].name);
                    let desc = document.createTextNode(lst[i].description);
                    let price = document.createTextNode("$" + lst[i].price);
                    
                    var img = document.createElement('img');
                    img.src = 'http://localhost:5000/api/GetItemPhoto/' + lst[i].id;
                    img.style.cssText = "width: 200px;height:200px; display: inline-block; background-color: white; position:relative;"

                    li.appendChild(img);
                    li.appendChild(name);
                    li.appendChild(document.createElement("br"))
                    li.appendChild(desc);
                    li.appendChild(document.createElement("br"))
                    li.appendChild(price);
                    li.appendChild(document.createElement("br"))
                    li.appendChild(buy_now)
                    li.appendChild(hr);
                    hr.style.cssText = "border: 1px solid #f1f1f1;margin-left: 50px; width: 90%; position:relative"
                    li.style.cssText = 'list-style-type: none;display: inline-block;padding: 5px 15px;width:100%';
                    content.appendChild(li);
                    
                    document.getElementById("buy_button"+lst[i].id).onclick = function(){
                        if (document.getElementById("login_btn").textContent.indexOf("Hello") == -1){
                            alert("Log in to purchase item");
                            document.getElementById("login-page").style.display = "block";
                        }
                        else{
                            const username = document.getElementById("Username").value;
                            const password = document.getElementById("Password").value;
                            fetch('http://localhost:5000/api/PurchaseSingleItem/'+ lst[i].id,
                            {
                                headers : new Headers({
                                    'Authorization': 'Basic ' + btoa(username + ":" + password), 
                                    'Content-Type': 'text/json'})
                            }).then((response) => response.json()).then(data=>console.log(data));
                            // alert("Item successfully purchased. Thank you for shopping with us!")
                            success_purchase.innerText = "Item '" + lst[i].name + "' successfully purchased. Thank you for shopping with us!"
                            success_purchase.style.display="block";
                            var sec = 2;
                            setInterval(() => {
                                sec--;
                                if (sec == 0){
                                    success_purchase.style.display="none";
                                    clearInterval(2);
                                }
                            }, 1000);
                        }
                    }
                }
            }); 
        } else{instituteshop_modal.style.display = "none"}
    }

    var searchItem = document.getElementById("getItem")
    var tempbtn = []
    searchItem.onkeyup = function() {
        content.innerHTML = "";
        var filter = searchItem.value.toLowerCase();
        fetch('http://localhost:5000/api/GetItems/' + filter,
        {
            headers : {
            "Accept" : "application/json", },
        }).then((response) => response.json()).then(data => {
            lst = data;
            for (let i=0; i<lst.length; i++) {
                let li = document.createElement("li");
                var hr = document.createElement('hr');
                let buy_now = document.createElement("button");
                buy_now.setAttribute("id", "buy_button"+lst[i].id);
                buy_now.innerHTML = "Buy Now";
                buy_now.style.cssText = "cursor: pointer"
                
                let name = document.createTextNode(lst[i].name);
                let desc = document.createTextNode(lst[i].description);
                let price = document.createTextNode("$" + lst[i].price);
                
                var img = document.createElement('img');
                img.src = 'http://localhost:5000/api/GetItemPhoto/' + lst[i].id;
                img.style.cssText = "width: 200px;height:200px; display: inline-block; background-color: white; position:relative;"

                li.appendChild(img);
                li.appendChild(name);
                li.appendChild(document.createElement("br"))
                li.appendChild(desc);
                li.appendChild(document.createElement("br"))
                li.appendChild(price);
                li.appendChild(document.createElement("br"))
                li.appendChild(buy_now)
                li.appendChild(hr);
                hr.style.cssText = "border: 1px solid #f1f1f1;margin-left: 50px; width: 90%; position:relative"
                li.style.cssText = 'list-style-type: none;display: inline-block;padding: 5px 15px;width:100%';
                content.appendChild(li);
                
                document.getElementById("buy_button"+lst[i].id).onclick = function(){
                    if (document.getElementById("login_btn").textContent.indexOf("Hello") == -1){
                        alert("Log in to purchase item");
                        document.getElementById("login-page").style.display = "block";
                    }
                    else{
                        const username = document.getElementById("Username").value;
                        const password = document.getElementById("Password").value;
                        console.log(lst[i].name)
                        fetch('http://localhost:5000/api/PurchaseSingleItem/'+ lst[i].id,
                        {
                            headers : new Headers({
                                'Authorization': 'Basic ' + btoa(username + ":" + password), 
                                'Content-Type': 'text/json'})
                        }).then((response) => response.json()).then(data=>console.log(data));
                        success_purchase.innerText = "Item '" + lst[i].name + "' successfully purchased. Thank you for shopping with us!"
                        success_purchase.style.display="block";
                        var sec = 2;
                        setInterval(() => {
                            sec--;
                            if (sec == 0){
                                success_purchase.style.display="none";
                                clearInterval(2);
                            }
                        }, 1000);
                    }
                }
            }
        }); 
    }


    //GUESTBOOK
    var comment_modal = document.getElementById("comment-page")
    var commentbtn = document.getElementById("guestbook")
    var submit = document.getElementById("submit-comment");

    commentbtn.onclick = function(){
        document.getElementById("instituteshop-page").style.display = "none";
        document.getElementById("login-page").style.display = "none";
        document.getElementById("signup-page").style.display = "none";
        document.getElementById("staff-page").style.display = "none"

        if (comment_modal.style.display == "none" || comment_modal.style.display == ""){
            comment_modal.style.display = "block";

            //write comment
            submit.onclick = function(){
                var comment = document.getElementById("comment-box").value;
                var name = document.getElementById("name-box").value;
                if (comment == ""){document.getElementById("no-comment").textContent = "Please fill in the comment box."}
                else{
                    fetch('http://localhost:5000/api/WriteComment',
                    {
                        headers : {
                            "Content-Type" : 'text/json',
                        },
                        method : "POST",
                        body : JSON.stringify(
                                {   Comment: comment,
                                    Name: name
                                }
                            )   
                    }).then(response => response.text());
                    alert("Comment submitted!")
                    document.getElementById("comment-box").value = "";
                    document.getElementById("name-box").value = "";
                    document.getElementById('iframe').src = document.getElementById('iframe').src;
                }
            }

        }else{comment_modal.style.display = "none"}
    }


    //LOGIN
    const username = document.getElementById("Username").value;
    const password = document.getElementById("Password").value;
    var span = document.getElementsByClassName("close")[0];

    var loginmodal = document.getElementById("login-page");
    var loginbtn = document.getElementById("login");
    var reg = document.getElementById("reg");
    
    loginbtn.onclick = function() {
        if (document.getElementById("login_btn").textContent.indexOf("Hello") == -1){loginmodal.style.display = "block";}
    }

    span.onclick = function() {
        loginmodal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == loginmodal) {
            loginmodal.style.display = "none";
        }
    }

    reg.onclick = function(){
        const username = document.getElementById("Username").value;
        const password = document.getElementById("Password").value;
        console.log("username: " + username )
        console.log("pw: " + password)
        var auth = fetch('http://localhost:5000/api/GetVersionA',
        {
            method: 'GET', 
            headers: new Headers({
                'Authorization': 'Basic ' + btoa(username + ":" + password), 
                'Content-Type': 'text/json'
        })}).then(response => response.text())
        .then(data => {
            if (data.indexOf("v") != -1){
                alert("Login Successful!")
                document.getElementById("login_btn").textContent = "Hello " + username + "! ▼"
                loginmodal.style.display='none'
                // document.getElementById("Username").value = ""
                // document.getElementById("Password").value = ""
                document.getElementById("signup_logout").textContent = "LOGOUT";
                document.getElementById("signup-page").style.display = "none";
            }
            else{
                document.getElementById("wrong_auth").textContent = "Incorrect username or password."
            }
        });
    }
    

    //SIGNUP
    var signup_logout_btn = document.getElementById("signup_logout");
    var signup_page = document.getElementById("signup-page")
    var signup_reg = document.getElementById("signup-reg")
    signup_logout_btn.onclick = function(){
        if (signup_logout_btn.textContent == "LOGOUT"){
            alert("You are Logged Out")
            document.getElementById("Username").value = ""
            document.getElementById("Password").value = ""
            document.getElementById("login_btn").textContent = "LOGIN ▼";
            signup_logout_btn.textContent = "REGISTER"
        }
        else{
            signup_page.style.display = "block";

            document.getElementsByClassName("close-reg")[0].onclick = function(){signup_page.style.display = "none";}

            document.getElementById("instituteshop-page").style.display = "none";
            document.getElementById("login-page").style.display = "none";
            document.getElementById("comment-page").style.display = "none";
            document.getElementById("staff-page").style.display = "none";
            
            signup_reg.onclick = function(){
                const username = document.getElementById("signup-Username").value;
                const password = document.getElementById("signup-Password").value;
                const address = document.getElementById("signup-Address").value;
                console.log("username: " + username )
                console.log("pw: " + password)
                if (username == "" || password == ""){
                    document.getElementById("username_taken").textContent = "Username & password fields required."
                }
                else{
                    var auth = fetch('http://localhost:5000/api/Register',
                    {
                        headers : {
                            "Content-Type" : 'text/json',
                        },
                        method : "POST",
                        body : JSON.stringify(
                                {
                                    UserName: username,
                                    Password: password,
                                    Address:address
                                }
                            )   
                    }).then(response => response.text())
                    .then(data=>{
                        if (data == "Username not available."){
                            document.getElementById("username_taken").textContent = "Username is taken, please choose another username."
                        }
                        else{
                            alert("You have been registered!")
                            signup_page.style.display = "none"
                            document.getElementById("signup-Username").value = ""
                            document.getElementById("signup-Password").value = ""
                            document.getElementById("signup-Address").value = ""
                        }
                    })
                }
            }
        }
    }

}