import pygame
import win32gui
import win32con
import cv2
import numpy as np
import os
import sys
import msvcrt 

def system_lock():
    lock_path = os.path.join(os.getenv('TEMP'), 'cat_wallpaper.lock')
    lock_file = open(lock_path, 'w')
    try:
        msvcrt.locking(lock_file.fileno(), msvcrt.LK_NBLCK, 1)
        return lock_file 
    except IOError:
        sys.exit(0)

def get_workerw():
    progman = win32gui.FindWindow("Progman", None)
    win32gui.SendMessageTimeout(progman, 0x052C, 0, 0, win32con.SMTO_NORMAL, 1000)
    workerw = [0]
    def enum_windows(hwnd, ctx):
        shell_view = win32gui.FindWindowEx(hwnd, 0, "SHELLDLL_DefView", None)
        if shell_view:
            workerw[0] = win32gui.FindWindowEx(0, hwnd, "WorkerW", None)
    win32gui.EnumWindows(enum_windows, None)
    return workerw[0]

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    pygame.init()
    
    info = pygame.display.Info()
    sw, sh = info.current_w, info.current_h
    
    screen = pygame.display.set_mode((sw, sh), pygame.NOFRAME)
    hwnd = pygame.display.get_wm_info()['window']
    
    target = get_workerw()
    if target:
        win32gui.SetParent(hwnd, target)
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        frame = cv2.resize(frame, (sw, sh))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        
        surf = pygame.surfarray.make_surface(frame)
        screen.blit(surf, (0, 0))
        pygame.display.flip()
        
        clock.tick(60)

if __name__ == "__main__":
    _lock = system_lock() 

    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        
    video_file = os.path.join(base_path, "video.mp4")
    
    if os.path.exists(video_file):
        main(video_file)
    else:
        print(f"Error: video.mp4 not found in {base_path}")