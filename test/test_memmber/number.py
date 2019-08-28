import random

def public():

    list_str = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    veri_str = random.sample(list_str, 4)
    center = ''.join(veri_str)
    print(center)

if __name__ == '__main__':
    public()