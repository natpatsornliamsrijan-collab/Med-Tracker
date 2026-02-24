# 💊 MediSafe: NHS-Standard Medication Expiry Calculator

A Python tool designed to improve patient safety by calculating the precise expiry date of medications after they have been opened. This project is specifically tailored for care home settings and individuals managing multiple medications (Polypharmacy).

## 📋 Project Overview
Many medications have a shortened shelf life once the original seal is broken. This tool helps users:
1. Select the correct medication category.
2. Enter the date of opening (Day/Month/Year).
3. Receive an instant expiry date calculation and voice notification.

## ⚖️ Medical Guidance & References
The calculation logic in this software is strictly based on official healthcare guidelines:
* **NHS Gloucestershire Health and Care:** Good Practice Guidance for Expiry Dates.
* **NHS Cheshire Formulary:** Storage and Expiry Dates Guidance (Sheet 6).

### Key Expiry Rules Implemented:
* **MDS/Blister Packs:** 56 days (8 weeks) from dispensing.
* **Oral Liquids:** 6 months (180 days) after opening.
* **Eye/Ear/Nose Drops:** 28 days (1 month) after opening.
* **Insulin (In-use):** 28 days at room temperature.
* **Antibiotics (Reconstituted):** 7 days after mixing.

## 🚀 How to Use
1. Run the Python script.
2. Listen to the voice options (TTS enabled).
3. Select your medication type (1-12).
4. Enter the opening date in **DD/MM/YYYY** format.
5. The system will alert you if the medicine is safe to use or must be discarded.

---
**Disclaimer:** This tool is for educational purposes and to assist in tracking. Always verify with the physical label provided by your pharmacist and the manufacturer's instructions.# medisafe-nhs-calc
Medication Expiry Calculator based on NHS Guidance.
