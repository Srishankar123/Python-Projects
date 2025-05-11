class EmployeeNotFoundException(Exception):
    def __init__(self, message="Employee Not Found with given ID"):
        super().__init__(message)

class ProjectNotFoundException(Exception):
    def __init__(self, message="Project Not Found with given ID"):
        super().__init__(message)
