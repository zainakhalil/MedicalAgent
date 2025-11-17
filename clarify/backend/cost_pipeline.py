# backend/cost_pipeline.py

def get_cost_options_for_order(order_id: int):
    """
    TEMP STUB for Role 3.
    Teammate will replace this with real Pathway-based implementation.
    """
    return [
        {
            "order_id": order_id,
            "patient_id": 101,
            "procedure_code": "MRI_BRAIN",
            "insurance_plan_id": "PPO_BASIC",
            "provider_id": "HOSP_1",
            "provider_name": "Downtown Hospital",
            "location": "hospital",
            "allowed_amount": 1200.0,
            "cash_price": 800.0,
            "estimated_patient_cost": 650.0,
        },
        {
            "order_id": order_id,
            "patient_id": 101,
            "procedure_code": "MRI_BRAIN",
            "insurance_plan_id": "PPO_BASIC",
            "provider_id": "IMG_1",
            "provider_name": "City Imaging Center",
            "location": "imaging_center",
            "allowed_amount": 600.0,
            "cash_price": 500.0,
            "estimated_patient_cost": 350.0,
        },
    ]