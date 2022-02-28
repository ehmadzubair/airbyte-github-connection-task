import requests


class AirbyteAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def list_registered_workspaces(self):
        registered_workspaces_url = f'{self.base_url}/v1/workspaces/list'
        result = requests.post(registered_workspaces_url)
        return result.json()

    def list_registered_source_definitions(self):
        list_registered_source_definitions_url = f'{self.base_url}/v1/source_definitions/list'
        result = requests.post(list_registered_source_definitions_url)
        return result.json()

    def list_registered_destination_definitions(self):
        list_registered_source_definitions_url = f'{self.base_url}/v1/destination_definitions/list'
        result = requests.post(list_registered_source_definitions_url)
        return result.json()

    def create_destination(self, destination_definition_id, connection_configuraiton, workspace_id, name):
        create_destination_url = f'{self.base_url}/v1/destinations/create'
        json_data = {
            "destinationDefinitionId": destination_definition_id,
            "connectionConfiguration": connection_configuraiton,
            "workspaceId": workspace_id,
            "name": name,

        }
        result = requests.post(create_destination_url, json=json_data)
        return result.json()

    def create_source(self, source_definition_id, connection_configuration, workspace_id, name):
        create_source_url = f'{self.base_url}/v1/sources/create'
        json_data = {
            "sourceDefinitionId": source_definition_id,
            "connectionConfiguration": connection_configuration,
            "workspaceId": workspace_id,
            "name": name
        }
        result = requests.post(create_source_url, json=json_data)
        return result.json()

    def create_connection(self, source_id, destination_id, streams):
        create_connection_url = f'{self.base_url}/v1/connections/create'
        json_data = {

            "sourceId": source_id,
            "destinationId": destination_id,
            "syncCatalog": {
                "streams": streams
            },
            "status": "active"
        }
        result = requests.post(create_connection_url, json=json_data)
        return result.json()

    def trigger_manual_sync(self, connection_id):
        trigger_manual_sync_url = f'{self.base_url}/v1/connections/sync'
        json_data = {
            "connectionId": connection_id
        }
        result = requests.post(trigger_manual_sync_url, json=json_data)
        return result.json()
