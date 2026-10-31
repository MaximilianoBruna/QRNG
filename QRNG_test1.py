from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

n_qubits = 24
shots = 1000

# Circuito: n qubits, n bits clásicos
qc = QuantumCircuit(n_qubits, n_qubits)
qc.h(range(n_qubits))                      # Hadamard en todos los qubits
qc.measure(range(n_qubits), range(n_qubits))

sim = AerSimulator()
result = sim.run(qc, shots=shots, memory=True).result()

memoria = result.get_memory()              # lista de 1000 strings de 24 bits
bits = "".join(memoria)                    # secuencia completa de 24,000 bits
print(len(bits), bits[:64])

''' Guardar números generados'''

with open("bits.txt", "w") as f:
    f.write(bits)

# Binario: agrupar de 8 en 8 bits en bytes
bytes_data = int(bits, 2).to_bytes(len(bits)//8, "big")
with open("bits.bin", "wb") as f:
    f.write(bytes_data)