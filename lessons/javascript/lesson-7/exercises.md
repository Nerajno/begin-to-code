# JS Lesson 7 Exercises

## Todo List

You will make a todo list application, in a number of phases.

1. Create the visual display for a todo list using a `<ul id="todos">` element
with `<li>` elements within it. You may hard code the names of your todos.
2. Create a form just above the `#todos` element containing:
    * a text input for entering a new todo
    * a submit button

    When the form is submitted, take the text from
    the text input as the new todo, and add a new `<li>` with the new todo to the `#todos` element.
3. Add a "Delete" button to each `<li>` element within the `#todos` element --- even for newly added todos. When "Delete" is clicked, it should remove its parent `<li>` from the `#todos` element.
4. Add a checkbox input to each `<li>` element (place it to the left of the text). It should reflect whether this task has been completed. The user can toggle this checkbox at will.
5. Make it so that whenever a todo is complete, the `<li>` item will display with a strike-through line across it. *Hint: use the `text-decoration` CSS property with the value of `line-through`.*

## Bonus Challenge: Inline Editing

Implement the inline editing feature, which works like this:

* When the user double-clicks (`dblclick`) on the text portion of a todo, it
will change the display of the text to become a text input and an "Save" button instead.

Then, the text input will contain the text of the todo. The user
can then make changes to the text, and then click on the "Save"
button to save the change, at which point, the text input and
"Save" button would disappear and you'd once again see the
text display as normal.

*Note: this exercise was inspired by [TodoMVC](http://todomvc.com/).*
