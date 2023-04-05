import pytest

@pytest.fixture
def cognito_payload():
    return {'sub': 'd78921ca-91a0-4ae8-aabe-ff632d12b70c',
            'cognito:groups': ['ACCOUNT_BACKOFFICE_ADMIN', 'MOBILITY2_ADMIN', 'MULTIFORCE', 'MOBILITY_MAN_AGENT',
                               'MOBILITY_MAN_INVOICING', 'CPO_EDIT', 'RELATION_CREATE', 'CDR', 'CONTO_ADMIN',
                               'ACCOUNT_OPS', 'RELATION_VIEW', 'CPO', 'CDR_EDIT', 'ABACUS_ADMIN',
                               'ACCOUNT_GROUPS_ADMIN', 'MOBILITY_MAN_TEAMLEAD', 'ABACUS_AUTHORISE_PAYMENT_BATCH',
                               'SUSTAINABLE_ADMIN', 'RELATION_EMAIL_STATUS', 'RELATION_EDIT', 'RELATIONS_ADMIN',
                               'SUSTAINABLE_EMPLOYEE_OPS', 'AccountManager', 'RELATION_VAT_EXCEPTIONS', 'MOBILITY',
                               'CONTO_VIEW', 'SUSTAINABLE_MAINTENANCE', 'ACCOUNT_ADMIN', 'MOBILITY_MANAGER',
                               'MOB_MAN_INVOICE', 'CONTO_OPS', 'MOBILITY_EDIT', 'SUSTAINABLE_VIEW'],
            'email_verified': True,
            'custom:domain': 'BACKOFFICE',
            'custom:is_impersonator': 'false',
            'iss': 'https://cognito-idp.eu-west-1.amazonaws.com/eu-west-1_EzyGuHkpL',
            'cognito:username': 'johndoe',
            'preferred_username': 'johndoe',
            'given_name': 'John',
            'custom:relation_id': '00000000-0000-0000-0000-000000000000',
            'aud': '4kbgn99p4pofsjel427c5n6omg',
            'custom:seller_id': '00000000-0000-0000-0000-000000000000',
            'event_id': '5ed7a1ea-2549-4af5-86b3-7cb2ae6eca7b',
            'token_use': 'id',
            'auth_time': 1679388933,
            'custom:account_id': '607b614d-87b2-431f-8af1-40d7dd841cd2',
            'exp': 1680694869,
            'custom:debtor_number': '00000000-0000-0000-0000-000000000000',
            'iat': 1680691269,
            'family_name': 'Doe',
            'email': 'john.doe@servicehouse.nl'
            }
