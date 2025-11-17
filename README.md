# Clairify 🩺✨  
### AI-Powered Patient Cost & Consent Clarity Assistant  
*Hack With Chicago 2.0 — Track 5: Open Innovation*

Clairify helps patients understand the **true cost**, **real meaning**, and **required steps** behind their medical procedures — *before* care happens.  
It unifies **real-time price transparency**, **plain-language consent explanations**, and **simple medical term translation**, powered by a live **Pathway streaming engine**.

Clairify is built for patients, clinicians, and care teams who need clarity — not confusion — during medical decision-making.

---

## ⚠️ Important Notice  
Clairify is an AI-assisted educational tool.  
It **does not replace** medical advice, clinical judgment, financial counseling, or legally required informed consent.  
All decisions should be confirmed with a licensed clinician.

---

# 🎬 Demo  
https://drive.google.com/file/d/1LjUzzNzO4ycCw8syzALj-DiXLXYSD88A/view?usp=sharing 

---

# ✔ Use Cases We Cover

## 1. Real-Time Medical Order Cost Estimation
Clairify calculates:

- Insurance allowed cost  
- Cash-price alternatives  
- Estimated out-of-pocket (deductible + coinsurance)  
- Cheapest provider across hospital/clinic/imaging  
- Cost-saving recommendations  

**Powered by Pathway:**  
When a *new order appears*, Pathway recomputes costs instantly and updates the UI live.

---

## 2. Smart Consent Understanding (Plain Language)
Clairify converts raw consent text into:

- What is the procedure?  
- Why is it done?  
- Risks  
- Benefits  
- Alternatives  

Readable at a **5th-grade level** so patients can understand before they sign.

---

## 3. Medical Term Translator
Clairify simplifies complex terminology:

- “hypokalemia” → low potassium  
- “MRI with contrast” → MRI scan using dye  
- “sedation risk” → risks from medicine that makes you sleepy  

Multilingual support (optional).

---

## 4. Real-Time Patient Workflow Automation  
Pathway enables instant updates:

- New order appears → show cost comparison immediately  
- Procedure type detected → load relevant consent summary  
- Patient enters medical term → translator explains it instantly  

---

# ❌ What Clairify Does NOT Do

- ❌ Diagnose medical conditions  
- ❌ Provide medical or legal advice  
- ❌ Replace clinician-performed informed consent  
- ❌ Guarantee insurance accuracy  
- ❌ Connect to real hospital EHR systems  
- ❌ Provide advanced multilingual medical translation  

Clairify is a **prototype** demonstrating AI + Pathway + real-time patient education workflows.

---

# 🏗 Architecture

### High-level Data Flow  


## 🧪 How to Use Clairify

- Enter an Order ID → View real-time cost comparison
- Click Consent Summary → Read accessible explanation
- Enter a Medical Term → Get simplified definition
- Update orders.jsonl → UI updates in real time via Pathway

## 🔮 Future Enhancements

- True insurance APIs (FHIR)
- Multilingual consent machine translation
- Real CMS price transparency integration
- Personalized deductible tracking
- Mobile-first UI
