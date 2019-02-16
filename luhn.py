class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num

    def is_valid(self):
        num_list = list(self.card_num.replace(' ',''))
        for n in num_list:
            if n.isdigit():
                pass
            else:
                return False
        num = [int(n) for n in num_list]
        if len(num) <=1:
            return False
        
        prod = [n*2 for n in num[-2::-2]]
        
        l = []
        for n in prod:
            if n > 9:
                l.append(n-9)
            else:
                l.append(n)
        
        total = sum(num[-1::-2]) + sum(l)

        if total %10 == 0:
            return True
        else:
            return False
