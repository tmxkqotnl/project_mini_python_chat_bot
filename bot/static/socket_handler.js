const chatSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/chat/chatroom/"
);

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    const message = data["message"];
    const textArea = document.querySelector("#chat-log");

    const timeNow = new Date()

    textArea.value +=`[${document.querySelector("#hidden").innerText}] ${timeNow.getHours()}:${timeNow.getMinutes()} : ${message}\n`;
    textArea.scrollTop = textArea.scrollHeight;
};

chatSocket.onclose = function (e) {
    console.error("Chat socket closed unexpectedly");
};

document.querySelector("#chat").focus();
document.querySelector("#chat").onkeyup = function (e) {
    if (e.keyCode === 13) {
        // enter, return
        document.querySelector("#submit").click();
    }
};

document.querySelector("#submit").onclick = function (e) {
    const messageInputDom = document.querySelector("#chat");
    const message = messageInputDom.value;
    
    let formData = new FormData();
    formData.append("d",'잘갔니?');

    axios.post('/chat/chatroom',formData).catch(errors=>console.log(errors));
    
    chatSocket.send(
        JSON.stringify({
            message: message,
        })
    );

    messageInputDom.value = "";
};