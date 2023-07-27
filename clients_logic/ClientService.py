class ClientService:
    def __init__(self):
        self.clientRecords = [
            {
                "id": 1,
                "name": "John Smith",
                "gender": "male",
                "age": "18-25" 
            },
            {
                "id": 2,
                "name": "Sandra Long",
                "gender": "female",
                "age": "25-40"
            }
        ]


    def getAllClients(self):
        return self.clientRecords
    
    def getClientByName(self, client_name : str):

        for client in self.clientRecords:

            if client["name"].__contains__(client_name.lower()):
                return client
            
        return {"message" : "client doesn't exist!"}