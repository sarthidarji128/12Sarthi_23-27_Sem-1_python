class LU:
    def __init__(self, lu_code, lu_name):
        self.lu_code = lu_code
        self.lu_name = lu_name

    def display_lu_info(self):
        print("LU Code:", self.lu_code)
        print("LU Name:", self.lu_name)


class ITM:
    def __init__(self, itm_code, itm_name):
        self.itm_code = itm_code
        self.itm_name = itm_name
    

    def display_itm_info(self):
        print("ITM Code:", self.itm_code)
        print(f"ITM Name:", self.itm_name)


class DerivedClass(LU, ITM):
    def __init__(self, lu_code, lu_name, itm_code, itm_name, derived_info):     
        LU.__init__(self, lu_code, lu_name)
        ITM.__init__(self, itm_code, itm_name)
        self.derived_info = derived_info

    def display_derived_info(self):
        print("Information:", self.derived_info)


lu_code = "001"
lu_name = "Marketing"
itm_code = "001"
itm_name = "Finance"
derived_info = "Thank you.."

derived_object = DerivedClass(lu_code, lu_name, itm_code, itm_name, derived_info)

derived_object.display_lu_info()
print()
derived_object.display_itm_info()
print()
derived_object.display_derived_info()