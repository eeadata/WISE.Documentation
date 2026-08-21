# Using Markdown

Some examples below.  
Follow the link to see more [basic syntax](https://www.markdownguide.org/basic-syntax/).

## Some text

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Lists

Let's make a list (empty surrounding lines required):

- item 1

  - nested item 1
  - nested item 2

- item 2
- item 3

## Table

| No.  |  Prime |
| ---- | ------ |
| 1    |  No    |
| 2    |  Yes   |
| 3    |  Yes   |
| 4    |  No    |

## Code blocks

The following is a Python code block:

```python
  def hello():
      print("Hello world")
```

And this is a C code block:

```c
#include <stdio.h>
int main()
{
    printf("Hello, World!");
    return 0;
}
```

## Math

### Using the `$` dollar sign notation

- Add `myst_parser` to your active extensions in the project `conf.py`

    ```python
        extensions = [
            'sphinx.ext.mathjax', # Keep MathJax enabled to render the math!
            'myst_parser',        # Adds Markdown support
        ]
    ````

- Tell MyST to allow dollar signs and advanced math blocks

    ```python
        myst_enable_extensions = [
            "amsmath",
            "dollarmath",
        ]
    ````

- Now you can use the `$` notation for in-line equations.

    Code:

    ````md
        The area of a circle is $A = \pi r^2$.
    ````

    Output:

    The area of a circle is $A = \pi r^2$.

- You can also use code blocks.

    Code:

    ````md
        $$
        \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
        $$
    ````

    Output:

    $$
    \int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
    $$

### Using a `{math}` block

- This also works for in-line equations.

    Code:

    ````md
        This is an in-line equation, {math}`a^2 + b^2 = c^2`, embedded in text.
    ````

    Output:

    This is an in-line equation, {math}`a^2 + b^2 = c^2`, embedded in text.

- And also works for code blocks.

    Code:

    ````md
        ```{math}
        a^2 + b^2 = c^2
        ```
    ````

    Output:

    ```{math}
    a^2 + b^2 = c^2
    ```

### How to label and cross-reference equations in Markdown

- Define the label after the closing `$$`

    Code:

    ````md
        $$
        E = mc^2
        $$ (einstein-mass-energy)
    ````

    Output:

    $$
    E = mc^2
    $$ (einstein-mass-energy)

- Once labeled, you can reference the equation anywhere in your documentation
    using the Sphinx `{eq}` role.

    Code:

    ````md
        As we can see in equation {eq}`einstein-mass-energy`, energy and mass are interchangeable.
    ````

    Output:

    As we can see in equation {eq}`einstein-mass-energy`, energy and mass are interchangeable.

By default, Sphinx only numbers equations that have a label attached to them.
If you want Sphinx to assign a number to every block equation in your documentation
(even the ones you haven't labeled), you can add this line to your conf.py:

````python
    math_number_all = True
````
