# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 14:23:12 2024

@author: it2022134 Exarchou Athos
"""

#imports:
import numpy as np
import matplotlib.pyplot as plt
import sys

#Συναρτήσεις
def bits_to_gray_symbols(input_bits, p):
    """Μετατροπή ακολουθίας bits σε σύμβολα Gray."""
    assert len(input_bits) % p == 0

    groups = [input_bits[i:i + p] for i in range(0, len(input_bits), p)]
    print("Ομάδες bits:", groups)
    
    symbols = []
    for group in groups:
        decimal_value = int(group, 2)
        gray_value = decimal_value ^ (decimal_value >> 1)
        symbols.append(gray_value) #Προσθήκη στη λίστα

    print("Σύμβολα Gray:", symbols)
    print("Σύμβολα Gray (σε δυαδική μορφή):", [bin(symbol)[2:].zfill(p) for symbol in symbols])

    return symbols

def generate_pam_waveform(symbols, M, b, Ts, N):
    """Δημιουργία κυματομορφής PAM από σύμβολα Gray."""
    #Μέγιστο και ελάχιστο σύμβολο
    max_symbol = M - 1
    min_symbol = 0

    #Κανονικοποίηση πλάτους για να καλύπτει θετικές και αρνητικές τιμές
    amplitudes = [b * (2 * (symbol - max_symbol // 2)) for symbol in range(min_symbol, M)]

    print("Αναλογικά πλάτη για τα σύμβολα:", amplitudes)

    #Εξασφάλιση ότι τα σύμβολα είναι εντός του εύρους [0, M-1]
    symbols = [min(max(symbol, 0), M-1) for symbol in symbols]

    #Δημιουργία των πλάτων σύμφωνα με τα σύμβολα
    ak = [amplitudes[symbol] for symbol in symbols]
    
    print("Αναλογικά πλάτη ak για τα σύμβολα:", ak)

    #Παραγωγή του τριγωνικού παλμού p(t)
    t = np.linspace(0, Ts, N, endpoint=False)
    
    p_t = np.zeros_like(t) #αρχικοποίηση του παλμού
    for i in range(len(t)):
        if 0 <= t[i] <= Ts / 2:
            p_t[i] = (2 / Ts) * t[i]
        elif Ts / 2 < t[i] <= Ts:
            p_t[i] = (2 / Ts) * (Ts - t[i])
        else:
            p_t[i] = 0
    print("Τριγωνικός παλμός p(t):\n", p_t)

    #Δημιουργία της PAM κυματομορφής
    waveform = np.zeros(len(ak) * N)
    for k, a in enumerate(ak):
        waveform[k * N:(k + 1) * N] = a * p_t #Μετατόπιση και κλιμάκωση για κάθε παλμό
    print("Τιμές πλάτους ak:", ak)
    
    return waveform

def plot_waveform(waveform, Ts, N):
    """Εμφάνιση PAM κυματομορφής"""
    t = np.linspace(0, len(waveform) / (1 / Ts), len(waveform)) #Δημιουργία άξονα χρόνου
    
    plt.figure(figsize=(10, 4))
    plt.plot(t, waveform)
    plt.title("Κυματομορφή PAM")
    plt.ylabel("Πλάτος (A)")
    plt.xlabel("Χρόνος (s)")
    plt.grid()
    plt.show()


"""
Main πρόγραμμα
"""
p = 4 #Ο ΑΜ μου τελειώνει σε 4 (2022134)
M = 2 ** (p + 3)
b = 1
bit_length = int(np.log2(M)) #Πλήθος bits
#Το bit_length πρέπει να είναι πολλαπλάσιο του p
if bit_length % p != 0:
    bit_length = (bit_length // p + 1) * p  #αυξάνεται στο επόμενο πολλαπλάσιο

#Δημιουργία τυχαίας ακολουθίας bits
input_bits = ''.join(str(bit) for bit in np.random.randint(0, 2, bit_length))
print("Τυχαία ακολουθία bits:", input_bits)

#Είσοδος χρήστη για αριθμό δειγμάτων και διάρκεια συμβόλου
try:
    N = int(input("Αριθμός δειγμάτων ανά σύμβολο (π.χ., 1024): "))
    if N <= 0:
        raise ValueError("Ο αριθμός δειγμάτων ανά σύμβολο πρέπει να είναι θετικός.")

    Ts = float(input("Διάρκεια συμβόλου Ts (π.χ., 1e-9 για 1 Gbit/s): ")) #1 nano second
    if Ts <= 0:
        raise ValueError("Η διάρκεια συμβόλου πρέπει να είναι θετικός αριθμός.")
except ValueError as err:
    print("Προέκυψε λάθος:", err)
    sys.exit()

print("\n")

#Μετατροπή bits σε σύμβολα Gray
symbols = bits_to_gray_symbols(input_bits, p)

#Δημιουργία PAM Κυματομορφής
waveform = generate_pam_waveform(symbols, M, b, Ts, N)

#Διάγραμμα PAM
plot_waveform(waveform, Ts, N)
