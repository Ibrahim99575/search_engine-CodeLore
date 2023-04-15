import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from googlesearch import search
from urllib.parse import urlparse



def search_results(request):
    if 'search' in request.GET:
        try:
            query = request.GET['search']
            num_results = 10 # number of search results to return
            start = 0 # start with the first search result page
            
            # construct the Google search URL with the 'start' and 'num' parameters
            # use the "intext" operator to search for the query in the body of the page
            # use the "site" operator to restrict results to a specific domain or URL
            #url = f'https://www.google.com/search?q={query}&start={start}&num={num_results}'
            
            keywords1 = '''html+OR+css+OR+javascript+OR+jquery+OR+ajax+OR+bootstrap+OR+angular+OR+react+OR+vue+OR+ember+OR+
						backbone+OR+polymer+OR+web+OR+components+OR+typescript+OR+flow+OR+graphql+OR+apollo+OR+redux+OR+
						mobx+OR+webpack+OR+gulp+OR+grunt+OR+python+OR+java+OR+c+++OR+c+OR+c#+OR+php+OR+ruby+OR+swift+OR+
						kotlin+OR+go+OR+scala+OR+haskell+OR+clojure+OR+perl+OR+lua+OR+rust+OR+dart+OR+groovy+OR+shell+OR+
						scripting+OR+mysql+OR+mongodb+OR+postgresql+OR+sql+OR+server+OR+oracle+OR+sqlite+OR+firebase+OR+aws+OR+
						azure+OR+google+OR+cloud+OR+platform+OR+docker+OR+kubernetes+OR+jenkins+OR+circleci+OR+travis+OR+CI+OR+
						git+OR+svn+OR+mercurial+OR+tortoise+OR+android+OR+ios+OR+windows+OR+mac+OR+os+OR+linux+OR+unix+OR+
						raspberry+OR+pi+OR+arduino+OR+raspbian+OR+ubuntu+OR+debian+OR+centos+OR+fedora+OR+arch+linux+OR+
						gnome+OR+kde+OR+xfce+OR+openbox+OR+i3+OR+vim+OR+emacs+OR+sublime+OR+text+OR+atom+OR+visual+OR+
						studio+OR+code+OR+eclipse+OR+intellij+OR+IDEA+OR+netbeans+OR+xcode+OR+android+OR+studio+OR+unity+OR+
						unreal+OR+engine+OR+blender+OR+autodesk+OR+photoshop+OR+illustrator+OR+figma+OR+sketch+OR+invision+OR+
						zeplin+OR+adobe+OR+creative+OR+cloud+OR+UI+OR+design+OR+UX+OR+design+OR+front-end+OR+development+OR+
						back-end+OR+development+OR+full-stack+OR+development+OR+devops+OR+artificial+OR+intelligence+OR+
						machine+OR+learning+OR+deep+OR+learning+OR+natural+OR+language+OR+processing+OR+computer+OR+vision+OR+
						data+OR+science+OR+big+OR+data+OR+data+OR+visualization+OR+business+OR+intelligence+OR+blockchain+OR+
						cryptocurrency+OR+smart+contracts+OR+solidity+OR+ethereum+OR+bitcoin+OR+litecoin+OR+ripple+OR+eos+OR+
						stellar+OR+cardano+OR+truffle+OR+web3+OR+metamask+OR+ganache+OR+remix+OR+infura+OR+IPFS+OR+filecoin+OR+
						storj+OR+sia+OR+maidsafe+OR+namecoin+OR+monero+OR+zcash+OR+dash+OR+augmented+reality+OR+virtual+reality+OR+
						game+development+OR+network+security+OR+cybersecurity+OR+ethical+hacking+OR+penetration+testing+OR+
						digital+forensics+OR+web+security'''
            
            keywords2 = '''How to reverse a string in Python+OR+How to find the largest number in an array in Java+OR+How to
							merge two sorted arrays in C+++OR+How to check if a string contains a substring in JavaScript+OR+How to sort an array in
							descending order in Python+OR+How to find the second largest number in an array in Java+OR+How to swap two variables without
							using a temporary variable in C+++OR+How to remove duplicates from an array in JavaScript+OR+How to check if a number is
							prime in Python+OR+How to find the factorial of a number in Java+OR+How to reverse a linked list in C+++OR+How to convert a
							string to an integer in JavaScript+OR+How to find the common elements between two arrays in Python+OR+How to find the maximum
							subarray sum in an array in Java+OR+How to implement a binary search tree in C+++OR+How to find the length of a string in
							JavaScript+OR+How to check if a string is a palindrome in Python+OR+How to find the sum of an array in Java+OR+How to sort
							a linked list in C+++OR+How to remove an element from an array in JavaScript+OR+How to implement a stack using an array in
							Python+OR+How to implement a queue using a linked list in Java+OR+How to traverse a binary tree in C+++OR+How to concatenate
							two strings in JavaScript+OR+How to find the greatest common divisor of two numbers in Python+OR+How to check if a number
							is even or odd in Java+OR+How to find the middle element of a linked list in C+++OR+How to convert a number to a string in
							JavaScript+OR+How to reverse a number in Python+OR+How to sort a two-dimensional array in Java+OR+How to implement a priority
							queue using a heap in C+++OR+How to remove whitespace from a string in JavaScript+OR+How to implement a binary search in
							Python+OR+How to find the length of a linked list in Java+OR+How to implement a graph using an adjacency list in C+++OR+How
							to find the number of occurrences of a character in a string in JavaScript+OR+How to find the sum of the digits of a number
							in Python+OR+How to find the maximum element in a linked list in C+++OR+How to find the minimum element in an array in
							Java+OR+How to implement a breadth-first search in a graph in C+++OR+How to split a string into an array in JavaScript+OR+
							How to implement a bubble sort in Python+OR+How to find the second smallest number in an array in Java+OR+How to implement
							a depth-first search in a graph in C+++OR+How to find the factorial of a number using recursion in C+++OR+How to count the
							number of words in a string in JavaScript+OR+How to find the sum of a geometric series in Python+OR+How to find the kth
							smallest element in an array in Java+OR+How to implement a quicksort algorithm in C+++OR+How to remove all occurrences
							of a character from a string in JavaScript+OR+How to find the maximum element in an array using recursion in Python+OR+How
							to find the length of the longest increasing subarray in an array in Java+OR+How to implement a Dijkstra's algorithm in
							C+++OR+How to find the nth Fibonacci number in Python+OR+How to remove duplicates from a linked list in Java+OR+How to
							implement a binary search tree traversal in C+++OR+How to reverse a linked list+OR+How to find the median of an array in
							Java+OR+How to implement a hash table in C+++OR+How to find the sum of a series in JavaScript+OR+How to find the length
							of the longest common subsequence in two strings in Python+OR+How to check if two strings are anagrams in Java+OR+How
							to implement a depth-first search on a binary tree in C+++OR+How to find the mode of an array in JavaScript+OR+How to
							implement a selection sort in Python+OR+How to find the smallest common element in two arrays in Java+OR+How to implement
							a Floyd-Warshall algorithm in C+++OR+How to find the GCD of two numbers using Euclid's algorithm in Python+OR+How to
							reverse a sentence in JavaScript+OR+How to find the sum of the even numbers in an array in Java+OR+How to implement a
							heap sort in C+++OR+How to remove the first occurrence of a character from a string in Python+OR+How to implement a
							binary search tree deletion in C+++OR+How to find the longest palindrome substring in a string in JavaScript+OR+How to
							find the kth largest element in an array in Java+OR+How to implement a Kruskal's algorithm in C+++OR+How to find the
							number of trailing zeros in a factorial of a number in Python+OR+How to implement a breadth-first search on a binary
							tree in C+++OR+How to check if a linked list is circular in Java+OR+How to implement a merge sort in Python+OR+How to
							find the smallest common element in three arrays in Java+OR+How to implement a Bellman-Ford algorithm in C+++OR+How to
							find the reverse complement of a DNA sequence in Python+OR+How to check if a string has all unique characters in
							JavaScript+OR+How to implement an AVL tree in C+++OR+How to find the sum of the odd numbers in an array in Java+OR+How
							to implement a topological sort in C+++OR+How to find the kth smallest element in a binary search tree in Java+OR+How
							to remove the last occurrence of a character from a string in Python+OR+How to implement a red-black tree in C+++OR+How
							to find the number of occurrences of a substring in a string in JavaScript+OR+How to implement a bucket sort in Python+
							OR+How to find the smallest positive integer not present in an array in Java+OR+How to implement a Ford-Fulkerson algorithm
							in C+++OR+How to find the length of the longest palindrome substring in a string in Python+OR+How to check if a linked list
							is a palindrome in Java+OR+How to implement a binary search tree insertion in C+++OR+How to find the longest common prefix
							of two strings in JavaScript+OR+How to implement a counting sort in Python+OR+How to find the largest rectangular area in
							a histogram in Java+OR+How to implement a Huffman coding in C+++OR+How to find the kth smallest element in a max heap in
							Java+OR+How to remove all white spaces from a string in Python+OR+How to implement a Trie data structure in C+++OR+How to
							find the sum of the first n natural numbers in JavaScript+OR+How to implement a segment tree in Python+OR+How to find the
							maximum sum subarray in a circular array in Java+OR+How to implement a traveling salesman problem in C+++OR+How to find
							the number of divisors of a number in Python+OR+How to check if a binary tree is balanced in Java+OR+How to implement a
							binary search tree traversal in C+++OR+How to find the first non-repeating character in a string in JavaScript+OR+How to
							implement a suffix array in Python+OR+How to find the sum of digits of a number in Java+OR+How to implement a Dijkstra's
							algorithm in C+++OR+How to find the length of the longest increasing subsequence in an array in Python+OR+How to check
							if a binary tree is a binary search tree in Java+OR+How to implement a depth-first search on a graph in C+++OR+How to
							find the maximum sum subarray in an array in JavaScript+OR+How to implement a dynamic programming solution for the
							knapsack problem in Java+OR+How to find the kth largest element in a max heap using a heap sort in Python+OR+How to
							reverse a linked list in Java+OR+How to implement a union-find data structure in C+++OR+How to find the number of
							occurrences of a character in a string in JavaScript+OR+How to implement a Radix sort in Python+OR+How to find the
							longest common suffix of two strings in Java+OR+How to implement a quicksort algorithm in C+++OR+How to find the
							maximum sum submatrix in a 2D array in Python+OR+How to check if a binary tree is a complete binary tree in Java+OR+
							How to implement a breadth-first search on a graph in C+++OR+How to find the smallest missing positive number in an
							unsorted array in JavaScript+OR+How to implement a dynamic programming solution for the longest common subsequence
							problem in Python+OR+How to find the diameter of a binary tree in Java+OR+How to implement a 2D segment tree in C+++OR+
							How to find the number of occurrences of a word in a string in Python+OR+How to implement a shell sort in Java+OR+How
							to find the maximum sum subarray in a 2D array in JavaScript+OR+How to implement a depth-first search on a graph using
							recursion in C+++OR+How to find the longest increasing subsequence in an array in Java+OR+How to implement a dynamic
							programming solution for the longest increasing subsequence problem in Python+OR+How to check if a binary tree is a
							mirror image of itself in Java+OR+How to implement a Kruskal's algorithm using a disjoint-set data structure in C+++OR+
							How to find the largest prime factor of a number in Python+OR+How to implement a bucket sort for floating-point numbers
							in Java+OR+How to find the maximum path sum in a binary tree in JavaScript+OR+How to implement a binary search algorithm
							in C+++OR+How to find the number of unique substrings of a string in Python+OR+How to implement a dynamic programming
							solution for the longest palindromic subsequence problem in Java+OR+How to check if a binary tree is a symmetric binary
							tree in C+++OR+How to find the kth smallest element in a min heap using a heap sort in JavaScript+OR+How to implement a
							Floyd-Warshall algorithm using a matrix in Python+OR+How to find the maximum sum subrectangle in a 2D array in Java+OR+
							How to implement a dynamic programming solution for the longest palindromic substring problem in C+++OR+How to find the
							level order traversal of a binary tree in JavaScript+OR+How to implement a binary search tree deletion using the in-order
							successor in Java+OR+How to find the maximum product subarray in an array in Python+OR+How to implement a Kruskal's
							algorithm using a priority queue+OR+How to find the largest sum of non-adjacent numbers in an array in Java+OR+How to
							implement a Bellman-Ford algorithm using a matrix in C+++OR+How to find the longest common prefix of two strings in Python+
							OR+How to implement a selection sort in JavaScript+OR+How to find the maximum sum circular subarray in an array in Java+OR+
							How to implement a binary search tree insertion in C+++OR+How to find the minimum number of swaps required to sort an array
							in Python+OR+How to implement a dynamic programming solution for the longest repeated substring problem in Java+OR+How to
							check if a binary tree is a binary search tree without using recursion in C+++OR+How to find the kth smallest element in an
							unsorted array in JavaScript+OR+How to implement a greedy algorithm for the coin change problem in Python+OR+How to find
							the shortest path in a weighted directed graph using Dijkstra's algorithm in Java+OR+How to implement a bubble sort in C+++
							OR+How to find the minimum number of platforms required at a railway station in JavaScript+OR+How to implement an insertion
							sort in Python+OR+How to find the maximum sum of a path in a triangle in Java+OR+How to implement a binary search tree
							deletion using the in-order predecessor in C+++OR+How to find the maximum difference between two elements in an array in
							JavaScript+OR+How to implement a topological sort on a directed acyclic graph in Python+OR+How to find the minimum cost
							path in a grid using Dijkstra's algorithm in Java+OR+How to implement a counting sort in C+++OR+How to find the maximum
							subarray product in an array in JavaScript+OR+How to implement a merge sort algorithm in Python+OR+How to find the largest
							rectangle of 1's in a binary matrix in Java+OR+How to implement a binary search tree search in C+++OR+How to find the longest
							substring without repeating characters in Python+OR+How to implement a heap sort in JavaScript+OR+How to find the shortest
							path in a weighted undirected graph using Dijkstra's algorithm in Java+OR+How to implement a bucket sort for integers in
							C+++OR+How to find the maximum sum subarray with at least one element in an array in Python+OR+How to implement a shell sort
							with a gap sequence in Java+OR+How to find the longest common substring of two strings in JavaScript+OR+How to implement a
							breadth-first search on a graph using a queue in Python+OR+How to find the minimum spanning tree of a graph using Prim's
							algorithm in Java+OR+How to implement a quickselect algorithm to find the kth element in an unsorted array in C+++OR+How
							to find the minimum number of jumps to reach the end of an array in JavaScript+OR+How to implement a radix sort for integers
							in Python+OR+How to find the maximum sum path between two leaves of a binary tree in Java+OR+How to implement a binary
							search tree deletion using the minimum node in C+++OR+How to find the longest common prefix of multiple strings in Python
							+OR+How to implement a shell sort with an insertion sort fallback in JavaScript+OR+How to find the shortest path in a
							weighted directed graph using Bellman-Ford algorithm in Java+OR+How to implement a top-down splay tree in C++'''

            keywords1 += "+OR+" + keywords2
            
            url = f'https://www.google.com/search?q=intext%3A%22{query}%22+{keywords1}&start={start}&num={num_results}'
            
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

                    # check if the search result URL belongs to Google's own GUI
                    if 'google.com' not in parsed_url.netloc:
                        results.append((title, url))
            context = {
                'query': query,
                'results': results
            }
            return render(request, 'search/results.html', context)
        except:
            error = 'An error occurred while searching. Please try again later.'
            context = {
                'error': error
            }
            return render(request, 'search/results.html', context)
    return render(request, 'search/index.html')









# def search_results(request):
#     query = request.GET.get('search')
#     if query:
#         try:
#             num_results = 10
#             start = 0
#             url = f'https://www.google.com/search?q={query}&start={start}&num={num_results}'
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
#                     url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
#                     if 'google.com' not in parsed_url.netloc:
#                         results.append((title, url))
#             context = {'query': query, 'results': results}
#             return render(request, 'search/results.html', context)
#         except:
#             error = 'An error occurred while searching. Please try again later.'
#             context = {'error': error}
#             return render(request, 'search/results.html', context)
#     else:
#         return render(request, 'search/index.html')








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
