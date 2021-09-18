from datetime import datetime
from os import listdir, mkdir
from os.path import basename, isdir, isfile, join
from shutil import copy2

from click import Path, argument, command, option
from yaml import dump

from .log import log


@command()
@argument("title_or_directory_path_or_md", nargs=1)
@option("--copy", type=Path(exists=True), multiple=True)
@option("--tag", multiple=True)
def cli(title_or_directory_path_or_md, copy, tag):
    """
    `mdpost` is a command line program for making markdown-based post.

    https://github.com/KwatME/MDPost.py
    """

    tag_ = list(tag)

    if isdir(title_or_directory_path_or_md):

        directory_path = title_or_directory_path_or_md.rstrip("/")

        log("Converting {} into a post...".format(directory_path))

        convert(directory_path, copy, tags=tag_)

    elif (
        3 < len(title_or_directory_path_or_md)
        and title_or_directory_path_or_md[-3] == ".md"
        and isfile(title_or_directory_path_or_md)
    ):

        md_path = title_or_directory_path_or_md

        log("Updating the frontmatter of {}...".format(md_path))

        update_frontmatter(md_path)

    else:

        title = title_or_directory_path_or_md

        log('Making a post "{}/"...'.format(title))

        make(title, copy, tags=tag_)


def convert(directory_path, copy_, **frontmatter):

    copy_file_(copy_, directory_path)

    md_path = join(directory_path, "index.md")

    md = ""

    image_directory_name = "image"

    image_directory_path = join(directory_path, image_directory_name)

    if isdir(image_directory_path):

        log("Listing {}/ in .md...".format(image_directory_path))

        for name in sorted(listdir(image_directory_path)):

            md += "\n![]({}/{})\n".format(image_directory_name, name)

    write_md(
        make_frontmatter(title=basename(directory_path), **frontmatter), md, md_path
    )


def make(title, copy_, **frontmatter):

    directory_path = title

    copy_file_(copy_, directory_path)

    md_path = join(directory_path, "index.md")

    md = ""

    mkdir(directory_path)

    write_md(make_frontmatter(title=title, **frontmatter), md, md_path)


def copy_file_(copy_, directory_path):

    for copy in copy_:

        to_path = join(directory_path, basename(copy))

        log("Copying {} to {}...".format(copy, to_path))

        copy2(copy, to_path)


def make_frontmatter(*args, **kwargs):

    separator = "---\n"

    return "{0}{1}{0}".format(
        separator,
        dump(
            {"time": datetime.now(), "cover": "cover.jpeg", **kwargs},
            default_flow_style=None,
        ),
    )


def write_md(frontmatter, md, md_path):

    error_exist(md_path)

    with open(md_path, mode="w") as io:

        io.write(frontmatter)

        io.write(md)


def error_exist(path,):

    if isfile(path):

        log("{} exists.".format(path), kind="error")
