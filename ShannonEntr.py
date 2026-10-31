import numpy as np
from collections import Counter

with open("bits_run1.txt") as f:
    bits = f.read().strip()

arr = np.frombuffer(bits.encode(), dtype=np.uint8) - ord("0")   # array de 0 y 1
N = len(arr)

def entropias(simbolos):
    """Recibe un array de símbolos enteros, devuelve (Shannon, min-entropía) en bits por símbolo."""
    _, cuentas = np.unique(simbolos, return_counts=True)
    p = cuentas / cuentas.sum()
    shannon = -np.sum(p * np.log2(p))
    min_ent = -np.log2(p.max())
    return shannon, min_ent

# 1) Por bit (símbolos de 1 bit)
s, m = entropias(arr)
print(f"Por bit   -> Shannon: {s:.6f}  Min-entropía: {m:.6f}")

# 2) Por símbolos de 8 bits (bytes), como usa NIST 800-90B
n8 = N // 8
bytes_ = np.packbits(arr[: n8 * 8])
s8, m8 = entropias(bytes_)
print(f"Por byte  -> Shannon: {s8:.4f}/8  Min-entropía: {m8:.4f}/8  (por bit: {m8/8:.6f})")

''' AUTOCORRELACION '''

import matplotlib.pyplot as plt

x = 2 * arr.astype(np.int8) - 1      # convierte 0/1 a -1/+1

max_lag = 1024
ac = np.array([np.mean(x[:-d] * x[d:]) for d in range(1, max_lag + 1)])

umbral = 3 / np.sqrt(N)              # ~3 desviaciones estándar
fuera = np.sum(np.abs(ac) > umbral)
print(f"Umbral (3σ): {umbral:.5f}")
print(f"Máx |AC|: {np.abs(ac).max():.5f}")
print(f"Lags fuera del umbral: {fuera} de {max_lag} (esperado: ~{0.0027*max_lag:.0f})")

plt.figure(figsize=(10, 4))
plt.vlines(range(1, max_lag + 1), 0, ac, linewidth=0.6)
plt.axhline(umbral, color="r", ls="--", lw=0.8)
plt.axhline(-umbral, color="r", ls="--", lw=0.8)
plt.xlabel("Desfase (lag)")
plt.ylabel("Autocorrelación")
plt.title("Autocorrelación de la secuencia de bits")
plt.savefig("autocorrelacion_run1.png", dpi=150, bbox_inches="tight")
plt.show()