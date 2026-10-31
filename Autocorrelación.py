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