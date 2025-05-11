from xmlrpc.client import DateTime
from datetime import datetime

from dao.IProjectRepository import IProjectRepository
from util.db_conn_util import DBConnUtil
from enity.task import Task
from exception.user_found_exception import EmployeeNotFoundException
from exception.user_found_exception import ProjectNotFoundException


class ProjectRepositoryImpl(IProjectRepository):
     def __init__(self):
         self.conn = DBConnUtil.get_connection()

     def createEmployee(self,Id: int,name: str, Designation:str, Gender: str, Salary: float, Project_Id: int  ):
         cursor= self.conn.cursor()

         insert_query="""
         INSERT INTO Employee (Id, Name, Designation, Gender, Salary, Project_id) VALUES
         (?, ?, ?, ?, ?, ?)
         """
         cursor.execute(insert_query,(Id, name, Designation, Gender, Salary, Project_Id))
         self.conn.commit()

         print(f"✅ Profile created for {name} .")


     def createProject(self,Id= int, ProjectName= str, Description= str, StartDate= str, Status= str):
         cursor=self.conn.cursor()

        # StartDate = datetime.strptime(StartDate, "%Y-%m-%d")

         insert_query="""
         INSERT INTO Project (Id, ProjectName, Description, StartDate, Status) VALUES
         (?, ?, ?, ?, ?)
         """
         cursor.execute(insert_query, (Id, ProjectName, Description, StartDate, Status))
         self.conn.commit()

         print(f"✅ Project created for {ProjectName} .")

     def createTask(self, Task_Id: int, Task_Name: str, Project_Id: int, Employee_Id: int, Status: str ):
         cursor=self.conn.cursor()
         
         insert_query="""
         INSERT INTO Task(Task_Id,Task_Name, Project_Id, Employee_Id, Status) VALUES
         (?, ?, ?, ?, ?)
         """
         
         cursor.execute(insert_query,(Task_Id, Task_Name, Project_Id, Employee_Id, Status))
         self.conn.commit()
         print(f"✅ Project created for {Task_Name} .")


     def assignProjectToEmployee(self, Project_Id: int, Id: int):
         cursor=self.conn.cursor()
         update_query = """
         UPDATE Employee
         SET Project_id = ?
         WHERE Id = ?
         """
         
         cursor.execute(update_query, (Project_Id, Id))
         self.conn.commit()
         print(f"✅ Project assigned to Employee with ID {Id} .")
         

     def assignTaskInProjectToEmployee(self, TaskId: int, Project_Id: int, Employee_Id: int):
         cursor=self.conn.cursor()
         update_query = """
         UPDATE Task    
         SET Project_ID = ?, Employee_ID = ?
         WHERE Task_ID = ?
         """
         cursor.execute(update_query,(Project_Id, Employee_Id, TaskId))
         self.conn.commit()
         print(f"✅ Task assigned to Employee with ID {Employee_Id} .")         

     def deleteEmployee(self, Id):
         cursor= self.conn.cursor()
         delete_query="""
         DELETE FROM Employee WHERE Id = ?
         """
         cursor.execute(delete_query, (Id))
         self.conn.commit()
         print(f"✅ Employee with ID {Id} deleted .")

     def deleteProject(self, Id):
         cursor=self.conn.cursor()
         delete_query="""
         DELETE FROM Project WHERE Id = ?
         """
         cursor.execute(delete_query, (Id))
         self.conn.commit()
         print(f"✅ Project with ID {Id} deleted .")
         


     def getAllTasks(self, Project_Id, Employee_Id):
        cursor = self.conn.cursor()
        query = """
        SELECT * FROM TASK WHERE
        Project_Id = ? AND Employee_Id = ?
        """
        cursor.execute(query, (Project_Id, Employee_Id))
        rows = cursor.fetchall()
        cursor.close()

        tasks = []
        
        for row in rows:
            task = Task(
                Task_Id=row[0],
                Task_Name=row[1],
                Project_Id=row[2],
                Employee_Id=row[3],
                Status=row[4]
            )
            tasks.append(task)

        return tasks
    
    
     def getAllProjects(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM Project"
        cursor.execute(query)
        projects = cursor.fetchall()
        cursor.close()
        return projects


         






