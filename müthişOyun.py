#pgzero

WIDTH = 600
HEIGHT = 400

TITLE = "düğmeye basma"
FPS = 30

# Nesneler
buton = Actor("sbutonn", (150, 250))
arkaplan = Actor("arkaplan")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
bonus_3 = Actor("bonus", (450, 300))
oyna = Actor("oyna", (300, 100))
carpi = Actor("çarpı", (580, 20))
magaza = Actor("mağaza", (300, 200))
koleksiyon = Actor("koleksiyon", (300, 300))
kbuton = Actor('kbutonn', (120, 200))
tbuton = Actor('tbutonn', (300, 200))
mbuton = Actor('mbutonn', (480, 200))

# Değişkenler
puan = 0
tiklama = 1
mod = 'menü'
ucret_1 = 15
ucret_2 = 200
ucret_3 = 600
butonlar = []

def draw():
    if mod == 'menü':
        arkaplan.draw()
        oyna.draw()
        screen.draw.text(puan, center=(30, 20), color="white", fontsize = 36)
        magaza.draw()
        koleksiyon.draw()
   
    elif mod == 'oyun':    
        arkaplan.draw()
        buton.draw()
        screen.draw.text(puan, center=(150, 100), color="white", fontsize = 96)
        bonus_1.draw()
        screen.draw.text("Her 2 saniye için 1p", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text(ucret_1, center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("Her 3 saniye için 15p", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text(ucret_2, center=(450, 210), color="black", fontsize = 20)
        bonus_3.draw()
        screen.draw.text("Her 4 saniye için 50p", center=(450, 280), color="black", fontsize = 20)
        screen.draw.text(ucret_3, center=(450, 310), color="black", fontsize = 20)
        carpi.draw()
    
    elif mod == 'mağaza':
        arkaplan.draw()
        kbuton.draw()
        screen.draw.text("500p", center= (120, 300), color="white", fontsize = 36)
        tbuton.draw()
        screen.draw.text("2500p", center= (300, 300), color="white", fontsize = 36)
        mbuton.draw()
        screen.draw.text("7000p", center= (480, 300), color="white", fontsize = 36)
        carpi.draw()
        screen.draw.text(puan, center=(30, 20), color="white", fontsize = 36)
    
    elif mod == 'koleksiyon':
        arkaplan.draw()
        for i in range(len(butonlar)):
            butonlar[i].draw()
        carpi.draw()
        screen.draw.text(puan, center=(30, 20), color="white", fontsize = 36)
        screen.draw.text("+2p", center= (120, 300), color="white", fontsize = 36)
        screen.draw.text("+3p", center= (300, 300), color="white", fontsize = 36)
        screen.draw.text("+4p", center= (480, 300), color="white", fontsize = 36)

def bonus_1_icin():
    global puan
    puan += 1

def bonus_2_icin():
    global puan
    puan += 15

def bonus_3_icin():
    global puan
    puan += 50

def on_mouse_down(button, pos):
    global puan
    global mod
    global ucret_1, ucret_2, ucret_3
    global tiklama
    # Oyun Modu
    if button == mouse.LEFT and mod == "oyun":
        
        if buton.collidepoint(pos):
            puan += tiklama
            buton.y = 200
            animate(buton, tween='bounce_end', duration=0.5, y=250)
       # bonus_1 butonu tıklandığında  
        elif bonus_1.collidepoint(pos):
            bonus_1.y = 105
            animate(bonus_1, tween='bounce_end', duration=0.5, y=100)
            if puan >= ucret_1:
                schedule_interval(bonus_1_icin, 2)
                puan -= ucret_1
                ucret_1 *= 2
        # bonus_2 butonu tıklandığında 
        elif bonus_2.collidepoint(pos):
            bonus_2.y = 205
            animate(bonus_2, tween='bounce_end', duration=0.5, y=200)
            if puan >= ucret_2:
                schedule_interval(bonus_2_icin, 3)
                puan -= ucret_2
                ucret_2 *= 2
        # bonus_3 button tıklandığında
        elif bonus_3.collidepoint(pos):
            bonus_3.y = 305
            animate(bonus_3, tween='bounce_end', duration=0.5, y=300)
            if puan >= ucret_3:
                schedule_interval(bonus_3_icin, 4)
                puan -= ucret_3
                ucret_3 *= 2
        elif carpi.collidepoint(pos):
            mod = 'menü'
    # Menü Modu
    elif mod == 'menü' and button == mouse.LEFT:
        if oyna.collidepoint(pos):
            mod = 'oyun'
        elif magaza.collidepoint(pos):
            mod = 'mağaza'
        elif koleksiyon.collidepoint(pos):
            mod = "koleksiyon"
    
    # Mağaza        
    elif  mod == 'mağaza' and button == mouse.LEFT:
        if carpi.collidepoint(pos):
            mod = 'menü'
        elif kbuton.collidepoint(pos):
            if kbuton in butonlar:
                buton.image = 'butonn'
            elif puan >= 500:
                puan -= 500
                tiklama = 2
                buton.image = 'kbutonn'
                butonlar.append(kbuton)
        elif tbuton.collidepoint(pos):
            if tbuton in butonlar:
                butonlar.image = 'tbutonn'
            elif puan >= 2500:
                puan -= 2500
                tiklama = 3
                buton.image = 'tbutonn'
                butonlar.append(tbuton)
        elif mbuton.collidepoint(pos):
            if mbuton in butonlar:
                buton.image = 'mbutonn'
            elif puan >= 7000:
                puan -= 7000
                tiklama = 4
                buton.image = 'mbutonn'
                butonlar.append(mbuton)
                
    # Koleksiyon
    elif  mod == 'koleksiyon' and button == mouse.LEFT:
        if carpi.collidepoint(pos):
            mod = 'menü'
        elif kbuton.collidepoint(pos):
            if kbuton in butonlar:
                buton.image = 'kbuton'
        
        elif tbuton.collidepoint(pos):
            if tbuton in butonlar:
                buton.image = 'tbuton'
        
        elif mbuton.collidepoint(pos):
            if mbuton in butonlar:
                buton.image = 'mbuton'
            animate(bonus_1, tween='bounce_end', duration=0.5, y=100)
            if puan >= ucret_1:
                schedule_interval(bonus_1_icin, 2)
                puan -= ucret_1
                ucret_1 *= 2
        # bonus_2 butonu tıklandığında 
        elif bonus_2.collidepoint(pos):
            bonus_2.y = 205
            animate(bonus_2, tween='bounce_end', duration=0.5, y=200)
            if puan >= ucret_2:
                schedule_interval(bonus_2_icin, 3)
                puan -= ucret_2
                ucret_2 *= 2
        # bonus_3 button tıklandığında
        elif bonus_3.collidepoint(pos):
            bonus_3.y = 305
            animate(bonus_3, tween='bounce_end', duration=0.5, y=300)
            if puan >= ucret_3:
                schedule_interval(bonus_3_icin, 4)
                puan -= ucret_3
                ucret_3 *= 2
        elif carpi.collidepoint(pos):
            mod = 'menü'
    # Menü Modu
    elif mod == 'menü' and button == mouse.LEFT:
        if oyna.collidepoint(pos):
            mod = 'oyun'
        elif magaza.collidepoint(pos):
            mod = 'mağaza'
        elif koleksiyon.collidepoint(pos):
            mod = "koleksiyon"
            
    # Mağaza        
    elif  mod == 'mağaza' and button == mouse.LEFT:
        if carpi.collidepoint(pos):
            mod = 'menü'
        
        elif kbuton.collidepoint(pos):
            if puan >= 500:
                puan -= 500
                tiklama = 2
                buton.image = 'kbuton'
                butonlar.append(kbuton)
        
        elif tbuton.collidepoint(pos):
            if puan >= 2500:
                puan -= 2500
                tiklama = 3
                buton.image = 'tbuton'
                butonlar.append(tbuton)
                
    # Koleksiyon
    elif  mod == 'koleksiyon' and button == mouse.LEFT:
        if carpi.collidepoint(pos):
            mod = 'menü'
    
        elif kbuton.collidepoint(pos):
            if kbuton in butonlar:
                buton.image = 'kbuton'
                
        elif tbuton.collidepoint(pos):
            if tbuton in butonlar:
                buton.image = 'tbuton'
