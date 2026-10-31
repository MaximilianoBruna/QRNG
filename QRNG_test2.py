import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

n_qubits = 24
shots = 65536
n_runs = 5

qc = QuantumCircuit(n_qubits, n_qubits)
qc.h(range(n_qubits))
qc.measure(range(n_qubits), range(n_qubits))

sim = AerSimulator()

for i in range(1, n_runs + 1):
    result = sim.run(qc, shots=shots, memory=True).result()
    bits = "".join(result.get_memory())

    with open(f"bits_run{i}.txt", "w") as f:
        f.write(bits)

    # Binario: np.packbits es más eficiente que int(bits, 2) para secuencias largas
    arr = np.frombuffer(bits.encode(), dtype=np.uint8) - ord("0")
    np.packbits(arr).tofile(f"bits_run{i}.bin")

    print(f"Run {i}: {len(bits)} bits guardados")

with open("bits_run1.txt") as f:
    bits = f.read()

n = len(bits)
unos = bits.count("1")
print(f"Total: {n} bits")
print(f"Proporción de unos: {unos / n:.5f}")   # debería estar muy cerca de 0.5