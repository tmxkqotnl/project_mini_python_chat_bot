axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

document.querySelector("#chat").onkeyup = function (e) {
    if (e.keyCode == 13) {
        // enter, return
        $("#submit").click();
    }
};

document.querySelector("#submit").onclick = async e => {
    const inputArea = document.querySelector("#chat");
    const chatLog = document.querySelector("#chat-log");
    const message = inputArea.value;

    // const img = document.createElement('img');
    // img.setAttribute('src','/img');
    // chatLog.append(img);

    let data = null;
    if (message.length > 0) {
        const parsedData = new FormData();
        const splited = message.split(' ');

        parsedData.append("message", JSON.stringify(splited));
        
        await axios({
            method: "post",
            url: "/chatroom",
            data: parsedData,
            headers: {
                "Content-Type": "application/json",
                Accept: "application/json",
            },
        });

        if(splited[0] === '/춘배야'){
            const res = await axios({
                method:'get',
                url:'/query',
                data:parsedData,
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                },
            })
            
            data = res.data;
        }   
    }

    let div_tag = document.createElement("div");
    div_tag.setAttribute("class", "myMessage");
    div_tag.innerText = message;

    chatLog.append(div_tag);

    chatLog.scrollTop = chatLog.scrollHeight;

    if(data != null){
        div_tag = document.createElement("div");
        div_tag.setAttribute("class", "myMessage");
        div_tag.innerText = data;

        chatLog.append(div_tag);
    }

    inputArea.value = "";
};
