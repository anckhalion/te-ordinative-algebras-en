import numpy as np
from typing import Dict, Tuple, Optional
from .remir import Remir
from .metric import ResonanceMetric

class CoherentContent:
    """Represents the un-collapsed potential (C) in the Coherent Field."""
    def __init__(self, content_id: str, required_vectors: dict, depth: float):
        self.content_id = content_id
        self.required_vectors = required_vectors
        self.depth = depth

class Expression:
    """Represents a decoherent output (E) resulting from a Collapse."""
    def __init__(self, source_content: CoherentContent, identity: Remir, context: str, rho_value: float):
        self.source_content = content_id = source_content.content_id
        self.identity_id = identity.identity_id
        self.context = context
        self.rho_value = rho_value
        
        # Kappa (coherence) is determined post-collapse, roughly correlated to rho and identity depth
        self.kappa = self._calculate_initial_kappa(source_content, identity, rho_value)
        
    def _calculate_initial_kappa(self, content: CoherentContent, identity: Remir, rho: float) -> float:
        # Simplified mock calculation for kappa
        depth_ratio = min(1.0, identity.get_structural_depth() / (content.depth + 0.001))
        return float(np.clip((rho * 0.7) + (depth_ratio * 0.3), 0.0, 1.0))

class StructuralInvariant:
    """Represents the invariant structure (I_k) extracted via Strip."""
    def __init__(self, invariant_type: str, core_vectors: dict):
        self.invariant_type = invariant_type
        self.core_vectors = core_vectors


class ProportionalOperators:
    """
    Implements the core operators of the Proportional Algebra:
    Phi (Collapse), S (Strip), and otimes (Resonance).
    """
    
    @staticmethod
    def phi_collapse(content: CoherentContent, 
                     identity: Remir, 
                     context: str, 
                     metric: ResonanceMetric,
                     threshold: float,
                     context_comp: float = 0.8,
                     temporal_phase: float = 0.9,
                     relational_readiness: float = 1.0) -> Optional[Expression]:
        """
        The Collapse Operator (Phi).
        Maps C x R(I) x K -> D.
        Only executes if rho(C, I, K) >= threshold.
        """
        rho = metric.calculate_resonance(
            content_vectors=content.required_vectors,
            identity=identity,
            context_compatibility=context_comp,
            temporal_phase=temporal_phase,
            relational_readiness=relational_readiness
        )
        
        if rho >= threshold:
            # Type A or B collapse depending on depth
            return Expression(content, identity, context, rho)
        else:
            # Type Delta or Failed collapse
            return None

    @staticmethod
    def s_strip(expression: Expression) -> Tuple[StructuralInvariant, float]:
        """
        The Strip Operator (S).
        Maps D -> I x [0, 1]. Extracts the invariant and returns it with its kappa measure.
        """
        # In a real scenario, this would apply Semantic Algebra NLP/structural extraction to real data.
        # Here we mock the invariant extraction based on the source expression's properties.
        invariant_type = f"I_structural_from_{expression.source_content}"
        
        return StructuralInvariant(invariant_type, {}), expression.kappa

    @staticmethod
    def resonance_otimes(id1: Remir, id2: Remir, coupling_threshold: float = 0.5) -> dict:
        """
        The Resonance Operator (otimes).
        Maps R x R -> C_shared.
        Computes the shared coherent field based on vector alignment between two identities.
        """
        shared_field = {}
        
        # Calculate cross-resonance matrix (simplified dot products between matching vectors)
        common_vectors = set(id1.vector_names).intersection(set(id2.vector_names))
        
        for vec in common_vectors:
            strength1 = id1.semantic_vectors[vec]
            strength2 = id2.semantic_vectors[vec]
            
            b_cross = strength1 * strength2 # Vector alignment
            
            if abs(b_cross) >= coupling_threshold:
                shared_field[vec] = b_cross
                
        return shared_field
