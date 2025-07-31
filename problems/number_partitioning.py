"""Implementation of the Number Partitioning Problem as a Hamiltonian."""
from core.base import Hamiltonian

def number_partitioning(numbers: list[float]) -> Hamiltonian:

    J = {}
    n = len(numbers)
    for i in range(n):
        for j in range(i+1,n):
            J[(i,j)] = float(numbers[i]*numbers[j])

    return Hamiltonian(h_terms={}, J_terms=J)
    