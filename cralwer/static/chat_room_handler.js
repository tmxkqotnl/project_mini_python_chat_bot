axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

document.querySelector("#chat").onkeyup = function (e) {
    if (e.keyCode == 13) {
        // enter, return
        $("#submit").click();
    }
};

document.querySelector("#submit").onclick = function (e) {
    const inputArea = document.querySelector("#chat");
    const chatLog = document.querySelector("#chat-log");
    const message = inputArea.value;

    if (message.length >0) {
        const parsedData = new FormData();
        const splited = message;

        parsedData.append("message", JSON.stringify(message.split(" ")));

        axios({
            method: "post",
            url: "/chatroom",
            data: parsedData,
            headers: {
                "Content-Type": "application/json",
                Accept: "application/json",
            },
        });
    }

    div_tag = document.createElement("div");
    div_tag.setAttribute("class", "myMessage");
    div_tag.innerText = message;

    chatLog.append(div_tag);

    chatLog.scrollTop = chatLog.scrollHeight;

    inputArea.value = "";
};
