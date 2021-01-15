class Router:
    '''Router Class'''
    def __init__(self, model, swversion, ip_add):
        '''initialize value'''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add

rtr1 = Router('iosV', '15.6.7', '192.168.155.71')
