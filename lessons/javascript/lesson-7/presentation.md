# jQuery 401
## DOM Traversal and Componentization

---
Hello! Welcome back. In this lecture we'll cover how to do DOM
traversal with jQuery and how to use that to implement
UI components.
***************************************************************
## DOM Traversal Methods

* `$(...).parent()` - get the parent element(s) of the selected element(s)
* `$(...).closest()` - get the closest ancestor element(s) of the
  selected element(s)
* `$(...).find()` - find one or more child or descendent element(s) of the selected element(s)

---
There are the methods we'll cover.
***************************************************************
## `.parent()`

```html
<ul id="fruits">
  [[[<li id="apple">Apple</li>]]]
  <li id="banana">Banana</li>
  <li id="kiwi">Kiwi</li>
</ul>
```

```js
[[[$("#apple")]]]
```

---
We'll start with `.parent()`.

You can get the parent element of an element by using the `.parent()`
method.

Let's say we use the ID selector `#apple` to find the
`<li>` for Apple.
***************************************************************
## `.parent()`

```html
[[[<ul id="fruits">]]]
  <li id="apple">Apple</li>
  <li id="banana">Banana</li>
  <li id="kiwi">Kiwi</li>
[[[</ul>]]]
```

```js
[[[$("#apple").parent()]]]
```

---
If you call the `.parent()` method on that list item,
you would get it's containing `<ul>` element: `#fruits`.
***************************************************************
## `.parent()`

```html
[[[<ul id="fruits">]]]
  <li id="apple">Apple</li>
  <li id="banana">Banana</li>
  <li id="kiwi">Kiwi</li>
[[[</ul>]]]
```

```js
$("#apple").parent([["#fruits"]][[Optional CSS selector]])
```

---
You can optionally give an argument to the `.parent()` method.
It is a CSS selector acts like a filter. It will make `.parent()`
return an element only if the parent in question matches
that selector.
***************************************************************
## `.parent()`

```html
<ul id="fruits">
  <li id="apple">Apple</li>
  <li id="banana">Banana</li>
  <li id="kiwi">Kiwi</li>
</ul>
```

```js
$("#apple").parent([["#nuts"]][[No match]])
```

---
For example, if we tried to match the `#nuts` selector for this
CSS selector, you'd get nothing returned.
***************************************************************
## `.closest()`

```html
[[[<ul id="fruits">]]]
  <li id="apple">Apple</li>
  <li id="banana">Banana</li>
  <li id="kiwi">Kiwi</li>
[[[</ul>]]]
```

```js
$("#apple")[[[.closest("ul")]]]
```

---
The `.closest()` method is for finding an element's closest
ancestor. It is like using the `.parent()` method
with a CSS selector, except that it could find any ancestor,
as long as it matched the selector.

In this example, the closest ancestor matching the `ul` selector
happens to be the immediate parent of `#apple`: `#fruits`.
***************************************************************
## `.closest()`

```html
<ul id="foods">
  <li>
    Carbohydrates
    <ul id="carbohydrates">
      <li>bread</li>
      <li>pasta</li>
      <li>rice</li>
    </ul>
  </li>
  <li>
    Fruits
    [[[<ul id="fruits">]]]
      <li id="apple">Apple</li>
      <li id="banana">Banana</li>
      <li id="kiwi">Kiwi</li>
    [[[</ul>]]]
  </li>
</ul>
```

```js
$("#apple")[[[.closest("ul")]]]
```

---
With this structure in the HTML, `.closest("ul")` will
still return the `#fruits` element, because it is the closest
`ul` element which is an ancestor element of `#apple`.
***************************************************************
## `.closest()`

```html
<ul id="foods">
  <li>
    Carbohydrates
    <ul id="carbohydrates">
      <li>bread</li>
      <li>pasta</li>
      <li>rice</li>
    </ul>
  </li>
  <li>
    Fruits
    [[[<ul id="fruits">]]]
      <li id="apple">Apple</li>
      <li id="banana">Banana</li>
      <li id="kiwi">Kiwi</li>
    [[[</ul>]]]
  </li>
</ul>
```

```js
$("#apple").closest([[["#foods"]]])
```

---
If you changed the CSS selector to `#foods`, then `.closest()` method
will return the top level `#foods` element.
***************************************************************
## `.find()`

```html
<ul id="fruits">
  <li id="apple">Apple</li>
  <li id="banana">Banana</li>
  <li id="kiwi">Kiwi</li>
</ul>
```

```js
$("#fruits").find("li");
```

---
The `.find()` method is for finding child elements within the
selected element.
***************************************************************
## `.find()`

```html
<ul id="fruits">
  <li id="apple">Apple</li>
  <li id="banana">Banana</li>
  <li id="kiwi">Kiwi</li>
</ul>
```

```js
$("#fruits").find([["li"]][[CSS selector]]);
```

---
It also takes a CSS selector as its first argument.
***************************************************************
## `.find()`

```html
<ul id="fruits">
  [[[<li id="apple">Apple</li>]]]
  [[[<li id="banana">Banana</li>]]]
  [[[<li id="kiwi">Kiwi</li>]]]
</ul>
```

```js
[[$("#fruits").find("li");]][[Find li elements in #fruits]]
```

---
This statement would find all `<li>` elements within the
`#fruits` element.
***************************************************************
## `.find()`

```html
<ul id="foods">
  [[[<li>]]]
    Carbohydrates
    <ul id="carbohydrates">
      [[[<li>bread</li>]]]
      [[[<li>pasta</li>]]]
      [[[<li>rice</li>]]]
    </ul>
  [[[</li>]]]
  [[[<li>]]]
    Fruits
    <ul id="fruits">
      [[[<li>Apple</li>]]]
      [[[<li>Banana</li>]]]
      [[[<li>Kiwi</li>]]]
    </ul>
  [[[</li>]]]
</ul>
```

```js
$("#foods").find("li");
```

---
With this markup, this statement: `$("#foods").find("li");`
would return all of the `li` elements in this graph, including
the ones with children elements within them: Carbohydrates,
and Fruits.
***************************************************************
![Thumbs Up/Thumbs Down](./lessons/javascript/lesson-7/images/thumbs-up-thumbs-down.png)

---
We are going to make this thumbs up/thumbs down clicker. This is a simplified
version of the widget you'd see on social media websites. When the
thumbs up icon is clicked, the count goes up, and when the thumbs down icon
is clicked, the count goes down. It's that simple. Let's do it.
***************************************************************
## Font Awesome Icons

![Font Awesome](./lessons/javascript/lesson-7/images/fontawesome.png)

---
To make it easy to render those thumb icons, we'll use the [Font Awesome](https://fontawesome.com/)
font library. Go to <http://fontawesome.com> and click on "Get Started".
***************************************************************
## Font Awesome Icons

![Getting Started](./lessons/javascript/lesson-7/images/fontawesome-getting-started.png)

---
Then scroll down and you should see this section called "Use Font Awesome Free CDN".
Copy the `<link>` tag in the black box --- you may click on the clipboard
"Copy Code" icon to the right of it to copy in one click.
***************************************************************
## Font Awesome Icons

```html
<head>
  <title>Thumbs Up Thumbs Down</title>
  [[[<link rel="stylesheet"
  href="https://use.fontawesome.com/releases/v5.0.10/css/all.css"
  integrity="sha384-+d0P83n9kaQMCwj8F4RJB66tzIwOKmrdb46+porD/OvrJ+37WqIM7UoBtwHO6Nlg"
  crossorigin="anonymous">]]]
</head>
```

---
Paste that code into the `<head>` element of a test page, and you are
ready to use Font Awesome.
***************************************************************
## Font Awesome Icons

```html
<div id="thumb-up" class="far fa-thumbs-up"></div>
<div id="count">0</div>
<div id="thumb-down" class="far fa-thumbs-down"></div>
```

![Thumbs Up/Thumbs Down](./lessons/javascript/lesson-7/images/thumbs-up-thumbs-down-initial.png)

---
Now, we'll write this markup code to make the thumbs up thumbs down widget.
It should look like the image below. If it doesn't work, double check
your steps in setting up Font Awesome or ask your mentor for help.
***************************************************************
## Font Awesome Icons

```html
<div id="thumb-up" class="[[[far fa-thumbs-up]]]"></div>
<div id="count">0</div>
<div id="thumb-down" class="[[[far fa-thumbs-down]]]"></div>
```

![Thumbs Up/Thumbs Down](./lessons/javascript/lesson-7/images/thumbs-up-thumbs-down-initial.png)

---
To make the icons show up, all we had to do was to add these two specific Font
Awesome classes.
***************************************************************
## Font Awesome Icons

```html
<div id="thumb-up" class="[[[far]]] fa-thumbs-up"></div>
<div id="count">0</div>
<div id="thumb-down" class="[[[far]]] fa-thumbs-down"></div>
```

![Thumbs Up/Thumbs Down](./lessons/javascript/lesson-7/images/thumbs-up-thumbs-down-initial.png)

---

The first class is `far`, it tells Font Awesome that this is an element
for it to apply an icon to.

`far` stands for Font Awesome Regular. "Regular" is an option you can apply
to any icon and gives it a hollow look. The other option is `fas` for "Solid",
which gives the icon a solid look.
***************************************************************
## Font Awesome Icons

```html
<div id="thumb-up" class="far [[[fa-thumbs-up]]]"></div>
<div id="count">0</div>
<div id="thumb-down" class="far [[[fa-thumbs-down]]]"></div>
```

![Thumbs Up/Thumbs Down](./lessons/javascript/lesson-7/images/thumbs-up-thumbs-down-initial.png)

---
`fa-<Icon Name>` is the second class used. It specifies the icon to be displayed.
Here we've used the "Thumps Up" and "Thumps Down" icons, which in turn have
the `fa-thumbs-up` and `fa-thumbs-down` classes.

To see what other icons are available with Font Awesome, you can [browser
or search the entire list](https://fontawesome.com/icons?d=gallery).
***************************************************************
## Challenge!!!

```html
<div id="thumb-up" class="far fa-thumbs-up"></div>
<div id="count">0</div>
<div id="thumb-down" class="far fa-thumbs-down"></div>
```

---
Now, time for a challenge! Given this markup, write some jQuery
to increase the count by 1 when the `#thumb-up` icon is clicked,
and decrease by 1 when the `#thumb-down` icon is clicked.

Give it a go! See the next slide for the solution.
***************************************************************
## Solution

```html
<div id="thumb-up" class="far fa-thumbs-up"></div>
<div id="count">0</div>
<div id="thumb-down" class="far fa-thumbs-down"></div>
```

```js
$("#thumb-up").on("click", function() {
  var count = Number($("#count").text());
  $("#count").text(String(count + 1));
});

$("#thumb-down").on("click", function() {
  var count = Number($("#count").text());
  $("#count").text(String(count - 1));
});
```

---
This is the solution.
***************************************************************
## Solution

```html
<div id="thumb-up" class="far fa-thumbs-up"></div>
<div id="count">0</div>
<div id="thumb-down" class="far fa-thumbs-down"></div>
```

```js
[[[$("#thumb-up").on("click", function() {]]]
  var count = Number($("#count").text());
  $("#count").text(String(count + 1));
[[[});]]]

$("#thumb-down").on("click", function() {
  var count = Number($("#count").text());
  $("#count").text(String(count - 1));
});
```

---
First, we add an event handler to listen to click events on the `#thumb-up`
icon.
***************************************************************
## Solution

```html
<div id="thumb-up" class="far fa-thumbs-up"></div>
<div id="count">0</div>
<div id="thumb-down" class="far fa-thumbs-down"></div>
```

```js
$("#thumb-up").on("click", function() {
  var count = Number([[$("#count").text()]][[Get text of #count element]]);
  $("#count").text(String(count + 1));
});

$("#thumb-down").on("click", function() {
  var count = Number($("#count").text());
  $("#count").text(String(count - 1));
});
```

---
When `#thumb-up` is clicked, we first get the text off of the `#count` element,
***************************************************************
## Solution

```html
<div id="thumb-up" class="far fa-thumbs-up"></div>
<div id="count">0</div>
<div id="thumb-down" class="far fa-thumbs-down"></div>
```

```js
$("#thumb-up").on("click", function() {
  var count = [[[Number(]]]$("#count").text()[[[)]]];
  $("#count").text(String(count + 1));
});

$("#thumb-down").on("click", function() {
  var count = Number($("#count").text());
  $("#count").text(String(count - 1));
});
```

---
Convert it to a number,
***************************************************************
## Solution

```html
<div id="thumb-up" class="far fa-thumbs-up"></div>
<div id="count">0</div>
<div id="thumb-down" class="far fa-thumbs-down"></div>
```

```js
$("#thumb-up").on("click", function() {
  var [[[count]]] = Number($("#count").text());
  $("#count").text(String(count + 1));
});

$("#thumb-down").on("click", function() {
  var count = Number($("#count").text());
  $("#count").text(String(count - 1));
});
```

---

and store it into a variable `count`.
***************************************************************
## Solution

```html
<div id="thumb-up" class="far fa-thumbs-up"></div>
<div id="count">0</div>
<div id="thumb-down" class="far fa-thumbs-down"></div>
```

```js
$("#thumb-up").on("click", function() {
  var count = Number($("#count").text());
  $("#count").text(String([[[count + 1]]]));
});

$("#thumb-down").on("click", function() {
  var count = Number($("#count").text());
  $("#count").text(String(count - 1));
});
```

---
Then we add one to the count,
***************************************************************
## Solution

```html
<div id="thumb-up" class="far fa-thumbs-up"></div>
<div id="count">0</div>
<div id="thumb-down" class="far fa-thumbs-down"></div>
```

```js
$("#thumb-up").on("click", function() {
  var count = Number($("#count").text());
  $("#count").text([[[String(]]]count + 1[[[)]]]);
});

$("#thumb-down").on("click", function() {
  var count = Number($("#count").text());
  $("#count").text(String(count - 1));
});
```

---
Convert it to a string,
***************************************************************
## Solution

```html
<div id="thumb-up" class="far fa-thumbs-up"></div>
<div id="count">0</div>
<div id="thumb-down" class="far fa-thumbs-down"></div>
```

```js
$("#thumb-up").on("click", function() {
  var count = Number($("#count").text());
  [[[$("#count").text(]]]String(count + 1)[[[)]]];
});

$("#thumb-down").on("click", function() {
  var count = Number($("#count").text());
  $("#count").text(String(count - 1));
});
```

---
and use that result to update the `#count` element.

And for the `#thumb-down` button, we do essentially the same thing, except
we are subtracting one instead of adding.

So there we have it! The Thumbs Up Thumbs Down Widget.
***************************************************************
![Latest Articles](./lessons/javascript/lesson-7/images/latest-articles.png)

---
Now, let's say you want to use this widget in multiple places
in an application --- like this one.

Let's say this is a list of blog articles, and you can increase
or decrease the count for each individual article.

We cannot simply drop in the code from the previous slide,
can we?
***************************************************************
## Original Widget

```html
<div [[[id="thumb-up"]]] class="far fa-thumbs-up"></div>
<div [[[id="count"]]]>0</div>
<div [[[id="thumb-down"]]] class="far fa-thumbs-down"></div>
```

```js
$("#thumb-up").on("click", function() {
  var count = Number($("#count").text());
  $("#count").text(String(count + 1));
});

$("#thumb-down").on("click", function() {
  var count = Number($("#count").text());
  $("#count").text(String(count - 1));
});
```

---
For one, we can not have multiple elements on the page with the same IDs.
So, instead of using IDs, we'll need to use classes instead.
***************************************************************
## Solution

```html
<div id="thumb-up" class="far fa-thumbs-up"></div>
<div id="count">0</div>
<div id="thumb-down" class="far fa-thumbs-down"></div>
```

```js
$([[["#thumb-up"]]]).on("click", function() {
  var count = Number($([[["#count"]]]).text());
  $("#count").text(String(count + 1));
});

$([[["#thumb-down"]]]).on("click", function() {
  var count = Number($([[["#count"]]]).text());
  $([[["#count"]]]).text(String(count - 1));
});
```

---
Secondly, all of these selectors are ID selectors, and with multiple
elements, that simply won't fly.
***************************************************************
## Multiple Widgets

```html
<ul id="articles">
  <li class="article">
    <div class="thumbs">
      <div class="far fa-thumbs-up"></div>
      <div class="count">0</div>
      <div class="far fa-thumbs-down"></div>
    </div>
    <a href="#">Why Use Functional Programming?</a>
  </li>
  <li class="article">
    <div class="thumbs">
      <div class="far fa-thumbs-up"></div>
      <div class="count">0</div>
      <div class="far fa-thumbs-down"></div>
    </div>
    <a href="#">ES6, 7, 8, and Beyond</a>
  </li>
  .
  .
  .
</ul>
```

---
We'll use an HTML structure like this, where there is one `<ul>` element
that contains any number of `<li>` elements.
***********************************************************
## Multiple Widgets

```html
<li class="article">
  <div class="thumbs">
    <div class="far fa-thumbs-up"></div>
    <div class="count">0</div>
    <div class="far fa-thumbs-down"></div>
  </div>
  <a href="#">Why Use Functional Programming?</a>
</li>
```

---
Within each `<li>` element, there is a nested `div#thumbs` element,
and then within that, there are 3 more nested `<div>` elements:

* `.fa-thumbs-up` for the thumbs up icon
* `.count` for displaying the current count for this article
* `.fa-thumbs-down` for the thumbs down icon

Finally, we have an `<a>` link element just outside of the `#thumbs`
element.
***********************************************************
## Multiple Widgets

```html
<li class="article">
  <div class="thumbs">
    <div class="far [[[fa-thumbs-up]]]"></div>
    <div class="count">0</div>
    <div class="far fa-thumbs-down"></div>
  </div>
  <a href="#">Why Use Functional Programming?</a>
</li>
```

```js
[[[$("#articles").on("click", ".fa-thumbs-up", function() {]]]

[[[});]]]
```

---
So, let's try to make the Thumbs Up icon work.

First, we'll use event delegation to listen on the `click` events
on the Thumbs Up icons. Although event delegation is not
strictly necessarily at this point, it will help ensure that
things work for even newly constructed articles afterwards.

This statement listens for `click` events on the `#articles` ul
element at the top, and then filters down to only trigger on
events coming from any `.fa-thumbs-up` elements.
***********************************************************
## Multiple Widgets

```html
<li class="[[[article]]]">
  <div class="thumbs">
    <div class="far fa-thumbs-up"></div>
    <div class="count">0</div>
    <div class="far fa-thumbs-down"></div>
  </div>
  <a href="#">Why Use Functional Programming?</a>
</li>
```

```js
$("#articles").on("click", ".fa-thumbs-up", function() {
  [[[var $li = $(this).closest(".article");]]]
});
```

---
Now, given that *some* Thumbs Up icon was clicked,
we'll use the `.closest()` method to find which parent `.article`
element it belonged to.

Using a `$` to prefix a variable name is a common convention
for denoting the fact that this variable contains a jQuery
wrapper object.
***********************************************************
## Multiple Widgets

```html
<li class="article">
  <div class="thumbs">
    <div class="far fa-thumbs-up"></div>
    <div class="[[[count]]]">0</div>
    <div class="far fa-thumbs-down"></div>
  </div>
  <a href="#">Why Use Functional Programming?</a>
</li>
```

```js
$("#articles").on("click", ".fa-thumbs-up", function() {
  var $li = $(this).closest(".article");
  [[[var $count = $li.find(".count");]]]
});
```

---
Now that we have the `$li` for the article we are dealing with,
we can use it to get the element that contains its count by using
the `.find()` method.
***********************************************************
## Multiple Widgets

```html
<li class="article">
  <div class="thumbs">
    <div class="far fa-thumbs-up"></div>
    <div class="count">[[[0]]]</div>
    <div class="far fa-thumbs-down"></div>
  </div>
  <a href="#">Why Use Functional Programming?</a>
</li>
```

```js
$("#articles").on("click", ".fa-thumbs-up", function() {
  var $li = $(this).closest(".article");
  var $count = $li.find(".count");
  [[[var count = Number($count.text());]]]
});
```

---
Next, we'll get the displayed text in the `$count` element and convert
it to a number.
***********************************************************
## Multiple Widgets

```html
<li class="article">
  <div class="thumbs">
    <div class="far fa-thumbs-up"></div>
    <div class="count">0</div>
    <div class="far fa-thumbs-down"></div>
  </div>
  <a href="#">Why Use Functional Programming?</a>
</li>
```

```js
$("#articles").on("click", ".fa-thumbs-up", function() {
  var $li = $(this).closest(".article");
  var $count = $li.find(".count");
  var count = Number($count.text());
  [[[count++;]]]
});
```

---
Add one to it.
***********************************************************
## Multiple Widgets

```html
<li class="article">
  <div class="thumbs">
    <div class="far fa-thumbs-up"></div>
    <div class="count">[[[1]]]</div>
    <div class="far fa-thumbs-down"></div>
  </div>
  <a href="#">Why Use Functional Programming?</a>
</li>
```

```js
$("#articles").on("click", ".fa-thumbs-up", function() {
  var $li = $(this).closest(".article");
  var $count = $li.find(".count");
  var count = Number($count.text());
  count++;
  [[[$count.text(String(count));]]]
});
```

---
And set the text value of `$count` to the new amount --- but first
converting it to a string.

That does it! This code will work for any number of articles with
the this same DOM structure within it, which is great because:

1. Who wants to repetitively write the same event handler code over
and over again?
2. If you don't know how many articles there will be, you wouldn't
even know how many of these you'd need to write.

This is componentization --- we have created a *reusable* component!
***********************************************************
## Multiple Widgets: Challenge

```html
<li class="article">
  <div class="thumbs">
    <div class="far fa-thumbs-up"></div>
    <div class="count">[[[1]]]</div>
    <div class="far fa-thumbs-down"></div>
  </div>
  <a href="#">Why Use Functional Programming?</a>
</li>
```

```js
$("#articles").on("click", ".fa-thumbs-up", function() {
  var $li = $(this).closest(".article");
  var $count = $li.find(".count");
  var count = Number($count.text());
  count++;
  $count.text(String(count));
});
```

---
Challenge time! Please do this exercises for the Thumbs Down
button as well, causing it to decrease the count by one.
Use [this template](https://gist.github.com/airportyh/18651353726d75bf60102d8193cbfe2a) as the starting point.

When you are done having a try at this, go to the next
slide for the solution.
***********************************************************
## Solution

```html
<li class="article">
  <div class="thumbs">
    <div class="far fa-thumbs-up"></div>
    <div class="count">1</div>
    <div class="far fa-thumbs-down"></div>
  </div>
  <a href="#">Why Use Functional Programming?</a>
</li>
```

```js
$("#articles").on("click", ".fa-thumbs-up", function() {
  var $li = $(this).closest(".article");
  var $count = $li.find(".count");
  var count = Number($count.text());
  count++;
  $count.text(String(count));
});

$("#articles").on("click", ".fa-thumbs-down", function() {
  var $li = $(this).closest(".article");
  var $count = $li.find(".count");
  var count = Number($count.text());
  count--;
  $count.text(String(count));
});
```

---
This is the solution.
***********************************************************
## Summary

* `.parent()` method
* `.closest()` method
* `.find()` method
* Componentization

---
This is what you've learned.
***********************************************************
## Homework

[Homework](https://gist.github.com/airportyh/e62acfe546a9a2c924ccbaa8e4caea09)

---
Enjoy your homework.
