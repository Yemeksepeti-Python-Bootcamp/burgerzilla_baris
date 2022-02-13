from app import db

class DatabaseHelper:
    database = db

    def saveDatabase(self, data):
        self.database.session.add(data)
        self.database.session.commit()
        return True
    
    def getModelById(self, model, id):
        return model.query.filter_by(id=id).first()
    
    def updateDatabase(self):
        self.database.session.commit()
        return True
    
    def deleteDatabase(self, data):
        self.database.session.delete(data)
        self.database.session.commit()
        return True
    
