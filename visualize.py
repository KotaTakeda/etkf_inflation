import itertools
import enum
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_inline.backend_inline import set_matplotlib_formats

# from states import to_mat_rep

set_matplotlib_formats("pdf", "svg")
plt.style.use("etkf_inflation.mplstyle")


class COLORS(enum.Enum):
    MAIN = "#107d79"  # or royalblue
    SUB1 = "#FF9933"  # or turquoise
    SUB2 = "#1F77B4"  # or teal
    ACCENT = "orange"
    THEORETICAL = "grey"
    BACKGROUND = "dimgrey"
    POSITIVE = "red"
    POSITIVE_SUB = "crimson"
    NEGATIVE = "cyan"
    NEGATIVE_SUB = "dodgerblue"


# only use as cmap not color palette
CMAP = {
    "main": sns.cubehelix_palette(light=1, as_cmap=True),
    "sub": plt.cm.hsv,
}

MARKERS = [
    ".",
    "*",
    "^",
    "v",
    "s",
    "h",
    "o",
    "x",
    "d",
    "p",
]

LINESTYLES = [
    "-",
    "--",
    ":",
    "-.",
]


# utility functions to draw lines
# ----------------------------
def get_marker_cycle():
    return itertools.cycle(MARKERS)


def get_linestyle_cycle():
    return itertools.cycle(LINESTYLES)


def get_color_palette(n_colors, pallet_name=None):
    """
    Args:
        n_colors (int):
        pallet_name (str): None, or pallet name for sns.color_palette, 
            e.g. "flare", "ch:s=.25,rot=-.25".
            https://seaborn.pydata.org/generated/seaborn.color_palette.html
    """
    if n_colors == 2:
        palette = [COLORS.MAIN.value, COLORS.ACCENT.value]
    if pallet_name is not None:
        palette = sns.color_palette(pallet_name, as_cmap=False, n_colors=n_colors)
    else:
        palette = sns.hls_palette(as_cmap=False, n_colors=n_colors)
    return palette
