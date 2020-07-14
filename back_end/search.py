import requests

__params_template = {
  'api_key': '5C42256FAF1E41E99E269259A6F52DDD',
  'q': ''
}


def findNews(source, title):
  # set up the request parameters
  params = __params_template
  params['q'] = "site:{0} {1}".format(source, title)
  print("Param_tem = " + str(__params_template))
  print("Param = " + str(params))


  # make the http GET request to Scale SERP
  api_result = requests.get('https://api.scaleserp.com/search', params)


  # package the needed data and return the results

  organic_results = api_result.json()["organic_results"]
  newsResult = {
    "title":organic_results[0]["title"],
    "link":organic_results[0]["link"],
    "snippet":organic_results[0]["snippet"]
  }

  return newsResult


if __name__ == '__main__':
    print(findNews("wsj.com","Trump Visa"))