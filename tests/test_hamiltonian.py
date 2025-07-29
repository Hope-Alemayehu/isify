from core.base import Hamiltonian

def test_hamiltonian_repr():
    h = {0: -1.0, 1:0.5}
    J ={(0,1): -0.8, (1,2):0.3}
    H = Hamiltonian(h,J)

    expected_repr = "Hamiltonian(h={ 0: -1.0, 1: 0.5 }, J={ (0, 1): -0.8, (1, 2): 0.3 })"
    actual_repr = repr(H)

    assert actual_repr == expected_repr, f"Expected: {expected_repr}, got: {actual_repr}"

def test_hamiltonian_energy():
    h = {0: -1.0, 1:0.5}
    J ={(0,1): -0.8, (1,2):0.3}
    H = Hamiltonian(h,J)

    spin_config = {0: 1, 1:-1,2:1}   # x0 = +1, x1 = -1, x2 = +1
    # Energy = h0*x0 + h1*x1 + J01*x0*x1 + J12*x1*x2
    #        = -1.0*1 + 0.5*(-1) + (-0.8)*1*(-1) + 0.3*(-1)*1
    #        = -1.0 -0.5 + 0.8 - 0.3 = -1.0
    expected_energy = -1.0
    actual_energy = H.energy(spin_config)

    assert abs(actual_energy - expected_energy) < 1e-6, f"Expected: {expected_energy}, got: {actual_energy}"
