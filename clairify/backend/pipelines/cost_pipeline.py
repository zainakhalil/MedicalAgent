import pathway as pw
from schemas.schemas import OrdersSchema, PricingSchema

DEDUCTIBLE = 500
COINSURANCE = 0.2

orders = pw.io.jsonlines.read(
    "../backend/data/orders.jsonl",
    schema=OrdersSchema,
    mode="streaming",
    primary_key="order_id"
)

pricing = pw.io.jsonlines.read(
    "../backend/data/pricing.jsonl",
    schema=PricingSchema,
    mode="streaming",
    primary_key=("procedure_code", "provider_id", "insurance_plan_id")
)

joined = orders.join(
    pricing,
    pw.left.procedure_code == pw.right.procedure_code,
    pw.left.insurance_plan_id == pw.right.insurance_plan_id
)

@pw.udf
def compute_cost(allowed: float):
    if allowed <= 0:
        return 0
    pay_deduct = min(DEDUCTIBLE, allowed)
    remainder = allowed - pay_deduct
    return round(pay_deduct + remainder * COINSURANCE, 2)

cost_table = joined.select(
    order_id = joined.left.order_id,
    patient_id = joined.left.patient_id,
    procedure_code = joined.left.procedure_code,
    provider_id = joined.right.provider_id,
    provider_name = joined.right.provider_name,
    allowed_amount = joined.right.allowed_amount,
    cash_price = joined.right.cash_price,
    estimated_cost = compute_cost(joined.right.allowed_amount)
)

def get_cost_options(order_id: int):
    data = pw.debug.table_to_dict(cost_table)
    results = [v for v in data.values() if v["order_id"] == order_id]
    results.sort(key=lambda x: x["estimated_cost"])
    return {"order_id": order_id, "options": results}

def run_engine():
    pw.run(cost_table)
