import pygame
import random
import numpy as np

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-7, 7])
        self.velocity_y = random.choice([-4, 4])

        # Initialize pygame mixer for sound
        pygame.mixer.init(frequency=44100, size=-16, channels=1)
    
    # Generate a simple beep sound
    def play_beep(self, frequency=440, duration_ms=100, volume=0.5):
        sample_rate = 44100
        n_samples = int(sample_rate * duration_ms / 1000)
        t = np.linspace(0, duration_ms/1000, n_samples, False)
        wave = np.sin(2 * np.pi * frequency * t)
        wave = np.int16(wave * 32767 * volume)
        wave_stereo = np.column_stack((wave, wave))  # duplicate for stereo
        sound = pygame.sndarray.make_sound(wave_stereo)
        sound.play()


    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Wall bounce
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1
            self.play_beep(frequency=400, duration_ms=80)  # wall bounce beep

    def check_collision(self, player, ai):
        if self.rect().colliderect(player.rect()):
            self.x = player.x + player.width
            self.velocity_x *= -1
            self.play_beep(frequency=600, duration_ms=80)  # paddle hit beep
        elif self.rect().colliderect(ai.rect()):
            self.x = ai.x - self.width
            self.velocity_x *= -1
            self.play_beep(frequency=600, duration_ms=80)  # paddle hit beep

    def reset(self):
        self.play_beep(frequency=800, duration_ms=150)  # score beep
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-4, 4])

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
