import time
from datetime import datetime, timedelta

# --- 1. Notification System ---
def announce(text):
    print(f"\n>>> {text.upper()} <<<")

# --- 2. Medication Data (Updated with Temperature Guidance) ---
CATEGORIES = {
    "1": {"name": "MDS / Weekly Blister Pack (จัดแผงรายสัปดาห์ / Wöchentliche Blisterpackung)", "days": 56},
    "2": {"name": "Original Manufacturer Blister (แผงฟอยล์เดิม / Originalblister)", "days": 365},
    "3": {"name": "Decanted Medicine (แบ่งใส่ขวดใหม่ / Umgefüllte Medikamente)", "days": 30},
    "4": {"name": "Oral Liquid / Syrup (ยาน้ำทั่วไป / Saft oder Sirup)", "days": 180},
    
    # --- ปรับปรุงข้อ 5: ยาปฏิชีวนะแยกตามอุณหภูมิ ---
    "5": {"name": "Antibiotics (Room Temp) (ยาปฏิชีวนะผสมน้ำ-อุณหภูมิห้อง / Antibiotika bei Raumtemp)", "days": 7},
    "6": {"name": "Antibiotics (Fridge) (ยาปฏิชีวนะผสมน้ำ-แช่เย็น / Antibiotika im Kühlschrank)", "days": 14},
    
    "7": {"name": "Topical Cream in Jar (ยาทากระปุก / Creme im Tiegel)", "days": 30},
    "8": {"name": "Topical Tube - SKIN ONLY (ยาทาหลอด / Tube für die Haut)", "days": 90},
    "9": {"name": "Standard Eye/Ear Drops (ยาหยอดตาหรือหู / Augen- oder Ohrentropfen)", "days": 28},
    "10": {"name": "Single-use Units (ยาหยอดตารายวัน / Einzeldosen)", "days": 1},
    "11": {"name": "Insulin Pen / Vial (อินซูลินที่กำลังใช้ / Insulin im Gebrauch)", "days": 28},
    "12": {"name": "Inhaler / MDI (ยาพ่น / Inhalator)", "days": 365}
}

def start_app():
    print("========================================")
    print("    MEDISAFE: NHS STORAGE GUIDANCE      ")
    print("========================================")
    print("Welcome. This tool helps you check medicine expiry dates.")
    
    print("\nPLEASE SELECT A CATEGORY:")
    for key, val in CATEGORIES.items():
        print(f"  [{key}] {val['name']}")

    choice = input("\nSELECT NUMBER (1-12): ")

    if choice in CATEGORIES:
        selected = CATEGORIES[choice]
        announce(f"Selected: {selected['name']}")
        
        # --- คำแนะนำเพิ่มเติมเรื่องตู้เย็น ---
        if choice == "6":
            print("(!) Note: Store between 2°C and 8°C. Do not freeze.")
        elif choice == "7":
            print("(!) Warning: For skin use only. Do not put in eyes.")

        print("\n--- ENTER DATE OF OPENING ---")
        try:
            d = int(input("DAY   (DD):   "))
            m = int(input("MONTH (MM):   "))
            y = int(input("YEAR  (YYYY): "))
            
            open_date = datetime(y, m, d)
            expiry_date = open_date + timedelta(days=selected['days'])
            days_left = (expiry_date - datetime.now()).days

            print("\n" + "*"*45)
            if days_left < 0:
                print("!!!  WARNING: EXPIRED - DISCARD IMMEDIATELY  !!!")
                print(f"Expired on: {expiry_date.strftime('%d/%m/%Y')}")
            else:
                print("            STATUS: SAFE TO USE            ")
                print(f"Calculated Expiry: {expiry_date.strftime('%d/%m/%Y')}")
                print(f"Days remaining: {days_left} days")
            print("*"*45)

        except ValueError:
            print("\nError: Invalid date format.")
    else:
        print("\nError: Invalid choice.")

if __name__ == "__main__":
    start_app()
