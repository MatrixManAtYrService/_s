import sys
import os


def try_stdin(if_empty_return=None):
    if os.name == "nt":
        raise NotImplementedError(
            "TODO: check stdin for input and return it from this function if present"
        )
    else:
        import select

        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            return sys.stdin.read()
        else:
            return if_empty_return
