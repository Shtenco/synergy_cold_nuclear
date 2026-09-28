from __future__ import annotations
from typing import Any

from nuclear_graph_consistency import build_graph

CONTRACT_ID = "synergy.science.model-consistency/v1"
AUTHORITY = "scientific_model_consistency"


def model_consistency_payload(
    *,
    experiment_id: str,
    max_abs_error: float,
    hypothesis_label: str,
    assumptions: list[str],
) -> dict[str, Any]:
    if not experiment_id.strip():
        raise ValueError("experiment_id required")
    if max_abs_error < 0:
        raise ValueError("max_abs_error cannot be negative")
    if hypothesis_label not in {"EVALUATED","DERIVED","HYPOTHESIS","STRESS_TEST","LEGACY"}:
        raise ValueError("invalid scientific label")
    if not assumptions:
        raise ValueError("assumptions required")
    g = build_graph()
    return {
        "experiment_id": experiment_id,
        "max_abs_error": float(max_abs_error),
        "table_graph_gate_pass": bool(max_abs_error < 1e-12),
        "graph_nodes": g.number_of_nodes(),
        "graph_edges": g.number_of_edges(),
        "epistemic_status": hypothesis_label,
        "assumptions": list(assumptions),
        "observed_physical_effect": False,
        "causal_claim_authority": False,
    }
