const GET_NEWS_BUTTON = document.querySelector("#get-news-button")
if(GET_NEWS_BUTTON){
    GET_NEWS_BUTTON.addEventListener("click",requestBalancedNews)
}
console.log("Testing New 1");


var apigClient = apigClientFactory.newClient();
var params = {

};

var body = {

};

var additionalParams = {
  headers: {

  },
  queryParams: {
    news_title: 'This Is Not a Normal Recession’: Banks Ready for Wave of Coronavirus Defaults',
    news_source: 'wsj.com',
    api:'rateCurrentNews'
  }
};


apigClient.balancednewsGet(params, body, additionalParams)
    .then(function(result){
      console.log("Success API CALL");
      console.log(result);
    }).catch( function(result){
      console.log("Failure API CALL");
      console.log(result);
    });



function requestBalancedNews() {
    // Get current tab's URL and name
    var currentURL;
    var currentTitle;

    getCurrentTab(console.log)
    sendNotification("tiiitle","meeeeeesg","https://www.google.com/")
}





function getCurrentTab(callBackFunction){
    var currentURL;
    chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
    function(tabs){
    	callBackFunction(tabs[0].url, tabs[0].title);
    });
}


function sendNotification(title, message, link) {
    console.log("Trying to notify!")
    chrome.notifications.clear('sendNews');
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
