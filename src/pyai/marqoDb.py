from dotenv import load_dotenv, find_dotenv

class marqo_db:
    '''
    Setup a marqo_db context for retrieving relevant context.
    '''

    def __init__(self) -> None:
        self._storedData = []
        pass

    def query(self, query: str) -> list:
        '''
        Queries your marqo db.
        Currently Unimplemented!
        '''
        return self._storedData
    
    def create(self, data_to_store: list):
        '''
        Pushes the data provided to your db. Returns 0 if successful.
        Currently Unimplemented!
        TODO:
            - Providing values should be done in terms of a list of dictionaries.
            - The list of dictionaries should typically contain the User query and the assistant's respons to that query
            - The values in the list should be associated in the db to be retrieved together.
        '''
        for value in data_to_store:
            self._storedData.append(value)

        return 0
    
    def update(self, data_to_update: list, existing_data: list):
        raise NotImplementedError
    
    def delete(self, data_to_delete: list):
        raise NotImplementedError

    def purge(self):
        '''
        Testing only! Deletes ALL CONTEXT.
        Currently unimplemented for actual the actual database, and it should stay that way.
        Only including for convience when working with initial list storage.
        '''
        self._storedData = []

        return 0