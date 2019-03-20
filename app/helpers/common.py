def create_user_session(request, user_obj):
    request.session['userauth'] = {
        'name': user_obj.name,
        'email': user_obj.email,
        'user_id': user_obj.id,
        'role': user_obj.role
    }
    return True
