# Isify

**Isify** is a Python library that converts NP-complete problems into Ising Hamiltonians.  
It enables researchers, quantum developers, and optimization engineers to prototype and test quantum and hybrid algorithms using well-defined energy formulations.

Inspired by Andrew Lucas’s paper *"Ising formulations of many NP problems"*.

### ✨ Features

- Modular implementations for NP problems like MaxCut, Number Partitioning, etc.
- Outputs in Ising or QUBO format
- Compatible with QAOA, D-Wave, PennyLane, and classical solvers
- Extensible architecture — plug in new problems easily
- Symbolic and numeric support (optional)

### 🧠 Example

```python
from isify.problems import number_partitioning
from isify.converters import qubo

nums = [3, 1, 4, 2]
H = number_partitioning.to_ising(nums)
Q = qubo.ising_to_qubo(H.h, H.J)
