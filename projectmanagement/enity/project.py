class Project:
    def __init__(self, Id="", ProjectName="", Description="", StartDate="", Status=""):
        self.__Id = Id
        self.__ProjectName = ProjectName
        self.__Description = Description
        self.__StartDate = StartDate
        self.__Status = Status

    # Getter and Setter for Id
    def get_Id(self):
        return self.__Id

    def set_Id(self, val):
        self.__Id = val

    # Getter and Setter for ProjectName
    def get_ProjectName(self):
        return self.__ProjectName

    def set_ProjectName(self, val):
        self.__ProjectName = val

    # Getter and Setter for Description
    def get_Description(self):
        return self.__Description

    def set_Description(self, val):
        self.__Description = val

    # Getter and Setter for StartDate
    def get_StartDate(self):
        return self.__StartDate

    def set_StartDate(self, val):
        self.__StartDate = val

    # Getter and Setter for Status
    def get_Status(self):
        return self.__Status

    def set_Status(self, val):
        self.__Status = val
