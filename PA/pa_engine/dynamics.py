import numpy as np
from typing import Dict, Tuple, Optional
from remir import Remir

class TemporalAttractor:
    """
    Represents an Attractor at a future temporal coordinate.
    Emits a signal sigma that increases in intensity as the system approaches.
    """
    def __init__(self, target_state: dict, kappa: float = 1.0, alpha: float = 2.0):
        self.target_state = target_state # The coherent required state
        self.kappa = kappa               # Base signal strength
        self.alpha = alpha               # Decay exponent (default gravitational is 2.0)

    def calculate_signal_intensity(self, distance: float) -> float:
        """
        Calculates sigma(S, A) = kappa / d(S, A)^alpha.
        """
        if distance <= 0:
            return float('inf') # Singularity / Junction reached
        return self.kappa / (distance ** self.alpha)


class DynamicsEngine:
    """
    Simulates the kinematics of the system in the Proportional Space.
    Applies the Ordinative Acceleration Constant (g_j) to compute the system trajectory
    and manages the Extended Bifurcation Window.
    """
    def __init__(self, 
                 g_j: float = 0.075, # Empirically measured acceleration constant
                 v_0: float = 0.054, # Initial velocity
                 dt: float = 1.0):   # Time step in months
        self.g_j = g_j
        self.v_0 = v_0
        self.dt = dt

    def get_integration_coefficient(self, t: float) -> float:
        """
        Calculates the phase-space traversal progress (IC).
        IC(t) = v_0 * t + 0.5 * g_j * t^2
        """
        return (self.v_0 * t) + (0.5 * self.g_j * (t ** 2))

    def get_time_to_junction(self, target_ic: float = 1.0) -> float:
        """
        Inverse quadratic solve to find t macro when IC(t) = target_ic.
        t_macro = (-v_0 + sqrt(v_0^2 + 2*g_j*IC)) / g_j
        """
        discriminant = (self.v_0 ** 2) + (2 * self.g_j * target_ic)
        if discriminant < 0:
            return -1.0 # Unreachable mathematically, but physically shouldn't happen with g_j > 0
            
        t = (-self.v_0 + np.sqrt(discriminant)) / self.g_j
        return float(t)

    def resolve_bifurcation(self, 
                            system_identity: Remir, 
                            attractor: TemporalAttractor, 
                            arys_inter_actor: bool, 
                            arys_struct_controfase: bool) -> str:
        """
        The Triple Bifurcation routing (Transformation, Postponement, Decomposition)
        executed when IC >= 1.0.
        """
        # 1. Calculate base alignment with the attractor
        # A rudimentary check: does the system have the required target state?
        phi_star = 0.0
        for vec, req_val in attractor.target_state.items():
            sys_val = system_identity.semantic_vectors.get(vec, 0.0)
            if sys_val * req_val > 0: # If directions match
                phi_star += min(abs(sys_val), abs(req_val))
                
        phi_thresh = 0.5 * sum(abs(v) for v in attractor.target_state.values())
        
        # Branch Evaluation
        if phi_star >= phi_thresh and arys_inter_actor:
            return "Branch 1: Transformation"
            
        elif phi_star >= phi_thresh and arys_struct_controfase:
            # Applies the Structural Controfase operator C_s
            return "Branch 2: Postponement (Structural Controfase activated)"
            
        else:
            return "Branch 3: Decomposition (Phase III Diffusion)"
