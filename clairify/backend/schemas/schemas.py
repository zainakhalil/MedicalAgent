import pathway as pw

class OrdersSchema(pw.Schema):
    order_id: int
    patient_id: int
    procedure_code: str
    location: str
    insurance_plan_id: str
    timestamp: str

class PricingSchema(pw.Schema):
    procedure_code: str
    provider_id: str
    provider_name: str
    location: str
    insurance_plan_id: str
    allowed_amount: float
    cash_price: float
