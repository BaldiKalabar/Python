def func():
    if start1==1:#счёт 1 камень 2 ножницы 3 бумага player bot
            if botOtvet==1 and playerOtvet==2:
                bot==bot+1
            if botOtvet==2 and playerOtvet==3:
                bot==bot+1
            if botOtvet==3 and playerOtvet==1:
                bot==bot+1#бот вин
            if botOtvet==1 and playerOtvet==2:
                player==player+1
            if botOtvet==2 and playerOtvet==3:
                player==player+1
            if botOtvet==3 and playerOtvet==1:
                player==player+1#игроквин
            #счётчик
            fill(255)
            textSize(200)
            text(player,400,500)
            text(bot,800,500) 
