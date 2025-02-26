from repository import person_repo

# mvc (controller/service)

'''Process the buisness logic data for the person model'''
class PersonService:
    repo = None
    def __init__(self):
        '''Initializes person's service'''
        self.repo = person_repo.PersonRepository()

    def add_person(self, person_id: int, name: str):
        '''Adds a person to the database'''
        exists = self.repo.get_person(person_id)
        if exists:
            return {"error": f"User already exists. {exists}"}
        else:
            new_person = {"_id": person_id, "name": name}
            try:
                result = self.repo.add_person(new_person)
                return {"msg": "User added succesfully.", "id": str(result.inserted_id)}
            except Exception as e:
                return {"error": f"Connection error or insert error: {e}"}
