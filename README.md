### Digital Communication System Simulation

This project was developed for the **Telecom Systems** course at [Harokopio University of Athens – Dept. of Informatics and Telematics](https://www.dit.hua.gr).

This project, developed in Python, simulates a digital communication system using Pulse Amplitude Modulation (PAM). It is split into two parts: one for generating a PAM waveform and another for analyzing its spectral characteristics.

---

### Project Structure

* `PartA.py`: Generates a random bit sequence, converts it into Gray-coded symbols, and creates the corresponding PAM waveform.
* `PartB.py`: Analyzes the spectral characteristics of the triangular pulse used in `PartA.py`, comparing analytical and numerical calculations for the power spectral density (PSD).
* `README.md`: This file.

---

### Getting Started

#### Prerequisites
Make sure you have Python installed, along with the following libraries:
* `numpy`
* `matplotlib`

You can install them using `pip`:
```bash
pip install numpy matplotlib
```

### How to Run

1. Generate a PAM Waveform:
Run `PartA.py` and follow the on-screen prompts to input the number of samples per symbol (N) and the symbol duration (Ts). The script will generate a random bit sequence, convert it to symbols, and display the resulting PAM waveform.
```bash
python PartA.py
```

2. Analyze the Power Spectral Density:
Run `PartB.py` to analyze the spectral properties of the triangular pulse. Similarly, you'll be prompted to enter N and Ts. The script will then plot the analytical and numerical power spectral density (PSD) for comparison.
```bash
python PartB.py
```

### Key Features
#### PartA.py
- `bits_to_gray_symbols(input_bits, p)`: Converts a bit sequence into a Gray-coded symbol sequence. Gray coding ensures that adjacent symbols differ by only a single bit, which minimizes bit errors during decoding.

- `generate_pam_waveform(symbols, M, b, Ts, N)`: Creates the PAM waveform using a triangular pulse shape for each symbol.

- `plot_waveform(waveform, Ts, N)`: Visualizes the generated PAM waveform over time.

#### PartB.py
- `generate_pulse(Ts, N)`: Creates the triangular pulse shape p(t).

- `power_spectral_density(p_t, Ts, N)`: Calculates the power spectral density (PSD) of the pulse both analytically (using the sinc function formula) and numerically (using the Fast Fourier Transform).

- **Visualizations**: Plots are generated to compare the analytical and numerical results for both the pulse spectrum ∣P(f)∣ and the PSD S_x(f).

### Configuration
The main script in `PartA.py` is configured with the following parameters:

- `p = 4`: A parameter based on the author's student ID, influencing the number of bits per symbol.

- `M = 2 ** (p + 3)`: The number of amplitude levels.

- `b = 1`: The scaling factor for the amplitude levels.

These parameters can be adjusted directly within the script to explore different system configurations.

## Author

- **Name**: Exarchou Athos
- **Student ID**: it2022134
- **Email**: it2022134@hua.gr

### License

MIT License
