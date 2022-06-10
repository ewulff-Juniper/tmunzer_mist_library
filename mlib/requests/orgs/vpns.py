def get(mist_session, org_id):
    uri = "/api/v1/orgs/%s/vpns" % org_id
    resp = mist_session.mist_get(uri, org_id=org_id)
    return resp

def create(mist_session, org_id, settings):
    uri = "/api/v1/orgs/%s/vpns" % org_id    
    body = settings
    resp = mist_session.mist_post(uri, org_id=org_id, body=body)
    return resp

def get_by_id(mist_session, org_id, vpn_id):
    uri = "/api/v1/orgs/%s/vpns/%s" %(org_id, vpn_id)
    resp = mist_session.mist_get(uri, org_id=org_id)
    return resp

def update(mist_session, org_id, vpn_id, settings):
    uri = "/api/v1/orgs/%s/vpns/%s" %(org_id, vpn_id)
    body = settings
    resp = mist_session.mist_put(uri, org_id=org_id, body=body)
    return resp

def delete(mist_session, org_id, vpn_id):
    uri = "/api/v1/orgs/%s/vpns/%s" %(org_id, vpn_id)    
    resp = mist_session.mist_delete(uri, org_id=org_id)
    return resp


