
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
# x = yukseklik
# y = uzunluk
# g = uzaklik
g1 = g
maks = x * y
x1 = x
y1 = y
yeter = 0
boardlenght = y
yatay_konum = 0
gameover = False
ana_list = []
tur = 0
score = 0
yazma = 0
yazdirma = 0
kayma = 0
gamewon = False
sildim = 0
for i in range(0,x):
    ana_list.append([])
    for a in range(0,y):
        ana_list[i].append(1)
if y % 2 == 0:
    yatay_konum = int(y / 2) - 1
if y % 2 == 1:
    yatay_konum = int((y+1)/2) - 1
if x == 0 or y == 0:
    gamewon = True
if gamewon == False and gameover == False:
    for i in range(len(ana_list)):
        for a in ana_list[i]:
            if a == 1:
                print("*",end="")
            if a == 0:
                print(" "*y, end="")
        print()
    else:
        for i in range(g):
            print(" "*y)
        print(" "*yatay_konum,end="")
        print("@",end=(" "*(y-yatay_konum-1)))
        print()
        print("-"*72)
while gameover == False and gamewon == False:
    score = 0
    if tur % 5 == 0 and tur != 0:
        g = g - 1
        kayma = kayma + 1
    if g < 0:
        for i in ana_list[g]:
            if i == 1:
                gameover = True
                break
    if gameover == True:
        break
    print("Choose your action!")
    action = input().lower()
    if action != "exit" and action != "fire" and action != "left" and action != "right" :
        tur = tur + 1
        if tur % 5 == 0 and tur != 0:
            g = g - 1
            kayma = kayma + 1
        if g < 0:
            for i in ana_list[g]:
                if i == 1:
                    gameover = True
                    break
        if gameover == True:
            break

        for i in range(kayma):
            print(" "*boardlenght)
        for i in range(len(ana_list)):
            k = 0
            for a in ana_list[i]:
                if k < boardlenght:
                    if a == 1:
                        print("*", end="")
                    if a == 0:
                        print(" ", end="")
                k = k + 1
            print()
        else:
            for i in range(g):
                print(" " * boardlenght)
            print(" " * yatay_konum, end="")
            print("@", end=" "*(boardlenght-yatay_konum-1))
            print()
            print("-" * 72)
        if tur % 5 == 0 and tur != 0:
            g = g + 1
            kayma = kayma - 1

        continue
    if action == "exit":
        gameover = False
        for i in range(kayma):
            print(" "*boardlenght)
        for i in range(len(ana_list)):
            k = 0
            for a in ana_list[i]:
                if k < boardlenght:
                    if a == 1:
                        print("*", end="")
                    if a == 0:
                        print(" ",end="")
                k = k + 1
            print()
        else:
            for i in range(g):
                print(" " * boardlenght)
            print(" " * yatay_konum, end="")
            print("@", end=" "*(boardlenght-yatay_konum-1))
            print()
            print("-" * 72)
        for i in range(len(ana_list)):
            for a in range(len(ana_list[i])):
                if ana_list[i][a] == 0:
                    score = score + 1
        score = score + yeter * y
        print("YOUR SCORE:", score)
        break
    if action == "left":
        tur = tur + 1
        if tur % 5 == 0 and tur !=0:
            g = g - 1
            kayma = kayma +1
            if g < 0:
                if yatay_konum > 0:
                    yatay_konum = yatay_konum - 1
                gameover = True
                break
            g = g+1
            kayma = kayma - 1
        if tur % 5 != 0:
            for i in range(kayma):
                print(" "*boardlenght)
            if yatay_konum > 0:
                yatay_konum = yatay_konum - 1

                for i in range(len(ana_list)):
                    k = 0
                    for a in ana_list[i]:

                        if a == 1:
                            print("*", end="")
                        if a == 0:
                            print(" ", end="")

                    print()
                else:
                    for i in range(g):
                        print(" " * boardlenght)
                    print(" " * yatay_konum, end="")
                    print("@", end=" "*(boardlenght-yatay_konum-1))
                    print()
                    print("-" * 72)
                #if tur % 5 == 0 and tur != 0 :
                   # g = g + 1
                    #kayma = kayma - 1
                continue
            else:
                yatay_konum = 0
                for i in range(len(ana_list)):
                    k = 0
                    for a in ana_list[i]:
                        if k < boardlenght:
                            if a == 1:
                                print("*", end="")
                            if a == 0:
                                print(" ", end="")
                        k = k + 1
                    print()
                else:
                    for i in range(g):
                        print(" " * boardlenght)
                    print(" " * yatay_konum, end="")
                    print("@", end=" "*(boardlenght-yatay_konum-1))
                    print()
                    print("-" * 72)
                continue
        if tur % 5 == 0 and  tur != 0:
            for i in range(kayma+1):
                print(" " * boardlenght)
            if yatay_konum > 0:
                yatay_konum = yatay_konum - 1

                for i in range(len(ana_list)):
                    k = 0
                    for a in ana_list[i]:

                        if a == 1:
                            print("*", end="")
                        if a == 0:
                            print(" ", end="")

                    print()
                else:
                    for i in range(g-1):
                        print(" " * boardlenght)
                    print(" " * yatay_konum, end="")
                    print("@", end=" " * (boardlenght - yatay_konum - 1))
                    print()
                    print("-" * 72)
                # if tur % 5 == 0 and tur != 0 :
                # g = g + 1
                # kayma = kayma - 1
                continue
            else:
                yatay_konum = 0
                for i in range(len(ana_list)):
                    k = 0
                    for a in ana_list[i]:
                        if k < boardlenght:
                            if a == 1:
                                print("*", end="")
                            if a == 0:
                                print(" ", end="")
                        k = k + 1
                    print()
                else:
                    for i in range(g-1):
                        print(" " * boardlenght)
                    print(" " * yatay_konum, end="")
                    print("@", end=" " * (boardlenght - yatay_konum - 1))
                    print()
                    print("-" * 72)
                continue

    if action == "right":
        tur = tur + 1
        if tur %5 == 0 and tur != 0:
            g = g - 1
            kayma = kayma +1
            if g < 0:
                if yatay_konum != boardlenght - 1:
                    yatay_konum = yatay_konum + 1
                gameover = True
                break
            g = g + 1
            kayma = kayma - 1
        if tur % 5 != 0:
            if yatay_konum != boardlenght-1:
                yatay_konum = yatay_konum + 1
            for i in range(kayma):
                print(" "*boardlenght)
            for i in range(len(ana_list)):
                k = 0
                for a in ana_list[i]:
                    if k < boardlenght:
                        if a == 1:
                            print("*", end="")
                        if a == 0:
                            print(" ", end="")
                    k = k + 1
                print()
            else:
                for i in range(g):
                    print(" " * boardlenght)
                print(" " * yatay_konum, end="")
                print("@", end=" "*(boardlenght-yatay_konum-1))
                print()
                print("-" * 72)
            continue
        if tur %5 ==0 and tur !=0:
            if yatay_konum != boardlenght - 1:
                yatay_konum = yatay_konum + 1
            for i in range(kayma+1):
                print(" " * boardlenght)
            for i in range(len(ana_list)):
                k = 0
                for a in ana_list[i]:
                    if k < boardlenght:
                        if a == 1:
                            print("*", end="")
                        if a == 0:
                            print(" ", end="")
                    k = k + 1
                print()
            else:
                for i in range(g-1):
                    print(" " * boardlenght)
                print(" " * yatay_konum, end="")
                print("@", end=" " * (boardlenght - yatay_konum - 1))
                print()
                print("-" * 72)
            continue
    if action == "fire":
        for c in range(0,g+len(ana_list)+kayma+1):

            if tur % 5 == 4 and g == 0:
                birsayisi=0
                cmax = 0
                olur = True
                for i in range(len(ana_list)-1,-1,-1):
                    if ana_list[i][yatay_konum] == 0:
                        cmax = cmax + 1
                    if ana_list[0][yatay_konum] == 0:
                        cmax = cmax + kayma
                for i in range(len(ana_list[-1])):
                    if ana_list[-1][i] == 1:
                        birsayisi = birsayisi + 1
                if birsayisi == 1:
                    if ana_list[-1].index(1) == yatay_konum:
                        olur = False

                if c == cmax and olur == True:
                    gameover = True
                    tur = tur + 1
                    bek = False
                    for k in range(len(ana_list)):
                        if ana_list[k][yatay_konum] == 1:
                            bek = True

                    if bek == True:
                        if ana_list[x-(c-(g-yeter))-1][yatay_konum] == 1:
                            ana_list[x - (c - (g-yeter)) - 1][yatay_konum] = 0
                    if tur % 5 == 0 and tur != 0 :
                        g = g -1
                        kayma = kayma + 1
                    break

            if gameover == True:
                break

            if c >= g and c <(len(ana_list)+g) :
                if True:
                    if ana_list[x-(c-(g-yeter))-1][yatay_konum] == 1:
                        ana_list[x - (c - (g-yeter)) - 1][yatay_konum] = 0
                        kek = True
                        for j in range(len(ana_list)):
                            for k in range(len(ana_list[j])):
                                if ana_list[j][k] == 1:
                                    kek = False
                        if kek == True:
                            gamewon = True
                            break
                        for i in range(kayma):
                            print(" " * boardlenght)
                        if tur % 5 == 4:
                            print(" "*boardlenght)
                        if tur % 5 == 4 and c<1:
                            silim = True
                            for i in ana_list[-1]:
                                if i == 1:
                                    silim = False
                            if silim == True:
                                ana_list.pop(-1)
                                sildim = 1

                        for i in range(len(ana_list)):
                            k = 0


                            for a in ana_list[i]:
                                if k < boardlenght:
                                    if a == 1:
                                        print("*", end="")
                                    if a == 0:
                                        print(" ", end="")
                                k = k + 1
                            print()

                        else:
                            if tur % 5 == 4 and c<1:
                                if sildim == 1:
                                    ana_list.append([])
                                    sildim = 0
                                    for i in range(y1):
                                        ana_list[-1].append(0)
                            if tur % 5 == 4:
                                g2 = g - 1

                            else:
                                g2 = g
                            for i in range(g2):
                                print(" " * boardlenght)
                            print(" " * yatay_konum, end="")
                            print("@", end=" "*(boardlenght- yatay_konum-1))
                            print()
                            print("-" * 72)
                            break
                    else:
                        for i in range(kayma):
                            print(" " * boardlenght)
                        for i in range(len(ana_list)):
                            for a in ana_list[i]:
                                sag = 0
                                sol = 0
                                orta = 0
                                if a == 1:
                                    print("*", end="")
                                    yazdirma = yazdirma + 1
                                if a == 0 and yatay_konum == yazdirma and i == (g-c+len(ana_list)-1) and  yazma == 0 and yatay_konum == (boardlenght-1):
                                    print("|", end="")
                                    ana_list[len(ana_list) - (c - g) - 1][yatay_konum] = 0
                                    yazma = yazma + 1
                                    yazdirma = yazdirma + 1
                                    sag = 1

                                if a == 0 and yatay_konum == yazdirma and i == (g-c+len(ana_list)-1) and  yazma == 0 and yatay_konum== 0:
                                    print("|", end="")
                                    ana_list[len(ana_list) - (c - g) - 1][yatay_konum] = 0
                                    yazma = yazma + 1
                                    yazdirma = yazdirma + 1
                                    sol = 1

                                if a == 0 and yatay_konum == yazdirma and i == (g-c+len(ana_list)-1) and  yazma == 0 and yatay_konum!= (boardlenght-1) and yatay_konum !=0:
                                    print("|", end="")
                                    ana_list[len(ana_list) - (c - g) - 1][yatay_konum] = 0
                                    yazma = yazma + 1
                                    yazdirma = yazdirma + 1
                                    orta = 1
                                if a == 0 and sag ==0 and sol ==0 and orta == 0:
                                    print(" ",end="")
                                    yazdirma = yazdirma + 1

                            print()
                            yazma = 0
                            yazdirma =0
                        else:
                            for i in range(g):
                                print(" " * boardlenght)
                            print(" " * yatay_konum, end="")
                            print("@", end=" "*(boardlenght-yatay_konum-1))
                            print()
                            print("-" * 72)
            if c < g:
                for i in range(kayma):
                    print(" " * boardlenght)
                for i in range(len(ana_list)):
                    k = 0
                    for a in ana_list[i]:
                        if k < boardlenght:
                            if a == 1:
                                print("*", end="")
                            if a == 0:
                                print(" ",end="")
                        k = k + 1
                    print()
                else:
                    for d in range(g):
                        if d == (g - c-1):
                            print(" " * yatay_konum,end="")
                            print("|",end=" "*(boardlenght-yatay_konum-1))
                            if x % 2 == 0:
                               print(" "*(0))
                            else:
                                print(" " * 0)

                        else:
                            print(" " * boardlenght)

                    print(" " * yatay_konum, end="")
                    print("@", end=" "*(boardlenght-yatay_konum-1))
                    print()
                    print("-" * 72)
            if c >= g+len(ana_list) and ana_list[0][yatay_konum] == 0:


                if c != len(ana_list)+g+kayma:
                    for i in range(kayma-(c-g-len(ana_list))-1):
                        print(" "*boardlenght)
                    print(" "*yatay_konum,end="")
                    print("|",end="")
                    print(" "*(boardlenght-yatay_konum-1))
                    for i in range(c-(len(ana_list)+g)):
                        print(" "*boardlenght)
                    for i in range(len(ana_list)):
                        for a in ana_list[i]:
                            if a == 1:
                                print("*",end="")
                            if a == 0:
                                print(" ",end="")
                        print()
                    else:
                        for i in range(g):
                            print(" " * boardlenght)
                        print(" " * yatay_konum, end="")
                        print("@", end=" " * (boardlenght - yatay_konum - 1))
                        print()
                        print("-" * 72)
                    if c == g+x+kayma-1 and 1 == 2:
                        for i in range(kayma):
                            print(" " * boardlenght)
                        if tur % 5 == 4:
                            print(" " * boardlenght)
                        for i in range(len(ana_list)):
                            k = 0
                            for a in ana_list[i]:
                                if k < boardlenght:
                                    if a == 1:
                                        print("*", end="")
                                    if a == 0:
                                        print(" ", end="")
                                k = k + 1
                            print()
                        else:

                            if tur % 5 == 4:
                                g2 = g - 1
                            else:
                                g2 = g
                            for i in range(g2):
                                print(" " * boardlenght)
                            print(" " * yatay_konum, end="")
                            print("@", end=" " * (boardlenght - yatay_konum - 1))
                            print()
                            print("-" * 72)
                            break
                if c == len(ana_list)+g+kayma:
                    if tur % 5 == 4 and g == 0:
                        kayma =kayma + 1
                        gameover = True
                        break
                    for i in range(kayma):
                        print(" " * boardlenght)
                    if tur % 5 == 4:
                        print(" " * boardlenght)
                    for i in range(len(ana_list)):
                        k = 0
                        for a in ana_list[i]:
                            if k < boardlenght:
                                if a == 1:
                                    print("*", end="")
                                if a == 0:
                                    print(" ", end="")
                            k = k + 1
                        print()
                    else:

                        if tur % 5 == 4:
                            g2 = g - 1
                        else:
                            g2 = g
                        for i in range(g2):
                            print(" " * boardlenght)
                        print(" " * yatay_konum, end="")
                        print("@", end=" " * (boardlenght - yatay_konum - 1))
                        print()
                        print("-" * 72)
                        break


        if gameover == True:
            break
        silme = True
        for i in range(len(ana_list[-1])):
            if ana_list[-1][i] == 1:
                silme = False
        if silme == True:
            ana_list.pop(-1)
            g = g + 1
            yeter = yeter + 1

        tur = tur + 1
    if gamewon == True:
        break
    lol = True
    for i in range(len(ana_list)):
        for a in range(len(ana_list[i])):
            if ana_list[i][a] == 1:
                lol = False
    if lol == True:
        gamewon = True
        break

if gamewon == True:
    gameover = False


if gamewon == True:
    print("YOU WON!")
    for i in range(len(ana_list)):
        k = 0
        for a in ana_list[i]:
            if k < boardlenght:
                if a == 1:
                    print("*",end="")
                if a == 0:
                    print(" ", end="")
            k = k + 1
        print()
    else:
        for i in range(g1+x):
            print(" "*boardlenght)
        print(" "*yatay_konum,end="")
        print("@",end=" "*(boardlenght-yatay_konum-1))
        print()
        print("-"*72)
    score = 0
    for i in range(len(ana_list)):
        for a in range(len(ana_list[i])):
            if ana_list[i][a] == 0:
                score = score +1
    score = score + y * yeter
    print("YOUR SCORE:",score)
if gameover == True:
    score_non = 0
    score = 0
    for i in range(len(ana_list)):
        for a in range(len(ana_list[i])):
            if ana_list[i][a] == 1:
                score_non = score_non + 1
    score = x1*y1 - score_non
    print("GAME OVER")
    for i in range(kayma-1):
        print(" " * boardlenght)
    for i in range(len(ana_list)):
        k = 0
        for a in ana_list[i]:
            if k < boardlenght:
                if a == 1:
                    print("*",end="")
                if a == 0:
                    print(" ", end="")
            k = k + 1
        print()
    else:
        for i in range(g):
            print(" "*boardlenght)
        print(" "*yatay_konum,end="")
        print("@",end=" "*(boardlenght-yatay_konum-1))
        print()
        print("-"*72)
    print("YOUR SCORE:",score)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
