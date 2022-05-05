sigma, eta = 0.2, 0.8
x = 1000
amm_config = {
    "sigma": sigma,
    "eta": eta,
    "init_a": x,
    "init_b": x,
}
# AMM stucture 

#USDT(Y) <-----> CNFT(X)
        # y=kx     |
       #           |             
#                  |
#              Z <---> CNFT(X)
#              | 
#              |
#              
class x_y_amm:

    # define an amm 
    class amm_nest:
 
        def __init__(self, config):
            self.config = config
            self.x = config['init_x'] # represents composite of nft_comps
            self.zs = config['init_zs'] # represents composite of nft_comps
            self.z_vec = [] 


    def __init__(self, config):
        self.config = config
        self.x = config["init_x"] # x represents composite of nft_comps
        self.y = config["init_y"] # y represents cash eq to nft_comps
        self.k = self.y/self.x
        # self.sig = config["sig"]
    #Y = k*x
    # when y is deposited, x quantity is increased, such that ratio of x to y is maintained
    def mu_function(self):
        return self.y/self.x

    def get_delta_x(self, y):
        #calculate  
        return self.mu_function() * y

    # def get_delta_x(self, y):
    #     #calculate  
    #     return self.mu_function(self.x, y) / (1 - self.sig)



    def deposit(self, amount):
        print("BALANCES before: ","y(cash):",  self.y, "x(nft):", self.x, "ratio:", self.y/self.x)
        self.x += self.get_delta_x(amount)
        self.y += amount
        print("BALANCES after: ","y(cash):",  self.y, "x(nft):", self.x, "ratio:", self.y/self.x)


    def withdraw(self, amount):
        print("BALANCES before: ","y(cash):",  self.y, "x(nft):", self.x, "ratio:", self.y/self.x)
        self.x -= self.get_delta_x(amount)
        self.y -= amount
        print("BALANCES after: ","y(cash):",  self.y, "x(nft):", self.x, "ratio:", self.y/self.x)


    def get_marginal_price(self):
        return self.y / self.x