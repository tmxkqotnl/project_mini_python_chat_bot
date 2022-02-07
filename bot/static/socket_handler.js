$(document).ready(async ()=>{
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

    
    const chatSocket = new WebSocket(
        "ws://" + window.location.host + "/ws/chat/chatroom/"
        );
    
    let res = await axios.get('/chat/chatroom/user_info');
    const msg = res.data.message;    
    const textArea = document.querySelector("#chat-log");  
    textArea.scrollTop = textArea.scrollHeight;

    chatSocket.onmessage = async function (e) {
        const data = JSON.parse(e.data);
        const message = data["message"];
        const timeNow = new Date()

        // let res = await axios.get('/chat/chatroom/user_info');
        // const user_id = res.data.user_id
    
        textArea.value +=`[${data["user"]}] ${timeNow.getHours()}:${timeNow.getMinutes()} : ${message}\n`;
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
            formData.append('content',message);
            formData.append('message',message);
        
            let res = await axios.post('/chat/chatroom',formData);
            
            chatSocket.send(
                JSON.stringify({
                    message: message,
                    user:res.data.user,
                })
            );
        
            messageInputDom.value = "";   
        }
    };

    // 시간 남으면 구현
    // $('#chat-log').scroll(()=>{
    //     const scrollTop = $(this).scrollTop();
    //     const innerHeight = $(this).innerHeight();
    //     const scrollHeight = $(this).prop('scrollHeight');

    //     if(scrollTop + innerHeight >= scrollHeight){
            
    //     }
    // })
})
