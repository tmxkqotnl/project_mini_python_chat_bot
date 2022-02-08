$(document).ready(async ()=>{
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

    document.querySelector("#chat").onkeyup = function (e) {
        if (e.keyCode === 13) {
            // enter, return
            document.querySelector("#submit").click();
        }
    };
    
    
    
})
