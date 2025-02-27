import numpy as np
import matplotlib.pyplot as plt

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
starling_peaks = {(362,250): 'violet', (449,320): 'blue', (504,340): 'green', (563,360): 'red'}

ANSI_COLORS = {
    "blue": "\033[34m",
    "red": "\033[31m",
    "green": "\033[32m",
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

def human_activations(color_name, wavelengths, verbose=False):
    raw_activations = {}
    for (peak1,peak2), color in human_peaks.items():
        raw_activations[color] = gaussian_sensitivity(peak1, peak2, sigma_human, wavelengths)

    if verbose:
        print(f"\033[1mHumans\033[m see {ANSI_COLORS[color_name]}{color_name}\033[m as:")

    activations = []
    for color,levels in raw_activations.items():
        k = sum(levels)/sum(sum(l) for l in raw_activations.values())
        activations.append(k)
        if verbose:
            print(f"{ANSI_COLORS[color]}{color}: \033[10G {k:%}\033[m")
    if verbose:
        print("")
    vec = np.array(activations)
    return vec / np.linalg.norm(vec)
    
human_activations("violet", np.array([380]), verbose=True)
human_activations("purple", np.array([623, 462]), verbose=True)
print("\nThey look the same to us!")

section_break()

def starling_activations(color_name, wavelengths, verbose=False):
    raw_activations = {}
    for (peak1,peak2), color in starling_peaks.items():
        raw_activations[color] = gaussian_sensitivity(peak1, peak2, sigma_starling, wavelengths)

    if verbose:
        print(f"\033[1mStarlings\033[m see {ANSI_COLORS[color_name]}{color_name}\033[m as:")

    activations = []
    for color,levels in raw_activations.items():
        k = sum(levels)/sum(sum(l) for l in raw_activations.values())
        activations.append(k)
        if verbose:
            print(f"{ANSI_COLORS[color]}{color}: \033[10G {k:%}\033[m")
    if verbose:
        print("")
    vec = np.array(activations)
    return vec / np.linalg.norm(vec)

starling_activations("violet", np.array([380]), verbose=True)
starling_purple = starling_activations("purple", np.array([623, 455]), verbose=True)
print("\nThey look completely differe to a starling!")


section_break()

print("...But what pure wavelength looks like purple?")

def wavelength_to_rgb(wavelength, gamma=0.8):
    '''
    This converts a given wavelength of light to an 
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).
    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    '''
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return (int(R), int(G), int(B))

print("")
closest_wavelength = None
best_dist = None
import time
for wavelength in range(100,700,2):
    activations = starling_activations("???", np.array([wavelength]), verbose=False)
    # dist = np.linalg.norm(starling_purple - activations)
    dist = np.dot(starling_purple, activations)
    if closest_wavelength is None or dist > best_dist:
        closest_wavelength, best_dist = wavelength, dist
    r,g,b = wavelength_to_rgb(wavelength)
    #print(f"\033[48;2;{r};{g};{b}m  Scanning: {closest_wavelength}nm...  \033[m dist = {dist}", end="\033[K\n", flush=True)

section_break()

r,g,b = wavelength_to_rgb(closest_wavelength)
print(f"\033[48;2;{r};{g};{b}m  WINNER: {closest_wavelength}nm! (blue)  \033[m\n\n")


# import subprocess
# subprocess.run(["sxiv", "retinal_cones.png"])
# plt.show()
