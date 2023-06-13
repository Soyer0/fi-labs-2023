def full_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x_prev, y_prev = full_gcd(b, a % b)
    x = y_prev
    y = x_prev - (a // b) * y_prev
    return gcd, x, y

def inverse(a, mod):
    gcd, x, y = full_gcd(a, mod)
    if gcd == 1:
        return x % mod
    else:
        print("no inverse")
        return 0
    
def solve_lin_eq(a, b, mod):
    M = mod
    a%=mod
    b%=mod
    d, x, _ = full_gcd(a, mod)
    if d==1:
        return [(x* b) % mod]
    elif b%d==0:
        a //= d
        b //= d
        mod //= d
        x = (inverse(a, mod) * b) % mod
        res = []
        for k in range(d):
            res.append(x + k * mod)
        return res
    else:
        return []

bigrams_lang=["ст", "но", "то", "на", "ен"]
bigrams_text=["ще","хе","чв","ле","цв"] #Без перетину та пробілів


alph1 = "абвгдежзийклмнопрстуфхцчшщыьэюя" #літера «ь» стоїть у алфавіті після літери «ы»
alph2 = "абвгдежзийклмнопрстуфхцчшщьыэюя" #«ь» ототожнюється із літерою «ъ» та стоїть перед літерою «ы» (що відповідає кодуванню ь = 26, ы = 27).
m=31
M=m*m
ALPH=alph2

def bigram_num(bigram):
    return ALPH.index(bigram[0])*m+ALPH.index(bigram[1])

n=5 #за умовою лаби

def findPair(bigrams_text):
    keys = []
    for a_1 in range(n):
        for b_1 in range(n):
            for a_2 in range(n):
                for b_2 in range(n):
                    if a_1 == a_2 or b_1 == b_2:
                        continue
                    
                    a1 = bigram_num(bigrams_lang[a_1])
                    b1 = bigram_num(bigrams_text[b_1])
                    a2 = bigram_num(bigrams_lang[a_2])
                    b2 = bigram_num(bigrams_text[b_2])

                    A = solve_lin_eq(a1 - a2, b1 - b2, M)
                    keys += [(a, (b1 - a * a1) % M) for a in A]
    return keys    

def find_bigram_by_number(number):
    first_index = number // m
    second_index = number % m
    bigram = ALPH[first_index] + ALPH[second_index]
    return bigram

def dec_bigram(txt, a_inv, b):
    Y = bigram_num(txt)
    if Y is None:
        return ''
    return find_bigram_by_number(a_inv * (Y - b) % M)

def dec_text(txt, key):
    (a, b) = key
    (d, a_inv, _) = full_gcd(a, M)
    if d != 1:
        return ""
    res = ""
    for i in range(1, len(txt), 2):
        temp = txt[i - 1] + txt[i]
        res += dec_bigram(temp, a_inv, b)
    
    return res

norm_I=0.05492369

def calc_index(txt):
    k = 0
    n = len(txt)
    for t in ALPH:
        tmp = 0
        for i in txt:
            if i == t:
                tmp += 1
        k += (tmp * (tmp - 1))
    k = float(k / (n * (n - 1)))
    return k    

with open('D:/KPI/crypto/lab3/06.txt', 'r', encoding="utf8") as f:
    text = f.read()
text = text.replace('\n', '')

keys = list(dict.fromkeys(findPair(bigrams_text)))
for key in keys:
    decoded_text = dec_text(text, key)
    if decoded_text == "":
        continue
    if abs(calc_index(decoded_text)- norm_I) < 0.001:
        print(decoded_text)
        print(key)
        break