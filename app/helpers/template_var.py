from django.conf import settings

def currentUserName(request):
	return request.session.get('userauth', {}).get('name')


def currentUserRole(request):
	return  request.session.get('userauth', {}).get('role')

def getRoleName(request):
	role_id = request.session.get('userauth', {}).get('role')
	if role_id == 1: 
		role_name = 'Student'
	elif role_id == 2:
		role_name = 'Faculty'
	else:
		role_name = 'Admin'
	
	return role_name

def globalTemplateVar(request):
	return {
		'USER_ROLE': currentUserRole(request),
		'USER_NAME': currentUserName(request),
		'ROLE_NAME': getRoleName(request),
	}
