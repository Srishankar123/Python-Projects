class Employee:
    def __init__(self, Id="", Name="", Designation="", Gender="", Salary="", ProjectId=""):
        self.__Id = Id
        self.__Name = Name
        self.__Designation = Designation
        self.__Gender = Gender
        self.__Salary = Salary
        self.__ProjectId = ProjectId

    # Getter and Setter for Id
    def get_Id(self):
        return self.__Id

    def set_Id(self, val):
        self.__Id = val

    # Getter and Setter for Name
    def get_Name(self):
        return self.__Name

    def set_Name(self, val):
        self.__Name = val

    # Getter and Setter for Designation
    def get_Designation(self):
        return self.__Designation

    def set_Designation(self, val):
        self.__Designation = val

    # Getter and Setter for Gender
    def get_Gender(self):
        return self.__Gender

    def set_Gender(self, val):
        self.__Gender = val

    # Getter and Setter for Salary
    def get_Salary(self):
        return self.__Salary

    def set_Salary(self, val):
        self.__Salary = val

    # Getter and Setter for ProjectId
    def get_ProjectId(self):
        return self.__ProjectId

    def set_ProjectId(self, val):
        self.__ProjectId = val