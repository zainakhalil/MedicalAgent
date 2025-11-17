# backend/cost_pipeline.py

import pathway as pw

from .schemas import OrdersSchema, PricingSchema

# ---------------------------
# Simple "fake" insurance logic
# ---------------------------
# In real life this depends on individual deductible, OOP max, etc.
# For the hackathon we hard-code something just to demonstrate the idea.
DEDUCTIBLE_REMAINING = 500.0   # patient still has $500 of deductible left
COINSURANCE_RATE = 0.2         # after deductible, patient pays 20% of remaining


# ---------------------------------
# 1) Read orders.jsonl as a stream
# ---------------------------------
# mode="streaming" tells Pathway to treat this as a live data source
orders = pw.io.jsonlines.read(
    "data/orders.jsonl",        # path relative to project root
    schema=OrdersSchema,        # the schema we defined
    mode="streaming",           # streaming = incremental updates
    primary_key="order_id",     # unique key per order
)


# ---------------------------------
# 2) Read pricing.jsonl as a stream
# ---------------------------------
pricing = pw.io.jsonlines.read(
    "data/pricing.jsonl",
    schema=PricingSchema,
    mode="streaming",
    # composite primary key (procedure, provider, plan)
    primary_key=("procedure_code", "provider_id", "insurance_plan_id"),
)


# ---------------------------------
# 3) Join orders with pricing
# ---------------------------------
# We want, for each order, all matching pricing rows
# matching by procedure_code AND insurance_plan_id.
joined = orders.join(
    pricing,
    pw.left.procedure_code == pw.right.procedure_code,
    pw.left.insurance_plan_id == pw.right.insurance_plan_id,
)


# ---------------------------------
# 4) UDF: estimate patient cost from allowed amount
# ---------------------------------
@pw.udf
def estimate_patient_cost(allowed_amount: float) -> float:
    """
    Very simplified insurance math:
    - Patient pays deductible first (up to DEDUCTIBLE_REMAINING).
    - Then they pay a percentage (COINSURANCE_RATE) of the remaining.
    """
    if allowed_amount <= 0:
        return 0.0

    # Patient pays up to the deductible amount first
    patient_portion = min(DEDUCTIBLE_REMAINING, allowed_amount)

    # Whatever is left after deductible
    remaining = max(0.0, allowed_amount - DEDUCTIBLE_REMAINING)

    # Coinsurance applies to the remaining part
    patient_portion += COINSURANCE_RATE * remaining

    # Round for nicer display
    return round(patient_portion, 2)


# ---------------------------------
# 5) Build final "cost_table" with all needed columns
# ---------------------------------
cost_table = joined.select(
    # order info
    order_id=joined.left.order_id,
    patient_id=joined.left.patient_id,
    procedure_code=joined.left.procedure_code,
    insurance_plan_id=joined.left.insurance_plan_id,

    # provider info (from pricing)
    provider_id=joined.right.provider_id,
    provider_name=joined.right.provider_name,
    location=joined.right.location,

    # money fields
    allowed_amount=joined.right.allowed_amount,
    cash_price=joined.right.cash_price,
    estimated_patient_cost=estimate_patient_cost(joined.right.allowed_amount),
)


# ---------------------------------
# 6) Helper function used by the API layer
# ---------------------------------
def get_cost_options_for_order(order_id: int):
    """
    Return a list of pricing options for a given order_id.

    Each option is a dict like:
    {
      'order_id': ...,
      'patient_id': ...,
      'procedure_code': ...,
      'insurance_plan_id': ...,
      'provider_id': ...,
      'provider_name': ...,
      'location': ...,
      'allowed_amount': ...,
      'cash_price': ...,
      'estimated_patient_cost': ...
    }

    The API teammate (Role 3) will call this.
    """

    # pw.debug.table_to_dict() materializes the current table into a Python dict
    snapshot = pw.debug.table_to_dict(cost_table)
    # snapshot format: {internal_row_id: {column_name: value, ...}, ...}

    # Filter rows by order_id
    options = [
        row for row in snapshot.values()
        if row["order_id"] == order_id
    ]

    # Sort from cheapest to most expensive for nice UI display
    options.sort(key=lambda r: r["estimated_patient_cost"])

    return options


# ---------------------------------
# 7) Dev-only: run Pathway and print updates
# ---------------------------------
# You can run this file directly to see what Pathway outputs.
if __name__ == "__main__":
    # This will keep the program running and reacting to file changes
    # in data/orders.jsonl and data/pricing.jsonl (in streaming mode).
    pw.run(cost_table)
