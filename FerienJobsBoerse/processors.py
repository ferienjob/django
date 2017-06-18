

def current_company_processor(request):
    current_company_id = request.session.get('company_id', None)
    current_company_name = request.session.get('company_name', None)

    return {
        'current_company': {
            'id': current_company_id,
            'name': current_company_name
        },
    }
