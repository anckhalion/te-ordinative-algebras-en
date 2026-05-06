from .operators import ProportionalOperators, Expression, CoherentContent
from .metric import ResonanceMetric
from .remir import Remir

class ERTDiagnostic:
    """
    Extended Round-Trip (ERT) Diagnostic Protocol (from Chapter 11).
    Evaluates the structural coherence and source fidelity of a decoherent expression.
    """
    
    def __init__(self, metric_engine: ResonanceMetric, threshold: float = 0.5):
        self.metric = metric_engine
        self.theta = threshold
        
    def evaluate_expression(self, expression: Expression, source_content: CoherentContent, delta_mock: float = 0.9) -> dict:
        """
        Executes the 4 steps of the ERT.
        In a real implementation, pi (re-projection) and delta (fidelity) would be computed
        via cross-domain semantic analysis. Here delta is mocked.
        """
        
        # Step 1: Strip
        extracted_invariant, kappa = ProportionalOperators.s_strip(expression)
        
        if kappa < 0.05:
            return {
                "Outcome": "Outcome 4: Structural Void (Type Delta)",
                "Diagnosis": "No structural content survives. The expression is noise.",
                "kappa": kappa,
                "rho": 0.0,
                "delta": 0.0
            }
            
        # Step 2: Source Resonance Check
        # Instead of an identity, the invariant itself is treated as a structural vector map 
        # to see if it resonates with the original Coherent Content.
        # We wrap the invariant in a temporary Remir to reuse the metric engine.
        temp_invariant_identity = Remir(identity_id="temp_inv", semantic_vectors=extracted_invariant.core_vectors)
        
        rho_source = self.metric.calculate_resonance(
            content_vectors=source_content.required_vectors,
            identity=temp_invariant_identity,
            context_compatibility=1.0, # Pure structural check
            temporal_phase=1.0,
            relational_readiness=1.0
        )
        
        if rho_source < self.theta:
            return {
                "Outcome": "Outcome 3: Distorted (Type Gamma)",
                "Diagnosis": "Expression carries structure that does not match its declared source. Propaganda, pathology, or misalignment.",
                "kappa": kappa,
                "rho": rho_source,
                "delta": delta_mock
            }
            
        # Step 3 & 4: Re-projection and Fidelity (Mocked here by delta_mock)
        delta = delta_mock 
        
        if delta >= 0.8:
            if kappa >= 0.7:
                return {
                    "Outcome": "Outcome 1: Full Coherence (Type Alpha)",
                    "Diagnosis": "Ideal collapse. Expression faithfully carries the content.",
                    "kappa": kappa,
                    "rho": rho_source,
                    "delta": delta
                }
            else:
                return {
                    "Outcome": "Outcome 2: Faithful but Shallow (Type Beta)",
                    "Diagnosis": "Accurate but lost significant structural depth. Competent but uninspired.",
                    "kappa": kappa,
                    "rho": rho_source,
                    "delta": delta
                }
        else:
            return {
                "Outcome": "Instability",
                "Diagnosis": "The re-projection fails to reproduce the original. Procedural error or structural instability.",
                "kappa": kappa,
                "rho": rho_source,
                "delta": delta
            }

    def print_report(self, report: dict):
        print("-" * 50)
        print(" EXTENDED ROUND-TRIP DIAGNOSTIC REPORT ")
        print("-" * 50)
        print(f"Outcome   : {report['Outcome']}")
        print(f"Diagnosis : {report['Diagnosis']}")
        print(f"Metrics   : kappa = {report['kappa']:.2f} | rho = {report['rho']:.2f} | delta = {report['delta']:.2f}")
        print("-" * 50)
