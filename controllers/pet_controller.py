import random
from models.pet_database import PetDatabase

class PetController:
    def __init__(self):
        self.db = PetDatabase()
    
    def generate_pet_id(self):
        return str(random.randint(10000000, 99999999))

    def add_pet(self, pet_type, last_checkup, vaccines, extra):
        pet_id = self.generate_pet_id()
        pet = {
            "รหัสสัตว์": pet_id,
            "ประเภท": pet_type,
            "ตรวจสุขภาพล่าสุด": last_checkup,
            "วัคซีนที่ได้รับ": vaccines
        }
        
        if pet_type == "นกฟินิกซ์" and extra is True:
            self.db.add_pet(pet, accepted=True)
            return f"✅ นกฟินิกซ์ (ID: {pet_id}) ถูกบันทึกเรียบร้อย"
        elif pet_type == "มังกร" and extra <= 70:
            pet["มลพิษควัน"] = extra
            self.db.add_pet(pet, accepted=True)
            return f"✅ มังกร (ID: {pet_id}) ถูกบันทึกเรียบร้อย"
        elif pet_type == "นกฮูก" and extra >= 100:
            pet["ระยะทางบิน"] = extra
            self.db.add_pet(pet, accepted=True)
            return f"✅ นกฮูก (ID: {pet_id}) ถูกบันทึกเรียบร้อย"
        else:
            self.db.add_pet(pet, accepted=False)
            return f"❌ {pet_type} ไม่ผ่านเงื่อนไข!"
    
    def generate_report(self):
        accepted, rejected, type_count = self.db.report()
        report = f"สัตว์ที่รับเข้าโรงเรียน: {accepted} ตัว\n"
        
        # แสดงรายชื่อสัตว์ที่รับเข้าโรงเรียน
        if accepted > 0:
           report += "\n--- รายชื่อสัตว์ที่รับเข้า ---\n"
        for pet_type, count in type_count.items():
            report += f"- {pet_type}: {count} ตัว\n"
    
        report += f"สัตว์ที่ถูกปฏิเสธ: {rejected} ตัว\n"
        return report

