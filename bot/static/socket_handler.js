$(document).ready(async ()=>{
    const res = await axios.get('/chat/chatroom/user_info');

    const user_id = res.data.user_id
    const user_pk = res.data.user_pk
    
    const chatSocket = new WebSocket(
        "ws://" + window.location.host + "/ws/chat/chatroom/"
    );
    
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
    
    document.querySelector("#chat").focus();
    
    chatSocket.onmessage = async function (e) {
        const data = JSON.parse(e.data);
        const message = data["message"];
        const textArea = document.querySelector("#chat-log");
    
        const timeNow = new Date()
    
        textArea.value +=`[${user_id}] ${timeNow.getHours()}:${timeNow.getMinutes()} : ${message}\n`;
        textArea.scrollTop = textArea.scrollHeight;
    };
    
    chatSocket.onclose = async function (e) {
        console.error("Chat socket closed unexpectedly");
    };
    document.querySelector("#chat").onkeyup = function (e) {
        if (e.keyCode === 13) {
            // enter, return
            document.querySelector("#submit").click();
        }
    };
    
    document.querySelector("#submit").onclick = async function (e) {
        const messageInputDom = document.querySelector("#chat");
        const message = messageInputDom.value;
        
        if(message.length != 0){
            let formData = new FormData();
            formData.append("d",'잘갔니?');
        
            formData.append('content',message);
            formData.append('user_pk',user_pk);
        
            axios.post('/chat/chatroom',formData).catch(errors=>console.log(errors));
            
            chatSocket.send(
                JSON.stringify({
                    message: message,
                    user_pk: user_pk
                })
            );
        
            messageInputDom.value = "";   
        }
    };
})
