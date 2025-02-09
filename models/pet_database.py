import json

class PetDatabase:
    def __init__(self, filename="petss.json"):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {"accepted": [], "rejected": []}

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)  

    def add_pet(self, pet, accepted=True):
        key = "accepted" if accepted else "rejected"
        self.data[key].append(pet)
        self.save_data()

    def report(self):
        accepted_count = len(self.data["accepted"])
        rejected_count = len(self.data["rejected"])
        type_count = {"นกฟินิกซ์": 0, "มังกร": 0, "นกฮูก": 0}
        
        for pet in self.data["accepted"]:
            type_count[pet["ประเภท"]] += 1
        
        return accepted_count, rejected_count, type_count
