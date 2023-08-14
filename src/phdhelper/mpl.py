"""Matplotlib formatting and defaults."""

from . import colours
from cycler import cycler
import matplotlib.pyplot as plt
import colorcet as cc
from enum import Enum

_cmaps = list(cc.cm.keys())


class Cmaps(str, Enum):
    """Standard colourmaps."""

    sequential = "cet_CET_L17"
    diverging = "cet_CET_D1A"
    cyclic = "cet_CET_C1"
    colorblind_r = "cet_CET_CBL1_r"
    isoluminant = "cet_CET_I2"
    iso_diverging = "cet_isoluminant_cm_70_c39_r"
    greyscale_r = "cet_CET_L1_r"


def format(cscheme: colours.ColourScheme = colours.sim):
    """Format matplotlib.

    Note:
        https://matplotlib.org/stable/tutorials/introductory/customizing.html#customizing-with-style-sheets
    """
    colours = cycler("color", cscheme.colours_hex)
    linestyles = cycler("linestyle", ["-", "--", "-.", ":"])
    prop_cycler = linestyles * colours
    # cm.register_cmap(cmap=cc.cm.CET_L17, override_builtin=True)

    plt.rc("axes", grid=True, prop_cycle=prop_cycler, xmargin=0)
    plt.rc(
        "lines",
        linewidth=1,
        markerfacecolor="none",
        markeredgecolor=cscheme.dark(),
        color=cscheme.dark(),
    )
    plt.rc("xtick", direction="in", top=True, bottom=True)
    plt.rc("xtick.minor", visible=True)
    plt.rc("ytick", direction="in", left=True, right=True)
    plt.rc("ytick.minor", visible=True)
    plt.rc(
        "legend",
        fancybox=False,
        edgecolor="0.95",
        facecolor="0.95",
        framealpha="0.9",
        fontsize="small",
    )
    plt.rc("font", family="serif", size=10)
    plt.rc("boxplot", notch=True, vertical=True, showcaps=True)
    plt.rc("axes.formatter", use_mathtext=True, useoffset=False)
    plt.rc("figure", dpi=300, figsize=(7, 5), facecolor="white")
    plt.rc("image", cmap=Cmaps.sequential.value)
    plt.rc("errorbar", capsize=5)
    plt.rc("savefig", dpi=300, bbox="tight", facecolor="white")
