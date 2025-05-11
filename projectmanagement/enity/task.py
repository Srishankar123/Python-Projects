class Task:
    def __init__(self, Task_Id="", Task_Name="", Project_Id="", Employee_Id="", Status=""):
        self.__Task_Id = Task_Id
        self.__Task_Name = Task_Name
        self.__Project_Id = Project_Id
        self.__Employee_Id = Employee_Id
        self.__Status = Status

    # Getter and Setter for Task_Id
    def get_Task_Id(self):
        return self.__Task_Id

    def set_Task_Id(self, val):
        self.__Task_Id = val

    # Getter and Setter for Task_Name
    def get_Task_Name(self):
        return self.__Task_Name

    def set_Task_Name(self, val):
        self.__Task_Name = val

    # Getter and Setter for Project_Id
    def get_Project_Id(self):
        return self.__Project_Id

    def set_Project_Id(self, val):
        self.__Project_Id = val

    # Getter and Setter for Employee_Id
    def get_Employee_Id(self):
        return self.__Employee_Id

    def set_Employee_Id(self, val):
        self.__Employee_Id = val

    # Getter and Setter for Status
    def get_Status(self):
        return self.__Status

    def set_Status(self, val):
        self.__Status = val
