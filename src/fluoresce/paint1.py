from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Static
from rich.console import Console, ConsoleOptions, RenderResult, ConsoleRenderable
from rich.text import Text
from itertools import cycle


class ManyString:
    def __init__(self, *strings):
        self.strings = list(reversed(sorted([(len(s), s) for s in strings])))
        print(self.strings)

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        for l, s in self.strings:
            if options.max_width > l:
                yield Text(s)
                return

        yield Text(s[: options.max_width])


class MessageArea(Static):
    def __init__(self):
        super().__init__()

    DEFAULT_CSS = """
        MessageArea {
            dock: bottom;
        }
        """

    def render(self) -> ConsoleRenderable:
        return ManyString(
            "doo",
            "fooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
        )


class Spacer(Static):
    def __init__(self):
        super().__init__()

    DEFAULT_CSS = """
        Spacer {
            width: 100%;
        }
        """


class TopBar(Horizontal):

    DEFAULT_CSS = """
        TopBar {
            dock: top;
        }
        """

    class StateToggle(Static):
        def __init__(self, states, id="state_toggle"):
            self.states = cycle(states)
            super().__init__(id=id)

        DEFAULT_CSS = """
            StateToggle {
                width: 1;
            }
            """

        def on_mount(self) -> None:
            self.action_next_highlight_mode()

        def action_next_highlight_mode(self) -> None:
            current_mode = next(self.states)
            self.update("[@click=next_highlight_mode()]{}[/]".format(current_mode[0]))

    class ColorList(Horizontal):

        DEFAULT_CSS = """
            ColorList {
                align: right top;
                content-align: center top;
                width: 10%;
            }
            """

        def __init__(self, *colors, id="color_list"):
            content = []
            # content.append(Spacer())
            for c in colors:
                content.append(c)
            # content.append(Spacer())
            super().__init__(*content)

    def __init__(self, *colors):
        view_mode = TopBar.StateToggle(
            ["Paint", "Subcanvas", "Feature"], id="view_mode"
        )
        view_mode.styles.dock = "left"

        select_mode = TopBar.StateToggle(
            ["Character", "Line", "Rectangle"], id="select_mode"
        )
        select_mode.styles.dock = "right"

        color_list = TopBar.ColorList(*colors)
        super().__init__(view_mode, color_list, select_mode)


#    def get_content_width(self, container: Size, viewport: Size) -> int:
#        return 2


class ActionsApp(App):
    def compose(self) -> ComposeResult:
        yield Container(
            TopBar(
                Static("red"),
                Static("green"),
                Static("blue"),
            ),
            MessageArea(),
        )


if __name__ == "__main__":
    app = ActionsApp()
    app.run()
