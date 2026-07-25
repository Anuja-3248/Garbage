class Sorting:
    cities = {
        "Bengaluru": 0, "Chennai": 0, "Delhi": 0, "Hyderabad": 0, "Kochi": 0, 
        "Kolkata": 0, "Mumbai": 0, "Noida": 0, "Pune": 0
    }
    
    genders = {
        "Male": 0, "Female": 0
    }
    
    salary_ranges = {
        "40000 - 70000": [],
        "70001 - 100000": [],
        "100001+": []
    }

    def __init__(self, id, list):
        self.id = id
        self.name = list[0]  
        self.post = list[1]  
        self.place = list[2].lower()
        self.gender = list[3].lower()
        self.salary = list[4]

    def PlaceSorter(self):
        
        b = Sorting.cities["Bengaluru"]
        c = Sorting.cities["Chennai"]
        d = Sorting.cities["Delhi"]
        h = Sorting.cities["Hyderabad"]
        ko = Sorting.cities["Kochi"]
        kl = Sorting.cities["Kolkata"]
        m = Sorting.cities["Mumbai"]
        n = Sorting.cities["Noida"]
        p = Sorting.cities["Pune"]

        if self.place == "bengaluru":
            b += 1
            Sorting.cities["Bengaluru"] = b
        elif self.place == "chennai":
            c += 1
            Sorting.cities["Chennai"] = c
        elif self.place == "delhi":
            d += 1
            Sorting.cities["Delhi"] = d
        elif self.place == "hyderabad":
            h += 1
            Sorting.cities["Hyderabad"] = h
        elif self.place == "kochi":
            ko += 1
            Sorting.cities["Kochi"] = ko
        elif self.place == "kolkata":
            kl += 1
            Sorting.cities["Kolkata"] = kl
        elif self.place == "mumbai":
            m += 1
            Sorting.cities["Mumbai"] = m
        elif self.place == "noida":
            n += 1
            Sorting.cities["Noida"] = n
        elif self.place == "pune":
            p += 1
            Sorting.cities["Pune"] = p

    def GenderSorter(self):
        
        m_count = Sorting.genders["Male"]
        f_count = Sorting.genders["Female"]
        
        if self.gender == "male":
            m_count += 1
            Sorting.genders["Male"] = m_count
        elif self.gender == "female":
            f_count += 1
            Sorting.genders["Female"] = f_count

    def SalarySorter(self):
        
        employee_info = {
    "ID": self.id,
    "Name": self.name,
    "Post": self.post,
    "City": self.place.title(),
    "Gender": self.gender.title(),
    "Salary": self.salary
}
        if 40000 <= self.salary <= 70000:
            Sorting.salary_ranges["40000 - 70000"].append(employee_info)
        elif 70001 <= self.salary <= 100000:
            Sorting.salary_ranges["70001 - 100000"].append(employee_info)
        elif self.salary > 100000:
            Sorting.salary_ranges["100001+"].append(employee_info)

    def Display(self):
        print("--- PLACE SUMMARY ---")
        for k, v in Sorting.cities.items():
            print(f"City: {k} | Employees Working: {v}")
            
        print("\n--- GENDER SUMMARY ---")
        for k, v in Sorting.genders.items():
            print(f"Gender: {k} | Count: {v}")
            
        print("\n--- SALARY RANGE REPORT ---")
        for range_name, employees in Sorting.salary_ranges.items():
            print(f"\nSalary Range: {range_name} (Total: {len(employees)})")
            print("-" * 50)
            for emp in employees:
                print(f"Name: {emp['Name']} | Post: {emp['Post']} | Salary: INR {emp['Salary']}")


employee_dict = { 
    101: ["Aarav Sharma", "AI Engineer", "Mumbai", "Male", 95000], 
    102: ["Priya Patel", "Data Analyst", "Pune", "Female", 62000], 
    103: ["Rohan Verma", "Software Developer", "Bengaluru", "Male", 78000], 
    104: ["Ananya Iyer", "HR Manager", "Chennai", "Female", 85000], 
    105: ["Vikram Singh", "Product Manager", "Delhi", "Male", 110000], 
    106: ["Neha Gupta", "UI/UX Designer", "Hyderabad", "Female", 67000], 
    107: ["Amit Kumar", "DevOps Engineer", "Noida", "Male", 88000], 
    108: ["Pooja Deshmukh", "QA Tester", "Pune", "Female", 52000], 
    109: ["Rahul Joshi", "Data Scientist", "Bengaluru", "Male", 125000], 
    110: ["Sneha Nair", "Content Writer", "Kochi", "Female", 48000], 
    111: ["Karan Malhotra", "ML Engineer", "Mumbai", "Male", 99000], 
    112: ["Divya Menon", "Financial Analyst", "Chennai", "Female", 74000], 
    113: ["Manish Tiwari", "Backend Developer", "Kolkata", "Male", 72000], 
    114: ["Ritu Kulkarni", "Frontend Developer", "Pune", "Female", 69000], 
    115: ["Siddharth Rao", "Cloud Architect", "Hyderabad", "Male", 135000], 
    116: ["Meera Pillai", "Scrum Master", "Bengaluru", "Female", 92000], 
    117: ["Abhishek Das", "Support Specialist", "Kolkata", "Male", 41000], 
    118: ["Tanvi Shah", "Marketing Lead", "Mumbai", "Female", 81000], 
    119: ["Varun Nambiar", "System Admin", "Kochi", "Male", 58000], 
    120: ["Kavita Reddy", "Data Engineer", "Hyderabad", "Female", 94000], 
    121: ["Aditya Chopra", "AI Researcher", "Delhi", "Male", 140000], 
    122: ["Shruti Joshi", "HR Associate", "Pune", "Female", 45000], 
    123: ["Deepak Verma", "Security Analyst", "Bengaluru", "Male", 89000], 
    124: ["Nisha Agarwal", "Business Analyst", "Mumbai", "Female", 79000], 
    125: ["Harsh Vardhan", "Software Architect", "Noida", "Male", 150000], 
    126: ["Swati Chatterjee", "UI/UX Designer", "Kolkata", "Female", 66000], 
    127: ["Alok Mukherjee", "DevOps Engineer", "Chennai", "Male", 86000], 
    128: ["Deepika Sen", "QA Lead", "Bengaluru", "Female", 77000], 
    129: ["Nikhil Pawar", "Data Scientist", "Pune", "Male", 115000], 
    130: ["Rachna Kacker", "Content Strategist", "Delhi", "Female", 63000], 
    131: ["Yashwant Rao", "ML Engineer", "Hyderabad", "Male", 97000], 
    132: ["Monika Jain", "Financial Controller", "Mumbai", "Female", 105000], 
    133: ["Tarun Bajaj", "Backend Developer", "Noida", "Male", 71000], 
    134: ["Pallavi Sinha", "Frontend Developer", "Bengaluru", "Female", 68000], 
    135: ["Zainab Khan", "Cloud Engineer", "Mumbai", "Female", 91000], 
    136: ["Sameer Khan", "Project Manager", "Pune", "Male", 102000], 
    137: ["Geeta Iyer", "Technical Writer", "Chennai", "Female", 55000], 
    138: ["Mohit Goyal", "Database Admin", "Delhi", "Male", 76000], 
    139: ["Sonalika Ghosh", "Marketing Analyst", "Kolkata", "Female", 59000], 
    140: ["Vineet Saxena", "AI Consultant", "Bengaluru", "Male", 130000], 
    141: ["Jaya Bhatt", "HR Specialist", "Mumbai", "Female", 54000], 
    142: ["Tushar Mehra", "Network Engineer", "Noida", "Male", 64000], 
    143: ["Bhavana Reddy", "Data Analyst", "Hyderabad", "Female", 63000], 
    144: ["Arjun Pillai", "Software Developer", "Kochi", "Male", 75000], 
    145: ["Kiranmayi Das", "UI Designer", "Chennai", "Female", 61000], 
    146: ["Naveen Kumar", "Systems Engineer", "Bengaluru", "Male", 70000], 
    147: ["Meenakshi Sundaram", "Security Lead", "Chennai", "Female", 98000], 
    148: ["Prateek Jain", "Full Stack Dev", "Pune", "Male", 83000], 
    149: ["Roshni Menon", "Operations Head", "Kochi", "Female", 112000], 
    150: ["Akash Deep", "R&D Engineer", "Delhi", "Male", 108000] 
}

def process_data():
    # Reset previous results
    Sorting.cities = {
        "Bengaluru": 0,
        "Chennai": 0,
        "Delhi": 0,
        "Hyderabad": 0,
        "Kochi": 0,
        "Kolkata": 0,
        "Mumbai": 0,
        "Noida": 0,
        "Pune": 0
    }

    Sorting.genders = {
        "Male": 0,
        "Female": 0
    }

    Sorting.salary_ranges = {
        "40000 - 70000": [],
        "70001 - 100000": [],
        "100001+": []
    }

    for k, v in employee_dict.items():
        emp = Sorting(k, v)
        emp.PlaceSorter()
        emp.GenderSorter()
        emp.SalarySorter()

    return {
        "cities": Sorting.cities,
        "genders": Sorting.genders,
        "salary_ranges": Sorting.salary_ranges
    }


if __name__ == "__main__":
    process_data()

    emp = Sorting(0, ["", "", "", "", 0])
    emp.Display()