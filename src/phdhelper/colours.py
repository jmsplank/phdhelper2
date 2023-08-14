"""Colours in hex format."""

from matplotlib.colors import LinearSegmentedColormap
from dataclasses import dataclass


def _hex2rgb(hexi: str) -> tuple[float, float, float]:
    """Convert hex to rgb."""
    hexi = hexi.lstrip("#")
    r = int(hexi[0:2], 16) / 255
    g = int(hexi[2:4], 16) / 255
    b = int(hexi[4:6], 16) / 255
    return r, g, b


class Colour:
    """Base Colour."""

    def __init__(
        self, c100: str, c200: str, c500: str, c800: str, c900: str, name: str
    ) -> None:
        """Initialise the different shades."""
        self.c100 = c100
        self.c200 = c200
        self.c500 = c500
        self.c800 = c800
        self.c900 = c900
        self.name = name

    @property
    def colors(self) -> list[str]:
        """Get the colours as a list of hex."""
        return [self.c900, self.c800, self.c500, self.c200, self.c100]

    def __call__(self) -> str:
        """Class returns shade 500."""
        return self.c500

    def cmap(self) -> LinearSegmentedColormap:
        """Return a matplotlib colormap with 256 shades."""
        return LinearSegmentedColormap.from_list(self.name, self.colors, N=256)

    def get_shade(self, shade: int) -> tuple[int, int, int]:
        """Get a shade in between the default set."""
        return self.cmap()(shade / 1000)


@dataclass
class ColourScheme:
    """Colour scheme."""

    dark: Colour
    red: Colour
    green: Colour
    blue: Colour
    accent: Colour
    accent2: Colour

    @property
    def colours_hex(self) -> list[str]:
        """Return list of colours."""
        return [
            self.dark(),
            self.red(),
            self.green(),
            self.blue(),
            self.accent(),
            self.accent2(),
        ]

    @property
    def colours(self) -> list[Colour]:
        """Return list of colours."""
        return [self.dark, self.red, self.green, self.blue, self.accent, self.accent2]

    def cycle(self):
        """Looping cycler through colours."""
        cols = self.colours_hex
        while True:
            for i in range(len(cols)):
                yield cols[i]


# classic = ColourScheme(
#     "#020E13",  # black
#     "#BF245A",  # red
#     "#4BB977",  # green
#     "#107EA9",  # blue
#     "#E67737",  # orange
#     "#82349C",  # purple
# )

sim = ColourScheme(
    dark=Colour(
        c900="#060605",
        c800="#313131",
        c500="#7e7e7b",
        c200="#c5c5c2",
        c100="#e3e3e0",
        name="dark",
    ),
    red=Colour(
        "#f9dcd6", "#f9b3a7", "#e6272e", "#630d0e", "#340f07", "alizarin_crimson"
    ),
    green=Colour("#7afca5", "#27e67f", "#028947", "#023a1b", "#05210e", "spring_green"),
    blue=Colour(
        "#d7e4f9", "#a8c8fa", "#278de6", "#0c3458", "#091d32", "cornflower_blue"
    ),
    accent=Colour(
        c900="#281809",
        c800="#4b280b",
        c500="#e67f27",
        c200="#f7b686",
        c100="#f8ddca",
        name="zest",
    ),
    accent2=Colour(
        c900="#37091f",
        c800="#600d38",
        c500="#e6278d",
        c200="#f9b0cc",
        c100="#f9dae5",
        name="cerise",
    ),
)
