from sys import argv, exit

import click
import pkg_resources

from fluoresce.main import (
    display_mode,
    paint_mode,
    paint_mode,
    regex_mode,
    manage_colors,
    query_mode,
)
from fluoresce.try_stdin import try_stdin


@click.command()
@click.argument("colors", required=True, nargs=-1)
def cli_regex_mode(colors):
    for color in colors:
        if "=" not in color and "#" not in color:
            raise ValueError(
                "In regex mode, every argument must be a color. "
                r"Colors look like '^hello=greeting=#2596be' or 'world$=#e2i743' or '(.)\1+=repetition'"
                f" and {color} looks like none of these"
            )
        components = color.split("=")
    regex_mode(colors)


def toplevel_help():
    print("toplevel help")
    exit(0)


def version():
    print(pkg_resources.get_distribution("fluoresce").version)
    exit(0)


@click.command(no_args_is_help=True)
@click.argument("colors", required=True, nargs=-1)
@click.option(
    "--version",
    "-v",
    is_flag=True,
    default=False,
)
@click.option(
    "--help",
    "-h",
    is_flag=True,
    default=False,
)
@click.option(
    "--paint",
    "-p",
    is_flag=True,
    default=False,
)
@click.option(
    "--query",
    "-q",
    is_flag=True,
    default=False,
)
@click.option(
    "--manage",
    "-m",
    is_flag=True,
    default=False,
)
def fluoresce(version, help, paint, query, manage, colors):

    if version:
        version()

    if help:
        help()

    if manage:
        manage_colors()

    data = try_stdin()
    if data:
        if not (paint or query):
            display_mode(data)
            exit(0)

        elif paint:
            paint_mode(data)
            exit(0)

        elif query:
            query_mode(data)
            exit(0)

        else:
            raise ValueError(f"Unexpected cli arg combo: {locals()}")
    else:

        if paint:
            print(
                "You need some data to paint on.  Try:\n"
                "    $  echo 'this is the data you will be painting' | fluoresce --paint"
            )
            exit(101)

        if query:
            print(
                "You need some data query with.  Try:\n"
                "    $  echo 'this is the data you will be querying for' | fluoresce --query"
            )
            exit(102)
