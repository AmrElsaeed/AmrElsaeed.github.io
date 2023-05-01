# from flask import Flask, render_template, request
# import requests
# from config import GOOGLE_API_KEY, GOOGLE_CX_ID

# app = Flask(__name__)

# #home page
# @app.route("/", methods=["POST", "GET"])
# def home():
#     #fetchig query from page form
#     if request.method == "POST":
#         query = request.form["q"]
#         search_results = get_search_results(query, 40) #calling function to get search results using google API
#         return render_template("search.html", results=search_results, content=query) #passing results and query to be displayed to user
#     else:
#         return render_template("index.html")

# #Search API results
# def get_search_results(query, num_results=10):
#     url = 'https://www.googleapis.com/customsearch/v1'
#     params = {'key': GOOGLE_API_KEY, 'q': query, 'cx': GOOGLE_CX_ID}
#     all_results = [] # to concat results together as max of 10 can be requested from API each time

#     for start_index in range(1, num_results, 10): # Start at 1, increment by 10
#         params['start'] = start_index #to request reamining results every time
#         params['num'] =  min(num_results - len(all_results), 10) # Request up to 10 results
#         response = requests.get(url, params=params) # HTTP GET request to the Google Custom Search API
#         results = response.json()['items'] #extracts the list of search results from the JSON response 
#         all_results.extend(results)

#     return all_results

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request
import requests
from config import BING_API_KEY

app = Flask(__name__)

#home page
@app.route("/", methods=["POST", "GET"])
def home():
    #fetchig query from page form
    if request.method == "POST":
        query = request.form["q"]
        search_results = get_search_results(query, 50) #calling function to get search results using Bing API
        return render_template("search.html", results=search_results, content=query) #passing results and query to be displayed to user
    else:
        return render_template("index.html")

#Search API results
def get_search_results(query, num_results=10):
    url = 'https://api.bing.microsoft.com/v7.0/search'
    headers = {'Ocp-Apim-Subscription-Key': BING_API_KEY}
    all_results = [] # to concat results together as max of 50 can be requested from API each time

    for offset in range(0, num_results, 50): # Start at 0, increment by 50
        params = {'q': query, 'count': min(num_results - len(all_results), 50), 'offset': offset}
        response = requests.get(url, params=params, headers=headers) # HTTP GET request to the Bing Search API
        results = response.json()['webPages']['value'] #extracts the list of search results from the JSON response 
        all_results.extend(results)

    

    return all_results


if __name__ == "__main__":
    app.run(debug=True)

