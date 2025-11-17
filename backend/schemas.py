# backend/schemas.py

import pathway as pw

# Schema for incoming "orders" (what the doctor ordered for the patient)
class OrdersSchema(pw.Schema):
    # Unique ID of this order (e.g., 1, 2, 3...)
    order_id: int

    # Patient identifier (fake ID for hackathon purposes)
    patient_id: int

    # What procedure/test was ordered (e.g., "MRI_BRAIN", "COLONOSCOPY")
    procedure_code: str

    # Where the doctor initially wants to do it (e.g., "hospital")
    location: str

    # Which insurance plan the patient has (used for pricing rules)
    insurance_plan_id: str

    # When the order was placed (ISO datetime string; okay to keep as str)
    timestamp: str


# Schema for pricing options (this is like a mini "price list" table)
class PricingSchema(pw.Schema):
    # Code of the procedure/test (must match OrdersSchema.procedure_code)
    procedure_code: str

    # Provider ID (e.g., "HOSP_1", "IMG_1")
    provider_id: str

    # Human-readable provider name (shown in UI)
    provider_name: str

    # Location type (e.g., "hospital", "imaging_center", "clinic")
    location: str

    # Insurance plan that this price applies to
    insurance_plan_id: str

    # Negotiated allowed amount by insurance for this procedure at this provider
    allowed_amount: float

    # Cash price if patient pays out-of-pocket instead of using insurance
    cash_price: float
