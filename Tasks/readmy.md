1. need deap investigation glob for working with files
2. os,sys also

### Data Serialization Formats
1. [JSON (JavaScript Object Notation)](https://json.org/) is the serialization format that we'll use the most in this course.
  - ````
     import json
     with open('people.json', 'w') as people_json:
       json.dump(people, people_json, indent=2)````
 This code uses the json.dump() function to serialize the people object into a JSON file. The contents of the file will look something like this: 
 - https://docs.python.org/3/library/json.html#py-to-json-table 
2. [YAML (Yet Another Markup Language)](https://yaml.org/) has a lot in common with JSON. They’re both formats that can be easily understood by a human when looking at the contents. In this example, we’re using the yaml.safe_dump() method to serialize our object into YAML:  
 
-
 ```` 
 import yaml
 with open('people.yaml', 'w') as people_yaml
   yaml.safe_dump(people, people_yaml)
   ````
  ### The Python Requests Library
  - The [Python Requests library](https://requests.readthedocs.io/) makes it super easy to write programs that send and receive HTTP
  - make very simple HTTP connections using Python objects, and then send and receive messages using the methods of those objects. Let's look at an example:  
  ````
  >>> import requests
  >>> response = requests.get('https://www.google.com')
  ````
  [requests.Response](https://requests.readthedocs.io/en/master/api/#requests.Response)
  ### Useful Operations for Python Requests
-  First, how do we know if a request we made got a successful response? You can check out the value of [Response.ok](https://requests.readthedocs.io/en/master/api/#requests.Response.ok), which will be True if the response was good, and False if it wasn't.  
``>>> response.ok``
``True``

Now, keep in mind that this will only tell you if the web server says that the response successfully fulfilled the request. The response module can’t determine if that data that you got back is the kind of data that you were expecting. You'll need to do your own checking for that!
If the boolean isn’t specific enough for your needs, you can get the [HTTP response code](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) that was returned by looking at [Response.status_code](https://requests.readthedocs.io/en/master/api/#requests.Response.ok):  
``>>> response.status_code``
``200``
- To write maintainable, stable code, you’ll always want to check your responses to make sure they succeeded before trying to process them further. For example, you could do something like this:  
````
response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))
````
But you don't really need to do that. Requests has us covered here, too! We can use the [Response.raise_for_status()](https://requests.readthedocs.io/en/master/api/#requests.Response.raise_for_status) method, which will raise an HTTPError exception only if the response wasn’t successful.  
````
response = requests.get(url)
response.raise_for_status()
````
### HTTP GET and POST Methods
HTTP supports several HTTP methods, like GET, POST, PUT, and DELETE. We're going to spend time on the two most common HTTP requests: GET and POST.
The [HTTP GET method](https://tools.ietf.org/html/rfc7231#section-4.3.1), of course, retrieves or **gets** the resource specified in the URL. By sending a GET request to the web server, you’re asking for the server to GET the resource for you. When you’re browsing the web, most of what you’re doing is using your web browser to issue a whole bunch of GET requests for the text, images, videos, and so forth that your browser will display to you.
A GET request can have **parameters***. Have you ever seen a URL that looked like this?  
``https://example.com/path/to/api/cat_pictures?search=grey+kitten&max_results=15``
The question mark separates the URL resource from the resource's parameters. These parameters are one or more key-value pairs, formatted as a query string. In the example above, the search parameter is set to "grey+kitten", and the max_results parameter is set to 15.

But you don't have to write your own code to create an URL like that one. With requests.get(), you can provide a dictionary of parameters, and the Requests module will construct the correct URL for you!  
````
>>> p = {"search": "grey kitten",
...      "max_results": 15}
>>> response = requests.get("https://example.com/path/to/api", params=p)
>>> response.request.url
'https://example.com/path/to/api?search=grey+kitten&max_results=15'
````
You might notice that using parameters in Requests is yet another form of data serialization. Query strings are handy when we want to send small bits of information, but as our data becomes more complex, it can get hard to represent it using query strings. 
An alternative in that case is using the [HTTP POST method](https://tools.ietf.org/html/rfc7231#section-4.3.3). This method sends, or posts, data to a web service. Whenever you fill a web form and press a button to submit, you're using the POST method to send that data back to the web server. This method tends to be used when there's a bunch of data to transmit.
In our scripts, a POST request looks very similar to a GET request. Instead of setting the params attribute, which gets turned into a query string and appended to the URL, we use the data attribute, which contains the data that will be sent as part of the POST request.  
````
>>> p = {"description": "white kitten",
...      "name": "Snowball",
...      "age_months": 6}
>>> response = requests.post("https://example.com/path/to/api", data=p)
````
Let's check out the generated URL for this request:  
````
>>> response.request.url
'https://example.com/path/to/api'
````
See how much simpler the URL is on this POST now? Where did all of the parameters go? They’re part of the body of the HTTP message. We can see them by checking out the body attribute.  
````
>>> response.request.body
'description=white+kitten&name=Snowball&age_months=6'
````
Ah, ha! There they are!

So, if we need to send and receive data from a web service, we can turn our data into dictionaries and then pass that as the data attribute of a POST request.

Today, it's super common to send and receive data specifically in JSON format, so the Requests module can do the conversion directly for us, using the json parameter.  
````
>>> response = requests.post("https://example.com/path/to/api", json=p)
>>> response.request.url
'https://example.com/path/to/api'
>>> response.request.body
b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 
````
And that's it for our brief introduction to the Requests module. If you want to learn more, feel free to work through the [Requests Quickstart](https://requests.readthedocs.io/en/master/user/quickstart/). 
