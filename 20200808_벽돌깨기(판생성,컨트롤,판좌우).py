import pygame as p

p.init()#초기화
s=(600,900)
white=(255,255,255)
sc=p.display.set_mode(s)#해상도(가로,세로)
p.display.set_caption("벽돌깨기")
x = 0
pan = p.image.load("p.png")
p_rect = pan.get_rect(left=250,top = 800)
bg = p.image.load("s.png")


playing = True
ball = p.image.load("c.png")
b_rect = ball.get_rect(left = 270 , top = 300)
b_x=10
b_y=10
block = p.image.load("b.png")
bl_list = []
for x in range(10):
    for y in range(5):
        bl_rect = block.get_rect(left = 60*x,top = 40*y)
        bl_list.append(bl_rect)
score = 0
font=p.font.SysFont("malgungothic",20)

font1=p.font.SysFont("malgungothic",50)


while playing:

    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            
        if event.type == p.KEYDOWN:
             if event.key == p.K_RIGHT:
                x = 8
             if event.key == p.K_LEFT:
                x = -8
        if event.type == p.KEYUP:
            if event.key == p.K_RIGHT:
                x = 0
            if event.key == p.K_LEFT:
                x = 0

    p_rect.left += x
    
    sc.fill(white)
    sc.blit(bg,(0,0))
    sc.blit(pan,(p_rect))
    if p_rect.left <= 0:
        p_rect.left = 0
    if p_rect.left >= 500:
        p_rect.left = 500

    sc.blit(ball,b_rect)
    b_rect.top += b_y
    if b_rect.top >= 880:
        playing = False
    if b_rect.top <= 0:
        b_y=-b_y
    b_rect.left += b_x
    if b_rect.left >=570:
       b_x=-b_x
    if b_rect.left <=0:
        b_x=-b_x

    if p_rect.colliderect(b_rect):
        b_y=-b_y


    for bl_rect in bl_list:
        sc.blit(block,bl_rect)
        
    for bl_rect in bl_list:
        if b_rect.colliderect(bl_rect):
            bl_list.remove(bl_rect)
            b_y =8
            score += 1
    text = font.render("점수{}".format(score),True,(255,255,0))
    text1 = font1.render("Clear",True,(0,255,0))
    sc.blit(text,(0,700))
    
    if len(bl_list) <=47:
        sc.blit(text1,(200,500))
        playing=False
        

        
    
    p.display.flip()
            
            
    
