class PetView:
    def __init__(self, controller):
        self.controller = controller

    def add_phoenix_view(self):
        # การเพิ่มข้อมูลสำหรับนกฟินิกซ์
        pet_type = "นกฟินิกซ์"
        last_checkup = input("วันที่ตรวจสุขภาพล่าสุด (DD/MM/YYYY): ")
        vaccines = int(input("จำนวนวัคซีนที่ได้รับ: "))
        fire_proof = input("มีใบรับรองไฟไม่ลามหรือไม่? (yes/no): ") == "yes"
        result = self.controller.add_pet(pet_type, last_checkup, vaccines, fire_proof)
        print(result)

    def add_dragon_view(self):
        # การเพิ่มข้อมูลสำหรับมังกร
        pet_type = "มังกร"
        last_checkup = input("วันที่ตรวจสุขภาพล่าสุด (DD/MM/YYYY): ")
        vaccines = int(input("จำนวนวัคซีนที่ได้รับ: "))
        pollution = int(input("ระดับมลพิษจากควัน (%): "))
        result = self.controller.add_pet(pet_type, last_checkup, vaccines, pollution)
        print(result)

    def add_owl_view(self):
        # การเพิ่มข้อมูลสำหรับนกฮูก
        pet_type = "นกฮูก"
        last_checkup = input("วันที่ตรวจสุขภาพล่าสุด (DD/MM/YYYY): ")
        vaccines = int(input("จำนวนวัคซีนที่ได้รับ: "))
        flight_distance = int(input("ระยะทางบินได้โดยไม่ทานข้าว (km): "))
        result = self.controller.add_pet(pet_type, last_checkup, vaccines, flight_distance)
        print(result)

    def show_report(self):
        # แสดงรายงาน
        print(self.controller.generate_report())