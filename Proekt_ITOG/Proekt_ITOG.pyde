#начало


#заставка
fonKNB=0
botOtvet=0
playerOtvet=0
start1=0
player=0
bot=0
n=0
b=0
k=0
kb=0
kk=0
kn=0
game=0
p1=150
p2=1000
p3=100
p4=200
s=0
pole=[[0,0,0],
      [0,1,1],
      [0,0,0],
      [1,1,1],
      [0,0,1],
      [1,0,0],
      [1,1,0],
      [1,0,1],
      [1,0,0],
      [0,1,1],
      [0,0,0],
      [0,0,1],
      [1,0,0],
      [1,1,0],
      [1,0,1],
      [1,0,0],
      [0,1,1],
      [0,0,0],
      [0,0,1],
      [1,0,0],
      [1,1,0],
      [1,0,1],
      [1,0,0],
      [0,1,1],
      [0,0,0]]#ПОЛЕ КЛЕТОЧНОЕ
nu=len(pole)
numStolb= len(pole[0])
def setup():
    global k,n,b,kk,kb,kn,fonKNB,s
    size(1366,1000)
    s=loadImage('Zastawka.png')
    fonKNB=loadImage('FonKNB.png')
    n=loadImage('nonews.png')
    b=loadImage('bymaga.jpg')
    k=loadImage('camen.jpg')
    kb=loadImage('BotBymaga.png')
    kn=loadImage('BotNonews.png')
    kk=loadImage('BotCamen.png')
def draw():
    global pole,nu,numStolb,s,p1,p2,p3,p4,game
    if game==0:
        image(s,80,0)
        for ryad in range (nu):
            for stolb in range(numStolb):
                if pole[ryad][stolb]== 1:
                    fill(0)
                else:
                    fill(255)
                rect(stolb*30,ryad* 30,30,30)#ПОЛЕ
        if mouseX>p1 and mouseX< p2 and mouseY>p3 and mouseY<p4 and mousePressed==True:
            game=1
            global k,n,b,bot,player,start1,playerOtvet,botOtvet,kk,kn,kb,fonKNB
            if start1==0:
                textSize(40)
                image(fonKNB,0,0,1366,750)
                text(u'Привет Это Камень-Ножницы-Бумага ты играешь против бота--',50,500)
                text(u'_1-камень,2-ножницы,3-бумага_',50,600)
                text(u'--Нажни на s что бы начать игру а на t что бы закончить игру',50,700)
            if start1==1:
                frameRate(0.5)
                #time.sleep(2)
                botOtvet=int(random(1,4))
            if botOtvet==1:
                fill(0)
                rect(1366/2,0,1000,1000)
                image(kk,700,0)
                botOtvet=1
            if botOtvet== 2:
                fill(0)
                rect(1366/2,0,1000,1000)
                image(kn,700,0)
                botOtvet=2
            if botOtvet== 3:
                fill(0)
                rect(1366/2,0,1000,1000)
                image(kb,700,0)
                botOtvet=3   
            if key == '1' and start1==1:
                playerOtvet=1
                fill(0)
                quad(0,0,1366/2,0,1366/2,1000,0,1366)
                image(k,100,0)
            if key == '2' and start1==1:
                playerOtvet=2
                fill(0)
                quad(0,0,1366/2,0,1366/2,1000,0,1366)
                image(n,100,0,500,300)
            if key == '3'  and start1==1:
                playerOtvet=3
                fill(0)
                quad(0,0,1366/2,0,1366/2,1000,0,1366)
                image(b,100,0)
                #1366,1
        if start1==1:
            if botOtvet==1 and playerOtvet==2:
                bot=bot+1
            if botOtvet==2 and playerOtvet==3:
                bot=bot+1
            if botOtvet==3 and playerOtvet==1:
                bot=bot+1#бот вин
            if botOtvet==2 and playerOtvet==1:
                player=player+1
            if botOtvet==3 and playerOtvet==2:
                player=player+1
            if botOtvet==1 and playerOtvet==3:
                player=player+1
            #счёт 1 камень 2 ножницы 3 бумага player bot
            fill(255)
            textSize(200)
            text(player,400,500)
            text(bot,800,500) 
def keyPressed():
    global start1
    if key =='s' or key == 'S' or key==u'Ы' or key==u'ы':
        start1=1
    if key == 't' or key == 'T'or key == u'е' or key == u'Е':
        start1=0
            #Кнопка 1 Камень Ножницф Бумага(150,100,850,100)
