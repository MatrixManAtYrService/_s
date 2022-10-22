from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Static
from textual.widget import Widget
from textual.geometry import Size
from rich.console import Console, ConsoleOptions, RenderResult, ConsoleRenderable
from rich.text import Text
from rich.align import Align
from itertools import cycle
from textwrap import dedent


class StateToggle(Static):
    def __init__(self, states):
        self.states = cycle(states)
        super().__init__()

    DEFAULT_CSS = """
        StateToggle {
            width: auto;
            height: 1;
        }
        """

    def on_mount(self) -> None:
        self.action_next_highlight_mode()

    def action_next_highlight_mode(self) -> None:
        current_mode = next(self.states)
        self.update("[@click=next_highlight_mode()]{}[/]".format(current_mode[0]))


#    def get_content_width(self, container: Size, viewport: Size) -> int:
#        return 2


class ShrinkyText(Static):
    def __init__(self, strings):
        super().__init__()
        self.strings = strings

    DEFAULT_CSS = """
        StateToggle {
            width: auto;
            height: 1;
            align: center top;
        }
        """

    class Renderable:
        def __init__(self, strings):
            self.strings = reversed(sorted([(len(s), s) for s in strings]))

        def __rich_console__(
            self, console: Console, options: ConsoleOptions
        ) -> RenderResult:
            for l, s in self.strings:
                if options.max_width > l:
                    yield Text(s)
                    break

    def render(self) -> ConsoleRenderable:
        return ShrinkyText.Renderable(self.strings)


class ActionsApp(App):
    def compose(self) -> ComposeResult:
        yield Container(
            Horizontal(
                StateToggle(["Paint", "Subcanvas", "Feature"]),
                StateToggle(["Character", "Line", "Rectangle"]),
            ),
            ShrinkyText(
                [
                    "foo",
                    "doooooooooooooooooooooo",
                    "rooooooooooooooooooooooooooooooooooooo",
                ]
            ),
        )


if __name__ == "__main__":
    app = ActionsApp()
    app.run()
