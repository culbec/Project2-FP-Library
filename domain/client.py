class Client:
    def __init__(self, identity, name, cnp, subscription_year):
        self._identity = identity
        self._name = name
        self._cnp = cnp
        self._subscription_year = subscription_year

    def get_identity(self):
        return self._identity

    def get_name(self):
        return self._name

    def get_cnp(self):
        return self._cnp

    def get_subscription_year(self):
        return self._subscription_year

    def set_identity(self, identity):
        self._identity = identity

    def set_name(self, name):
        self._name = name

    def set_cnp(self, cnp):
        self._cnp = cnp

    def set_subscription_year(self, subscription_year):
        self._subscription_year = subscription_year
