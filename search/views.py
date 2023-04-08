import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from googlesearch import search
from urllib.parse import urlparse




def search_results(request):
    query = request.GET.get('search')
    if query:
        try:
            num_results = 10
            start = 0
            url = f'https://www.google.com/search?q={query}&start={start}&num={num_results}'
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            links = soup.find_all('a')
            results = []
            for link in links:
                href = link.get('href')
                if href.startswith('/url?q='):
                    title = link.get_text()
                    url = href.split('/url?q=')[1].split('&sa=')[0]
                    parsed_url = urlparse(url)
                    url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
                    if 'google.com' not in parsed_url.netloc:
                        results.append((title, url))
            context = {'query': query, 'results': results}
            return render(request, 'search/results.html', context)
        except:
            error = 'An error occurred while searching. Please try again later.'
            context = {'error': error}
            return render(request, 'search/results.html', context)
    else:
        return render(request, 'search/index.html')








# def search_results(request):
#     if 'search' in request.GET:
#         try:
#             query = request.GET['search']
#             num_results = 10 # number of search results to return
#             start = 0 # start with the first search result page
#             
#             # construct the Google search URL with the 'start' and 'num' parameters
#             # use the "intext" operator to search for the query in the body of the page
#             # use the "site" operator to restrict results to a specific domain or URL
#             url = f'https://www.google.com/search?q={query}&start={start}&num={num_results}'
#             #url = f'https://www.google.com/search?q=intext%3A%22{query}%22+education+OR+learning+OR+tutorial+OR+how+to+OR+coding+OR+programming+OR+web+development+OR+geeksforgeeks&start={start}&num={num_results}'
#             
#             page = requests.get(url)
#             soup = BeautifulSoup(page.content, 'html.parser')
#             links = soup.find_all('a')
#             results = []
#             for link in links:
#                 href = link.get('href')
#                 if href.startswith('/url?q='):
#                     title = link.get_text()
#                     url = href.split('/url?q=')[1].split('&sa=')[0]
#                     parsed_url = urlparse(url)
#                     
#                     url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
# 
#                     # check if the search result URL belongs to Google's own GUI
#                     if 'google.com' not in parsed_url.netloc:
#                         results.append((title, url))
#             context = {
#                 'query': query,
#                 'results': results
#             }
#             return render(request, 'search/results.html', context)
#         except:
#             error = 'An error occurred while searching. Please try again later.'
#             context = {
#                 'error': error
#             }
#             return render(request, 'search/results.html', context)
#     return render(request, 'search/search.html')



















# def search_results(request):
#     if 'search' in request.GET:
#         try:
#             query = request.GET['search']
#             num_results = 10 # number of search results to return
#             start = 0 # start with the first search result page
#             
#             # construct the Google search URL with the 'start' and 'num' parameters
#             url = f'https://www.google.com/search?q={query}&start={start}&num={num_results}'
#             
#             page = requests.get(url)
#             soup = BeautifulSoup(page.content, 'html.parser')
#             links = soup.find_all('a')
#             results = []
#             for link in links:
#                 href = link.get('href')
#                 if href.startswith('/url?q='):
#                     title = link.get_text()
#                     url = href.split('/url?q=')[1].split('&sa=')[0]
#                     parsed_url = urlparse(url)
#                     
#                     url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
#                     
#                     # check if the search result URL belongs to Google's own GUI
#                     if 'google.com' not in parsed_url.netloc:
#                         results.append((title, url))
#             context = {
#                 'query': query,
#                 'results': results
#             }
#             return render(request, 'search/results.html', context)
#         except:
#             error = 'An error occurred while searching. Please try again later.'
#             context = {
#                 'error': error
#             }
#             return render(request, 'search/results.html', context)
#     return render(request, 'search/search.html')





# def search_results(request):
#     if 'search' in request.GET:
#         try:
#             query = request.GET['search']
#             url = f'https://www.google.com/search?q={query}'
#             page = requests.get(url)
#             soup = BeautifulSoup(page.content, 'html.parser')
#             links = soup.find_all('a')
#             results = []
#             for link in links:
#                 href = link.get('href')
#                 if href.startswith('/url?q='):
#                     title = link.get_text()
#                     # parsed_url = urlparse(href.lstrip('/url?q='))
#                     url = href.split('/url?q=')[1].split('&sa=')[0]
#                     parsed_url = urlparse(url)
#                     
#                     url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
#                     results.append((title, url))
#             context = {
#                 'query': query,
#                 'results': results
#             }
#             return render(request, 'search/results.html', context)
#         except:
#             error = 'An error occurred while searching. Please try again later.'
#             context = {
#                 'error': error
#             }
#             return render(request, 'search/results.html', context)
#     return render(request, 'search/search.html')



# def search_results(request):
#     if 'search' in request.GET:
#         try:
#             query = request.GET['search']
#             url = f'https://www.google.com/search?q={query}'
#             page = requests.get(url)
#             soup = BeautifulSoup(page.content, 'html.parser')
#             links = soup.find_all('a')
#             results = []
#             for link in links:
#                 href = link.get('href')
#                 if href.startswith('/url?q='):
#                     title = link.get_text()
#                     url = href.lstrip('/url?q=')
#                     results.append((title, url))
#             context = {
#                 'query': query,
#                 'results': results
#             }
#             return render(request, 'search/results.html', context)
#         except:
#             error = 'An error occurred while searching. Please try again later.'
#             context = {
#                 'error': error
#             }
#             return render(request, 'search/results.html', context)
#     return render(request, 'search/search.html')
