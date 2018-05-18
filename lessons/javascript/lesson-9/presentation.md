# Rest APIs and Ajax

---
Welcome back! In this lesson we'll get your hands dirty with using Rest APIs
and Ajax.
***********************************************************************
## APIs

* A - Application
* P - Programming
* I - Interface

---
What are APIs? The acronym stands for Application Programming Interface.

Given that there is a piece of software that someone made, and that they
want to make it available to other software developers to use in some way
within their own programs. An Application Programming Interface --- or API
--- is the way in which they've prescribed for other developers to use
that software.
***********************************************************************
![API](./lessons/javascript/lesson-9/images/controls.png)

---
Suppose this is a black box that does something useful. The API for this
black box is:

* the display panel on the box
* the buttons on the box
* the knob on the the box, and
* the sliders on the box

All of those things are the black box's interface --- allowing a user
to interact with it and use it.
***********************************************************************
## Different Types of APIs

* jQuery API
* JavaScript API
* iOS API
* Android API
* Java API

---
There are many different types of APIs, and you've actually used some of them
before. In particular, jQuery has an API, and you have been using it ever
since you started using jQuery. JavaScript itself has an API as well, which
encompasses the functions, methods, and properties you commonly use such as
array's `push` and `slice` methods, and string's `split` method and `length`
property.

If you write apps for iOS or Android based devices, you'll have to learn
their API. If you learn Java or another programming language, you'll have
learn their API.
***********************************************************************
## Different Types of APIs

* jQuery API
* JavaScript API
* iOS API
* Android API
* Java API
* [[[Rest APIs]]]

---
In this lesson, we'll focus on Rest APIs. These
are APIs that are made available over the web.
***********************************************************************
# What is Rest?

---
Rest stands for *Representation State Transfer*, and is an way (or style)
of designing, building, and using APIs based on the design of HTTP.
***********************************************************************
# What is HTTP?

---
What is HTTP? HTTP is the protocol your web browser uses to communicate
with the world wide web. You may have notice that web addresses (URLs) all
start with the letters `http` or `https`.
For example: `https://google.com` is the URL that is used to request
the front page of google.com.

`https` is the the secure version of `http`. All websites which
have secure user logins use `https` in favor of `http`. But conceptually
they are the same.
***********************************************************************
![Google](./lessons/javascript/lesson-9/images/google.png)

---
When you put `https://google.com` into the web address bar of your browser
and hit ENTER, you browser sends a request to a *server*
at Google Headquarters. *Server* is a term you'll hear a lot --- it is
a computer whose primary purpose is to serve you information.

When the server receives your request, it will send a response back to
your browser, telling it how to display the Google front page for you.
***********************************************************************
# The Network Panel

---
Chrome's Developer Tools (DevTools for short) has a feature for watching
the HTTP requests that have been made as a result of loading any web page.
***********************************************************************

![Network Panel](./lessons/javascript/lesson-9/images/www.png)

---
This is the first ever web page created for the World Wide Web. We'll
use the *network panel* to look the HTTP request that is used to retrieve it.

Follow along by going to <http://info.cern.ch/hypertext/WWW/TheProject.html>.
***********************************************************************
![Network Panel](./lessons/javascript/lesson-9/images/www-network-panel.png)

---
This is the network panel. You can access it by

1. Opening the Chrome DevTools by either
    * Using a shortcut key, or
    * Right-clicking on any DOM element and then selecting "Inpect"
2. Click on the "Network" tab.

Please follow along. You should see something like this.
***********************************************************************
![Network Panel](./lessons/javascript/lesson-9/images/www-network-panel.png)

---
Because the Network Panel does not track HTTP requests until you activate it
(by opening it), you won't see any requests here, until you reload this page.

Go ahead and reload the page.
***********************************************************************
![Network Panel](./lessons/javascript/lesson-9/images/www-network-panel-2.png)

---
Once you reload the page, you should see the network requests in a table
like this.

This table contains a line for each HTTP request. For this web page,
there is only one request.

It has a number of columns:

* Name - this is the URL (or address) of the file requested
* Status - this *HTTP status* number tells us if the request worked or not.
200 means it worked.
* Type - what is the type of the document that was returned? This is a document,
but we'll also see other types, such as stylesheet (CSS), script (JS), and xhr (JSON).
* Initiator - this is the file that initiated this request. It is "other" here
because it is the user who initiated this request.
* Size - this is the size of the HTML file that was returned
* Time - how long did it take this request to complete?
* Waterfall - this is a detailed timing diagram of the request used for performance
tuning purposes

I know there is a lot of information here, don't worry about completely
understanding all of it at this point.
***********************************************************************
![Network Panel](./lessons/javascript/lesson-9/images/www-network-panel-2.png)

---
You can get more detail about a request by clicking on the line. Go ahead
and click on this line,
***********************************************************************
![Network Panel](./lessons/javascript/lesson-9/images/www-network-panel-3.png)

---
and you should see this detail panel, where you can see the full response to
the request within the *Response Tab*. It contains the HTML file that is displayed in the browser.
***********************************************************************
![Network Panel](./lessons/javascript/lesson-9/images/www-network-panel-4.png)

---
Another tab you should pay attention to is the *Headers Tab*. This tab is more
about the request. It contains the request URL, request method, status code,
request headers, and more. Although we won't go into detail about what of
these mean right now, they will come into play later.
***********************************************************************
![Network Panel](./lessons/javascript/lesson-9/images/tobyho.png)

---
Let's look at a different example: my home page: <http://tobyho.com>. Now, open up
the network panel, and then reload the page...
***********************************************************************
![Network Panel](./lessons/javascript/lesson-9/images/tobyho-network-panel.png)

---
You should see this.

Notice that there are many more HTTP requests in this table. The types of the
resources requested include:

* document - the HTML page itself
* stylesheets - the CSS files that are referenced by the HTML page. Each `<link href="...">` tag
initiates an HTTP request in order to retrieve a CSS file
* scripts - the JS files that are referenced by the HTML page. Each `<script src="...">` tag initiates an HTTP request in order to retrieve teh JS file
* gif and png - these are images used in the HTML page. Each `<img src="...">` tag initiates an HTTP request to retrieve the image file

Please follow along. Look through these request lines and click on some of them
to see what their response looks like by looking at the "Response" tab. And then
look at what the request looks like by looking at the "Headers" tab.
***********************************************************************
# Ajax

---
Now that you have some familiarity with HTTP requests, let's deeper into
Ajax.

Ajax stands for *Asynchronous JavaScript and XML* --- which at this point
is a misnomer because most developers now use JSON in favor of XML. Still,
the term Asynchronous JavaScript and XML does not tell you very much about
what Ajax means, other than that it has something to do with JavaScript.
***********************************************************************

![Ajax](./lessons/javascript/lesson-9/images/ajax.png)

---

Ajax is when you write JavaScript code to initiate an HTTP request, but
rather than to fetch a stylesheet or a JavaScript file or an image file,
you initiate the request in order to fetch data, or to initiate an action
to be performed on the server.

***********************************************************************
![Ajax](./lessons/javascript/lesson-9/images/google-suggest-1.png)

---
Here is a concrete example. You are on Google's search page, and you
start to type in your search query.

Google has a feature called "Google Suggest", where even before you
finish typing your query, it shows you some suggestions based on your
unfinished sentence.
***********************************************************************
![Ajax](./lessons/javascript/lesson-9/images/google-suggest-2.png)

---
This is how it works:

1. There is a JavaScript event handler function on the page which executes
whenever you type into the search box.
2. That code initiates an Ajax request, sending your partial sentence
along with it.
***********************************************************************
![Ajax](./lessons/javascript/lesson-9/images/google-suggest-3.png)

---
This is how it works:

1. There is a JavaScript event handler function on the page which executes
whenever you type into the search box.
2. That code initiates an Ajax request, sending your partial sentence
along with it.
3. The Google server receives that request and sends back a response
containing an array of suggestions that are well suited for the partial
sentence that was sent in.
***********************************************************************
![Ajax](./lessons/javascript/lesson-9/images/google-suggest-4.png)

---
This is how it works:

1. There is a JavaScript event handler function on the page which executes
whenever you type into the search box.
2. That code initiates an Ajax request, sending your partial sentence
along with it.
3. The Google server receives that request and sends back a response
containing an array of suggestions that are well suited for the partial
sentence that was sent in.
4. The JavaScript code receives the array of suggestions, and then dynamically
generates new DOM elements that represent a list of the suggestions, and
displays them on the screen.
***********************************************************************
## jQuery Ajax
## and `XMLHttpRequest` Object

---
In this lesson, we will cover how to use jQuery to make Ajax requests.

In the wild, you may also hear about the `XMLHttpRequest` object.
The `XMLHttpRequest` is the native browser API that enables you to making
Ajax calls. The jQuery code you will write in essence asks jQuery to utilize
the `XMLHttpRequest` object to make the request for you.

It is possible to access the `XMLHttpRequest` object directly. The code
to do that is a bit more verbose than asking jQuery to do it for you.
***********************************************************************
## Ajax with jQuery

```js
var url = "http://someapiyouareusing.com/api/getdata";
$.getJSON(url, function(data) {
  // You have access to the data!!
});
```

---
This is the simplest Ajax call you can make with jQuery. It makes an HTTP
request to the url location specified, and it expects the data to come back in
JSON format.
***********************************************************************
## Ajax with jQuery

```js
var url = [["http://someapiyouareusing.com/api/getdata"]][[URL(location) of the data]];
$.getJSON(url, function(data) {
  // You have access to the data!!
});
```

---
This code assumes that you already know the URL (location) from which you'll
need to get the data, and that it is stored in a `url` variable.

For this example, we are using a fake, placeholder URL address.
***********************************************************************
## Ajax with jQuery

```js
var url = "http://someapiyouareusing.com/api/getdata";
[[$.getJSON]][[getJSON method of $]](url, function(data) {
  // You have access to the data!!
});
```

---
To initiate the request, we are calling the `getJSON` method of the `$` object.
***********************************************************************
## Ajax with jQuery

```js
var url = "http://someapiyouareusing.com/api/getdata";
[[$.getJSON]][[getJSON method of $]](url, function(data) {
  // You have access to the data!!
});
```

---
But wait! `$` is a function, right???!!!

Yes, but it turns out that in JS, functions are also objects, and as such,
they can also have methods.

![Head explode](./lessons/javascript/lesson-9/images/mindblown.gif)
***********************************************************************
## Ajax with jQuery

```js
var url = "http://someapiyouareusing.com/api/getdata";
$.getJSON(url, function(data) {
  // You have access to the data!!
});
```

---
Anyhow, we are passing to the `getJSON` method two arguments.
***********************************************************************
## Ajax with jQuery

```js
var url = "http://someapiyouareusing.com/api/getdata";
$.getJSON([[url]][[URL to get data]], function(data) {
  // You have access to the data!!
});
```

---
The first argument is the URL,
***********************************************************************
## Ajax with jQuery

```js
var url = "http://someapiyouareusing.com/api/getdata";
$.getJSON(url, [[function(data) {
  // You have access to the data!!
}]][[Callback function]]);
```

---
and the second argument is a function. This function is commonly called a
*callback function*, or simply *callback*.

This function will be called when the response comes back, and its first
parameter --- `data` --- will receive the data that is sent back by the
response.
***********************************************************************
## Ajax with jQuery

```js
var url = "http://someapiyouareusing.com/api/getdata";
$.getJSON(url, function(data) {
  // You have access to the data!!
  console.log("This is the data", data);
});
```

---

Within the function, you may use `console.log` to print out the data to see
what it looks like. It is usually a data structure, either an object or an
array at the top level, and may contain nested objects and or arrays.

Ultimately, you'll probably want to use the data to dynamically generate
DOM elements and update the display of the page in some way.
***********************************************************************
![Giphy Developers Page](./lessons/javascript/lesson-9/images/giphy-developer-page.png)

---
With the theory out of the way, let's do something real. We'll use the Giphy
API as an example.

Giphy is an online repository of animated gifs. Animated gifs
are images that are commonly used on the internet as [memes](https://en.wikipedia.org/wiki/Meme)
because they can contain short and funny animations.

In fact, I've already used an animated gif in this lesson:

![Head explode](./lessons/javascript/lesson-9/images/mindblown.gif)
***********************************************************************
![Giphy Developers Page](./lessons/javascript/lesson-9/images/giphy-developer-page.png)

---
Giphy provides an API for web developers to be able to incorporate any of
the Giphy's library of animated gifs into their own web pages.

With the API, you can

* Get a random animate gif and display it on your own page
* Search for animate gifs using a search query, and display it on your own page
* Translate a word or a phrase into an animate gif, and display it on your own page
* and more...
***********************************************************************
## Sign Up

![Giphy Developers Page](./lessons/javascript/lesson-9/images/giphy-developer-page.png)

---
In order to do any of these things, you first need to sign up for an account on
Giphy. To do that, go to <https://developers.giphy.com>, and click the "Log In"
button on the top right corner.
***********************************************************************
## Sign Up

![Giphy Developers Page](./lessons/javascript/lesson-9/images/sign-up.png)

---
If you already have an account, log in.

If you don't already have an account, then click "Join Giphy!".
***********************************************************************
![Giphy Developers Page](./lessons/javascript/lesson-9/images/create-an-app.png)

---
Once you've signed up and logged in. You'll need to "create an app".
***********************************************************************
![Giphy Developers Page](./lessons/javascript/lesson-9/images/create-an-app-2.png)

---
Pick an app name and a description of what your app is. You may make this
generic. I chose to call the app "Playground", and the description
"Play with the API". Now click on "Create New App".
***********************************************************************
![Giphy Developers Page](./lessons/javascript/lesson-9/images/create-an-app-3.png)

---
You should see something like this, and in particular you'll see an Api Key.
I have smeared out mine so that you cannot steal mine. But you'll need to
use this when you are writing your code.
***********************************************************************
## Get a Random Gif

```js
var url = "https://api.giphy.com/v1/gifs/random?api_key=YOUR_API_KEY";
$.getJSON(url, function(data) {
  console.log("This is the data", data);
});
```

---
Now we'll use this code to get a random Gif from Giphy. Create an HTML
page, use a `<script>` tag to add jQuery to it, and then put in this JavaScript.

Replace `YOUR_API_KEY` with the API key that you were given in the last step.

Open the page, and open up the JavaScript console.
***********************************************************************
## Get a Random Gif

![Ajax Result](./lessons/javascript/lesson-9/images/ajax-result.png)

---
This is what you should see.
***********************************************************************
## Get a Random Gif

![Ajax Error](./lessons/javascript/lesson-9/images/ajax-error.png)

---
If you see this instead, that means you haven't put in your own API key. Do
that now.
***********************************************************************
## Get a Random Gif

![Ajax Result](./lessons/javascript/lesson-9/images/ajax-result.png)

---
Now, you can expand and collapse the data you see here in the console by
clicking on the little triangle next to it.
***********************************************************************
## Get a Random Gif

![Ajax Result](./lessons/javascript/lesson-9/images/ajax-result-2.png)

---
This shows that data is an object at the top level that has 2 keys: `data`,
and `meta`. Let's expand the `data` key...
***********************************************************************
## Get a Random Gif

![Ajax Result](./lessons/javascript/lesson-9/images/ajax-result-3.png)

---
*That's* a lot of data! If you scroll through this big object, you'll see that
there are many URLs for gifs, and based on the names of those keys, such as
`fixed_width_small_url`, and `fixed_height_small_still_url`, we can infer
that there are many different versions of that animated gif with different
properties. The most straightforward one seems to be `image_url`.
***********************************************************************
## Get a Random Gif

![Giphy Ajax](./lessons/javascript/lesson-9/images/giphy-ajax.png)

---

Now, switch to the network panel. If something goes wrong with an Ajax request,
the first thing you should check is the network panel.

Here, you should see the HTTP request with the URL of `random?api_key=...`.
That's our Ajax request. Click on it...

***********************************************************************
## Get a Random Gif: Network Panel

![Giphy Ajax](./lessons/javascript/lesson-9/images/giphy-ajax-headers.png)

---
This is the headers tab, where you can see the request URL.
***********************************************************************
## Get a Random Gif: Network Panel

![Giphy Ajax](./lessons/javascript/lesson-9/images/giphy-ajax-response.png)

---
This is the response tab, where the response is text in JSON format. It is
in one long line though, which isn't very readable.
***********************************************************************
## Get a Random Gif: Network Panel

![Giphy Ajax](./lessons/javascript/lesson-9/images/giphy-ajax-preview.png)

---
Switch to the preview tab instead, and you'll get this expandable tree ---
similar to what we had in the console --- for you to examine and navigate
the shape of the data.
***********************************************************************
## Get a Random Gif: JSON

```json
{
  "data": {
    "type": "gif",
    "id": "5nx8ts94S8kwg",
    "slug": "imgur-servers-5nx8ts94S8kwg",
    "url": "https://giphy.com/gifs/imgur-servers-5nx8ts94S8kwg",
    "bitly_gif_url": "https://gph.is/1kxzLzo",
    "bitly_url": "https://gph.is/1kxzLzo",
    "embed_url": "https://giphy.com/embed/5nx8ts94S8kwg",
    "username": "",
    "source": "https://www.reddit.com/r/gifs/comments/3rpa03/imgur_servers_as_of_late/",
    "content_url": "",
    "source_tld": "www.reddit.com",
    "source_post_url": "https://www.reddit.com/r/gifs/comments/3rpa03/imgur_servers_as_of_late/",
    "is_sticker": 0,
    "import_datetime": "2015-11-06 00:56:39",
    "trending_datetime": "0000-00-00 00:00:00",
    "images": {...},
    "title": "servers GIF",
    "image_original_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.gif",
    "image_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.gif",
    "image_mp4_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.mp4",
    "image_frames": "4",
    "image_width": "500",
    "image_height": "320",
    "fixed_height_downsampled_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/200_d.gif",
    "fixed_height_downsampled_width": "313",
    "fixed_height_downsampled_height": "200",
    "fixed_width_downsampled_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/200w_d.gif",
    "fixed_width_downsampled_width": "200",
    "fixed_width_downsampled_height": "128",
    "fixed_height_small_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/100.gif",
    "fixed_height_small_still_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/100_s.gif",
    "fixed_height_small_width": "156",
    "fixed_height_small_height": "100",
    "fixed_width_small_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/100w.gif",
    "fixed_width_small_still_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/100w_s.gif",
    "fixed_width_small_width": "100",
    "fixed_width_small_height": "64",
    "caption": ""
  },
  "meta": {
    "status": 200,
    "msg": "OK",
    "response_id": "5aff0fd44b2e764a511653bd"
  }
}
```

---
The JSON data looks like this. This is a lot, and the `images` key contains
another nested object that contains even more detailed information about each
version of the image --- I omitted it for simplicity.

But in reality, if you simply want to render
an image, all we need is one URL.
***********************************************************************
## Get a Random Gif: JSON

```json
{
  "data": {
    "type": "gif",
    "id": "5nx8ts94S8kwg",
    "slug": "imgur-servers-5nx8ts94S8kwg",
    ...
    "title": "servers GIF",
    "image_original_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.gif",
    "image_url": [[["https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.gif"]]],
    "image_mp4_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.mp4",
    "image_frames": "4",
    "image_width": "500",
    "image_height": "320",
    ...
  },
  "meta": {...}
}
```

---

Let's use this URL under the `image_url` key.
***********************************************************************
## Get a Random Gif: JSON

```js
[[[var data]]] = {
  "data": {
    "type": "gif",
    "id": "5nx8ts94S8kwg",
    "slug": "imgur-servers-5nx8ts94S8kwg",
    ...
    "title": "servers GIF",
    "image_original_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.gif",
    "image_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.gif",
    "image_mp4_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.mp4",
    "image_frames": "4",
    "image_width": "500",
    "image_height": "320",
    ...
  },
  "meta": {...}
}
```

---
Let's suppose that we had a variable called `data` which contains this top
level object. How can we access this URL?

Try to work this out on your own. Then see the solution on the next slide.
***********************************************************************
## Get a Random Gif: JSON

```js
var data = {
  [["data"]][[Key]]: [[{
    "type": "gif",
    "id": "5nx8ts94S8kwg",
    "slug": "imgur-servers-5nx8ts94S8kwg",
    ...
    "title": "servers GIF",
    "image_original_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.gif",
    "image_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.gif",
    "image_mp4_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.mp4",
    "image_frames": "4",
    "image_width": "500",
    "image_height": "320",
    ...
  }]][[Value]],
  "meta": {...}
}
```

---
First, we need to descend into this tree of objects and go into the object
within the `data` key. This is done by accessing that the `data` key on the
`data` variable: `data.data`.
***********************************************************************
## Get a Random Gif: JSON

```js
var data = {
  "data": {
    "type": "gif",
    "id": "5nx8ts94S8kwg",
    "slug": "imgur-servers-5nx8ts94S8kwg",
    ...
    "title": "servers GIF",
    "image_original_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.gif",
    [["image_url"]][[Key]]: [["https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.gif"]][[Value]],
    "image_mp4_url": "https://media2.giphy.com/media/5nx8ts94S8kwg/giphy.mp4",
    "image_frames": "4",
    "image_width": "500",
    "image_height": "320",
    ...
  },
  "meta": {...}
}
```

---
Then we descend further into the `image_url` within that nested object:
`data.data.image_url`. This is what we need to use in the callback function.
***********************************************************************
## Get a Random Gif

```js
var url = "https://api.giphy.com/v1/gifs/random?api_key=YOUR_API_KEY";
$.getJSON(url, function(data) {
  console.log("This is the data", data);
[[[  var url = data.data.image_url;
  console.log("This is the url", url);]]]
});
```

---
Add these 2 lines to the JS. Reload the page, it should now print out the
URL of the image.

Next, let's render that image on the page.
***********************************************************************
## Get a Random Gif

```js
var url = "https://api.giphy.com/v1/gifs/random?api_key=YOUR_API_KEY";
$.getJSON(url, function(data) {
  console.log("This is the data", data);
  var url = data.data.image_url;
  console.log("This is the url", url);
[[[  var imageElement = "<img src='" + url + "'>";
  $("body").append(imageElement);]]]
});
```

---
Add these 2 lines. They will

1. Generate the HTML markup for a new `<img>` element.
2. Append that element to the body of the page.

Reload this page and you should see a random animate gif!!! Each time
you reload, you will see a different animation.
***********************************************************************
## Get a Random Gif: Challenge!

```js
var url = "https://api.giphy.com/v1/gifs/random?api_key=YOUR_API_KEY";
$.getJSON(url, function(data) {
  console.log("This is the data", data);
  var url = data.data.image_url;
  console.log("This is the url", url);
  var imageElement = "<img src='" + url + "'>";
  $("body").append(imageElement);
});
```

---
Now, time for a challenge!

1. Add a "Random!" button to your HTML page.
2. Modify this program so that every time you click the "Random!" button,
a new random animated gif is added to the page.

Go to the next slide for the solution.
***********************************************************************
## Solution

```html
<button id="random-button">Random!</button>
```

```js
$("#random-button").on("click", function() {
  var url = "https://api.giphy.com/v1/gifs/random?api_key=YOUR_API_KEY";
  $.getJSON(url, function(data) {
    console.log("This is the data", data);
    var url = data.data.image_url;
    console.log("This is the url", url);
    var imageElement = "<img src='" + url + "'>";
    $("body").append(imageElement);
  });
});
```
---
This is the solution. In order to generate the random image on the event of a
click, we've simply moved the existing JS code into a click event handler for
the button.

Awesome! You've had your first taste of using a 3rd party Rest API to expand
your capabilities as a developer! But there's more!
***********************************************************************
## Query Parameters

```js
var url = "https://api.giphy.com/v1/gifs/random?api_key=YOUR_API_KEY";
```

---
Before we get fancy, we'll need to learn a bit about query parameters, and
an easier way of working with them.
***********************************************************************
## Query Parameters

```js
var url = "https://api.giphy.com/v1/gifs/random[[[?]]]api_key=YOUR_API_KEY";
```

---
As you may have noticed, there is a question mark in this URL.
***********************************************************************
## Query Parameters

```js
var url = "[[https://api.giphy.com/v1/gifs/random]][[Locates an API Endpoint]]?api_key=YOUR_API_KEY";
```

---
The string to the left of the `?` specifies an API endpoint. You
can think of this as a method (.i.e. string's `split()` method). Let's
say this is the "random" method.
***********************************************************************
## Query Parameters

```js
var url = "https://api.giphy.com/v1/gifs/random?[[api_key=YOUR_API_KEY]][[query parameters]]";
```

---
To the right of the `?` specifies the query parameters that are sent
to that end point. You can think of this as the arguments that are passed
to a method (.i.e. the `","` in `aString.split(",")`).
***********************************************************************
## Query Parameters

```
api_key=YOUR_API_KEY
```

---
So these are our query parameters. Query parameters are like
dictionaries/objects in that they are key/value pairs. This one says
that the `api_key` parameter takes on the value of `YOUR_API_KEY` (which
  again, you'll need to substitute in your own).
***********************************************************************
## Query Parameters

```
api_key=YOUR_API_KEY&tag=burrito&rating=g
```

---
It turns that, based on their [documentation page](https://developers.giphy.com/docs/),
the random gif endpoint (`https://api.giphy.com/v1/gifs/random`) supports more
query parameters, including: `tag` and `rating`. The documentation page listed
`burrito` as an example of `tag`, and `g` as an example of `rating`.

Based on that, we can query for random g-rated burrito animated gifs using
this query string.
***********************************************************************
## Query Parameters

```
[[[api_key=YOUR_API_KEY]]]&[[[tag=burrito]]]&[[[rating=g]]]
```

---
Note that we have 3 separate key/value pairs in this query string.
***********************************************************************
## Query Parameters

```
api_key=YOUR_API_KEY[[[&]]]tag=burrito[[[&]]]rating=g
```

---
And that they are separated by the `&` character.
***********************************************************************
## Query Parameters

```js
var url = "https://api.giphy.com/v1/gifs/random?api_key=YOUR_API_KEY&tag=burrito&rating=g";
```

---
This is what that code would look like. If you want the tag and/or the rating
to be based on user input, you'd need to use string concatenation to
piece this long URL string together.
***********************************************************************
## Query Parameters

```js
var tag = $("#tag-input").val();
var rating = $("#rating-select").val();
var url = "https://api.giphy.com/v1/gifs/random?api_key=YOUR_API_KEY&tag=" +
  tag + "&rating=" + rating;
```

---
Something like this. And this is a little ungainly. But there is a nicer way...
***********************************************************************
## Query Parameters

```js
var tag = $("#tag-input").val();
var rating = $("#rating-select").val();
var url = "https://api.giphy.com/v1/gifs/random";
var params = [[{
  api_key: "YOUR_API_KEY",
  tag: tag,
  rating: rating
}]][[Query parameters as object]];
$.getJSON(url, params, function(data) {
  // You have data available here!
});
```

---
You can encode all your query parameters as an object, and then
***********************************************************************
## Query Parameters

```js
var tag = $("#tag-input").val();
var rating = $("#rating-select").val();
var url = "https://api.giphy.com/v1/gifs/random";
var params = {
  api_key: "YOUR_API_KEY",
  tag: tag,
  rating: rating
};
$.getJSON(url, [[params]][[extra argument]], function(data) {
  // You have data available here!
});
```

---
Pass it in as an extra, second argument of the `getJSON` method.

This approach --- although is more verbose --- affords to be so because
it is more readable.
***********************************************************************
## Summary

* APIs
* HTTP
* Network Panel
* Ajax
* The Giphy API
* Query Parameters

---
This is what you've learned in this lesson. Phew! That was a lot.
***********************************************************************
## Homework

[Enjoy your Homework](https://gist.github.com/airportyh/2a6cf9c645c870386586600db8e86692)
