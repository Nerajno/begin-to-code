# JS Lesson 9 Exercises

## Network Panel

Use the network panel to explore:

1. Go to your favorite web site
2. Open the network panel
3. Reload the page
4. Take note of how many HTTP requests were made in order to load the page
5. What types of requests are needed in order to load this page?
6. Look at what some of the requests' URLs were
7. Look at what some of the responses look like

## Random Gif Generator

Make a random gif generator using the Giphy API. Your widget will have

* a text input specify a tag
* a "Random!" button

When the button is clicked, fetch a random image based on that tag, and
display it on the page. If the "Random!" button is clicked again, replace
the existing image with the new image.

## Trending Gifs

Read about the Giphy API's trending endpoint at their [documentation page](https://developers.giphy.com/docs/).

The endpoint URL is `https://api.giphy.com/v1/gifs/trending`. `api_key` is
the only required query parameter, but there are additonal optional parameters.

Make a page that displays the first 10 trending gifs on Giphy immediately
when the page loads.

## A Surprise Visitor

My son Marty wrote a story called "A Surprise Visitor". I helped him
convert his story to HTML. Please [download the HTML](https://gist.github.com/airportyh/cdb8248f56486db088124ab3656e5437),
and the add the following functionality:

Note that many of the words within the story are wrapped in a `<span class="click">`
element. Make it so that when any of these words are clicked, that word
is replaced with the translated version of that word --- as an animated gif.

Read about the Giphy API's translate endpoint at their [documentation page](https://developers.giphy.com/docs/).

You will use the translate endpoint to get an animated gif that best
translates/represents a particular word or phrase.

## Super Duper Challenge: Gif Search Engine

You will write an animated gif search engine reminiscent the Google search
engine.

Read about the Giphy API's search endpoint at their [documentation page](https://developers.giphy.com/docs/).

Like Google's search engine, it should have a front page where there is a
large search box in the middle of the page.

Like Google's search engine, after a search is performed, it should lead you
to a second "search results" page. Only instead of showing a list of
links, you will display a whole page worth of animated gifs.

Like Google's search engine, if there are more than one page worth of results,
there are "Next" and "Previous" paging buttons, as well as jump-to-page-#
buttons to allow the user to navigate between pages.
