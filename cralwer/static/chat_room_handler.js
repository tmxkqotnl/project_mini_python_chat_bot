axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

document.querySelector("#chat").onkeyup = function (e) {
    if (e.keyCode == 13) {
        // enter, return
        $("#submit").click();
    }
};

document.querySelector("#submit").onclick = async (e) => {
    const inputArea = document.querySelector("#chat");
    const chatLog = document.querySelector("#chat-log");
    const message = inputArea.value;

    let div_tag = document.createElement("div");

    div_tag.setAttribute("class", "myMessage");
    div_tag.innerText = message;
    chatLog.append(div_tag);

    // const img = document.createElement('img');
    // img.setAttribute('src','/img');
    // chatLog.append(img);

    if (message.length > 0) {
        const parsedData = new FormData();
        const splited = message.split(" ");
        let msg = message;

        inputArea.value = "";
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

        

        if (splited[0] === "/춘배야") {
            const res = await axios({
                method: "get",
                url: "/query",
                params: {"message":JSON.stringify(splited)},
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                },
            });
            msg = JSON.stringify(res.data.data);
        } else {
            msg = '잘못된 입력값';
        }
        div_tag = document.createElement("div");
        div_tag.setAttribute('class','myMessage');  
        div_tag.innerText = msg;
        chatLog.append(div_tag);

        chatLog.scrollTop = chatLog.scrollHeight;
    }
    inputArea.value = "";
};
