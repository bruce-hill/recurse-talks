import numpy as np
import math
import matplotlib.pyplot as plt
from wavelength import wavelength_to_ansi

def gaussian_sensitivity(peak1, peak2, sigma, wavelengths, depth=2):
    if depth <= 0: return 0
    return (np.exp(-((wavelengths - peak1) ** 2) / (2 * sigma ** 2))
            + .25*np.exp(-((wavelengths - peak2) ** 2) / (2 * sigma ** 2)))

def section_break():
    input("\n" + "="*80 + "\n")

wavelengths = np.linspace(300, 700, 500)

# Estimated sigma values for human and bird cones
sigma_human = 40
sigma_starling = 35

# Human cone sensitivities
human_peaks = {(437, 315): 'blue', (533,345): 'green', (564,355): 'red'}

# Starling cone sensitivities (including UV)
starling_peaks = {(362,250): 'violet', (449,320): 'cyan', (504,340): 'green', (563,360): 'red'}

ANSI_COLORS = {
    "blue": "\033[34m",
    "red": "\033[31m",
    "green": "\033[32m",
    "cyan": "\033[36m",
    "violet": "\033[38;5;177m",
    "purple": "\033[38;5;177m",
}

'''
plt.figure(figsize=(10, 6))

# Plot human sensitivities
plt.subplot(2, 1, 1)
for (peak1, peak2), color in human_peaks.items():
    plt.plot(wavelengths, gaussian_sensitivity(peak1, peak2, sigma_human, wavelengths), color=color, label=f'λ_max = {peak1} nm')
plt.title("Human Retinal Cone Sensitivity")
plt.ylabel("Relative Absorption")
plt.legend()

# Plot starling sensitivities
plt.subplot(2, 1, 2)
for (peak1,peak2), color in starling_peaks.items():
    plt.plot(wavelengths, gaussian_sensitivity(peak1, peak2, sigma_starling, wavelengths), color=color, label=f'λ_max = {peak1} nm')
plt.title("European Starling Retinal Cone Sensitivity")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Relative Absorption")
plt.legend()

plt.tight_layout()
plt.savefig("retinal_cones.png") 
'''

def bar(progress : float, width : int):
    progress = min(1, max(0, progress))
    whole_width = math.floor(progress * width)
    remainder_width = (progress * width) % 1
    part_width = math.floor(remainder_width * 8)
    part_char = [" ", "▏", "▎", "▍", "▌", "▋", "▊", "▉"][part_width]
    if (width - whole_width - 1) < 0:
        part_char = ""
    line = "\033[48;5;237m" + "█" * whole_width + part_char + " " * (width - whole_width - 1) + "\033[40m"
    return line

def human_activations(color_name, wavelengths, verbose=False):
    raw_activations = {}
    for (peak1,peak2), color in human_peaks.items():
        raw_activations[color] = gaussian_sensitivity(peak1, peak2, sigma_human, wavelengths)

    if verbose:
        print(f"\033[1mHumans\033[m see {color_name}\033[m as:")

    activations = []
    for color,levels in raw_activations.items():
        k = sum(levels)/sum(sum(l) for l in raw_activations.values())
        activations.append(k)
        if verbose:
            print(f"{ANSI_COLORS[color]}{color}: \033[10G {k:%} \033[30G{bar(k, 30)}\033[m")
    if verbose:
        print("")
    vec = np.array(activations)
    return vec / np.linalg.norm(vec)

colored_purple = "".join(f"\033[38;2;255;78;0m{c}" if i % 2 == 0 else f"\033[38;2;0;146;255m{c}" for i,c in enumerate("purple")) + "\033[m"
colored_purple += " (\033[38;2;255;78;0m630nm\033[m & \033[38;2;0;146;255m465nm\033[m)"
human_activations("\033[38;5;177mviolet (384nm)\033[m", np.array([384]), verbose=True)
human_activations(colored_purple, np.array([630, 465]), verbose=True)
print("\nThey look the same to us!")

section_break()

def starling_activations(color_name, wavelengths, verbose=False):
    raw_activations = {}
    for (peak1,peak2), color in starling_peaks.items():
        raw_activations[color] = gaussian_sensitivity(peak1, peak2, sigma_starling, wavelengths)

    if verbose:
        print(f"\033[1mStarlings\033[m see {color_name} as:")

    activations = []
    for color,levels in raw_activations.items():
        k = sum(levels)/sum(sum(l) for l in raw_activations.values())
        activations.append(k)
        if verbose:
            print(f"{ANSI_COLORS[color]}{color}: \033[10G {k:%} \033[30G{bar(k, 30)}\033[m")
    if verbose:
        print("")
    vec = np.array(activations)
    return vec / np.linalg.norm(vec)

starling_activations("\033[38;5;177mviolet (384nm)\033[m", np.array([384]), verbose=True)
starling_purple = starling_activations(colored_purple, np.array([630, 465]), verbose=True)
print("\nThey look completely differe to a starling!")


section_break()

print("...But what pure wavelength looks like purple?")

closest_wavelength = None
best_dist = None
for wavelength in range(100,700,1):
    activations = starling_activations("???", np.array([wavelength]), verbose=False)
    # dist = np.linalg.norm(starling_purple - activations)
    dist = np.dot(starling_purple, activations)
    if closest_wavelength is None or dist > best_dist:
        closest_wavelength, best_dist = wavelength, dist
    #print(f"\033[48;2;{r};{g};{b}m  Scanning: {closest_wavelength}nm...  \033[m dist = {dist}", end="\033[K\n", flush=True)

section_break()

color = wavelength_to_ansi(closest_wavelength)
print(f"{color}\033[30m  WINNER: {closest_wavelength}nm! (blue)  \033[m\n\n")

starling_activations(f"{color}blue ({closest_wavelength}nm)\033[m", np.array([closest_wavelength]), verbose=True)
print(f"Which looks more like {colored_purple} than any other pure wavelength!")


# import subprocess
# subprocess.run(["sxiv", "retinal_cones.png"])
# plt.show()
