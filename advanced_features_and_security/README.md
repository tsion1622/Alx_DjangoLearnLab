# Permissions and Groups Setup
This project uses Django's groups & permissions system.

## Groups:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

Permissions are enforced in views using `@permission_required`.
