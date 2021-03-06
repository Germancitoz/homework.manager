from .database import mySQL

class Homeworks(): 
    def __init__(self, userId):
        self.userId = userId
        self.homeworks = []
        self.refreshHomework(userId)

    def refreshHomework(self, userId):
        mySQL.cursor.execute("SELECT * FROM users_works WHERE id_user = %s", (userId,))
        result = mySQL.cursor.fetchall()
        self.homeworks = result

    def createHomework(self, nameA = None, descriptionA = None, data_startA = None, data_endA = None):
        #mySQL.cursor.execute("")
        pass
        
    def deleteHomework(self, homeworkId):
        mySQL.cursor.execute("DELETE FROM users_works WHERE id = %s", (homeworkId,))
        mySQL.database.commit()
        self.refreshHomework(self.userId)

    def modifyHomework(self, homeworkId, nameA = None, descriptionA = None, data_startA = None, data_endA = None):
        toModify = {'name':nameA, 'description':descriptionA, 'data_start':data_startA, 'data_end':data_endA}
        for key, value in toModify.items():
            if value != None:
                mySQL.cursor.execute(f"UPDATE users_works SET {key} = '{value}' WHERE id = {homeworkId}")
                mySQL.database.commit()
    
