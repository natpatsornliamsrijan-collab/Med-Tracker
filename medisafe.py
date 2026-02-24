import time
from datetime import datetime, timedelta

# --- 1. Medication Data Configuration ---
# days_thai: Strictly following your Thai FDA transcript (USP 795)
# days_nhs: Following NHS UK standards
CATEGORIES = {
    "1": {
        "en_de": "MDS / Weekly Blister Pack (Wöchentliche Blisterpackung)", 
        "th": "ยาเม็ด / แคปซูล (แบ่งใส่แผงรายสัปดาห์)", 
        "days_nhs": 56, 
        "days_thai": 180  # Thai FDA: Max 6 months
    },
    "2": {
        "en_de": "Original Blister Pack (Originalblister)", 
        "th": "ยาเม็ดในแผงฟอยล์เดิม", 
        "days_nhs": 3650, 
        "days_thai": 3650  # Use Manufacturer Expiry
    },
    "3": {
        "en_de": "Repacked Medicine (Umgefüllte Medikamente)", 
        "th": "ยาที่แบ่งใส่ขวดใหม่", 
        "days_nhs": 30, 
        "days_thai": 180  # Thai FDA: Max 6 months (as per tablets/powders repackaged)
    },
    "4": {
        "en_de": "Oral Liquid / Syrup (Saft oder Sirup)", 
        "th": "ยาน้ำทั่วไป / ยาน้ำเชื่อม (แบ่งบรรจุ)", 
        "days_nhs": 180, 
        "days_thai": 14   # Thai FDA: Max 14 days (Refrigerated 2-8°C)
    },
    "5": {
        "en_de": "Antibiotic Syrup - Room Temp (Antibiotika - Raumtemp.)", 
        "th": "ยาปฏิชีวนะผสมน้ำ (อุณหภูมิห้อง)", 
        "days_nhs": 7, 
        "days_thai": 7
    },
    "6": {
        "en_de": "Antibiotic Syrup - Fridge (Antibiotika - Kühlschrank)", 
        "th": "ยาปฏิชีวนะผสมน้ำ (ตู้เย็น)", 
        "days_nhs": 14, 
        "days_thai": 14
    },
    "7": {
        "en_de": "Cream in Jar - Aqueous (Creme im Tiegel)", 
        "th": "ยาทากระปุก (สูตรน้ำ/Aqueous)", 
        "days_nhs": 30, 
        "days_thai": 30   # Thai FDA: Max 30 days
    },
    "8": {
        "en_de": "Cream/Ointment Tube (Creme / Salbe in der Tube)", 
        "th": "ยาทาหลอด / สูตรไม่มีน้ำ (Non-aqueous)", 
        "days_nhs": 90, 
        "days_thai": 90   # Thai FDA: Max 90 days
    },
    "9": {
        "en_de": "Eye / Ear Drops (Augen- / Ohrentropfen)", 
        "th": "ยาหยอดตา / หู", 
        "days_nhs": 28, 
        "days_thai": 30   # Thai FDA: 1 month after opening
    },
    "10": {
        "en_de": "Single-dose Eye Drops (Einzeldosis-Augentropfen)", 
        "th": "ยาหยอดตาหลอดเล็ก (SDU)", 
        "days_nhs": 1, 
        "days_thai": 1
    },
    "11": {
        "en_de": "Insulin - In Use (Insulin - im Gebrauch)", 
        "th": "อินซูลินที่กำลังใช้งาน", 
        "days_nhs": 28, 
        "days_thai": 28
    },
    "12": {
        "en_de": "Inhaler / MDI (Inhalator)", 
        "th": "ยาพ่น (Inhaler)", 
        "days_nhs": 3650, 
        "days_thai": 3650
    }
}

def start_app():
    # User selects language preference at the start
    print("========================================")
    print("      MED-TRACKER: GLOBAL STANDARDS     ")
    print("========================================")
    print("Choose Language / Sprache wählen:")
    print("1. English / Deutsch (NHS Standard)")
    print("2. ภาษาไทย (Thai FDA / USP Standard)")
    
    lang_choice = input("\nSelect (1/2): ")
    is_thai = lang_choice == "2"

    while True:
        menu_title = "--- SELECT CATEGORY ---" if not is_thai else "--- เลือกหมวดหมู่ยา ---"
        print(f"\n{menu_title}")
        
        for key, val in CATEGORIES.items():
            name = val['th'] if is_thai else val['en_de']
            print(f"  [{key}] {name}")

        choice = input("\nChoice (1-12) [or 'q' to quit]: ")
        
        if choice.lower() == 'q':
            break

        if choice in CATEGORIES:
            item = CATEGORIES[choice]
            # Select days based on language/standard
            days = item['days_thai'] if is_thai else item['days_nhs']
            
            if days > 1000:
                msg = ">>> Follow Manufacturer's Expiry Date <<<" if not is_thai else ">>> ใช้ตามวันหมดอายุที่ระบุบนกล่อง <<<"
                print(f"\n{msg}")
            else:
                try:
                    prompt = "Enter Opening Date:" if not is_thai else "กรอกวันที่เริ่มเปิดใช้งาน:"
                    print(f"\n{prompt}")
                    d = int(input("  DD: "))
                    m = int(input("  MM: "))
                    y = int(input("  YYYY: "))
                    
                    open_date = datetime(y, m, d)
                    expiry_date = open_date + timedelta(days=days)
                    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                    days_left = (expiry_date - today).days

                    print("\n" + "*"*45)
                    if days_left < 0:
                        if not is_thai:
                            print("!!! EXPIRED (ABGELAUFEN) !!!")
                            print(f"Status: Please discard. Expired on: {expiry_date.strftime('%d/%m/%Y')}")
                        else:
                            print("!!! ยาหมดอายุแล้ว !!!")
                            print(f"สถานะ: ควรทิ้งทันที (หมดอายุเมื่อ: {expiry_date.strftime('%d/%m/%Y')})")
                    else:
                        if not is_thai:
                            print("STATUS: SAFE TO USE (SICHER)")
                            print(f"EXPIRY (ABLAUFDATUM): {expiry_date.strftime('%d/%m/%Y')}")
                            print(f"REMAINING: {days_left} Days (Tage)")
                        else:
                            print("สถานะ: ✅ ยังใช้ได้")
                            print(f"วันหมดอายุ: {expiry_date.strftime('%d/%m/%Y')}")
                            print(f"เหลืออีก: {days_left} วัน")
                    print("*"*45)

                except ValueError:
                    err = "Invalid date!" if not is_thai else "วันที่ไม่ถูกต้อง!"
                    print(f"\nError: {err}")
            
            again_prompt = "\nCheck another item? (y/n): " if not is_thai else "\nตรวจสอบรายการอื่นต่อไหม? (y/n): "
            again = input(again_prompt)
            if again.lower() != 'y':
                break
        else:
            err_choice = "Invalid selection!" if not is_thai else "เลือกไม่ถูกต้อง!"
            print(f"\nError: {err_choice}")

    bye = "Goodbye! / Auf Wiedersehen!" if not is_thai else "ขอบคุณที่ใช้งานค่ะ!"
    print(f"\n{bye}")

if __name__ == "__main__":
    start_app()
