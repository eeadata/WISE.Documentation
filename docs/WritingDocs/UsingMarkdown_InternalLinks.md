# Using Markdown - Internal links

To link to a heading in another Markdown file using Sphinx, you will generally be using the **MyST Parser** (the standard way to use Markdown in Sphinx).

There are two main ways to do this: using standard Markdown relative links, or using Sphinx's robust cross-referencing system. The cross-referencing method is highly recommended because Sphinx will warn you if the link ever breaks.

Here is how to do both.

## Sphinx cross-referencing

```{warning}
This is the recommended option.
```

This method uses "labels" (anchors). It is the best practice because the link will work no matter where the files are moved within your project, and Sphinx will generate a warning during the build if the target label is missing.

**1. Create a label in the target file (`file_a.md`)**
Place a label in parentheses and an equals sign immediately before the heading you want to link to.

```markdown
(my-custom-heading)=
## The Heading I Want to Link To

Here is the content under the heading.

```

**2. Link to the label in the source file (`file_b.md`)**
You can link to this label using MyST's `{ref}` role or standard Markdown syntax pointing to the anchor.

```markdown
<!-- Option A: Using the MyST {ref} role (Uses the heading text automatically) -->
Read more in {ref}`my-custom-heading`.

<!-- Option B: Using {ref} with custom link text -->
Read more by clicking {ref}`this custom link <my-custom-heading>`.

<!-- Option C: Using standard Markdown anchor syntax -->
Read more by clicking [this custom link](#my-custom-heading).

```

---

## Standard relative Markdown links

If you prefer not to use custom labels, MyST parser can automatically resolve standard Markdown relative links. It automatically creates anchors for all headings by lowercasing the text and replacing spaces with hyphens.

**1. The target file (`file_a.md`)**

```markdown
## My Awesome Heading

Here is the content.

```

**2. Link to it from another file (`file_b.md`)**
Point to the file path relative to your current file, and add `#` followed by the automatically generated slug of the heading.

```markdown
Check out the [Awesome Heading section](file_a.md#my-awesome-heading) for more info.

```

*(Note: If `file_a.md` is in a different folder, you would use relative paths like `../folder/file_a.md#my-awesome-heading`).*
