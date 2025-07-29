"""Converters between different problem formulations."""

from .qubo import ising_to_qubo, qubo_to_ising

__all__ = ['ising_to_qubo', 'qubo_to_ising']
