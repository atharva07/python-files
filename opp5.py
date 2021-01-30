class Football:
    num_of_play = 0

    def __init__(self,first,last,pay,nation,goals):
        self.first = first
        self.last = last
        self.pay = pay
        self.nation = nation
        self.email = first + last + '@gmail.com'
        self.goals = goals

        Football.num_of_play = 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def know_status(self):
        if self.pay >= 4000 and self.pay <= 15000:
            print('You are in class-3 tier')
            print('You are getting some bonus')
            self.pay += 2300
        elif self.pay >= 16000 and self.pay <= 30000:
            print('You are in class-2 tier')
            print('You are getting some bonus')
            self.pay += 1400
        else:
            print('You are a class-1 tier employee')
            print('gotta pay some tax')
            self.pay -= 2178
        
plr_1 = Football('Andre','Gomez',24000,'Spain',12)
plr_2 = Football('Federico','Bernadechi',18000,'Italy',14)
plr_3 = Football('Thomas','Muller',48000,'Germany',24)
plr_4 = Football('Leonel','Messi',57000,'Argentina',34)

plr_list = [plr_1,plr_2,plr_3,plr_4]

for Football in plr_list:
    print(f'the full name of player is as = {Football.first} {Football.last}')
    print(f'You are from {Football.nation}')
for Football in plr_list:
    print(f'Hello {Football.first} {Football.last}')
    Football.know_status()
    print(f"The salary is as follows = ${Football.pay}")

for Football in plr_list:
    print(f"Number of goals scored by you = {Football.goals}")

hash(Football)
print(hash)