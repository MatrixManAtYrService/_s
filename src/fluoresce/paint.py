from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Grid
from textual.widgets import Placeholder, Static
from textual.widget import Widget
from rich.console import (
    Console,
    ConsoleOptions,
    RenderableType,
)
from rich.align import Align
from rich.style import Style
from rich.segment import Segment
from rich.measure import Measurement
from rich.panel import Panel
from copy import deepcopy

dummy_content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla fringilla varius urna vitae porttitor. Praesent ligula nisl, tincidunt vitae bibendum id, interdum sed nibh. Vivamus fermentum, tortor vitae tempus vestibulum, elit mi interdum risus, id porttitor magna odio et dui. Cras sit amet eros tempus neque congue venenatis vel non neque. Morbi rutrum sit amet lorem eu tempor. Suspendisse potenti. Praesent sagittis arcu a rhoncus suscipit. Maecenas rutrum sem nec eros vehicula accumsan. Duis diam lacus, laoreet ullamcorper lorem et, suscipit fermentum magna. Integer gravida leo quis magna congue fringilla. Sed sed justo ex.
Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Duis ipsum enim, ultrices non iaculis in, bibendum vitae quam. Mauris laoreet nisl eget eleifend malesuada. Etiam aliquet, erat quis rutrum pharetra, libero mi pretium sem, vel consequat purus dolor nec nibh. Duis viverra massa ut ligula dapibus, eget mollis sapien euismod. Donec consequat leo vel ligula mollis tincidunt. Nullam fringilla risus at orci maximus lacinia. Quisque mauris diam, congue a arcu sed, laoreet tincidunt nisl. Integer scelerisque lectus eu nibh fermentum dapibus. Suspendisse risus ante, facilisis et lacus sed, molestie venenatis urna.
Aliquam pulvinar sagittis elit, eu luctus nisi eleifend vel. Nunc lobortis vel quam in ullamcorper. Etiam et vulputate dui. Ut eu posuere nulla, vel tempor tortor. Vestibulum sapien dui, mattis in eleifend eget, efficitur a enim. In sed aliquam enim, id gravida turpis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sed posuere nibh. Suspendisse facilisis nunc vel est vestibulum aliquet. Nam in metus et erat luctus congue. Pellentesque a nisi scelerisque, tincidunt orci eget, mattis enim. In ultrices lacinia enim vitae lacinia.
Curabitur dignissim nisi vel felis sodales tristique. Praesent facilisis metus vitae porttitor auctor. Aenean nec placerat est. Cras vestibulum egestas diam ultrices tempus. Sed volutpat scelerisque massa eget vulputate. Nam eu aliquam lacus. Nulla a orci sit amet mi tincidunt condimentum in eget purus. Nulla consectetur magna eget pretium lacinia. Nulla non facilisis elit. Ut mattis dapibus lacus, ut vehicula lorem dapibus sed. Nunc sapien tellus, vulputate nec tellus ut, pretium lobortis eros. Etiam ultricies nec augue nec consequat. Fusce porta urna nec varius bibendum.
Aliquam sollicitudin accumsan lacus, sit amet rutrum quam sodales nec. Sed ut ullamcorper turpis. Nullam a rutrum orci, dictum ornare quam. Aliquam vel nisl ut mauris sagittis porttitor et vel dolor. Donec porttitor, purus at luctus suscipit, orci turpis aliquet erat, a porttitor risus arcu et libero. Vivamus maximus nisi non augue vulputate, et auctor quam malesuada. Aliquam erat volutpat. Morbi volutpat et orci ut consectetur. Nunc finibus pretium laoreet. Donec et sem eu justo ultricies semper.
"""


dummy_colors = {
    "foo": Style(color="black", bgcolor="red"),
    "bar": Style(color="black", bgcolor="blue"),
    "baz": Style(color="black", bgcolor="green"),
    "qux": Style(color="white", bgcolor="red"),
    "quux": Style(color="white", bgcolor="blue"),
    "wakka": Style(color="black", bgcolor="green"),
    "bang": Style(color="red", bgcolor="blue"),
    "splat": Style(color="blue", bgcolor="green"),
    "antidisestablishmentarianism": Style(color="green", bgcolor="red"),
}


class ColorIndicator(Widget):
    def __init__(self, index, color, style):
        super().__init__(name=f"color_{index}")
        self.height = 1
        self.index = index
        self.color = color
        self.base_style = style
        self.selected = False

    def __rich_console__(self, console: Console, options: ConsoleOptions):
        if self.selected:
            style: Style = deepcopy(self.base_style)
            style.bold = True
            istyle = Style(bold=True)
        else:
            istyle = Style()
            style = self.base_style
        yield Segment(f"{self.index}", istyle)
        yield Segment(f"{self.color}", style)

    def render(self) -> RenderableType:
        return Panel(Align.center(self))


class ViewToggle(Placeholder):
    pass


class ActionToggle(Placeholder):
    pass


class ColorList(Grid):
    def __init__(self, colors):
        indicators = [
            ColorIndicator(i + 1, color, style)
            for i, (color, style) in enumerate(colors.items())
        ]
        super().__init__(*indicators, id="color_list")


class TopBar(Placeholder):
    pass


class ContentArea(Static):
    pass


class MessageArea(Placeholder):
    pass


class Editor(Container):

    DEFAULT_CSS = """
        Editor {
            align: center top;
            max-width: 120;
        }
        TopBar {
            dock: top;
            align: center top;
            width: 100%;
            height: 6;
        }
        ViewToggle {
            dock: right;
            width: 10;
            height: 3;
        }
        ActionToggle {
            dock: left;
            width: 10;
            height: 3;
        }
        ColorList {
            align: center top;
            grid-size: 5;
        }
        ColorIndicator {
            width: 10;
            height: 3;
            align: center top;
        }
        ContentArea {
            align: left middle;
            width: 100%;
            height: 50;
        }
        MessageArea {
            dock: bottom;
            align: center top;
            width: 100%;
            height: 10%;
        }
        """

    def __init__(self, content=dummy_content, colors=dummy_colors):
        super().__init__(
            TopBar(ViewToggle(), ColorList(dummy_colors), ActionToggle()),
            ContentArea(dummy_content),
            MessageArea(),
        )


class ActionsApp(App):
    def compose(self) -> ComposeResult:
        yield Editor()


if __name__ == "__main__":
    app = ActionsApp()
    app.run()
