from fastapi_cognito.models import CBECognitoToken


def test_cbe_token_model(cognito_payload):
    token = CBECognitoToken(**cognito_payload)
    assert token.username == cognito_payload['cognito:username']
    assert token.groups == cognito_payload['cognito:groups']
