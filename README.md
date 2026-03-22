# 💊 Med-Tracker: Medication Expiry Helper (Dual-Validation System)

**Med-Tracker** is a Python-based utility designed to support medication safety by calculating the most appropriate expiry limit after opening or repacking. 

The system performs a **dual-validation process** by comparing the manufacturer’s original expiry date with the **Beyond-Use Date (BUD)**, which applies once a product has been opened or transferred from its original packaging.

---

## 💡 Why I Built This

During my pharmacy practice, I noticed that many patients misunderstand medicine expiry dates after opening.
This is especially a problem for older patients who take multiple medications and may forget when each one expires.

To address this, I developed a simple tool that helps patients track and detect medication expiry more clearly and safely.



**This project was developed to:**
* **Automate** the comparison between manufacturer shelf life and in-use stability.
* **Support** patients managing multiple medications (polypharmacy) without manual calculation.
* **Apply** internationally recognized guidance from **NHS** and **Thai FDA** standards, taking climate differences into account.

---

## 📋 Key Features

* **Dual-Validation Logic:** Automatically determines which limit occurs first: manufacturer expiry or BUD.
* **Localized Standards:** Selectable **English/Deutsch** mode (based on NHS guidance) and **Thai** mode (based on Thai FDA/USP guidance).
* **Storage-Specific Antibiotic Logic:** Specialized calculations for reconstituted antibiotic syrups with two stability windows:
    * **Room Temperature Storage:** 7 days.
    * **Refrigerated Storage (2°C - 8°C):** 14 days.
* **Built-in Safety Restrictions:** Prevents calculation for "repacked" sterile eye or ear drops to ensure patient safety.
* **Step-by-Step Date Entry:** Reduces formatting errors by requesting Day, Month, and Year separately.
* **Multilingual Interface:** Full support for English, German, and Thai terminology.

---

## 🔬 Medical Reference and Stability Logic

Stability recommendations differ depending on the climate zone and regulatory framework. This tool integrates logic derived from publicly available NHS guidance and Thai FDA/USP-based recommendations.

### ⏳ Stability Rules Implemented

| Category | NHS (UK/EU) | Thai FDA (USP) | Condition / Storage |
| :--- | :--- | :--- | :--- |
| **Tablets and Capsules** | 56 days | 180 days | MDS or repacked |
| **Oral liquids** | 30 days | 14 days | Increased microbial risk (Repacked) |
| **Antibiotic syrup** | **7 or 14 days** | **7 or 14 days** | **Room Temp vs. Refrigeration** |
| **Cream in jar** | 30 days | 90 days | Aqueous formulation |
| **Cream/Ointment in tube** | 90 days | 90 days | Tube packaging |
| **Sterile multi-dose drops** | 28 days | 30 days | Eye or ear drops |
| **Single-use sterile drops** | 1 day | 1 day | Preservative-free |
| **Insulin in use** | 28 days | 28 days | In-use protein stability |
| **Inhaler (MDI)** | Label Expiry | Label Expiry | Follow manufacturer label |

---

## 🚀 How to Use

1.  **Run the script:**
    
bash
    python med_tracker.py
    

2.  **Follow the guided prompts:**
    * Select your preferred language and standard.
    * Choose the medication category (1-9).
    * **For antibiotics:** Select your actual storage condition (Room vs. Fridge).
    * **Enter dates:** Input the Day, Month, and Year step-by-step as prompted.
3.  **The system displays:**
    * Calculated Beyond-Use Date (BUD).
    * Remaining days until expiry.
    * Safety status: ✅ **SAFE** or 🛑 **EXPIRED**.

---

## 🛠 Technical Stack

* **Language:** Python 3
* **Modules:** datetime (for precise date arithmetic).
* **Logic:** Dictionary-based rule engine with sterile_warning and is_antibiotic flags.

---

## 📌 Development Journey

This project demonstrates the intersection of healthcare expertise and software engineering:
* **Translation of pharmaceutical regulatory guidance** into structured program logic.
* **Safety-focused conditional logic**, including storage-dependent antibiotic stability.
* **Input validation design** to reduce user error in date formatting.

> **Professional Background Note:**
> The medical reasoning and stability interpretation are based on clinical pharmacy training and publicly available regulatory guidance. AI was used as a coding assistant for structural refinement and formatting.

---

## 📚 Sources

* **Thai FDA:** Guidelines for Assigning Beyond-Use Dates (BUD) in Healthcare Facilities.
* **NHS England:** Guidance Sheet 6 - Storage and Expiry Dates.
* **USP <795>:** Pharmaceutical Compounding - Nonsterile Preparations.

---

## ⚖️ Disclaimer

This tool is intended for **educational and informational purposes only**. 
It does not replace professional medical advice or official manufacturer instructions. Always verify information using the physical label and consult a pharmacist when in doubt.
