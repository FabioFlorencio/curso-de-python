# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (Xself, Xcls)

class Connection:
    def __init__(self, host="localhost") :
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user  = user

    def set_password(self, password):
        self.password = password

    @classmethod    
    def create_with_auth(cls, user, password):
        # criei uma nova instância da classe
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def soma(x,y):
        return x + y

# Criar objeto
c1 = Connection()

# c1.set_user = 'Fábio'

# print(c1.set_user)

c1 = Connection.create_with_auth('Fábio', 1234)        

print(c1.user)
print(c1.password)

print('Somar número:' , Connection.soma(2,2))


