from api.bases.resource.base import BaseResource

class CovidResource(BaseResource):
    def get(self):
        return {
            'message': 'Hello World!'
        }