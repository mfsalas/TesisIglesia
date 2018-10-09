from rolepermissions.roles import AbstractUserRole

class Usuario(AbstractUserRole):
    available_permissions = {
        'persona_list': True
    }

class Administrador(AbstractUserRole):
    available_permissions = {
        'persona_view': True,
        'persona_edit': True,
        'persona_delete': True
    }
