class Hamiltonian:
    def __init__(self, h_terms: dict[int, float], J_terms: dict[tuple[int,int], float]) -> None:
        """
        h_terms: dict mapping qubit index to local field (h_i)
        J_terms: dict mapping qubit index pairs to coupling (J_ij)
        """

        #validate h_terms
        for i, h_i in h_terms.items():
            if not isinstance(i,int) or not isinstance(h_i, float):
                raise ValueError(f"h_terms must be{int: float}, got {type(i): {type(h_i)}}")

        #validate J_terms
        for (i,j), J_ij in J_terms.items():
            if not (isinstance(i,int) and isinstance(j,int) and isinstance(J_ij, float)):
                raise ValueError(f"J_terms must be {(int,int): float}, got {type(i), type(j): {type(J_ij)}}")
          
        self.h = h_terms
        self.J = J_terms

    def __repr__(self) -> str:
        h_str = ", ".join([f"{k}: {v}" for k, v in self.h.items()])
        J_str = ", ".join([f"{k}: {v}" for k, v in self.J.items()])
        return f"Hamiltonian(h={{ {h_str} }}, J={{ {J_str} }})"

    def energy(self, spin_config:dict[int,int]) -> float:
        #validate spin values are +1 or -1
        for i, val in spin_config.items():
            if val not in [-1,1]:
                raise ValueError(f"Spin values must be +1 or -1, got {val}")
            
        #h_terms : sum over h_i * x_i
        h_energy = 0.0
        for i, h_i in self.h.items():
            if i not in spin_config:
                raise ValueError(f"Spin configuration missing key {i}")
            h_energy += h_i * spin_config[i]
        
        #J_terms: sum over J_ij * x_i * x_j
        J_energy = 0.0
        for (i,j), J_ij in self.J.items():
            if i not in spin_config or j not in spin_config:
                raise ValueError(f"Spin config missing keys{i} or {j}")
            J_energy += J_ij * spin_config[i] * spin_config[j]
        
        return h_energy + J_energy