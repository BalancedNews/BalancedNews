const GET_NEWS_BUTTON = document.querySelector("#get-news-button")
if(GET_NEWS_BUTTON){
    GET_NEWS_BUTTON.addEventListener("click",requestBalancedNews)
}

function requestBalancedNews() {
    // Get current tab's URL and name
    var currentURL;
    var currentTitle;

    console.log("Requesting!");
    sendNotification("tiiitle","meeeeeesg","https://www.google.com/")
}

function sendNotification(title, message, link) {
    chrome.notifications.clear('sendNews')
    chrome.notifications.onClicked.addListener(function(){
        window.open(link);
        window.focus();
    })

    var notifOptions = {
        type: "basic",
        iconUrl:"../../images/balanced_news_icon.png",
        title: title,
        message: message,
        requireInteraction: true,
    };


    chrome.notifications.create('sendNews', notifOptions);
    chrome.notifications.clear('sendNews')
    console.log("Creating Done")
}
