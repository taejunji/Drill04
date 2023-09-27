from pico2d import *

open_canvas()
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('walk.png')


def handle_events():
    global running, dir_x, dir_y, RL
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                RL = True
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                RL = False
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir_x = 0
dir_y = 0
RL = True

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if RL == True:
        character.clip_draw(frame * 165, 0, 165, 230, x, y)
    else:
        character.clip_composite_draw(frame * 165, 0, 165, 230, 0, 'h', x, y,165,230)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 7
    x += dir_x * 5
    y += dir_y * 5
    delay(0.05)

close_canvas()
