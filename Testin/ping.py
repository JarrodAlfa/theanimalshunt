# Example file showing a basic pygame "game loop"
import sys, pygame, random

def ResetBall():
    global ballSpeedX, ballSpeedY
    ballSpeedX = random.choice(range(-6,6))
    ballSpeedY = random.choice(range(-6,6))
    ball.x = sWidth/2
    ball.y = random.randint(10,100)

def PointWon(winner):
    global cpuPoints, playerPoints

    if winner == "cpu":
        cpuPoints += 1
        ResetBall()
    elif winner == "player":
        playerPoints += 1
        ResetBall()

def BallPhysics():
    global ballSpeedY, ballSpeedX, playerPoints, cpuPoints

    ball.x += ballSpeedX
    ball.y += ballSpeedY
    if ball.bottom >= sHeight or ball.top <= 0:
        ballSpeedY = -ballSpeedY
    if ball.right >= sWidth:
        PointWon("cpu")
        ballSpeedX = -ballSpeedX
    if ball.left <= 0:
        PointWon("player")
        ballSpeedX = -ballSpeedX
    if ball.colliderect(player) or ball.colliderect(cpu):
        ballSpeedX = -ballSpeedX

def PlayerController():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= sHeight:
        player.bottom = sHeight
    player.y += playerSpeed

def CpuMovement():
    global cpuSpeed
    cpu.y += cpuSpeed

    if ball.centery <= cpu.centery:
        cpuSpeed = -6
    if ball.centery >= cpu.centery:
        cpuSpeed = 6
    if cpu.top <= 0:
        cpu.top = 0
    if cpu.bottom >= sHeight:
        cpu.bottom = sHeight
# pygame setup
pygame.init()

sWidth, sHeight = 1280, 800
screen = pygame.display.set_mode((sWidth, sHeight))
pygame.display.set_caption('ping')
pygame.display.toggle_fullscreen()

clock = pygame.time.Clock()

ball = pygame.FRect(0,0,30,30)
ball.center = (sWidth/2, sHeight/2)

ballSpeedX = 6
ballSpeedY = 6
playerSpeed = 0
cpuSpeed = 6

cpu = pygame.FRect(0,0,20,100)
cpu.centery = sHeight/2

playerPoints = 0
cpuPoints = 0

player = pygame.FRect(0,0,20,100)
player.midright = (sWidth, sHeight/2)

scoreFont = pygame.font.Font(None, 100)
while True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed = 6
            if event.key == pygame.K_UP:
                playerSpeed = -6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed = 0
            if event.key == pygame.K_UP:
                playerSpeed = 0
    PlayerController()
    BallPhysics()
    CpuMovement()
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    pygame.draw.aaline(screen,'white',(sWidth/2,0),(sWidth/2,sHeight), 3)

    # RENDER YOUR GAME HERE
    cpuScoreSurface = scoreFont.render(str(cpuPoints), True, "white")
    playerScoreSurface = scoreFont.render(str(playerPoints), True, "white")
    screen.blit(cpuScoreSurface, (sWidth/4,sHeight/20))
    screen.blit(playerScoreSurface, (3*sWidth/4,sHeight/20))

    pygame.draw.ellipse(screen, "white", ball)
    pygame.draw.rect(screen, "white", cpu)
    pygame.draw.rect(screen, "white", player)

    pygame.display.flip()
    clock.tick(60)