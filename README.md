`md-post` is a command line program for making a post.

It complements [Gatsby.js](https://www.gatsbyjs.com) markdown workflow.

## Install

```sh
python -m pip install git+https://github.com/KwatME/md_post
```

## Use

### Make a post

Make a post and start adding content to Title/index.md:

```sh
md-post Title
```

Add some tags to the frontmatter:

```sh
md-post "Title with Space" --tag Tag --tag "Tag with Space"
```

Copy some files to the post directory:

```sh
md-post "Title with Space" --copy path/to/file --copy test/cover_template.key
```

### Convert a directory into a post

```sh
md-post /path/to/directory
```

If directory/image/ exists, the images will be sorted and listed in directory/index.md.
You can simply take bunch of screenshots and automatically make a post with them.

```sh
md-post test/Kobe\ and\ Jordan/
```

### Update frontmatter

```sh
md-post path/to/index.md
```

```sh
md-post test/Kobe\ and\ Jordan/index.md
```

---

Check out [kwatme.com](https://kwatme.com), which is built with [Gatsby.js](https://gatsbyjs.com) and this program.
