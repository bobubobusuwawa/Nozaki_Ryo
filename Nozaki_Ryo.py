import pygame
import pickle
import sys
import math
import random
import numpy as np
import time
import os
import pprint
import cv2
from pygame.locals import *

BLACK  = (  0,   0,   0)
SILVER = (192, 208, 224)
RED    = (255,   0,   0)
CYAN   = (  0, 224, 255)



#背景
bg = [
    pygame.image.load("images/moromoro/bg1.png"),
    pygame.image.load("images/moromoro/pause.png"),
    pygame.image.load("images/moromoro/alert.png")
    ]
img_pause = [
    pygame.image.load("images/moromoro/pause_pause.png"),
    pygame.image.load("images/moromoro/pause_bar.png"),
    pygame.image.load("images/moromoro/pause_none.png"),
    pygame.image.load("images/moromoro/pause_kaijo.png"),
    pygame.image.load("images/moromoro/pause_title.png"),
    pygame.image.load("images/moromoro/pause_manual.png"),
    pygame.image.load("images/moromoro/pause_restart.png"),#6
    pygame.image.load("images/moromoro/title_yesno.png"),
    pygame.image.load("images/moromoro/title_yes.png"),
    pygame.image.load("images/moromoro/title_no.png"),
    
    ]

img_kiroku = [
    pygame.image.load("images/moromoro/kiroku_yesno.png"),
    pygame.image.load("images/moromoro/kiroku_yes.png"),
    pygame.image.load("images/moromoro/kiroku_no.png"),
    pygame.image.load("images/moromoro/kirokuchu01.png"),
    pygame.image.load("images/moromoro/kirokuchu02.png"),
    
    ]

#かぶせ
bg_over = [
    pygame.image.load("images/moromoro/bg_over.png"),
    pygame.image.load("images/moromoro/bg_over2.png")

    ]

#自機
img_jiki = [
    pygame.image.load("images/jiki/jiki.png"),
    pygame.image.load("images/jiki/atarihantei.png"),
    pygame.image.load("images/jiki/atarihantei2.png"),
    pygame.image.load("images/jiki/jiki_muteki.png"),

    ] 

#自機のショット画像
img_weapon = [
    pygame.image.load("images/jiki/bullet.png"),
    pygame.image.load("images/jiki/bullet2.png"),
    pygame.image.load("images/jiki/BOMB.png")
    ]


#敵画像
img_enemy = [
    pygame.image.load("images/teki/zako01_mae.png"),
    pygame.image.load("images/teki/zako01_hidari.png"),
    pygame.image.load("images/teki/zako01_migi.png"),
    pygame.image.load("images/teki/zako02_mae.png"),
    pygame.image.load("images/teki/zako02_hidari.png"),
    pygame.image.load("images/teki/zako02_migi.png"),
    pygame.image.load("images/teki/zako03_mae.png"),
    pygame.image.load("images/teki/zako03_hidari.png"),
    pygame.image.load("images/teki/zako03_migi.png"),
    pygame.image.load("images/teki/zako04.png"),
    pygame.image.load("images/teki/zako05.png"),#10

    #stage01
    pygame.image.load("images/teki/zako01_hidari.png"),#11
    pygame.image.load("images/teki/zako01_migi.png"),#12
    pygame.image.load("images/teki/zako02_mae.png"),#13
    pygame.image.load("images/teki/zako01_hidari.png"),#14
    pygame.image.load("images/teki/zako01_migi.png"),#15
    ]

img_boss = [
    pygame.image.load("images/teki/boss01.png"),
    pygame.image.load("images/teki/boss01_hit.png"),

    ]

img_item = [
    pygame.image.load("images/icon/zanki_icon.png"),
    pygame.image.load("images/icon/bomb_icon.png"),
    pygame.image.load("images/icon/Power.png"), #2
    pygame.image.load("images/icon/Ten.png"),

    ]

#弾幕画像
img_tama = [
    None,
    pygame.image.load("images/tama/01.png"),
    pygame.image.load("images/tama/02.png"),
    pygame.image.load("images/tama/03.png"),
    pygame.image.load("images/tama/04.png"),
    pygame.image.load("images/tama/05.png"),
    pygame.image.load("images/tama/06.png"),
    pygame.image.load("images/tama/07.png"),
    pygame.image.load("images/tama/08.png"),
    pygame.image.load("images/tama/09.png"),
    pygame.image.load("images/tama/10.png"),
    pygame.image.load("images/tama/11.png"),
    pygame.image.load("images/tama/12.png"),
    pygame.image.load("images/tama/13.png"),
    pygame.image.load("images/tama/14.png"),
    pygame.image.load("images/tama/01.png"),#15
    
    ]

#爆発エフェクト用画像
img_explode = [
    None,
    pygame.image.load("images/anime/explosion1.png"),
    pygame.image.load("images/anime/explosion2.png"),
    pygame.image.load("images/anime/explosion3.png"),
    pygame.image.load("images/anime/explosion4.png"),
    pygame.image.load("images/anime/explosion5.png")
    ]

img_graze = [
    None,
    pygame.image.load("images/anime/graze1.png"),
    pygame.image.load("images/anime/graze2.png"),
    pygame.image.load("images/anime/graze3.png"),
    pygame.image.load("images/anime/graze4.png"),
    pygame.image.load("images/anime/graze5.png"),
    pygame.image.load("images/anime/graze6.png"),
    pygame.image.load("images/anime/graze7.png"),
    pygame.image.load("images/anime/graze1.png"),
    pygame.image.load("images/anime/graze2.png"),
    pygame.image.load("images/anime/graze3.png"),
    pygame.image.load("images/anime/graze4.png"),
    pygame.image.load("images/anime/graze5.png"),
    pygame.image.load("images/anime/graze6.png"),
    pygame.image.load("images/anime/graze7.png"),
    
    ]

#タイトルロゴ
img_title = [
    pygame.image.load("images/title/logo.png"), 
    pygame.image.load("images/title/logo2.png"),
    pygame.image.load("images/title/start.png"), 
    pygame.image.load("images/title/music.png"), 
    pygame.image.load("images/title/practice.png"), 
    pygame.image.load("images/title/record.png"), #5
    pygame.image.load("images/title/manual.png"), 
    pygame.image.load("images/title/setting.png"), 
    pygame.image.load("images/title/quit.png"), 
    pygame.image.load("images/title/loading.png"),
    pygame.image.load("images/title/logo2-1.png"),#10
    pygame.image.load("images/title/logo2-2.png"),
    pygame.image.load("images/title/logo2-3.png"),
    ]

img_logo = [
    pygame.image.load("images/moromoro/stage01_logo.png"), 
    pygame.image.load("images/moromoro/stage02_logo.png"), 
    pygame.image.load("images/moromoro/stage03_logo.png"), 

    ]

img_manual = [
    pygame.image.load("images/title/manual2.png"), 
    ]

img_diff = [
    pygame.image.load("images/title/diff.png"), 
    pygame.image.load("images/title/easy.png"), 
    pygame.image.load("images/title/normal.png"),
    pygame.image.load("images/title/hard.png"),    
    pygame.image.load("images/moromoro/stage_easy.png"), 
    pygame.image.load("images/moromoro/stage_normal.png"),
    pygame.image.load("images/moromoro/stage_hard.png"), 

    ]

img_jiki_sentaku = [
    pygame.image.load("images/title/jiki_sentaku.png"), 
    pygame.image.load("images/title/jiki_power.png"), 
    pygame.image.load("images/title/jiki_horming.png"),
    
    ]

img_stage_select = [
    pygame.image.load("images/moromoro/stage00_select.png"), 
    pygame.image.load("images/moromoro/stage01_select.png"), 
    pygame.image.load("images/moromoro/stage02_select.png"), 
    pygame.image.load("images/moromoro/stage03_select.png"), 
    pygame.image.load("images/moromoro/stage04_select.png"), 
    pygame.image.load("images/moromoro/stage05_select.png"), 
    ]

img_stand = [
    pygame.image.load("images/title/jiki01.png"), 
    

    ]

img_icon = [
    pygame.image.load("images/icon/zanki_icon.png"),
    pygame.image.load("images/icon/bomb_icon.png"),
    pygame.image.load("images/icon/icon.png"),
    
    ]

img_kaiwa = [
    pygame.image.load("images/kaiwa/kaiwa01.png"),
    pygame.image.load("images/kaiwa/kaiwa02.png"),
    pygame.image.load("images/kaiwa/kaiwa03.png"),
    pygame.image.load("images/kaiwa/kaiwa04.png"),
    pygame.image.load("images/kaiwa/kaiwa05.png"),
    pygame.image.load("images/kaiwa/kaiwa06.png"),
    pygame.image.load("images/kaiwa/kaiwa07.png"),
    pygame.image.load("images/kaiwa/kaiwa08.png"),

    ]

img_load = [
    pygame.image.load("images/anime/load01.png"),
    pygame.image.load("images/anime/load02.png"),
    pygame.image.load("images/anime/load03.png"),
    pygame.image.load("images/anime/load04.png"),

    ]

se_list=[
    None,
    "sounds/se/se_sentaku.ogg",
    "sounds/se/se_kettei.ogg",
    "sounds/se/se_quit.ogg",
    "sounds/se/se_pause.ogg",
    "sounds/se/jiki_shot.ogg",
    "sounds/se/jiki_bomb.ogg",
    "sounds/se/jiki_shinu.ogg",#7
    "sounds/se/jiki_extend.ogg",
    "sounds/se/jiki_get_bomb.ogg",
    "sounds/se/jiki_graze.ogg",#10
    "sounds/se/teki_shot.ogg",
    "sounds/se/teki_damage.ogg",
    "sounds/se/teki_shinu.ogg",
    "sounds/se/boss_deru.ogg",
    "sounds/se/boss_shinu.ogg",#15
    "sounds/se/se_ring01.ogg",
    "sounds/se/jiki_item_get.ogg",
    ]

bgm_list =[
    "sounds/bgm/bgm_title.ogg",#タイトル画面0
    "sounds/bgm/bgm_stage01.ogg",#一面1
    "sounds/bgm/bgm_boss01.ogg",#一面ボス2
    "sounds/bgm/bgm_stage02.ogg",#二面3
    "sounds/bgm/bgm_boss02.ogg",#二面ボス4
    "sounds/bgm/bgm_stage03.ogg",#三面5
    "sounds/bgm/bgm_boss03.ogg",#三面ボス6
    "sounds/bgm/bgm_gameclear.ogg",#クリア7
    "sounds/bgm/bgm_gameover.ogg",#ゲームオーバー8
    
    ]


stage_idx = 0
stage_count = 0
title_idx = 0
title_idx2 = 0

idx = 12    #初期値0.5
tmr = 0
bomb_tmr = 0
score = 0
hisco = 10000
ten_max = 0
new_record = False
bg_y = 0
diff = 0

WAKU = [65, 665, 80, 608]

ZAKO = 0
BOSS = 1
ITEM = 2
TAMA = 3


ss_x = 344                     #自機のx座標
ss_y = 620                     #自機のy座標
ss_d = 0                     #自機の傾き(0:なし, 1:左, 2:右　)    
ss_shield = 5                #残機
ss_muteki = 0                #無敵判定用
key_spc = 0
key_z = 0
key_x = 0
key_shift = 0
MISSILE_MAX = 2000          #自機の弾の最大数
msl_no = 0                   #弾の発射に使う変数
speed_mod = False            #自機の移動速度遅くする変数(True:遅い, False:速い)
speed_jiki = 10              #自機の移動距離の変数


#ホーミング系の陰陽玉座標
tama_x_p1 = 0
tama_y_p1 = 0
tama_x_p2 = 0
tama_y_p2 = 0
tama_x_p3 = 0
tama_y_p3 = 0
tama_x_p4 = 0
tama_y_p4 = 0
tama_x_p5 = 0
tama_y_p5 = 0

msl_f = [False]*MISSILE_MAX  #弾の存在を確認する変数
msl_x = [0]*MISSILE_MAX      #弾のx座標
msl_y = [0]*MISSILE_MAX      #弾のy座標
msl_a = [0]*MISSILE_MAX      #弾の角度
msl_type = [0]*MISSILE_MAX     #弾の種類
kakudo = 0 #弾の角度
BOMB = 3
POWER = 0
graze = 0
jiki_id = 0

ENEMY_MAX = 200             #敵の最大数
emy_no = 0                   #敵を出すときに使うリストの添え字用の変数
emy_f = [False]*ENEMY_MAX    #敵が出現しているか管理するフラグのリスト
emy_x = [0]*ENEMY_MAX        #敵のx座標
emy_y = [0]*ENEMY_MAX        #敵のy座標
emy_a = [0]*ENEMY_MAX        #敵の角度
emy_type = [0]*ENEMY_MAX     #敵の種類
emy_speed = [0]*ENEMY_MAX    #敵の速さ
emy_shield = [0]*ENEMY_MAX   #敵の体力
emy_decay = [0]*ENEMY_MAX     #敵の弾の種類
emy_id = [0]*ENEMY_MAX       #敵の種類
emy_count = [0]*ENEMY_MAX    #敵の動きを管理するリスト

LINE_T = 0                 #敵が消える上ラインの座標
LINE_B = 702                 #敵が消える下ラインの座標
LINE_L = 22                 #敵が消える左ラインの座標
LINE_R = 630                #敵が消える右ラインの座標

EFFECT_MAX = 150             #爆発の最大数
eff_no = 0                   #爆発を使う変数
eff_p = [0]*EFFECT_MAX       #爆発の画像番号用のリスト
eff_x = [0]*EFFECT_MAX       #爆発のx座標
eff_y = [0]*EFFECT_MAX       #爆発のy座標

eff_nog = 0                   #爆発を使う変数
eff_pg = [0]*EFFECT_MAX       #爆発の画像番号用のリスト
eff_xg = [0]*EFFECT_MAX       #爆発のx座標
eff_yg = [0]*EFFECT_MAX       #爆発のy座標
key_if = False

rooper = 0

tamadashi = True
counter = -1
choose_kabuse = 1
theta = 0

geji = 0


def get_ang(x1, y1, x2, y2):#1:自機　2:敵
    X = x2-x1
    Y = y2-y1
    if X == 0:
        X = 1
    if Y == 0:
        Y = 1
    theta = np.arctan( Y/X ) + math.radians(180)
    if X < 0:
        theta = theta + math.radians(180)     

    return theta#自機狙い用の関数

def get_dis(x1, y1, x2, y2): #二点間の距離を求める関数

    return( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) )



def move_starship(scrn, key, id): #自機に関する関数
    global idx, tmr, ss_x, ss_y, ss_d, key_spc, key_z, key_x, key_shift, ss_shield, ss_muteki, speed_mod, speed_jiki, mini_big, BOMB, bomb_tmr, graze, score, POWER
    global tama_x_p1, tama_y_p1, tama_x_p2, tama_y_p2, tama_x_p3, tama_y_p3, tama_x_p4, tama_y_p4, tama_x_p5, tama_y_p5
    global ZAKO, BOSS, ITEM, TAMA
    jiki = id

    if key[pygame.K_UP] == 1: #上操作
        ss_y = ss_y - speed_jiki
        if ss_y < WAKU[0]:
            ss_y = WAKU[0]
    if key[pygame.K_DOWN] == 1: #下操作
        ss_y = ss_y + speed_jiki
        if ss_y > WAKU[1]:
            ss_y = WAKU[1]
    if key[pygame.K_LEFT] == 1: #左操作
        ss_d = 1 #傾きを１（左）にする
        ss_x = ss_x - speed_jiki
        if ss_x < WAKU[2]:
            ss_x = WAKU[2]
    if key[pygame.K_RIGHT] == 1: #右操作
        ss_d = 2 #傾きを２（右）にする
        ss_x = ss_x + speed_jiki
        if ss_x > WAKU[3]:
            ss_x = WAKU[3]

    key_z = (key_z+1)*key[K_z]   #Zキーで通常ショット
    if key_z%4 == 1:
        if jiki == 0:
            set_missile_power(0)
        if jiki == 1:
            set_missile_horming(0)
        set_se(5)

    key_x = (key_x+1)*key[K_x]   #Xキーでボム
    if key_x == 1 and BOMB > 0:# and bomb_tmr == 0:
        set_missile_power(10)
        BOMB = BOMB - 1
        set_se(6)

    if key[pygame.K_LSHIFT] == 1: #Shiftで低速
        speed_mod = True
    else:
        speed_mod = False

    
    if bomb_tmr > 0:
        bomb_tmr = bomb_tmr - 1

    
    if ss_muteki > 0:
        ss_muteki = ss_muteki - 1    
    elif idx == 8:#ヒット判定
        for i in range(ENEMY_MAX):
            if emy_f[i] ==True and emy_type[i] == ZAKO:
                w = img_enemy[emy_id[i]].get_width()
                h = img_enemy[emy_id[i]].get_height()
                r = int ((w+h)/4 + (18+18)/4)
                if get_dis(emy_x[i], emy_y[i], ss_x-10, ss_y-8) < r*r:
                    set_effect(ss_x, ss_y)
                    ss_shield = ss_shield - 1
                    set_se(7)
                    BOMB = 3
                        
                    if ss_muteki == 0:
                        ss_muteki = 180
                    if ss_shield <= 0:
                        ss_shield = 0
                        idx = 10
                        tmr = 0
                    emy_f[i] = False #自機の操作に関する関数

            if emy_f[i] ==True and emy_type[i] == TAMA:
                w = img_tama[emy_id[i]].get_width()
                h = img_tama[emy_id[i]].get_height()
                r = int ((w+h)/4 + (18+18)/4)
                if get_dis(emy_x[i], emy_y[i], ss_x-10, ss_y-8) < r*r:
                    set_effect(ss_x, ss_y)
                    ss_shield = ss_shield - 1
                    set_se(7)
                    BOMB = 3
                        
                    if ss_muteki == 0:
                        ss_muteki = 180
                    if ss_shield <= 0:
                        ss_shield = 0
                        idx = 10
                        tmr = 0
                    emy_f[i] = False #自機の操作に関する関数
                if get_dis(emy_x[i], emy_y[i], ss_x-14, ss_y-8) < r*r+1000:
                    set_graze(ss_x, ss_y)
                    graze = graze + 1
                    set_se(10)
                    score = score + 1

    if speed_mod == True:
        if jiki == 1:
            if POWER < 15:
                tama_x_p1 = ss_x
                tama_y_p1 = ss_y
            if 15 <= POWER and POWER < 30:#2
                tama_x_p1 = ss_x+60
                tama_y_p1 = ss_y+20
                tama_x_p2 = ss_x-60
                tama_y_p2 = ss_y+20
                scrn.blit(img_jiki[1], [tama_x_p1-17, tama_y_p1-13])
                scrn.blit(img_jiki[1], [tama_x_p2-17, tama_y_p2-13])

            if 30 <= POWER and POWER < 45:#3
                tama_x_p1 = ss_x+60
                tama_y_p1 = ss_y+20
                tama_x_p2 = ss_x-60
                tama_y_p2 = ss_y+20
                tama_x_p3 = ss_x
                tama_y_p3 = ss_y+40
                scrn.blit(img_jiki[1], [tama_x_p1-17, tama_y_p1-13])
                scrn.blit(img_jiki[1], [tama_x_p2-17, tama_y_p2-13])
                scrn.blit(img_jiki[1], [tama_x_p3-17, tama_y_p3-13])
        
            if 45 <= POWER and POWER < 60:#4
                tama_x_p1 = ss_x+60
                tama_y_p1 = ss_y+20
                tama_x_p2 = ss_x-60
                tama_y_p2 = ss_y+20
                tama_x_p3 = ss_x+120
                tama_y_p3 = ss_y+40
                tama_x_p4 = ss_x-120
                tama_y_p4 = ss_y+40
                scrn.blit(img_jiki[1], [tama_x_p1-17, tama_y_p1-13])
                scrn.blit(img_jiki[1], [tama_x_p2-17, tama_y_p2-13])
                scrn.blit(img_jiki[1], [tama_x_p3-17, tama_y_p3-13])
                scrn.blit(img_jiki[1], [tama_x_p4-17, tama_y_p4-13])

            if 60 <= POWER:#5
                tama_x_p1 = ss_x+60
                tama_y_p1 = ss_y+20
                tama_x_p2 = ss_x-60
                tama_y_p2 = ss_y+20
                tama_x_p3 = ss_x+120
                tama_y_p3 = ss_y+40
                tama_x_p4 = ss_x-120
                tama_y_p4 = ss_y+40
                tama_x_p5 = ss_x
                tama_y_p5 = ss_y+50
                scrn.blit(img_jiki[1], [tama_x_p1-17, tama_y_p1-13])
                scrn.blit(img_jiki[1], [tama_x_p2-17, tama_y_p2-13])
                scrn.blit(img_jiki[1], [tama_x_p3-17, tama_y_p3-13])
                scrn.blit(img_jiki[1], [tama_x_p4-17, tama_y_p4-13])
                scrn.blit(img_jiki[1], [tama_x_p5-17, tama_y_p5-13])

        speed_jiki = 4
        atarihantei = pygame.transform.rotozoom(img_jiki[2], tmr%360, 1.0)
        scrn.blit(atarihantei, [ss_x-100, ss_y-100])
        scrn.blit(img_jiki[0], [ss_x-37, ss_y-48])
        scrn.blit(img_jiki[1], [ss_x-17, ss_y-13])
        
    else:
        if jiki == 1:
            if POWER < 15:
                tama_x_p1 = ss_x
                tama_y_p1 = ss_y

            if 15 <= POWER and POWER < 30:#2
                tama_x_p1 = ss_x + 60*math.sin(math.radians((tmr*8)%360))
                tama_y_p1 = ss_y + 60*math.cos(math.radians((tmr*8)%360))
                tama_x_p2 = ss_x + 60*math.sin(math.radians((tmr*8)%360+180))
                tama_y_p2 = ss_y + 60*math.cos(math.radians((tmr*8)%360+180))
                scrn.blit(img_jiki[1], [tama_x_p1-17, tama_y_p1-13])
                scrn.blit(img_jiki[1], [tama_x_p2-17, tama_y_p2-13])

            if 30 <= POWER and POWER < 45:#3
                tama_x_p1 = ss_x + 60*math.sin(math.radians((tmr*8)%360))
                tama_y_p1 = ss_y + 60*math.cos(math.radians((tmr*8)%360))
                tama_x_p2 = ss_x + 60*math.sin(math.radians((tmr*8)%360+120))
                tama_y_p2 = ss_y + 60*math.cos(math.radians((tmr*8)%360+120))
                tama_x_p3 = ss_x + 60*math.sin(math.radians((tmr*8)%360+240))
                tama_y_p3 = ss_y + 60*math.cos(math.radians((tmr*8)%360+240))
                scrn.blit(img_jiki[1], [tama_x_p1-17, tama_y_p1-13])
                scrn.blit(img_jiki[1], [tama_x_p2-17, tama_y_p2-13])
                scrn.blit(img_jiki[1], [tama_x_p3-17, tama_y_p3-13])
        
            if 45 <= POWER and POWER < 60:#4
                tama_x_p1 = ss_x + 60*math.sin(math.radians((tmr*8)%360))
                tama_y_p1 = ss_y + 60*math.cos(math.radians((tmr*8)%360))
                tama_x_p2 = ss_x + 60*math.sin(math.radians((tmr*8)%360+90))
                tama_y_p2 = ss_y + 60*math.cos(math.radians((tmr*8)%360+90))
                tama_x_p3 = ss_x + 60*math.sin(math.radians((tmr*8)%360+180))
                tama_y_p3 = ss_y + 60*math.cos(math.radians((tmr*8)%360+180))
                tama_x_p4 = ss_x + 60*math.sin(math.radians((tmr*8)%360+270))
                tama_y_p4 = ss_y + 60*math.cos(math.radians((tmr*8)%360+270))
                scrn.blit(img_jiki[1], [tama_x_p1-17, tama_y_p1-13])
                scrn.blit(img_jiki[1], [tama_x_p2-17, tama_y_p2-13])
                scrn.blit(img_jiki[1], [tama_x_p3-17, tama_y_p3-13])
                scrn.blit(img_jiki[1], [tama_x_p4-17, tama_y_p4-13])

            if 60 <= POWER:#5
                tama_x_p1 = ss_x + 60*math.sin(math.radians((tmr*8)%360))
                tama_y_p1 = ss_y + 60*math.cos(math.radians((tmr*8)%360))
                tama_x_p2 = ss_x + 60*math.sin(math.radians((tmr*8)%360+72))
                tama_y_p2 = ss_y + 60*math.cos(math.radians((tmr*8)%360+72))
                tama_x_p3 = ss_x + 60*math.sin(math.radians((tmr*8)%360+144))
                tama_y_p3 = ss_y + 60*math.cos(math.radians((tmr*8)%360+144))
                tama_x_p4 = ss_x + 60*math.sin(math.radians((tmr*8)%360+216))
                tama_y_p4 = ss_y + 60*math.cos(math.radians((tmr*8)%360+216))
                tama_x_p5 = ss_x + 60*math.sin(math.radians((tmr*8)%360+288))
                tama_y_p5 = ss_y + 60*math.cos(math.radians((tmr*8)%360+288))
                scrn.blit(img_jiki[1], [tama_x_p1-17, tama_y_p1-13])
                scrn.blit(img_jiki[1], [tama_x_p2-17, tama_y_p2-13])
                scrn.blit(img_jiki[1], [tama_x_p3-17, tama_y_p3-13])
                scrn.blit(img_jiki[1], [tama_x_p4-17, tama_y_p4-13])
                scrn.blit(img_jiki[1], [tama_x_p5-17, tama_y_p5-13])
        
        speed_jiki = 10
        scrn.blit(img_jiki[0], [ss_x-37, ss_y-48])

    if ss_muteki > 0:
        if ss_muteki%2 == 0: #無敵状態で点滅させる
            scrn.blit(img_jiki[3], [ss_x-37, ss_y-48])
        
    #atarihantei = pygame.transform.rotozoom(img_icon[0], 0, 0.5)  #当たり判定表示
    #scrn.blit(atarihantei, [ss_x-17, ss_y-13])

def set_missile_power(typ):#弾生成時のパラメーター
    global msl_no, ss_muteki, bomb_tmr, jiki, POWER
    global tama_x_p1, tama_y_p1, tama_x_p2, tama_y_p2, tama_x_p3, tama_y_p3, tama_x_p4, tama_y_p4, tama_x_p5, tama_y_p5
    if typ == 0:#パワー系
        if POWER < 20:
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x-8
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX

        if 20 <= POWER and POWER < 40:
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x-17
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX

        if 40 <= POWER and POWER < 60:
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x-25
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x-8
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x+9
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX

        if 60 <= POWER and POWER < 80:
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x-34
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x-17
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x+17
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX

        if 80 <= POWER and POWER < 100:
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x-42
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x-25
            msl_y[msl_no] = ss_y-16
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x-8
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x+9
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x+26
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX

        if 100 <= POWER:
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x-34
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x-17
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x+17
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x-48
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x+34
            msl_y[msl_no] = ss_y-50
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX

    if typ == 10:
        msl_f[msl_no] = True
        msl_x[msl_no] = ss_x
        msl_y[msl_no] = ss_y-50
        msl_a[msl_no] = 270
        msl_type[msl_no] = 2
        ss_muteki = 240
        bomb_tmr = 180
        msl_no = (msl_no+1)%MISSILE_MAX#自機の弾をセット

def set_missile_horming(typ):#弾生成時のパラメーター
    global msl_no, ss_muteki, bomb_tmr, jiki, POWER
    global tama_x_p1, tama_y_p1, tama_x_p2, tama_y_p2, tama_x_p3, tama_y_p3, tama_x_p4, tama_y_p4, tama_x_p5, tama_y_p5
    if typ == 0:#ホーミング
        if POWER < 15:
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p1-8.5
            msl_y[msl_no] = tama_y_p1
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX

        if 15 <= POWER and POWER < 30:
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p1-8.5
            msl_y[msl_no] = tama_y_p1
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p2-8.5
            msl_y[msl_no] = tama_y_p2
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX

        if 30 <= POWER and POWER < 45:
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p1-8.5
            msl_y[msl_no] = tama_y_p1
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p2-8.5
            msl_y[msl_no] = tama_y_p2
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p3-8.5
            msl_y[msl_no] = tama_y_p3
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX

        if 45 <= POWER and POWER < 60:
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p1-8.5
            msl_y[msl_no] = tama_y_p1
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p2-8.5
            msl_y[msl_no] = tama_y_p2
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p3-8.5
            msl_y[msl_no] = tama_y_p3
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p4-8.5
            msl_y[msl_no] = tama_y_p4
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX

        if 60 <= POWER:
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p1-8.5
            msl_y[msl_no] = tama_y_p1
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p2-8.5
            msl_y[msl_no] = tama_y_p2
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p3-8.5
            msl_y[msl_no] = tama_y_p3
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p4-8.5
            msl_y[msl_no] = tama_y_p4
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
            msl_f[msl_no] = True
            msl_x[msl_no] = tama_x_p5-8.5
            msl_y[msl_no] = tama_y_p5
            msl_a[msl_no] = 270
            msl_type[msl_no] = 1
            msl_no = (msl_no+1)%MISSILE_MAX
    if typ == 10:
        msl_f[msl_no] = True
        msl_x[msl_no] = ss_x
        msl_y[msl_no] = ss_y-50
        msl_a[msl_no] = 270
        msl_type[msl_no] = 2
        ss_muteki = 240
        bomb_tmr = 180
        msl_no = (msl_no+1)%MISSILE_MAX#自機の弾をセット

def move_missile(scrn):
    global jiki_id
    for i in range(MISSILE_MAX):
            if msl_f[i] == True:
                if msl_type[i] == 1:#通常弾
                    msl_x[i] = msl_x[i] + 36*math.cos(math.radians(msl_a[i]))
                    msl_y[i] = msl_y[i] + 36*math.sin(math.radians(msl_a[i]))
                    img_rz = pygame.transform.rotozoom(img_weapon[jiki_id], -90-msl_a[i], 1.0)
                    scrn.blit(img_rz, [msl_x[i]-img_rz.get_width()/2, msl_y[i]-img_rz.get_height()/2])

                elif msl_type[i] == 2:#ボム
                    msl_x[i] = msl_x[i] + 36*math.cos(math.radians(msl_a[i]))
                    msl_y[i] = msl_y[i] + 3*math.sin(math.radians(msl_a[i]))
                    img_rz = pygame.transform.rotozoom(img_weapon[2], -90-msl_a[i], 1.0)
                    scrn.blit(img_rz, [msl_x[i]-img_rz.get_width()/2, msl_y[i]-img_rz.get_height()/2])


            if msl_type[i] == 1:
                if msl_y[i] < 0 or msl_x[i] < 0 or msl_x[i] > 960:
                    msl_f[i] = False#弾の移動

            elif msl_type[i] == 2:
                if msl_y[i] < -300 or msl_x[i] < -300 or msl_x[i] > 960:
                    msl_f[i] = False#弾の移動

def bring_enemy():#敵を出すシナリオ
    global ss_x, ss_y, kakudo, stage_idx, counter, idx, stage_count, ZAKO, BOSS, ITEM, TAMA, tmr, diff
    sec = tmr/30
    if stage_count == 0:#テスト用
        if stage_idx == 0:
            if 1 <= sec and sec <= 5:
                if tmr%30 == 0:
                    set_enemy(570, LINE_T, 90, ZAKO, 3, 3, 160, 11)
                    #set_enemy(540, LINE_T+20, 90, ZAKO, 3, 3, 180, 11)

            if 6 <= sec and sec <= 11:
                if tmr%30 == 0:
                    set_enemy(118, LINE_T, 90, ZAKO, 3, 3, 180, 12)
                    #set_enemy(148, LINE_T+20, 90, ZAKO, 3, 3, 200, 12)

            if 25 <= sec and sec <= 29:
                if tmr%30 == 0:
                    set_enemy(570, LINE_T, 90, ZAKO, 3, 3, 180, 11)
                    set_enemy(540, LINE_T+20, 90, ZAKO, 3, 3, 160, 11)

            if 30 <= sec and sec <= 35:
                if tmr%30 == 0:
                    set_enemy(118, LINE_T, 90, ZAKO, 3, 3, 200, 12)
                    set_enemy(148, LINE_T+20, 90, ZAKO, 3, 3, 180, 12)

            if sec == 50:
                set_enemy(334, LINE_T, 90, BOSS, 3, 1000,120, 0)

    if stage_count == 1:#stage1
        if stage_idx == 1:
            if 1 <= sec and sec <= 5:
                if tmr%30 == 0:
                    set_enemy(570, LINE_T, 90, ZAKO, 3, 3, 160, 11)
                    #set_enemy(540, LINE_T+20, 90, ZAKO, 3, 3, 180, 11)

            if 6 <= sec and sec <= 11:
                if tmr%30 == 0:
                    set_enemy(118, LINE_T, 90, ZAKO, 3, 3, 180, 12)
                    #set_enemy(148, LINE_T+20, 90, ZAKO, 3, 3, 200, 12)

            if 25 <= sec and sec <= 29:
                if tmr%30 == 0:
                    set_enemy(570, LINE_T, 90, ZAKO, 3, 3, 180, 11)
                    set_enemy(540, LINE_T+20, 90, ZAKO, 3, 3, 160, 11)

            if 30 <= sec and sec <= 35:
                if tmr%30 == 0:
                    set_enemy(118, LINE_T, 90, ZAKO, 3, 3, 200, 12)
                    set_enemy(148, LINE_T+20, 90, ZAKO, 3, 3, 180, 12)

            if sec == 50:
                set_enemy(334, LINE_T, 90, BOSS, 3, 100*diff,120, 0)

        if stage_idx == 2:
            if 1 <= sec and sec <= 5:
                if tmr%30 == 0:
                    set_enemy(570, LINE_T, 90, ZAKO, 3, 3, 160, 14)
                    #set_enemy(540, LINE_T+20, 90, ZAKO, 3, 3, 180, 11)

            if 6 <= sec and sec <= 11:
                if tmr%30 == 0:
                    set_enemy(118, LINE_T, 90, ZAKO, 3, 3, 180, 15)
                    #set_enemy(148, LINE_T+20, 90, ZAKO, 3, 3, 200, 12)

            if 25 <= sec and sec <= 30:
                if tmr%120 == 0:
                    set_enemy(570, LINE_T, 90, ZAKO, 3, 3, 800, 13)
                    set_enemy(540, LINE_T+20, 90, ZAKO, 3, 3, 800, 13)

            if 30 <= sec and sec <= 35:
                if tmr%120 == 0:
                    set_enemy(118, LINE_T, 90, ZAKO, 3, 3, 800, 13)
                    set_enemy(148, LINE_T+20, 90, ZAKO, 3, 3, 800, 13)

            if sec == 50:
                set_bgm(2)
                set_enemy(334, LINE_T, 90, BOSS, 3, 2000, 120, 0)


        if stage_idx == 3:
            if tmr == 1:
                pygame.mixer.fadeout(4000)
            if tmr == 120:
                stage_count += 1
                idx = 0.5
                tmr = 270+150*(stage_count-1)

    if stage_count == 2:#stage
        if stage_idx == 1:
            if tmr == 180:
                idx = 11
                tmr = 0

                


def set_enemy(x, y, a, ty, sp, sh, dec, id):
    global emy_no
    while True:
        if emy_f[emy_no] == False:
            emy_f[emy_no] = True
            emy_x[emy_no] = x         #敵のX
            emy_y[emy_no] = y         #敵のY
            emy_a[emy_no] = a         #敵の角度
            emy_type[emy_no] = ty     #敵のtype
            emy_speed[emy_no] = sp    #敵のspeed
            emy_shield[emy_no] = sh   #敵の体力
            emy_decay[emy_no] = dec
            emy_id[emy_no] = id
            emy_count[emy_no] = 0
            break
        emy_no = (emy_no+1)%ENEMY_MAX#敵機のセット



def move_enemy(scrn):#敵機の移動
    global tmr, sec, idx, score, ss_shield, hisco, new_record, stage_idx, tamadashi, ss_x, ss_y, BOMB, POWER, ten_max, diff, bomb_tmr, geji, stage_count
    global ZAKO, BOSS, ITEM, TAMA
    
    for i in range(ENEMY_MAX):
        jikinerai = math.degrees(get_ang(ss_x, ss_y, emy_x[i], emy_y[i]))
        if emy_f[i] == True and tamadashi == True:
            png = emy_id[i]
            if emy_type[i] == ZAKO:
                ang = 0 

                emy_x[i] = emy_x[i] + emy_speed[i]*math.cos(math.radians(emy_a[i]))
                emy_y[i] = emy_y[i] + emy_speed[i]*math.sin(math.radians(emy_a[i]))

                w = img_enemy[png].get_width()
                h = img_enemy[png].get_height()
                r = int((w+h)/4)+12
                er = int((w+h)/4)
                for n in range(MISSILE_MAX):
                    if msl_f[n] == True and msl_type[n] == 2 and get_dis(emy_x[i], emy_y[i], msl_x[n], msl_y[n]) < 180*180:
                        set_effect(emy_x[i]+random.randint(-er, er), emy_y[i]+random.randint(-er, er))
                        set_se(13)
                        emy_f[i] = False
                        score = score + 100


                    if msl_f[n] == True and get_dis(emy_x[i], emy_y[i], msl_x[n], msl_y[n]) < r*r:
                        msl_f[n] = False
                        set_effect(emy_x[i]+random.randint(-er, er), emy_y[i]+random.randint(-er, er))
                        if msl_type[i] == 1 and emy_count[i] != 2:
                            emy_shield[i] = emy_shield[i] - 1
                        if msl_type[i] == 2 and emy_count[i] != 2:
                            emy_shield[i] = emy_shield[i] - 10
                        score = score + 100
                        if score > hisco:
                            hisco = score
                            new_record = True
                if emy_shield[i] <= 0:
                    set_se(13)
                    emy_f[i] = False
                            

            if emy_type[i] == ZAKO:
                
                #STAGE01
                if emy_id[i] == 11:
                    if emy_count[i] < diff:
                        if tmr%45 == 0:
                            set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 2.5, 0, 0, 2)
                            set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 3.0, 0, 0, 2)
                            emy_count[i] += 1
                            set_se(11)
                    if emy_y[i] >= emy_decay[i]:
                        if emy_a[i] <= 180:
                            emy_a[i] += (abs(emy_y[i]-emy_decay[i]))

                    if emy_shield[i] == 0:
                        set_enemy(emy_x[i], emy_y[i], 90, ITEM, 1.5, 0, 0, 2)
                if emy_id[i] == 12:
                    if emy_count[i] < diff:
                        if tmr%45 == 0:
                            set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 2.5, 0, 0, 2)
                            set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 3.0, 0, 0, 2)
                            emy_count[i] += 1
                            set_se(11)
                    if emy_y[i] >= emy_decay[i]:
                        if emy_a[i] >= 0:
                            emy_a[i] -= (abs(emy_y[i]-emy_decay[i]))

                    if emy_shield[i] == 0:
                        set_enemy(emy_x[i], emy_y[i], 90, ITEM, 1.5, 0, 0, random.choice([2, 3]))


                if emy_id[i] == 13:
                    if emy_count[i] < 3:
                        if tmr%45 == 0:
                            for j in range(diff):
                                set_enemy(emy_x[i], emy_y[i], jikinerai+5, TAMA, 3.0+j, 0, 0, 6)
                                set_enemy(emy_x[i], emy_y[i], jikinerai-5, TAMA, 3.0+j, 0, 0, 6)
                            set_se(11)
                            emy_count[i] += 1
                    if emy_y[i] >= emy_decay[i]:
                        emy_y[i] = emy_decay[i]

                    if emy_shield[i] == 0:
                        for j in range(random.randint(5, 8)):
                                 set_enemy(emy_x[i]+random.randint(-8, 8)*5, emy_y[i]+random.randint(-8, 8)*5, 90, ITEM, 1.5, 0, 0, random.choice([2, 3]))


                if emy_id[i] == 14:
                    if emy_count[i] < 3:
                        if tmr%45 == 0:
                            for j in range(diff):
                                set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 3.0+j, 0, 0, 6)
                                set_enemy(emy_x[i], emy_y[i], jikinerai+random.randint(-45, 45), TAMA, 3.0+j, 0, 0, 6)
                                set_enemy(emy_x[i], emy_y[i], jikinerai+random.randint(-45, 45), TAMA, 3.0+j, 0, 0, 6)
                                set_enemy(emy_x[i], emy_y[i], jikinerai+random.randint(-45, 45), TAMA, 3.0+j, 0, 0, 6)
                            set_se(11)
                            emy_count[i] += 1
                    if emy_y[i] >= emy_decay[i]:
                        if emy_a[i] <= 180:
                            emy_a[i] += (abs(emy_y[i]-emy_decay[i]))

                    if emy_shield[i] == 0:
                        for j in range(random.randint(5, 8)):
                                 set_enemy(emy_x[i]+random.randint(-8, 8)*5, emy_y[i]+random.randint(-8, 8)*5, 90, ITEM, 1.5, 0, 0, random.choice([2, 3]))


                if emy_id[i] == 15:
                    if emy_count[i] < diff:
                        if tmr%45 == 0:
                            for j in range(diff):
                                set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 3.0+j, 0, 0, 6)
                                set_enemy(emy_x[i], emy_y[i], jikinerai+random.randint(-45, 45), TAMA, 3.0+j, 0, 0, 6)
                                set_enemy(emy_x[i], emy_y[i], jikinerai+random.randint(-45, 45), TAMA, 3.0+j, 0, 0, 6)
                                set_enemy(emy_x[i], emy_y[i], jikinerai+random.randint(-45, 45), TAMA, 3.0+j, 0, 0, 6)
                            emy_count[i] += 1
                            set_se(11)
                    if emy_y[i] >= emy_decay[i]:
                        if emy_a[i] >= 0:
                            emy_a[i] -= (abs(emy_y[i]-emy_decay[i]))

                    if emy_shield[i] == 0:
                        for j in range(random.randint(8, 13)):
                                 set_enemy(emy_x[i]+random.randint(-8, 8)*5, emy_y[i]+random.randint(-8, 8)*5, 90, ITEM, 1.5, 0, 0, random.choice([2, 3]))

            if emy_type[i] == BOSS:
                ang = 0
                for n in range(MISSILE_MAX):
                    w = img_boss[png].get_width()
                    h = img_boss[png].get_height()
                    r = int((w+h)/4)+12
                    er = int((w+h)/4)
                    if msl_f[n] == True and get_dis(emy_x[i], emy_y[i], msl_x[n], msl_y[n]) < r*r:
                            msl_f[n] = False
                            set_effect(emy_x[i]+random.randint(-er, er), emy_y[i]+random.randint(-er, er))
                            if emy_count[i]%1 == 0:
                                if msl_type[i] == 1:
                                    emy_shield[i] = emy_shield[i] - 1
                                if msl_type[i] == 10:
                                    emy_shield[i] = emy_shield[i] - 10
                                score = score + 100
                                if score > hisco:
                                    hisco = score
                                    new_record = True
                if emy_shield[i] <= 0:
                    emy_shield[i] = 0
                    emy_f[i] = False
                    set_se(15)
                        
           
            if emy_type[i] == BOSS:
                geji = emy_shield[i]

                if emy_id[i] == 0:#アルファ設定
                    if emy_count[i] == 0:
                        for j in range(ENEMY_MAX):
                            if emy_f[j] == True and emy_type[j] == TAMA:
                                set_effect(emy_x[j]+random.randint(-er, er), emy_y[j]+random.randint(-er, er))
                                emy_f[j] = False
                                score = score + 100
                        if emy_y[i] < emy_decay[i]:
                            emy_y[i] += emy_speed[i]
                        else:
                            emy_count[i] = stage_idx
                            if emy_count[i] == 2:
                                set_se(14)
                    elif emy_count[i] == 1:#中ボス
                        if tmr%60 == 0:
                            for j in range(0, 180, (20-diff+6)):
                                if diff == 1:
                                    set_enemy(emy_x[i], emy_y[i], j, TAMA, 3.0, 0, 0, 4)
                                    set_se(11)
                                else:
                                    for k in range(5):
                                        set_enemy(emy_x[i], emy_y[i], j, TAMA, k, 0, 0, 4)
                                    set_se(11)
                        if tmr%120 == 0:
                            for j in range(diff):
                                set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 2.0+j, 0, 0, 6)
                                set_se(11)

                        if diff == 10:
                            if tmr%90 == 0:
                                set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 5, 0, 0, 4)
                                set_se(11)

                        if emy_shield[i] == 0:
                            for j in range(ENEMY_MAX):
                                if emy_f[j] == True and emy_type[j] == TAMA:
                                    set_effect(emy_x[j]+random.randint(-er, er), emy_y[j]+random.randint(-er, er))
                                    emy_f[j] = False
                                    score = score + 100
                            set_se(14)
                            set_enemy(emy_x[i], emy_y[i], 90, ITEM, 1.0, 0, 0, 1)
                            for j in range(random.randint(10, 15)):
                                set_enemy(emy_x[i]+random.randint(-8, 8)*5, emy_y[i]+random.randint(-8, 8)*5, 90, ITEM, 1.5, 0, 0, random.choice([2, 3]))
                            stage_idx += 1
                            tmr = 0

                    elif emy_count[i] == 2:
                        if tmr%60 == 0:
                            for j in range(0, 180, (20-diff+6)):
                                if diff == 1:
                                    set_enemy(emy_x[i], emy_y[i], j, TAMA, 5.0, 0, 0, 4)

                                else:
                                    for k in range(5):
                                        set_enemy(emy_x[i], emy_y[i], j, TAMA, k+1, 0, 0, 4)
                            set_se(11)
                        if tmr%120 == 0:
                            for j in range(diff):
                                set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 5.0+j, 0, 0, 6)

                            set_se(11)

                        if diff == 10:
                            if tmr%90 == 0:
                                set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 5, 0, 0, 4)
                                set_se(11)
                        if emy_shield[i] <= 2000*0.9:
                            emy_count[i] += 0.5

                    elif emy_count[i] == 2.5:
                        for j in range(ENEMY_MAX):
                            if emy_f[j] == True and emy_type[j] == TAMA:
                                set_effect(emy_x[j]+random.randint(-er, er), emy_y[j]+random.randint(-er, er))
                                emy_f[j] = False
                                score = score + 100
                        emy_count[i] += 0.5
                        set_se(14)

                    elif emy_count[i] == 3:#スペカ「雀の涙」
                         if tmr%(16-diff) == 0:
                                set_enemy(emy_x[i]+100, emy_y[i], jikinerai, TAMA, diff+3, 0, 0, 1)
                                set_enemy(emy_x[i]-100, emy_y[i], jikinerai, TAMA, diff+3, 0, 0, 1)
                                set_enemy(emy_x[i]+100, emy_y[i], jikinerai+10, TAMA, diff+3, 0, 0, 6)
                                set_enemy(emy_x[i]-100, emy_y[i], jikinerai-10, TAMA, diff+3, 0, 0, 6)
                                set_se(11)
                         if tmr%30 == 0:
                            for j in range(diff):
                                set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 5.0+j, 0, 0, 6)
                            set_se(11)
                         if emy_shield[i] <= 2000*0.6:
                            for j in range(random.randint(10, 15)):
                                set_enemy(emy_x[i]+random.randint(-8, 8)*5, emy_y[i]+random.randint(-8, 8)*5, 90, ITEM, 1.5, 0, 0, random.choice([2, 3]))
                            emy_count[i] += 0.5

                    elif emy_count[i] == 3.5:
                        for j in range(ENEMY_MAX):
                            if emy_f[j] == True and emy_type[j] == TAMA:
                                set_effect(emy_x[j]+random.randint(-er, er), emy_y[j]+random.randint(-er, er))
                                emy_f[j] = False
                                score = score + 100
                        emy_count[i] += 0.5
                        set_se(13)

                    elif emy_count[i] == 4:
                        if tmr%60 == 0:
                            for j in range(0, 180, (20-diff+6)):
                                if diff == 1:
                                    set_enemy(emy_x[i], emy_y[i], j, TAMA, 5.0, 0, 0, 4)
                                else:
                                    for k in range(5):
                                        set_enemy(emy_x[i], emy_y[i], j, TAMA, k+3, 0, 0, 4)
                            set_se(11)
                        if tmr%30 == 0:
                            for j in range(diff):
                                set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 5.0+j, 0, 0, 6)
                                set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 5.0+j, 0, 0, 6)
                            set_se(11)
                        if diff == 10:
                            if tmr%90 == 0:
                                set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 5, 0, 0, 4)
                                set_se(16)
                        if emy_shield[i] <= 2000*0.4:
                            emy_count[i] += 0.5

                    elif emy_count[i] == 4.5:
                        for j in range(ENEMY_MAX):
                            if emy_f[j] == True and emy_type[j] == TAMA:
                                set_effect(emy_x[j]+random.randint(-er, er), emy_y[j]+random.randint(-er, er))
                                emy_f[j] = False
                                score = score + 100
                        emy_count[i] += 0.5
                        set_se(14)

                    elif emy_count[i] == 5.0:#スペカ「卵割「野崎の夢」」
                        BOMB = 0
                        set_enemy(emy_x[i], emy_y[i], 270, TAMA, 6, 0, 0, 15)
                        emy_count[i] += 1
                        set_se(11)
                    elif emy_count[i] == 6:
                        if tmr%180 == 0:
                                set_enemy(emy_x[i], emy_y[i], jikinerai-5, TAMA, 5.0, 0, 0, 6)
                                set_enemy(emy_x[i], emy_y[i], jikinerai+5, TAMA, 5.0, 0, 0, 6)
                                set_se(11)
                        if BOMB != 0:
                            if tmr%120 == 0:
                                set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 5, 0, 0, 4)
                                set_enemy(emy_x[i], emy_y[i], 60, TAMA, 6, 0, 0, 15)
                                set_se(11)
                        if diff == 10:
                            if tmr%90 == 0:
                                set_enemy(emy_x[i], emy_y[i], jikinerai, TAMA, 5, 0, 0, 4)
                                set_enemy(emy_x[i], emy_y[i], 60+j*32, TAMA, 6, 0, 0, 15)
                                set_se(11)
                        if emy_shield[i] <= 0:
                            for j in range(ENEMY_MAX):
                                if emy_f[j] == True and emy_type[j] == TAMA:
                                    set_effect(emy_x[j]+random.randint(-er, er), emy_y[j]+random.randint(-er, er))
                                    emy_f[j] = False
                                    score = score + 100
                            
                            for j in range(random.randint(10, 15)):
                                set_enemy(emy_x[i]+random.randint(-8, 8)*5, emy_y[i]+random.randint(-8, 8)*5, jikinerai, ITEM, 30, 0, 0, random.choice([2, 3]))

                            stage_idx += 1
                            tmr = 0

            if emy_type[i] == ITEM:
                if stage_idx == 3:
                    emy_a[i] = jikinerai
                    emy_speed[i] = 30
                if bomb_tmr >= 60:
                    emy_a[i] = jikinerai
                    emy_speed[i] = 20
                if ss_y <= 160:
                    emy_a[i] = jikinerai
                    emy_speed[i] = 20

                png = emy_id[i]
                ang = 0
                emy_x[i] = emy_x[i] + emy_speed[i]*math.cos(math.radians(emy_a[i]))
                emy_y[i] = emy_y[i] + emy_speed[i]*math.sin(math.radians(emy_a[i]))
                if emy_id[i] == 0: #エクステンドヒットチェック
                    w = img_icon[0].get_width()
                    h = img_icon[0].get_height()
                    r = int((w+h)/4)+12
                    er = int((w+h)/4)
                    for n in range(ENEMY_MAX):
                        if get_dis(emy_x[i], emy_y[i], ss_x, ss_y) < r*r+1600:
                            emy_a[i] = jikinerai
                            emy_speed[i] = 3
                        if emy_f[n] == True and get_dis(emy_x[i], emy_y[i], ss_x, ss_y) < r*r:
                            emy_f[i] = False
                            ss_shield = ss_shield + 1
                            set_se(8)
                            return
                              
                if emy_id[i] == 1: #ボムヒットチェック
                    w = img_icon[0].get_width()
                    h = img_icon[0].get_height()
                    r = int((w+h)/4)+12
                    er = int((w+h)/4)
                    for n in range(ENEMY_MAX):
                        if get_dis(emy_x[i], emy_y[i], ss_x, ss_y) < r*r+1600:
                            emy_a[i] = jikinerai
                            emy_speed[i] = 3
                        if emy_f[n] == True and get_dis(emy_x[i], emy_y[i], ss_x, ss_y) < r*r:
                            emy_f[i] = False
                            BOMB = BOMB + 1
                            set_se(9)
                            return

                if emy_id[i] == 2: #POWERヒットチェック
                    w = img_icon[0].get_width()
                    h = img_icon[0].get_height()
                    r = int((w+h)/4)+12
                    er = int((w+h)/4)
                    for n in range(ENEMY_MAX):
                        if get_dis(emy_x[i], emy_y[i], ss_x, ss_y) < r*r+1600:
                            emy_a[i] = jikinerai
                            emy_speed[i] = 3
                        if emy_f[n] == True and get_dis(emy_x[i], emy_y[i], ss_x, ss_y) < r*r:
                            emy_f[i] = False
                            POWER = POWER + 1
                            set_se(17)
                            return

                if emy_id[i] == 3: #点数ヒットチェック
                    w = img_icon[0].get_width()
                    h = img_icon[0].get_height()
                    r = int((w+h)/4)+12
                    er = int((w+h)/4)
                    for n in range(ENEMY_MAX):
                        if get_dis(emy_x[i], emy_y[i], ss_x, ss_y) < r*r+1600:
                            emy_a[i] = jikinerai
                            emy_speed[i] = 3
                        if emy_f[n] == True and get_dis(emy_x[i], emy_y[i], ss_x, ss_y) < r*r:
                            emy_f[i] = False
                            score = score + 50
                            ten_max = ten_max + 50
                            set_se(17)
                            return


            if emy_type[i] == TAMA:
                png = emy_id[i]
                ang = -emy_a[i]+90           
                emy_x[i] = emy_x[i] + emy_speed[i]*math.cos(math.radians(emy_a[i]))
                emy_y[i] = emy_y[i] + emy_speed[i]*math.sin(math.radians(emy_a[i]))
                w = img_tama[png].get_width()
                h = img_tama[png].get_height()
                r = int((w+h)/4)+12
                er = int((w+h)/4)
                for n in range(MISSILE_MAX):
                    if msl_f[n] == True and msl_type[n] == 2 and get_dis(emy_x[i], emy_y[i], msl_x[n], msl_y[n]) < 180*180:
                        set_effect(emy_x[i]+random.randint(-er, er), emy_y[i]+random.randint(-er, er))
                        emy_f[i] = False
                        score = score + 100

            if emy_type[i] == TAMA:
                if emy_id[i] == 15:#壁に当たると分裂し続ける丸小弾
                    if emy_x[i] <= 50 and emy_count[i] <= 2:
                        emy_x[i] = 52
                        emy_a[i] = jikinerai
                        emy_speed[i] = emy_speed[i] + 1
                        set_enemy(emy_x[i], emy_y[i], jikinerai+random.choice([-90, -80, -70, -60, -50, -40, -30, -20, -10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]), TAMA, emy_speed[i], 0, 0, 15)
                        emy_count[i] += 1
                        set_se(16)
                        return

                    if emy_x[i] >= 620 and emy_count[i] <= 2:
                        emy_x[i] = 618
                        emy_a[i] = jikinerai
                        emy_speed[i] = emy_speed[i] + 1
                        set_enemy(emy_x[i], emy_y[i], jikinerai+random.choice([-90, -80, -70, -60, -50, -40, -30, -20, -10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]), TAMA, emy_speed[i], 0, 0, 15)
                        emy_count[i] += 1
                        set_se(16)
                        return

                    if emy_y[i] <= 24 and emy_count[i] <= 2:
                        emy_y[i] = 26
                        emy_a[i] = jikinerai
                        emy_speed[i] = emy_speed[i] + 2
                        set_enemy(emy_x[i], emy_y[i], jikinerai+random.choice([-90, -80, -70, -60, -50, -40, -30, -20, -10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]), TAMA, emy_speed[i], 0, 0, 15)
                        emy_count[i] += 1
                        set_se(16)
                        return

                    if emy_y[i] >= 670 and emy_count[i] <= 2:
                        emy_y[i] = 668
                        emy_a[i] = jikinerai
                        emy_speed[i] = emy_speed[i] - 0.5
                        set_enemy(emy_x[i], emy_y[i], jikinerai+random.choice([-90, -80, -70, -60, -50, -40, -30, -20, -10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95]), TAMA, emy_speed[i], 0, 0, 15)
                        emy_count[i] += 1
                        set_se(16)
                        return

            if emy_x[i] < LINE_L or emy_x[i] > LINE_R or LINE_B < emy_y[i] or LINE_T > emy_y[i]:#敵が画面外に出たら消す
                emy_f[i] = False


            if emy_type[i] == ZAKO:
                img_rz = pygame.transform.rotozoom(img_enemy[png], ang, 1.5) #敵機を回転させた画像を作る(transformで変形)

            if emy_type[i] == BOSS:
                img_rz = pygame.transform.rotozoom(img_boss[png], ang, 1.5) #敵機を回転させた画像を作る(transformで変形)

            if emy_type[i] == ITEM:
                img_rz = pygame.transform.rotozoom(img_item[png], ang, 1.5) #敵機を回転させた画像を作る(transformで変形)

            if emy_type[i] == TAMA:
                img_rz = pygame.transform.rotozoom(img_tama[png], ang, 1.5) #敵機を回転させた画像を作る(transformで変形)

            scrn.blit(img_rz, [emy_x[i]-img_rz.get_width()/2, emy_y[i]-img_rz.get_height()/2])#上で作った画像を敵の座標に表示する 
            #敵の設定

def pickle_load(path):
    with open(path, mode='rb') as f:
        data = pickle.load(f)
        return data

def draw_text(scrn, txt, x, y, siz, col): #文字を表示する関数
    fnt = pygame.font.SysFont("arialblack", siz)
    cr = int(col[0]/2)
    cg = int(col[0]/2)
    cb = int(col[0]/2)
    sur = fnt.render(txt, True, (cr, cg, cb))
    x = x - sur.get_width()/2
    y = y - sur.get_height()/2
    scrn.blit(sur, [x+1, y+1])
    cr = col[0]+128
    if cr > 255: cr = 255
    cg = col[1]+128
    if cg > 255: cg = 255
    cb= col[1]+128
    if cb > 255: cb = 255
    sur = fnt.render(txt, True, (cr, cg, cb))
    scrn.blit(sur, [x-1,y-1])
    sur = fnt.render(txt, True, col)
    scrn.blit(sur, [x,y])#文字を表示する関数

def set_effect(x, y):
    global eff_no
    eff_p[eff_no] = 1
    eff_x[eff_no] = x
    eff_y[eff_no] = y
    eff_no = (eff_no+1)%EFFECT_MAX

def set_graze(x, y):
    global eff_nog
    eff_pg[eff_nog] = 1
    eff_xg[eff_nog] = x
    eff_yg[eff_nog] = y
    eff_nog = (eff_nog+1)%EFFECT_MAX

def draw_effect(scrn):
    for i in range(EFFECT_MAX):
        if eff_p[i] > 0:
            scrn.blit(img_explode[eff_p[i]], [eff_x[i]-48, eff_y[i]-48])
            eff_p[i] = eff_p[i] + 1
            if eff_p[i] == 6:
                eff_p[i] = 0

def draw_graze(scrn):
    for i in range(EFFECT_MAX):
        if eff_pg[i] > 0:
            scrn.blit(img_graze[eff_pg[i]], [eff_xg[i]-48, eff_yg[i]-48])
            eff_pg[i] = eff_pg[i] + 1
            if eff_pg[i] == 15:
                eff_pg[i] = 0

def set_icon(scrn):
    for i in range(ss_shield-1):
        scrn.blit(img_icon[0], [735+i*30, 140])#残機

    for j in range(BOMB):
        scrn.blit(img_icon[1], [735+j*30, 200])#ボム


def set_kaiwa(scrn):
    global counter, stage_idx, idx, tmr, stage_count
    if tmr%180 == 75:
        counter = counter + 1
        set_se(5)
    if counter == 1:
        pygame.mixer.fadeout(3000)
    if counter <= 6:
        
        scrn.blit(img_kaiwa[counter*stage_count], [0, 0])

    if counter == 7 :
        
        idx = 8
        stage_idx = 2
        tmr = 0
        
def set_bgm(number):
    pygame.mixer.stop()
    #pygame.mixer.set_reserved(2)
    channelbgm =  pygame.mixer.Channel(20)
    channelbgm.set_volume(1)

    bgm =  pygame.mixer.Sound(bgm_list[number])
    channelbgm.play(bgm, -1)

def set_se(number):
        #pygame.mixer.set_reserved(2)
        channel =  pygame.mixer.Channel(number)

        se =  pygame.mixer.Sound(se_list[number])
        channel.play(se, 0)

   


def main():
    global idx, bg_y, tmr, score, ss_x, ss_y, ss_d, ss_shield, ss_muteki, new_record, choose_kabuse, tamadashi, stage_idx, hisco, BOMB, POWER, graze, title_idx, title_idx2, diff, stage_count, jiki_id, ten_max, geji


    pygame.init()
    pygame.display.set_caption("Nozaki_Ryo")
    pygame.display.set_icon(img_icon[2])
    screen = pygame.display.set_mode((960, 720))
    pygame.mixer.set_num_channels(25)
    

 

    scores = {} # scores is an empty dict already

    if os.path.getsize('records/scores.pkl') > 0:      
        with open('records/scores.pkl', "rb") as f:
            scores = pickle.Unpickler(f)
        # if file is not empty scores will be equal
        # to the value unpickled
            scores = scores.load()


    clock = pygame.time.Clock()

    #idx==0
    zoom_start = 1.0
    zoom_music = 1.0
    zoom_practice = 1.0
    zoom_record = 1.0
    zoom_manual = 1.0
    zoom_setting = 1.0
    zoom_quit = 1.0

    #idx==1
    diff = 1
    easy_x = 0
    normal_x = 0
    hard_x = 0


    #idx=4
    text_scores = {}

    tmr_keep = 0
    continue_nokori = 3
    warning_count = 0

    while True:
        if score > hisco:
                            hisco = score
                            new_record = True
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and idx == 8:
                    
                    idx = 9
                    tmr = 0
                    title_idx = 1
                


        
#背景のスクロール

        bg_y = (bg_y+8)%960
        screen.blit(bg[0], [0, bg_y-960])
        screen.blit(bg[0], [0, bg_y])
        
        key = pygame.key.get_pressed()

        if idx == 0:#タイトル
            if title_idx == 0:
               zoom_start = 1.0
               zoom_music = 1.0
               zoom_practice = 1.0
               zoom_record = 1.0
               zoom_manual = 1.0
               zoom_setting = 1.0
               zoom_quit = 1.0

            if title_idx == 1:
               zoom_start = 1.1
               zoom_music = 1.0
               zoom_practice = 1.0
               zoom_record = 1.0
               zoom_manual = 1.0
               zoom_setting = 1.0
               zoom_quit = 1.0

            if title_idx == 2:
               zoom_start = 1.0
               zoom_music = 1.1
               zoom_practice = 1.0
               zoom_record = 1.0
               zoom_manual = 1.0
               zoom_setting = 1.0
               zoom_quit = 1.0

            if title_idx == 3:
               zoom_start = 1.0
               zoom_music = 1.0
               zoom_practice = 1.1
               zoom_record = 1.0
               zoom_manual = 1.0
               zoom_setting = 1.0
               zoom_quit = 1.0

            if title_idx == 4:
               zoom_start = 1.0
               zoom_music = 1.0
               zoom_practice = 1.0
               zoom_record = 1.1
               zoom_manual = 1.0
               zoom_setting = 1.0
               zoom_quit = 1.0

            if title_idx == 5:
               zoom_start = 1.0
               zoom_music = 1.0
               zoom_practice = 1.0
               zoom_record = 1.0
               zoom_manual = 1.1
               zoom_setting = 1.0
               zoom_quit = 1.0

            if title_idx == 6:
               zoom_start = 1.0
               zoom_music = 1.0
               zoom_practice = 1.0
               zoom_record = 1.0
               zoom_manual = 1.0
               zoom_setting = 1.1
               zoom_quit = 1.0

            if title_idx == 7:
               zoom_start = 1.0
               zoom_music = 1.0
               zoom_practice = 1.0
               zoom_record = 1.0
               zoom_manual = 1.0
               zoom_setting = 1.0
               zoom_quit = 1.1
            

            
            if key[K_UP] == 1 and idx == 0:
                    if title_idx > 1 and title_idx <8:
                        time.sleep(0.015)
                        set_se(1)
                        title_idx = title_idx - 1                        
            if key[K_DOWN] == 1 and idx == 0:
                    if title_idx >= 0 and title_idx <7:
                        time.sleep(0.015)
                        set_se(1)
                        title_idx = title_idx + 1

                

            screen.blit(img_title[0], [0, 0])

            if tmr >= 7 and tmr < 9:
                screen.blit(img_title[10], [0, 0])
            if tmr >= 9 and tmr < 11:
                screen.blit(img_title[11], [0, 0])
            if tmr >= 11:
                screen.blit(img_title[12], [0, 0])

            
            img_rz_start = pygame.transform.rotozoom(img_title[2], 0, 1.0)
            img_rz_music = pygame.transform.rotozoom(img_title[3], 0, 1.0)
            img_rz_practice = pygame.transform.rotozoom(img_title[4], 0, 1.0)
            img_rz_record = pygame.transform.rotozoom(img_title[5], 0, 1.0)
            img_rz_manual = pygame.transform.rotozoom(img_title[6], 0, 1.0)
            img_rz_setting = pygame.transform.rotozoom(img_title[7], 0, 1.0)
            img_rz_quit = pygame.transform.rotozoom(img_title[8], 0, 1.0)
            screen.blit(img_rz_start, [(1-zoom_start)*200, 0])
            screen.blit(img_rz_music, [(1-zoom_music)*200, 0])
            screen.blit(img_rz_practice, [(1-zoom_practice)*200, 0])
            screen.blit(img_rz_record, [(1-zoom_record)*200, 0])
            screen.blit(img_rz_manual, [(1-zoom_manual)*200, 0])
            screen.blit(img_rz_setting, [(1-zoom_setting)*200, 0])
            screen.blit(img_rz_quit, [(1-zoom_quit)*200, 0])


            if key[K_z] == 1 and title_idx == 1:
                time.sleep(0.3)
                set_se(2)
                idx = 1
                title_idx = 0
                

            if key[K_z] == 1 and title_idx == 3:
                time.sleep(0.3)
                set_se(2)
                idx = 3
                title_idx = 0
                title_idx = 0
                

            if key[K_z] == 1 and title_idx == 4:
                time.sleep(0.3)
                set_se(2)
                idx = 4
                title_idx = 0
                

            if key[K_z] == 1 and title_idx == 5:
                time.sleep(0.3)
                set_se(2)
                idx = 5
                title_idx = 0
                

            if key[K_z] == 1 and title_idx == 7:
                set_se(2)
                time.sleep(0.5)
                pygame.quit()
                sys.exit()

            if key[K_x] == 1:
                set_se(3)
                title_idx = 7
                time.sleep(0.1)

           
                
        if idx == 0.5:#読み込み画面
            if tmr <= 330:
                screen.blit(img_title[9], [0, 0])
            if tmr > 330:
                screen.blit(img_title[9], [0, 0])
            screen.blit(img_load[(int(tmr/30))%4], [80, 25])
            if tmr == 180:
                idx = 0
                stage_count = 1
                stage_idx = 1
                title_idx = 0
                title_idx2 = 0
                zoom_start = 1.0
                zoom_music = 1.0
                zoom_practice = 1.0
                zoom_record = 1.0
                zoom_manual = 1.0
                zoom_setting = 1.0
                zoom_quit = 1.0
                tamadashi = False
                #idx==1
                diff = 1
                easy_x = 0
                normal_x = 0
                hard_x = 0

               
                
                time.sleep(0.3)
                set_bgm(0)
                tmr = 0

            if tmr == 330:#1面から
                tmr = 0
                
                stage_idx = 1
                stage_count = 1
                title_idx = 1
                
                score = 0
                ten_max = 0
                new_record = False
                ss_x = 334
                ss_y = 600
                ss_d = 0
                ss_shield = 5
                BOMB = 3
                POWER = 0
                graze = 0
                ss_muteki = 0
                tamadashi = True
                
                for i in range(ENEMY_MAX):
                    emy_f[i] = False
                for i in range(MISSILE_MAX):
                    msl_f[i] = False
                idx = 8
                time.sleep(0.2)
                set_bgm(1)

            if tmr == 480:#2面から
                tmr = 0
                
                stage_idx = 1
                stage_count = 2
                title_idx = 1
                
                score = 0
                ten_max = 0
                new_record = False
                ss_x = 334
                ss_y = 600
                ss_d = 0
                ss_shield = 5
                BOMB = 3
                POWER = 0
                graze = 0
                ss_muteki = 0
                tamadashi = True
                
                for i in range(ENEMY_MAX):
                    emy_f[i] = False
                for i in range(MISSILE_MAX):
                    msl_f[i] = False
                idx = 8
                time.sleep(0.2)
                set_bgm(3)

            if tmr == 630:#3面から
                tmr = 0
                
                stage_idx = 1
                stage_count = 3
                title_idx = 1
                
                score = 0
                ten_max = 0
                new_record = False
                ss_x = 334
                ss_y = 600
                ss_d = 0
                ss_shield = 5
                BOMB = 3
                POWER = 0
                graze = 0
                ss_muteki = 0
                tamadashi = True
                
                for i in range(ENEMY_MAX):
                    emy_f[i] = False
                for i in range(MISSILE_MAX):
                    msl_f[i] = False
                idx = 8
                time.sleep(0.2)
                set_bgm(5)

            if tmr == 780:#4面から
                tmr = 0
                
                stage_idx = 1
                stage_count = 4
                title_idx = 1
                
                score = 0
                ten_max = 0
                new_record = False
                ss_x = 334
                ss_y = 600
                ss_d = 0
                ss_shield = 5
                BOMB = 3
                POWER = 0
                graze = 0
                ss_muteki = 0
                tamadashi = True
                
                for i in range(ENEMY_MAX):
                    emy_f[i] = False
                for i in range(MISSILE_MAX):
                    msl_f[i] = False
                idx = 8
                time.sleep(0.2)
                set_bgm(6)

            if tmr == 930:#5面から
                tmr = 0
                
                stage_idx = 1
                stage_count = 5
                title_idx = 1
                
                score = 0
                ten_max = 0
                new_record = False
                ss_x = 334
                ss_y = 600
                ss_d = 0
                ss_shield = 5
                BOMB = 3
                POWER = 0
                graze = 0
                ss_muteki = 0
                tamadashi = True
                
                for i in range(ENEMY_MAX):
                    emy_f[i] = False
                for i in range(MISSILE_MAX):
                    msl_f[i] = False
                idx = 8
                time.sleep(0.2)
                set_bgm(9)
        if idx == 1:#難易度選択
            screen.blit(img_title[0], [0, 0])
            screen.blit(img_diff[title_idx], [0, 0])

            if title_idx == 0:
                diff = 1
            if title_idx == 1:
                diff = 1
            if title_idx == 2:
                diff = 5
            if title_idx == 3:
                diff = 11
            

            
            if key[K_UP] == 1:
                    if title_idx > 1 and title_idx <4:
                        time.sleep(0.15)
                        set_se(1)
                        title_idx = title_idx - 1     
                        
            if key[K_DOWN] == 1:
                    if title_idx >= 0 and title_idx <3:
                        time.sleep(0.15)
                        set_se(1)
                        title_idx = title_idx + 1


            if key[K_z] == 1 and title_idx != 0:
                time.sleep(0.1)
                set_se(2)
                idx = 7
                title_idx = 0
                jiki = -1


            if key[K_x] == 1:
                    idx = 0
                    time.sleep(0.3)
                    set_se(3)
                    title_idx = 1
                    zoom_start = 1.0
                    

        #if idx == 2:#曲

        if idx == 3:#練習
            if title_idx2 == 0:
                if key[K_UP] == 1 and idx == 3:
                    if title_idx > 1 and title_idx <6:
                        title_idx = title_idx - 1
                        set_se(1)
                        time.sleep(0.15)
                if key[K_DOWN] == 1 and idx == 3:
                    if title_idx >= 0 and title_idx <5:
                        title_idx = title_idx + 1
                        set_se(1)
                        time.sleep(0.15)

                screen.blit(img_title[0], [0, 0])
                screen.blit(img_stage_select[title_idx], [0, 0])
            
                if key[K_z] == 1 and title_idx == 1:#1
                    set_se(2)
                    title_idx = 0
                    title_idx2 = 1
                    stage_count = 1
                    time.sleep(0.3)

                if key[K_z] == 1 and title_idx == 2:#2
                    set_se(2)
                    title_idx = 0
                    title_idx2 = 1
                    stage_count = 2
                    time.sleep(0.3)

                if key[K_z] == 1 and title_idx == 3:#3
                    set_se(2)
                    title_idx = 0
                    title_idx2 = 1
                    stage_count = 3
                    time.sleep(0.3)

                if key[K_z] == 1 and title_idx == 4:#4
                    set_se(2)
                    title_idx = 0
                    title_idx2 = 1
                    stage_count = 4
                    time.sleep(0.3)

                if key[K_z] == 1 and title_idx == 5:#5
                    set_se(2)
                    title_idx = 0
                    title_idx2 = 1
                    stage_count = 5
                    time.sleep(0.3)

                if key[K_x] == 1:
                    set_se(3)
                    idx = 0
                    time.sleep(0.3)
                    title_idx = 3

            if title_idx2 == 1:#難易度選択
                screen.blit(img_title[0], [0, 0])
                screen.blit(img_diff[title_idx], [0, 0])

                if title_idx == 0:
                    diff = 1
                if title_idx == 1:
                    diff = 1
                if title_idx == 2:
                    diff = 5
                if title_idx == 3:
                    diff = 11
            

            
                if key[K_UP] == 1 and idx == 3:
                    if title_idx > 1 and title_idx <4:
                        time.sleep(0.1)
                        set_se(1)
                        title_idx = title_idx - 1     
                        
                if key[K_DOWN] == 1 and idx == 3:
                    if title_idx >= 0 and title_idx <3:
                        time.sleep(0.1)
                        set_se(1)
                        title_idx = title_idx + 1


                if key[K_z] == 1 and title_idx != 0:
                    time.sleep(0.1)
                    set_se(2)
                    title_idx = 0
                    title_idx2 = 2
                    jiki = 0


                if key[K_x] == 1:
                    time.sleep(0.3)
                    set_se(3)
                    title_idx = 0
                    title_idx2 = 0


            if title_idx2 == 2:#自機選択
                screen.blit(img_title[0], [0, 0])
                screen.blit(img_jiki_sentaku[jiki+1], [0, 0])

                if title_idx == 1:
                    easy_x = -50
                    normal_x = 0
                    hard_x = 0
                    jiki = 0
                if title_idx == 2:
                    easy_x = 0
                    normal_x = -50
                    hard_x = 0
                    jiki = 1
            

            
                if key[K_UP] == 1:
                    if title_idx == 2:
                        set_se(1)
                        title_idx = 1
                        time.sleep(0.15)
                if key[K_DOWN] == 1:
                    if title_idx >= 0 :
                        set_se(1)
                        title_idx = 2
                        time.sleep(0.15)

                if key[K_z] == 1 and title_idx != 0:
                    set_se(2)
                    jiki = title_idx - 1
                    idx = 0.5
                    tmr = 270+150*(stage_count-1)
                    time.sleep(0.3)

                if key[K_x] == 1:
                    time.sleep(0.3)
                    set_se(3)
                    title_idx = 1
                    title_idx2 = 0



        if idx == 4:#記録
            screen.blit(img_title[0], [0, 0])
            with open('records/scores.pkl', 'rb') as f:
                scores = pickle.load(f)
                #pprint.pformat(scores, width=10)

            text_scores = pprint.pformat(scores, width=10)
            draw_text(screen, text_scores, 600, 260, 30, (255, 255, 255))
            if key[K_x] == 1:
                    time.sleep(0.3)
                    idx = 0
                    set_se(3)
                    title_idx = 4

        if idx == 5:#マニュアル
            screen.blit(img_title[0], [0, 0])
            screen.blit(img_manual[0], [0, 0])
            if key[K_x] == 1:
                    time.sleep(0.3)
                    idx = 0
                    set_se(3)
                    title_idx = 5

       # if idx == 6:#設定
        if idx == 7:#自機選択
            screen.blit(img_title[0], [0, 0])
            screen.blit(img_stand[0], [0, 0])
            screen.blit(img_jiki_sentaku[title_idx], [0, 0])

            if title_idx == 1:
                easy_x = -50
                normal_x = 0
                hard_x = 0
                jiki_id = 0
            if title_idx == 2:
                easy_x = 0
                normal_x = -50
                hard_x = 0
                jiki_id = 1
            

            
            if key[K_UP] == 1 and idx == 7:
                    if title_idx > 1 and title_idx <3:
                        set_se(1)
                        title_idx = title_idx - 1      
                        time.sleep(0.1)
            if key[K_DOWN] == 1 and idx == 7:
                    if title_idx >= 0 and title_idx <2:
                        set_se(1)
                        title_idx = title_idx + 1
                        time.sleep(0.1)

            if key[K_z] == 1 and title_idx != 0:
                set_se(2)
                jiki = title_idx-1
                idx = 0.5
                tmr = 240
                time.sleep(0.3)

            if key[K_x] == 1:
                time.sleep(0.3)
                set_se(3)
                idx = 1
                title_idx = 1
                diff = 1
                easy_x = 0
                normal_x = 0
                hard_x = 0
                

        if idx == 8:#ゲームプレイ中
            if stage_idx%1 == 0:
                
                tmr_keep = tmr
                move_starship(screen, key, jiki_id)
                move_missile(screen)
                bring_enemy()
                move_enemy(screen)
                screen.blit(bg_over[choose_kabuse], [0, 0])

                if diff == 1:#easy
                    screen.blit(img_diff[4], [0, 0])
                if diff == 5:#normal
                    screen.blit(img_diff[5], [0, 0])
                if diff == 11:#hard
                    screen.blit(img_diff[6], [0, 0])
                
                draw_text(screen, str(hisco), 800, 75, 20, (255, 255, 255))
                draw_text(screen, str(score), 800, 110, 20, (255, 255, 255))
                set_icon(screen)
                draw_text(screen, str(POWER), 820, 285, 20, (255, 255, 255))
                draw_text(screen, str(ten_max), 820, 317, 20, (255, 255, 255))
                draw_text(screen, str(graze), 820, 348, 20, (255, 255, 255))

                if tmr > 600 and tmr < 780 and stage_idx == 1:
                    screen.blit(img_logo[stage_count-1], [0, 0])
            else:#ゲームプレイ中(BOSS 会話)
                tmr_keep = tmr
                screen.blit(bg_over[choose_kabuse], [0, 0])
                if diff == 1:#easy
                    screen.blit(img_diff[4], [0, 0])
                if diff == 5:#normal
                    screen.blit(img_diff[5], [0, 0])
                if diff == 11:#hard
                    screen.blit(img_diff[6], [0, 0])
                
                draw_text(screen, str(hisco), 800, 75, 20, (255, 255, 255))
                draw_text(screen, str(score), 800, 100, 20, (255, 255, 255))
                draw_text(screen, str(POWER), 820, 285, 20, (255, 255, 255))
                draw_text(screen, str(ten_max), 820, 315, 20, (255, 255, 255))
                draw_text(screen, str(graze), 820, 345, 20, (255, 255, 255))
                set_icon(screen)
                set_kaiwa(screen)

        if idx == 9:#ポーズ
            if key[K_UP] == 1 and title_idx % 1 == 0:
                    if title_idx > 1 and title_idx <5:
                        time.sleep(0.1)
                        set_se(1)
                        title_idx = title_idx - 1     
                        
            if key[K_DOWN] == 1 and title_idx % 1 == 0:
                    if title_idx >= 0 and title_idx <4:
                        time.sleep(0.1)
                        set_se(1)
                        title_idx = title_idx + 1

            screen.blit(bg_over[choose_kabuse], [0, 0])
            if diff == 1:#easy
                screen.blit(img_diff[4], [0, 0])
            if diff == 5:#normal
                screen.blit(img_diff[5], [0, 0])
            if diff == 11:#hard
                screen.blit(img_diff[6], [0, 0])
                
            draw_text(screen, str(hisco), 800, 75, 20, (255, 255, 255))
            draw_text(screen, str(score), 800, 100, 20, (255, 255, 255))
            set_icon(screen)
            draw_text(screen, str(POWER), 820, 285, 20, (255, 255, 255))
            draw_text(screen, str(ten_max), 820, 317, 20, (255, 255, 255))
            draw_text(screen, str(graze), 820, 348, 20, (255, 255, 255))
            screen.blit(bg[1], [0, 0])
            img_bar = pygame.transform.rotozoom(img_pause[1], math.sin(math.radians((tmr/8)%360)*60), 1.0)

            if title_idx % 1 == 0 and title_idx < 5: 
                img_p = pygame.transform.rotozoom(img_pause[title_idx+2], 0, 1.0)
                screen.blit(img_bar, [0, 320])
                screen.blit(img_pause[0], [0, 0])
                screen.blit(img_p, [0, 0])

            if title_idx == 13.5:
                screen.blit(img_manual[0], [0, 0])
                if key[K_x] == 1:
                        time.sleep(0.3)
                        title_idx = 0

            if title_idx == 10:#はいいいえ
                screen.blit(img_bar, [200, 320]) 
                screen.blit(img_p, [0, 0])
                if key[K_UP] == 1 and title_idx2 == 2:
                    time.sleep(0.1)
                    set_se(1)
                    title_idx2 = 1
                    img_p = pygame.transform.rotozoom(img_pause[title_idx2+7], 0, 1.0)     
                    screen.blit(img_p, [0, 0])   
                    
                if key[K_DOWN] == 1 and title_idx2 == 1:
                    time.sleep(0.1)
                    set_se(1)
                    title_idx2 = 2
                    img_p = pygame.transform.rotozoom(img_pause[title_idx2+7], 0, 1.0)
                    screen.blit(img_p, [0, 0])

                if key[K_DOWN] == 1 and title_idx2 == 0:
                    time.sleep(0.1)
                    set_se(1)
                    title_idx2 = 1
                    img_p = pygame.transform.rotozoom(img_pause[title_idx2+7], 0, 1.0)
                    screen.blit(img_p, [0, 0])
                    

                if key[K_z] == 1 and title_idx2 == 1:#タイトルに戻る
                    set_se(2)
                    time.sleep(0.2)
                    title_idx = 0
                    title_idx2 = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.stop()
                    idx = 0.5
                    tmr = 150

                if key[K_z] == 1 and title_idx2 == 2:#いいえ
                    time.sleep(0.3)
                    set_se(3)
                    title_idx = 0
                    title_idx2 = 0


                if key[K_x] == 1:
                        time.sleep(0.3)
                        set_se(3)
                        title_idx = 0
                        title_idx2 = 0

                

            if tmr == 1:
                pygame.mixer.pause()
                tamadashi = False
                set_se(4)

            if key[K_z] == 1 and title_idx == 1:#一時停止を解除
                    time.sleep(0.1)
                    set_se(2)
                    title_idx = 0
                    pygame.mixer.music.stop()
                    pygame.mixer.unpause()
                    idx = 8
                    tmr = tmr_keep
                    tamadashi = True

            if key[K_z] == 1 and title_idx == 2:#タイトルに戻る
                    time.sleep(0.1)
                    set_se(2)
                    title_idx = 10
                    img_p = pygame.transform.rotozoom(img_pause[7], 0, 1.0)     
            if key[K_z] == 1 and title_idx == 3:#操作法
                    time.sleep(0.1)
                    set_se(2)
                    title_idx = 13.5

            if key[K_z] == 1 and title_idx == 4:#最初から始める
                    time.sleep(0.1)
                    title_idx = 0
                    pygame.mixer.music.stop()
                    set_se(2)
                    idx = 0.5
                    tmr = 300+150*(stage_count-1)
                    tamadashi = True#ポーズ

            if key[K_x] == 1:
                    time.sleep(0.1)
                    set_se(3)
                    title_idx = 1
                    


        if idx == 10:#ゲームオーバー
            move_missile(screen)
            move_enemy(screen)
            screen.blit(bg_over[choose_kabuse], [0, 0])
            draw_text(screen, str(score), 750, 190, 30, (255, 255, 255))
            draw_text(screen, str(hisco), 750, 100, 30, (255, 255, 255))
            if tmr == 1:
                pygame.mixer.pause()
                tamadashi = False
            if tmr == 1:
                for i in range(ENEMY_MAX):
                    if emy_type[i] != 13:
                        emy_f[i] = False
            if tmr <=90:
                if tmr%5 == 0:
                    set_effect(ss_x+random.randint(-60, 60), ss_y+random.randint(-60, 60))
                #if tmr%10 == 0:
           # if tmr == 120:
            if tmr > 120:
                draw_text(screen, "GAME OVER", 334, 300, 50, RED)
                if new_record == True:
                    draw_text(screen, "NEW RECORD "+str(hisco), 334, 400, 30, CYAN)

            if tmr >= 300:
                draw_text(screen, "Press Z key to return to Title.", 334, 430, 30, SILVER)
                if continue_nokori != 0:
                    draw_text(screen, "Press C key to continue.", 334, 480, 30, SILVER)
                    draw_text(screen, "NOKORI"+str(continue_nokori)+"KAI", 334, 530, 30, SILVER)
                if key[K_z] == 1 and key[K_c] != 1:
                    tmr = 0
                    stage_idx = 0
                    title_idx == 0
                    pygame.mixer.music.stop()
                    pygame.mixer.stop()
                    time.sleep(0.3)
                    idx = 0.5

                if key[K_c] == 1 and key[K_z] != 1 and continue_nokori > 0:
                    pygame.mixer.music.stop()
                    pygame.mixer.unpause()
                    ss_shield = 3
                    idx = 8
                    tmr = tmr_keep
                    continue_nokori = continue_nokori - 1
                    tamadashi = True
                    ss_muteki = 180
                    BOMB = 3
                    ss_x = 344                     #自機のx座標
                    ss_y = 620                     #自機のy座標

        if idx == 11:#クリア
            draw_text(screen, str(score), 750, 190, 30, (255, 255, 255))
            draw_text(screen, str(hisco), 750, 100, 30, (255, 255, 255))
            if tmr == 1:
                pygame.mixer.music.stop()
                pygame.mixer.stop()
            if tmr < 30 and tmr%2 == 0:
                pygame.draw.rect(screen, (192, 0, 0), [0, 0, 960, 720])
            #if tmr == 120:
            if tmr > 120:
                draw_text(screen, "GAME CLEAR", 334, 300, 50, SILVER)
                if new_record == True:
                    draw_text(screen, "NEW RECORD "+str(hisco), 334, 400, 30, CYAN)
                elif new_record == False:
                    draw_text(screen, "SCORE"+str(score), 334, 400, 30, (255, 255, 255))
            if tmr >= 300:
                draw_text(screen, "Press Z key to return to Title.", 334, 440, 30, SILVER)
                if key[K_z] == 1:
                    idx = 12
                    title_idx = 0
                    title_idx2 = 0
                    tmr = 0
                    stage_idx = 0
                    pygame.mixer.music.stop()

        if idx == 12:#スコア記録
            if key[K_LEFT] == 1 and title_idx == 2 and key[K_RIGHT] != 1:
                title_idx = 1
                set_se(1)                 
                        
                        
            if key[K_RIGHT] == 1 and title_idx == 1 and key[K_LEFT] != 1:
                title_idx = 2
                set_se(1)
                

            if key[K_RIGHT] == 1 and title_idx == 0 and key[K_LEFT] != 1:
                title_idx = 1
                set_se(1)
                time.sleep(0.15)
                    

            screen.blit(img_title[0], [0, 0])

            if title_idx2 == 0:
                screen.blit(img_kiroku[title_idx], [0, 0])
            
            if key[K_z] == 1 and title_idx == 1:#記録する
                time.sleep(0.1)
                set_se(2)
                title_idx2 = 1

            if key[K_z] == 1 and title_idx == 2:#記録しない
                time.sleep(0.1)
                title_idx = 0
                pygame.mixer.music.stop()
                pygame.mixer.stop()
                set_se(2)
                idx = 0.5
                tmr = 150

            if title_idx2 == 1:#記録する
                host = os.environ['USERNAME']
                scores[host] = hisco

                with open('records/scores.pkl',"wb") as f:
                    pickle.dump(scores, f)
                if tmr>0 and tmr<180:
                    screen.blit(img_kiroku[3], [0, 0])

                if tmr>210:
                    screen.blit(img_kiroku[4], [0, 0])

                if tmr==270:
                    time.sleep(0.1)
                    title_idx = 0
                    title_idx2 = 0
                    idx = 0.5
                    tmr = 150



        draw_effect(screen)
        draw_graze(screen)

        #draw_text(screen, str(geji), 334, 300, 50, SILVER)
        pygame.display.update()
        clock.tick(120)#フレームレート
        

        #メインループ

if __name__ == '__main__':
    main()
