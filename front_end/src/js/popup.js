function main(){
  console.log("   Method - Main");
  getCurrentTab(rateCurrentNews);
  const GET_NEWS_BUTTON = document.querySelector("#get-news-button")
  GET_NEWS_BUTTON.addEventListener("click",
                  function(){getCurrentTab(getBalancedNews);})
  // const GET_NEWS_BUTTON = document.querySelector("#get-news-button")
  // GET_NEWS_BUTTON.addEventListener("click",
  //                 function(){sendNotification("Test title", "test message", "https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html");})

}


function getCurrentTab(callBackFunction){
    console.log("   Method - getCurrentTab");
    var currentURL;
    chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
    function(tabs){
      console.log("Current Title and URL:",tabs[0].title, tabs[0].url);
    	callBackFunction(tabs[0].title, tabs[0].url);
    });
}



function rateCurrentNews(title, url){
  console.log("   Method - rateCurrentNews");
  var apigClient = apigClientFactory.newClient();
  var params = {
  };
  var body = {};
  var additionalParams = {
    headers: {},
    queryParams: {
      news_title:title,
      news_source:url,
      api:'rateCurrentNews'
    }
  };
  apigClient.balancednewsGet(params, body, additionalParams)
      .then(function(result){
        console.log("      Success API CALL");
        console.log("result", result);
        changeCurrentRating(result.data.partisanScore)
      }).catch( function(result){
        console.log("      Failure API CALL");
        console.log(result);
      });
}

function getBalancedNews(title, url){
  console.log("   Method - getBalancedNews");
  var apigClient = apigClientFactory.newClient();
  var params = {
  };
  var body = {};
  var additionalParams = {
    headers: {},
    queryParams: {
      news_title:title,
      news_source:url,
      api:'getBalancedNews'
    }
  };
  apigClient.balancednewsGet(params, body, additionalParams)
      .then(function(result){
        console.log("      Success API CALL");
        console.log("result", result);
        var content = result.data.content
        var title = content["title"]
        var message = content["snippet"]
        var link = content["link"]
        sendNotification(title, message, link)
      }).catch( function(result){
        console.log("      Failure API CALL");
        console.log(result);
      });
}


function changeCurrentRating(partisanScore){
  console.log("   Method - changeCurrentRating");
  const descriptionText = document.querySelector(".text_top_1")
  if (partisanScore>0.1){
    descriptionText.innerText = "The news website you’re on is right leaning ("
                                + partisanScore.toString()+")"
  }else if (partisanScore<-0.1) {
    descriptionText.innerText = "The news website you’re on is left leaning ("
                                + partisanScore.toString()+")"
  }else{
    descriptionText.innerText = "The news website you’re on is relatively neutral ("
                                + partisanScore.toString()+")"
  }
  const slider = document.querySelector(".slider")
  slider.value = partisanScore*100
}


function sendNotification(title, message, link) {
    console.log("   Method - sendNotification");
    console.log(title, message, link);

    chrome.notifications.clear('test');
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
    chrome.notifications.create('test', notifOptions);
    console.log("   Notification pushed")
}
main();
