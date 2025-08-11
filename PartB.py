# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 13:08:22 2024

@author: it2022134 Exarchou Athos
"""

#imports:
import numpy as np
import matplotlib.pyplot as plt
import sys

def generate_pulse(Ts, N):
    """Δημιουργία τριγωνικού παλμού p(t)."""
    t = np.linspace(-Ts / 2, Ts / 2, N, endpoint=False) #Άξονας χρόνου
    
    p_t = np.zeros_like(t) #αρχικοποίηση του παλμού
    for i in range(len(t)):
        if 0 <= t[i] <= Ts / 2:
            p_t[i] = (2 / Ts) * t[i]
        elif Ts / 2 < t[i] <= Ts:
            p_t[i] = (2 / Ts) * (Ts - t[i])
        else:
            p_t[i] = 0
            
    return t, p_t

def power_spectral_density(p_t, Ts, N):
    """Υπολογισμός φασματικής πυκνότητας ισχύος (αναλυτικά και αριθμητικά)."""
    #Υπολογισμός FFT για το αριθμητικό φάσμα P(f)
    P_f_numeric = np.fft.fftshift(np.fft.fft(p_t, n=N)) * Ts / N
    frequencies = np.fft.fftshift(np.fft.fftfreq(N, d=Ts / N)) #Άξονας συχνότητας σε Hz

    #Αναλυτικός υπολογισμός του |P(f)| με τη συνάρτηση sinc
    def P_f(f):
        return np.abs((Ts/2) * np.sinc(f * Ts/2)**2)

    #Υπολογισμός φασματικής πυκνότητας ισχύος (Sx(f))
    Sx_f_numeric = np.abs(P_f_numeric) ** 2 #Αριθμητικό Sx(f)
    Sx_f_analytic = (P_f(frequencies)) ** 2 #Αναλυτικό Sx(f)

    return frequencies, P_f_numeric, Sx_f_analytic, Sx_f_numeric

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

#Δημιουργία τριγωνικού παλμού p(t)
t, p_t = generate_pulse(Ts, N)

#Υπολογισμός φάσματος P(f) και φασματικής πυκνότητας ισχύος Sx(f)
frequencies, P_f_numeric, Sx_f_analytic, Sx_f_numeric = power_spectral_density(p_t, Ts, N)

#1ο Διάγραμμα: Σύγκριση Αναλυτικού και Αριθμητικού P(f)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(frequencies, np.abs(P_f_numeric), label="Αριθμητικό P(f)", linestyle='--')
plt.plot(frequencies, Ts * np.sinc(frequencies * Ts), label="Αναλυτικό P(f)")
plt.title("Σύγκριση Αναλυτικού και Αριθμητικού P(f)")
plt.xlabel("Συχνότητα (Hz)")
plt.ylabel("|P(f)|")
plt.legend()
plt.grid()

#Εμφάνιση κλίμακας σε επιστημονική σημείωση (βελτίωση εμφάνισης αξόνων)
plt.gca().ticklabel_format(axis="y", style="sci", scilimits=(-9, -9)) #κάθετος άξονας
plt.gca().ticklabel_format(axis="x", style="sci", scilimits=(10, 10)) #οριζόντιος άξονας

#2ο Διάγραμμα: Φασματική Πυκνότητα Ισχύος (Sx(f))
plt.subplot(2, 1, 2)
plt.plot(frequencies, Sx_f_numeric, label="Αριθμητικό Sx(f)", linestyle='--')
plt.plot(frequencies, Sx_f_analytic, label="Αναλυτικό Sx(f)")
plt.title("Φασματική Πυκνότητα Ισχύος Sx(f)")
plt.xlabel("Συχνότητα (Hz)")
plt.ylabel("Sx(f)")
plt.legend()
plt.grid()

#Εμφάνιση κλίμακας σε επιστημονική σημείωση (βελτίωση εμφάνισης αξόνων)
plt.gca().ticklabel_format(axis="y", style="sci", scilimits=(-18, -18)) #κάθετος άξονας
plt.gca().ticklabel_format(axis="x", style="sci", scilimits=(9, 9)) #οριζόντιος άξονας

plt.tight_layout()
plt.show()

