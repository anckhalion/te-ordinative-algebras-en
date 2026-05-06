import numpy as np
from remir import Remir
from metric import ResonanceMetric
from operators import ProportionalOperators, CoherentContent, Expression
from ert_diagnostic import ERTDiagnostic

def test_h2o_formation():
    print("\n" + "="*50)
    print("TEST 1: H2O Formation (Chemistry Domain, Chap 13)")
    print("="*50)
    
    # 1. Define the Coherent Content (Quantum Field configuration for H2O)
    c_atomic = CoherentContent(
        content_id="H_O_Quantum_Field", 
        required_vectors={"orbital_symmetry": 1.0, "proportional_optimum": 1.0},
        depth=0.8
    )
    
    # 2. Define the Identity (Thermodynamic & Kinetic Conditions: temp 300K, 1 atm)
    # We assign an internal resonance matrix B_I with some depth
    identity_conditions = Remir("Conditions_300K_1atm")
    identity_conditions.add_vector("orbital_symmetry", 0.95, [])
    identity_conditions.add_vector("proportional_optimum", 0.90, [0.8]) # Correlation
    
    # 3. Setup Metric Engine
    engine = ResonanceMetric()
    
    # 4. Execute Collapse
    print(f"Executing Collapse Phi(C, I, K)...")
    # Using high context compatibility, phase, and readiness as per Chapter 13.2.2
    expression_h2o = ProportionalOperators.phi_collapse(
        content=c_atomic,
        identity=identity_conditions,
        context="Aqueous Phase",
        metric=engine,
        threshold=0.6,
        context_comp=0.85,
        temporal_phase=0.92,
        relational_readiness=1.00
    )
    
    if expression_h2o:
        print(f"Collapse SUCCESSFUL. rho = {expression_h2o.rho_value:.3f}, kappa = {expression_h2o.kappa:.3f}")
        
        # 5. Run ERT Diagnostic
        ert = ERTDiagnostic(engine, threshold=0.7)
        # We mock delta=0.82 as in the text (H2O -> Music Consonance)
        report = ert.evaluate_expression(expression_h2o, c_atomic, delta_mock=0.82)
        ert.print_report(report)
    else:
        print("Collapse FAILED (rho < threshold).")


def test_uae_opec_exit():
    print("\n" + "="*50)
    print("TEST 2: UAE OPEC Exit (Civilization Dynamics, April 2026)")
    print("="*50)
    
    # 1. Coherent Content (Attractor pull for fragmentation of the Petrodollar structure)
    c_attractor = CoherentContent(
        content_id="Attractor_Post_OPEC",
        required_vectors={"autonomy_seeking": 1.0, "relational_fracture": 1.0},
        depth=0.9
    )
    
    # 2. Identity (UAE State in April 2026)
    uae_identity = Remir("UAE_State")
    uae_identity.add_vector("autonomy_seeking", 0.95, [])
    uae_identity.add_vector("relational_fracture", 0.85, [0.6]) # Correlation
    
    # 3. Metric Engine
    engine = ResonanceMetric()
    
    # 4. Execute Collapse (Decision to Exit)
    print(f"Executing Collapse Phi(C, I, K)...")
    exit_expression = ProportionalOperators.phi_collapse(
        content=c_attractor,
        identity=uae_identity,
        context="Hormuz Crisis Context",
        metric=engine,
        threshold=0.5,
        context_comp=0.9, # Context strongly favors fragmentation
        temporal_phase=1.0, # Aligned with the micro-junction mu_2
        relational_readiness=0.9
    )
    
    if exit_expression:
        print(f"Collapse SUCCESSFUL. rho = {exit_expression.rho_value:.3f}, kappa = {exit_expression.kappa:.3f}")
        ert = ERTDiagnostic(engine, threshold=0.6)
        report = ert.evaluate_expression(exit_expression, c_attractor, delta_mock=0.95)
        ert.print_report(report)
    else:
        print("Collapse FAILED.")

if __name__ == "__main__":
    test_h2o_formation()
    test_uae_opec_exit()
