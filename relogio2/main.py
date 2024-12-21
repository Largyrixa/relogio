import pygame as pg
from time import  localtime, sleep, time
import math
from os import listdir, system
from PIL import Image


def menu():
    while True:
        print('>>>\033[33;1mESCOLHA A IMAGEM DE FUNDO\033[m<<<')
        sleep(1)
        for i, file in enumerate(files:=listdir('imagens')):
            print(f'[\033[36;1m{i}\033[m] {file}')
            sleep(0.7)
        print(f'[\033[36;1mX\033[m] sair')
        escolha = input('\033[35m>').strip()
        print('\033[m')

        try:
            escolha = int(escolha)
        except ValueError:
            if escolha.lower() == 'x':
                return False
            print('\033[31;1mINSIRA APENAS NÚMEROS!\033[m')
            continue
        if escolha not in range(len(files)):
            print('\033[31;1mINSIRA UM NÚMERO NA LISTA!\033[m')
            continue
        for _ in range(30):
            print()
        return files[escolha]   
        
def main():
    
    while localtime().tm_sec%2 != 0:
        continue
    while True:
        time1 = time()
        horario = localtime()
        h,m,s = horario.tm_hour, horario.tm_min, horario.tm_sec
        
        fundo()
        ponteiros((h,m,s))
        sleep(1-(time()-time1))
        pg.display.update()
        if not HandleEvents():
            break


def HandleEvents():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
    return True
     
def fundo():
    screen.blit(relogio,(0,0))

def ponteiros(horario:tuple[int,int,int]):
    h,m,s = horario
    # angulo de cada ponteiro 'w' de deslocamento angular
    wSec = s/60*math.pi*2 - math.pi/2
    wMin = (m/60)*math.pi*2 - math.pi/2
    wHor = (h%12)/12*math.pi*2 - math.pi/2 
    
    # posição da ponta de cada ponteiro (x,y)
    # obs: x = Raio*cos(angulo), y = Raio*sen(angulo)
    posSec = (round(100+90*math.cos(wSec)),round(100+90*math.sin(wSec)))
    posMin = (round(100+70*math.cos(wMin)),round(100+70*math.sin(wMin)))
    posHor = (round(100+50*math.cos(wHor)),round(100+50*math.sin(wHor)))
    
    # criando os ponteiros na tela
    
    pg.draw.line(screen,color=cor(centro, posSec, 'seg'),start_pos=centro,end_pos=posSec,width=2)
    pg.draw.line(screen,color=cor(centro, posMin, 'min'),start_pos=centro,end_pos=posMin,width=4)
    pg.draw.line(screen,color=cor(centro, posHor, 'hor'),start_pos=centro,end_pos=posHor,width=6)
    pg.draw.circle(screen,color=cor(centro, posSec, 'seg'),center=posSec,radius=2)
    pg.draw.circle(screen,color=cor(centro, posMin, 'min'),center=posMin,radius=2)
    pg.draw.circle(screen,color=cor(centro, posHor, 'Hor'),center=posHor,radius=3)
    
    # pinto central no relogio
    pg.draw.circle(screen,color= (0,0,0),center= centro,radius=4)

def cor(comeco, fim, tipo):
    x1,x2 = sorted((comeco[0],fim[0]))
    y1,y2 = sorted((comeco[1],fim[1]))
    if x1 == x2 or y1 == y2:
        return (255,0,0)
    area = (x1,y1,x2,y2)
    recorte = imagem.crop(area)
    pixels = list(recorte.getdata())
    media = list(sum(c)//len(c) for c in zip(*pixels))
    media = media[0:3]
    for i, el in enumerate(media):
        media[i] = abs(255-el)
    match tipo:
        case 'seg':
            media[0] += 100
            if media[0] > 255:
                media[0] = 255
        case 'min':
            for i in range(len(media)):
                media[i] -= 100
                if media[i] < 0:
                    media[i] = 0
    invertido = tuple(x for x in media)
    return invertido



if __name__ == '__main__':
    while (op:=menu()) != False:
        pg.init()
        tamanho_tela = (201,201)
        screen = pg.display.set_mode(tamanho_tela)
        centro = (100,100)
        relogio = pg.image.load(f'imagens/{op}').convert_alpha()
        imagem = Image.open(f'imagens/{op}')
        main()
        pg.quit()
        