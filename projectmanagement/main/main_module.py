from xmlrpc.client import DateTime
import pyodbc
#############


import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
########### Only for Vs Code apparantly

from dao.ProjectRepositoryImpl import ProjectRepositoryImpl


if __name__ == "__main__":
    print("="*60)
    print("Welcome to Project App".center(60))
    print("="*60)
    choice = input("enter the choice: ")


    pr= ProjectRepositoryImpl()
    while True:

        if choice == "1":
            Id=int(input("Enter the ID: "))
            name=input("Enter the name: ")
            Designation=input("Enter that Desi: ")
            Gender=input("Gender: ")
            Salary=float(input("Salary: "))
            Project_Id=int(input("ProjectID: "))
            pr.createEmployee(Id, name, Designation, Gender, Salary, Project_Id)
            break

        if choice =="2":
            Id = int(input("Enter the ID: "))
            ProjectName = input("Enter the Proname: ")
            Description = input("Enter that Desicrip: ")
            StartDate = input("StartDate: ")
            Status = input("Status: ")
            pr.createProject(Id, ProjectName, Description, StartDate, Status)
            break
        
        if choice == "3":
            Task_Id=int(input("Enter the ID: "))
            Task_Name=input("Enter The Task Name: ")
            Project_Id=int(input("Enter the ProID: "))
            Employee_Id=int(input("Enter the EmpID: "))
            Status=input("Enter the Status: ")
            pr.createTask(Task_Id, Task_Name, Project_Id, Employee_Id, Status)
            break
            
            
        if choice == "4":
            Id=int(input("Enter the  Emp ID: "))
            Project_Id=int(input("Enter the ProID: "))
            pr.assignProjectToEmployee(Project_Id, Id)
            break
            
        if choice == "5":
            Task_Id=int(input("Enter the Task ID: "))
            Project_Id=int(input("Enter the ProID: "))
            Employee_Id=int(input("Enter the EmpID: "))
            pr.assignTaskInProjectToEmployee(Task_Id, Project_Id, Employee_Id)
            break
        
        if choice == "6":
            Id=int(input("Enter the Emp ID: "))
            pr.deleteEmployee(Id)
            break
        
        if choice == "7":
            Id=int(input("Enter the ProID: "))
            pr.deleteProject(Id)
            break
        
        if choice == "8":
            Project_Id = int(input("Enter the Project ID: "))
            Employee_Id = int(input("Enter the Employee ID: "))

            tasks = pr.getAllTasks(Project_Id, Employee_Id)
            
            if tasks:
                print("\nList of Tasks:")
                for task in tasks:
                    print(f"Task ID: {task.get_Task_Id()}, Name: {task.get_Task_Name()}, Status: {task.get_Status()}")
            else:
                print("No tasks found for the given employee and project.")
            break
        
        
        if choice == "9":
            projects = pr.getAllProjects()
            
            print("\n📋 List of Projects:")
            for project in projects:
                print(f"Project ID: {project.Id}, Name: {project.ProjectName}, Description: {project.Description}, Start Date: {project.StartDate}, Status: {project.Status}")
            break