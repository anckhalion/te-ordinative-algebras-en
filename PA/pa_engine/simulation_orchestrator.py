import json
import os
import datetime
from remir import Remir
from dynamics import DynamicsEngine, TemporalAttractor

class SimulationOrchestrator:
    """
    Simulates the kinematics of the civilization model bridging Proportional Algebra
    with the macroscopic equations of The Collapse Equation.
    Also handles logging for future LoRA dataset generation.
    """
    def __init__(self, output_dir: str = "./logs"):
        self.engine = DynamicsEngine(g_j=0.075, v_0=0.054)
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def run_bifurcation_simulation(self, 
                                   scenario_name: str,
                                   t_months: float,
                                   system_identity: Remir, 
                                   attractor: TemporalAttractor,
                                   arys_inter: bool,
                                   arys_struct: bool):
        
        print(f"\n--- RUNNING SIMULATION: {scenario_name} ---")
        
        # 1. Compute position in phase space
        ic_t = self.engine.get_integration_coefficient(t_months)
        sigma = attractor.calculate_signal_intensity(distance=max(0.01, 1.0 - ic_t))
        
        print(f"Time t: {t_months:.2f} months from t_0")
        print(f"Integration Coefficient IC(t): {ic_t:.3f} (Saturation at 1.0)")
        print(f"Attractor Pull Intensity (sigma): {sigma:.2f}")
        
        # 2. Check Bifurcation window
        if ic_t >= 1.0:
            print("\n>>> MACRO-JUNCTION REACHED: IC >= 1.0")
            outcome = self.engine.resolve_bifurcation(
                system_identity, attractor, arys_inter, arys_struct
            )
            print(f">>> OUTCOME: {outcome}")
        else:
            print("\n>>> System is within the phase space traversing toward the attractor.")
            t_junction = self.engine.get_time_to_junction()
            print(f">>> Projected time to Macro-Junction: {t_junction:.2f} months.")
            outcome = "Traversal"

        # 3. Log to JSONL for LoRA Training Ground Truth
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "scenario": scenario_name,
            "inputs": {
                "t_months": t_months,
                "g_j": self.engine.g_j,
                "system_vectors": system_identity.semantic_vectors,
                "attractor_target": attractor.target_state,
                "arys_inter_actor": arys_inter,
                "arys_struct_controfase": arys_struct
            },
            "outputs": {
                "ic_t": ic_t,
                "sigma": sigma,
                "outcome": outcome
            }
        }
        
        self._log_to_jsonl(log_entry)

    def _log_to_jsonl(self, entry: dict):
        file_path = os.path.join(self.output_dir, "lora_ground_truth.jsonl")
        with open(file_path, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"--> Logged to {file_path}")

if __name__ == "__main__":
    orchestrator = SimulationOrchestrator()
    
    # Mocking the April 6-7 2026 Structural Controfase Event
    us_system = Remir("US_System_2026")
    us_system.add_vector("hegemonic_stability", 0.6)
    us_system.add_vector("legal_refusal_memory", 0.9) # Strong structural controfase class
    
    # Attractor pulling towards systemic resolution
    macro_attractor = TemporalAttractor(target_state={"hegemonic_stability": -0.8})
    
    # Simulation at t ~ 1.5 months (mid-April approximation for saturation testing)
    orchestrator.run_bifurcation_simulation(
        scenario_name="April 6-7 Controfase Event",
        t_months=2.0, # Push time to simulate crossing the threshold
        system_identity=us_system,
        attractor=macro_attractor,
        arys_inter=False, # No mutual recognition with adversary
        arys_struct=True  # Structural controfase activates
    )
