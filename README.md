# 💊 Med-Tracker: Medication Expiry Helper (NHS-Based)

Med-Tracker is a small Python project I built while learning programming. It helps calculate how long medicines remain safe to use after opening. 

The idea connects my background in pharmacy with my current journey into software development, aiming to bridge the gap between medical standards and everyday safety.

---

## 💡 Why I Built This
During my time working in pharmacy, I noticed that many people were unsure about one important detail:

**The expiry date printed on the box is not always the same as the safe period after opening.**

For example, eye drops may show a manufacturer expiry date years in the future, but once opened they are usually only safe for around 28 days. The same applies to insulin, oral liquids, and certain creams.

Even when pharmacists explain this clearly, patients or caregivers may forget the details later at home. Labels can fade, opening dates may not be written down, and confusion can happen easily — especially in elderly patients managing multiple medications (polypharmacy).

I built this project as a simple way to turn medical guidance into something practical and easy to check again later.

---

## 📋 Project Overview
This is a simple command-line tool that allows users to:
1. **Select a medication category** (English, Thai, and German terms supported)
2. **Enter the opening date** (DD/MM/YYYY)
3. **Receive a calculated expiry date**
4. **See a clear status message** (Safe / Near Expiry / Expired)

The focus is clarity and safety rather than complexity.

---

## 📖 Medical Reference & Global Standards
The expiry logic in this tool is primarily based on:
> **NHS Guidance Sheet 6 – Storage and Expiry Dates**

### 🔬 Comparative Analysis: NHS vs. USP
As a pharmacist, I understand that standards vary depending on the country and clinical context:

* **NHS (UK/Europe):** Recommends a strict **30-day limit** for decanted (repacked) medicines. This aligns with Europe's climate (Zone I/II) and prioritizes maximum drug stability once the original seal is broken.
* **USP (USA/Thailand):** In countries like Thailand, the **USP standard** is often used, which may allow for up to **4 months (120 days)**. This is a practical adjustment for healthcare systems with high patient volumes and different resource management needs.

### 🌡️ The Climate Factor (Why I chose the stricter 30-day rule)
Thailand is in **Climate Zone IVb (Hot & Very Humid)**, while Europe is in **Zone I/II (Temperate)**. High humidity significantly accelerates medicine degradation once removed from the original blister pack. 

Even though local guidelines might allow for a longer period (USP), I have intentionally implemented the **stricter 30-day NHS standard** in this tool. This ensures the highest level of **Patient Safety**, especially in home environments where storage conditions (temperature and humidity) cannot always be strictly controlled.

### ⏳ Example Expiry Rules After Opening (Used in this Tool)
| Formulation | Suggested Expiry | Note |
| :--- | :--- | :--- |
| MDS / Weekly Blister Pack | 56 Days | |
| Oral Liquids / Syrup | 6 Months | |
| Decanted / Repacked | 30 Days | Strict Safety Choice (NHS) |
| Eye, Ear, Nose Drops | 28 Days | |
| Topical Cream (Tube) | 3 Months | |
| Insulin (In Use) | 28 Days | |

---

## ⚠️ If the Opening Date Is Unknown
If someone does not remember the opening date:
* Use the dispensing date as a rough reference.
* Discard the medicine if appearance or smell has changed.
* Ask a pharmacist if unsure.
* Write the opening date clearly on the label next time.

**Safety should always come first.**

---

## 🚀 How to Use
1. Run the Python script `med_tracker.py`.
2. Select your medication type from the menu (1-12).
3. Enter the opening date in **DD/MM/YYYY** format.
4. The system will calculate the expiry and alert you if the medicine is safe or must be discarded.

---

## 🛠 Technical Stack
* **Python 3**
* **`datetime` module**
* **Command-line interface**
* **Dictionary-based data structure**

---

## 📌 What I Learned
Through this project, I practiced:
* **Domain Integration:** Translating written healthcare guidelines into logical software conditions.
* **Data Engineering:** Structuring categorized medical data effectively.
* **Risk Management:** Making informed decisions on which standards to implement based on safety analysis.
* **Programming Skills:** Working with date calculations and designing user-centric CLI.

**Development Note:**
I used AI as a coding assistant while learning. The project idea, structure, and medical reasoning are based on my own professional experience and comparative research of global standards.

---

## 📚 Sources
* **NHS Gloucestershire Health and Care** – Good Practice Guidance for Expiry Dates
* **NHS Cheshire Formulary** – Storage and Expiry Dates Guidance (Sheet 6)
* **ICH Q1A (R2):** Stability Testing of New Drug Substances and Products (Reference for Climate Zones)

---

## ⚖️ Disclaimer
This tool is for educational purposes only. Always verify information using official pharmacy labels and manufacturer instructions.
