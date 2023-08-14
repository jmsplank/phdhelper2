# %%
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from phdhelper import mpl
import numpy as np
from random import choices

from PIL import Image
from numpy.matlib import repmat
from string import ascii_lowercase
from tqdm import tqdm

mpl.format()

cet = ["CET_C1", "CET_C1s", "CET_C2", "CET_C2s", "CET_C3", "CET_C3s", "CET_C4", "CET_C4s", "CET_C5", "CET_C5s", "CET_C6", "CET_C6s", "CET_C7", "CET_C7s", "CET_C8", "CET_C8s", "CET_C9", "CET_C9s", "CET_C10", "CET_C10s", "CET_C11", "CET_C11s", "CET_CBC1", "CET_CBC2", "CET_CBD1", "CET_CBD2", "CET_CBL1", "CET_CBL2", "CET_CBL3", "CET_CBL4", "CET_CBTC1", "CET_CBTC2", "CET_CBTD1", "CET_CBTL1", "CET_CBTL2", "CET_CBTL3", "CET_CBTL4", "CET_D1", "CET_D1A", "CET_D2", "CET_D3", "CET_D4", "CET_D6", "CET_D7", "CET_D8", "CET_D9", "CET_D10", "CET_D11", "CET_D12", "CET_D13", "CET_I1", "CET_I2", "CET_I3", "CET_L1", "CET_L2", "CET_L3", "CET_L4", "CET_L5", "CET_L6", "CET_L7", "CET_L8", "CET_L9", "CET_L10", "CET_L11", "CET_L12", "CET_L13", "CET_L14", "CET_L15", "CET_L16", "CET_L17", "CET_L18", "CET_L19", "CET_L20", "CET_R1", "CET_R2", "CET_R3", "CET_R4", "CET_C1_r", "CET_C1s_r", "CET_C2_r", "CET_C2s_r", "CET_C3_r", "CET_C3s_r", "CET_C4_r", "CET_C4s_r", "CET_C5_r", "CET_C5s_r", "CET_C6_r", "CET_C6s_r", "CET_C7_r", "CET_C7s_r", "CET_C8_r", "CET_C8s_r", "CET_C9_r", "CET_C9s_r", "CET_C10_r", "CET_C10s_r", "CET_C11_r", "CET_C11s_r", "CET_CBC1_r", "CET_CBC2_r", "CET_CBD1_r", "CET_CBD2_r", "CET_CBL1_r", "CET_CBL2_r", "CET_CBL3_r", "CET_CBL4_r", "CET_CBTC1_r", "CET_CBTC2_r", "CET_CBTD1_r", "CET_CBTL1_r", "CET_CBTL2_r", "CET_CBTL3_r", "CET_CBTL4_r", "CET_D1_r", "CET_D1A_r", "CET_D2_r", "CET_D3_r", "CET_D4_r", "CET_D6_r", "CET_D7_r", "CET_D8_r", "CET_D9_r", "CET_D10_r", "CET_D11_r", "CET_D12_r", "CET_D13_r", "CET_I1_r", "CET_I2_r", "CET_I3_r", "CET_L1_r", "CET_L2_r", "CET_L3_r", "CET_L4_r", "CET_L5_r", "CET_L6_r", "CET_L7_r", "CET_L8_r", "CET_L9_r", "CET_L10_r", "CET_L11_r", "CET_L12_r", "CET_L13_r", "CET_L14_r", "CET_L15_r", "CET_L16_r", "CET_L17_r", "CET_L18_r", "CET_L19_r", "CET_L20_r", "CET_R1_r", "CET_R2_r", "CET_R3_r", "CET_R4_r"]  # fmt: skip


# %%
def sinfunc(x: np.ndarray, a: float, omega: float, phi: float) -> np.ndarray:
    """Sinusoidal function."""
    return a * np.sin(omega * x + phi)


fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
for i in range(10):
    params = np.random.rand(3)
    name = "".join(choices(ascii_lowercase, k=6))

    y = sinfunc(x, *params)
    ax.plot(x, y, label=name)

plt.legend()
plt.show()

# %%
num_series = 1000
num_points = 100
SNR = 0.1
x = np.linspace(0, 4 * np.pi, num_points)
Y = np.cumsum(np.random.randn(num_series, num_points), axis=-1)
num_signal = round(SNR * num_series)
phi = (np.pi / 8) * np.random.randn(num_signal, 1)
Y[-num_signal:] = np.sqrt(np.arange(num_points))[None, :] * (
    np.sin(x[None, :] - phi) + 0.05 * np.random.randn(num_signal, num_points)
)


num_fine = 800
x_fine = np.linspace(x.min(), x.max(), num_fine)
y_fine = np.empty((num_series, num_fine), dtype=float)
for i in range(num_series):
    y_fine[i, :] = np.interp(x_fine, x, Y[i, :])
y_fine = y_fine.flatten()
x_fine = repmat(x_fine, num_series, 1).flatten()
h, xe, ye = np.histogram2d(x_fine, y_fine, bins=[400, 100])

for i in tqdm(cet):
    fig, ax = plt.subplots()
    pcm = ax.pcolormesh(
        xe,
        ye,
        h.T + 1,
        cmap=f"cet_{i}",
        norm=LogNorm(vmin=1, vmax=h.max()),
        rasterized=True,
    )
    for j in range(6):
        n = np.random.randint(0, num_series)
        index_start = int(n * num_fine)
        ax.plot(x_fine[0:num_fine], y_fine[index_start : index_start + num_fine])
    ax.set_title(i)
    fig.colorbar(pcm, ax=ax, label="# points", pad=0)
    plt.savefig(f"{i}.png")
    plt.close()

# %% plot image
img_pth = "/Users/jamesplank/Documents/PHD/phdhelper2/download.jpeg"
img = Image.open(img_pth)
img = img.convert("L")

fig, ax = plt.subplots()
ax.imshow(img, cmap="cet_CET_L20")  # type: ignore

plt.show()

z = [f'"{i}"' for i in cet]
f"[{', '.join(z)}]"
