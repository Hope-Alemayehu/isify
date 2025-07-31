from problems.number_partitioning import number_partitioning
from core.base import Hamiltonian

def test_partitioning_builds_correct_hamiltonian():
    numbers = [3,1,4]
    H = number_partitioning(numbers)
    
    assert H.h == {}
    assert H.J == {
        (0,1): 3*1,
        (0,2): 3*4,
        (1,2): 1*4,
    }