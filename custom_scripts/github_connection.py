import argparse
import uuid

from utils.airbyte_api_client import AirbyteAPIClient
from utils.constants import GITHUB_STREAMS_DATA


def get_default_workspace_id(api_client):
    registered_workspaces = api_client.list_registered_workspaces()
    try:
        first_ws = registered_workspaces['workspaces'][0]
    except IndexError:
        raise Exception('No workspaces found')
    workspace_id = first_ws['workspaceId']
    return workspace_id


def get_github_source_definition_id(api_client):
    registered_source_defs = api_client.list_registered_source_definitions()
    github_source_defs = [sd for sd in registered_source_defs['sourceDefinitions'] if sd['name'].lower() == 'github']
    try:
        return github_source_defs[0]['sourceDefinitionId']
    except IndexError:
        raise Exception('Github Source definition not found')


def create_github_source(api_client, workspace_id, github_access_token, github_source_definition_id, repository_name, source_name):
    result = api_client.create_source(github_source_definition_id, {
        # "branch": "unicef/iogt/develop",
        "repository": repository_name,
        "start_date": "2021-01-01T00:00:00Z",
        "credentials": {
            "option_title": "PAT Credentials",
            "personal_access_token": github_access_token
        },
        "page_size_for_large_streams": 10
    }, workspace_id, source_name)

    return result['sourceId']


def get_postgres_destination_definition_id(api_client):
    registered_definitions = api_client.list_registered_destination_definitions()
    postgres_destination_defs = [dd for dd in registered_definitions['destinationDefinitions'] if dd['name'].lower() == 'postgres']
    try:
        return postgres_destination_defs[0]['destinationDefinitionId']
    except IndexError:
        raise Exception('Postgres destination definition not found')


def create_postgres_destination(api_client, postgres_destination_definition_id, workspace_id, destination_name):
    result = api_client.create_destination(postgres_destination_definition_id, {
        # Database configuration can be added via ArgParse
        "ssl": False,
        "host": "localhost",
        "port": 5432,
        "schema": "public",
        "database": "postgres",
        "password": "postgres",
        "username": "postgres",
        "tunnel_method": {
            "tunnel_method": "NO_TUNNEL"
        }
    }, workspace_id, destination_name)
    return result['destinationId']


def create_connection(api_client, github_source_id, postgres_destination_id):
    result = api_client.create_connection(github_source_id, postgres_destination_id, GITHUB_STREAMS_DATA)
    return result['connectionId']


def trigger_manual_sync(api_client, connection_id):
    return api_client.trigger_manual_sync(connection_id)


def run(api_base_url, github_access_token, repository_name):
    api_client = AirbyteAPIClient(base_url=api_base_url)

    default_workspace_id = get_default_workspace_id(api_client)

    github_source_definition_id = get_github_source_definition_id(api_client)
    github_source_id = create_github_source(api_client, default_workspace_id, github_access_token, github_source_definition_id,
                                            repository_name, f'ehmad-github-source-{str(uuid.uuid4())}')

    postgres_destination_definition_id = get_postgres_destination_definition_id(api_client)
    postgres_destination_id = create_postgres_destination(api_client, postgres_destination_definition_id, default_workspace_id,
                                                          f'ehmad-postgres-destination-{str(uuid.uuid4())}')
    connection_id = create_connection(api_client, github_source_id, postgres_destination_id)
    trigger_manual_sync(api_client, connection_id)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--api-base-url', type=str, help='The BASE URL of Airbyte API',
                        default='http://localhost:8000/api')
    parser.add_argument('-g', '--github-access-token', type=str, help='The Personal Access Token of Github', required=True)
    parser.add_argument('-r', '--repository-name', type=str, required=True,
                        help='Space-delimited list of GitHub organizations/repositories, e.g. `airbytehq/airbyte` for single repository,'
                             ' `airbytehq/*` for get all repositories from organization and `airbytehq/airbyte airbytehq/another-repo` '
                             'for multiple repositories. (e.g. airbytehq/airbyte airbytehq/another-repo, airbytehq/*, airbytehq/airbyte) ',
                        )

    arguments = parser.parse_args()

    run(api_base_url=arguments.api_base_url, github_access_token=arguments.github_access_token, repository_name=arguments.repository_name)
