import numpy as np
from typing import Dict
from .remir import Remir

class ResonanceMetric:
    """
    Computes the Resonance Metric rho(C, I, K) which determines if a collapse can occur.
    The metric is a composite of 5 components, weighted by default operational values,
    though these weights can be dynamically tuned.
    """
    
    # Default heuristic weights as defined in PA Foundations (Chapter 5 & 18)
    DEFAULT_WEIGHTS = {
        'v': 0.25, # Vectorial Alignment
        'd': 0.20, # Proportional Depth
        'K': 0.15, # Contextual Compatibility
        'tau': 0.15, # Temporal Phase
        'R': 0.25  # Relational Readiness
    }

    def __init__(self, weights: Dict[str, float] = None):
        self.weights = weights if weights else self.DEFAULT_WEIGHTS
        self._validate_weights()

    def _validate_weights(self):
        total = sum(self.weights.values())
        if not np.isclose(total, 1.0):
            raise ValueError(f"Resonance weights must sum to 1.0, got {total}")

    def calculate_resonance(self, 
                            content_vectors: dict, 
                            identity: Remir, 
                            context_compatibility: float, 
                            temporal_phase: float, 
                            relational_readiness: float) -> float:
        """
        Calculates the composite resonance metric rho.
        
        :param content_vectors: dict representing the structural vectors required by the Coherent Content C.
        :param identity: The Remir R(I) attempting the collapse.
        :param context_compatibility: Context K alignment [0, 1].
        :param temporal_phase: Synchronization with systemic pulsation tau [0, 1].
        :param relational_readiness: Lack of internal/external resistance [0, 1].
        :return: Float value of rho in [0, 1].
        """
        
        rho_v = self._calculate_vectorial_alignment(content_vectors, identity)
        rho_d = self._calculate_proportional_depth(content_vectors, identity)
        rho_K = max(0.0, min(1.0, context_compatibility))
        rho_tau = max(0.0, min(1.0, temporal_phase))
        rho_R = max(0.0, min(1.0, relational_readiness))
        
        rho_total = (
            self.weights['v'] * rho_v +
            self.weights['d'] * rho_d +
            self.weights['K'] * rho_K +
            self.weights['tau'] * rho_tau +
            self.weights['R'] * rho_R
        )
        
        return float(np.clip(rho_total, 0.0, 1.0))

    def _calculate_vectorial_alignment(self, content_vectors: dict, identity: Remir) -> float:
        """
        rho_v: Computes how well the identity's semantic vectors align with the content requirements.
        Uses normalized dot product logic over shared dimensions.
        """
        if not content_vectors or not identity.semantic_vectors:
            return 0.0
            
        alignment_score = 0.0
        total_content_strength = sum(abs(v) for v in content_vectors.values())
        
        if total_content_strength == 0:
            return 1.0 # Empty content aligns trivially
            
        for vec_name, c_strength in content_vectors.items():
            if vec_name in identity.semantic_vectors:
                # Basic alignment: matching magnitude and direction
                i_strength = identity.semantic_vectors[vec_name]
                # If they share the same direction (sign), it's positive alignment
                if c_strength * i_strength > 0:
                    alignment_score += min(abs(c_strength), abs(i_strength))
                    
        return float(alignment_score / total_content_strength)

    def _calculate_proportional_depth(self, content_vectors: dict, identity: Remir) -> float:
        """
        rho_d: Checks if the identity has enough internal complexity (depth) to hold the content.
        """
        content_complexity = len(content_vectors) * 0.2 # Rough heuristic for content complexity
        identity_depth = identity.get_structural_depth()
        
        if content_complexity == 0:
            return 1.0
            
        # Depth penalty if identity is too shallow for the content
        depth_ratio = identity_depth / content_complexity
        return float(min(1.0, depth_ratio))
