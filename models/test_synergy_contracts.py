from synergy_contracts import CONTRACT_ID, model_consistency_payload

def test_model_consistency_stays_computational():
    p=model_consistency_payload(
        experiment_id="cn-1",max_abs_error=0.0,hypothesis_label="DERIVED",
        assumptions=["graph reproduces tabular bookkeeping only"]
    )
    assert CONTRACT_ID=="synergy.science.model-consistency/v1"
    assert p["table_graph_gate_pass"] is True
    assert p["observed_physical_effect"] is False
    assert p["causal_claim_authority"] is False
