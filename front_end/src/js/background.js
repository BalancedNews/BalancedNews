

// When the extension is installed or upgraded ...
chrome.runtime.onInstalled.addListener(function() {
    // Replace all rules ...
    chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
        // With a new rule ...
        chrome.declarativeContent.onPageChanged.addRules([
            {
                // That fires when a page's URL contains a 'g' ...
                conditions:[
                    new chrome.declarativeContent.PageStateMatcher(
                    {pageUrl: { hostSuffix: 'abcnews.go.com',},
                    }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'bloomberg.com',},
                    }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'bostonglobe.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'breitbart.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'businessinsider.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'cbsnews.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'cnbc.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'cnn.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'dailycaller.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'dailymail.co.uk',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'fivethirtyeight.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'forbes.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:   'foxnews.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'theguardian.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:   'huffingtonpost.ca',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'latimes.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'motherjones.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'msnbc.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'nationalreview.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:   'nymag.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'nytimes.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'politico.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'realclearpolitics.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:   'talkingpointsmemo.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'thedailybeast.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:   'thehill.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'usnews.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'vox.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'wsj.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'washingtonexaminer.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'washingtonpost.com',},
                        }),

                    new chrome.declarativeContent.PageStateMatcher(
                        {pageUrl: { hostSuffix:  'washingtontimes.com'},
                        }),

                ] ,
                // And shows the extension's page action.
                actions: [ new chrome.declarativeContent.ShowPageAction() ]
            }
        ]);
    });
});
