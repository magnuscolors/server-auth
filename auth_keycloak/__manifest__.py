
{
    "name": "Keycloak Sync Users",
    "summary": "Integrate Keycloak into your SSO",
    "version": "16.0.0.0.0",
    'category': 'Tools',
    "website": "https://github.com/OCA/server-auth",
    'author': 'Deep, The Open Source Company (TOSC), Camptocamp, Odoo Community Association (OCA)',
    "license": "AGPL-3",
    "depends": [
        "auth_oauth", "auth_oidc"
    ],
    "data": [
        "security/ir.model.access.csv",
        'data/auth_oauth_provider.xml',
        'wizard/keycloak_sync_wiz.xml',
        'wizard/keycloak_create_wiz.xml',
        'views/auth_oauth_views.xml',
        'views/res_users_views.xml',
    ],
}
