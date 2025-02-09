from controllers.pet_controller import PetController
from views.pet_view import PetView

if __name__ == "__main__":
    controller = PetController()
    view = PetView(controller)
    
    while True:
        print("\n--- ระบบจัดการสัตว์เลี้ยงเวทมนตร์ ---")
        print("1. เพิ่มนกฟินิกซ์\n2. เพิ่มมังกร\n3. เพิ่มนกฮูก\n4. รายงานสถานะ\n5. ออกจากระบบ")
        choice = input("เลือกตัวเลือก: ")
        
        if choice == "1":
            view.add_phoenix_view()
        elif choice == "2":
            view.add_dragon_view()
        elif choice == "3":
            view.add_owl_view()
        elif choice == "4":
            view.show_report()
        elif choice == "5":
            print("👋 ออกจากระบบ...")
            break
        else:
            print("❌ กรุณาเลือกตัวเลือกที่ถูกต้อง")

1