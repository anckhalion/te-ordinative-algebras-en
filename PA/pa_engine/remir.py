import numpy as np

class Remir:
    """
    Representation of an Identity in the Proportional Space (P).
    A Remir R(I) = (V_I, B_I) consists of:
    - V_I: Semantic Vectors (the capacity to access specific regions of the Coherent Field)
    - B_I: Internal Resonance Matrix (the proportional relations between those vectors)
    """
    def __init__(self, identity_id: str, semantic_vectors: dict = None, resonance_matrix: np.ndarray = None):
        """
        Initialize a new Remir.
        :param identity_id: Unique identifier for this identity.
        :param semantic_vectors: Dictionary mapping vector_name to a numerical value (capacity/strength).
        :param resonance_matrix: NxN numpy array representing the non-commutative proportional relations.
        """
        self.identity_id = identity_id
        self.semantic_vectors = semantic_vectors if semantic_vectors is not None else {}
        self.vector_names = list(self.semantic_vectors.keys())
        
        # If no matrix is provided, initialize an identity matrix (no structural depth)
        if resonance_matrix is not None:
            self._validate_matrix(resonance_matrix)
            self.B_I = resonance_matrix
        else:
            n = len(self.vector_names)
            self.B_I = np.eye(n) if n > 0 else np.array([])
            
        self.trajectory_history = [] # History of collapses (E) and updates (U)
            
    def _validate_matrix(self, matrix: np.ndarray):
        n = len(self.vector_names)
        if matrix.shape != (n, n):
            raise ValueError(f"Resonance matrix shape {matrix.shape} does not match number of vectors {n}.")
            
    def add_vector(self, name: str, strength: float, correlations: list = None):
        """
        Add a new semantic vector to the Remir and update the resonance matrix.
        correlations: List of float values representing the correlation with existing vectors.
        """
        self.semantic_vectors[name] = strength
        self.vector_names.append(name)
        
        n = len(self.vector_names)
        new_matrix = np.eye(n)
        
        if n > 1:
            # Copy old matrix into the top-left of the new matrix
            new_matrix[:n-1, :n-1] = self.B_I
            
            # Apply correlations if provided (non-commutative, so row and col can differ, 
            # but for simplicity we initialize symmetrically if only a list is passed)
            if correlations and len(correlations) == n - 1:
                for i in range(n - 1):
                    new_matrix[i, n-1] = correlations[i]
                    new_matrix[n-1, i] = correlations[i] # Initial symmetric default
                    
        self.B_I = new_matrix

    def get_structural_depth(self) -> float:
        """
        Calculate the proportional depth of the identity based on its internal coherence (b_bar).
        An identity with a highly structured B_I has higher capacity for deep collapses.
        """
        if self.B_I.size == 0:
            return 0.0
            
        # Simplified calculation: average of non-diagonal off-elements
        n = self.B_I.shape[0]
        if n == 1:
            return 1.0 # Base coherence
            
        off_diagonals = self.B_I[~np.eye(n, dtype=bool)]
        return float(np.mean(np.abs(off_diagonals)))
        
    def get_dominant_vector(self) -> str:
        """
        Returns the name of the semantic vector with the highest structural integration.
        In PA terms, lambda(I).
        """
        if not self.vector_names:
            return None
            
        # The dominant vector is the one with the highest sum of absolute resonances
        integration_scores = np.sum(np.abs(self.B_I), axis=1)
        dominant_index = np.argmax(integration_scores)
        return self.vector_names[dominant_index]

    def update_from_experience(self, expression_impact: dict, plasticity: float = 0.1):
        """
        The U (Update) operator: modifies the Remir based on a new decoherent expression or encounter.
        expression_impact: dict mapping vector_name to a delta change.
        plasticity: how easily the B_I matrix restructures.
        """
        self.trajectory_history.append(expression_impact)
        
        # 1. Update vector strengths
        for name, delta in expression_impact.items():
            if name in self.semantic_vectors:
                self.semantic_vectors[name] += delta * plasticity
            else:
                self.add_vector(name, delta)
                
        # 2. Restructure B_I (simplified placeholder logic)
        # In the full model, repeated activation of vectors together increases their resonance.
        active_vectors = [i for i, name in enumerate(self.vector_names) if name in expression_impact]
        for i in active_vectors:
            for j in active_vectors:
                if i != j:
                    # Non-commutative update: order matters in real experience, here simplified
                    self.B_I[i, j] += plasticity * expression_impact[self.vector_names[i]] * 0.1
                    
        # Normalize slightly to prevent explosion
        np.clip(self.B_I, -1.0, 1.0, out=self.B_I)

    def __repr__(self):
        depth = self.get_structural_depth()
        dominant = self.get_dominant_vector()
        return f"<Remir '{self.identity_id}' | {len(self.vector_names)} vectors | Depth: {depth:.2f} | Dom: {dominant}>"
