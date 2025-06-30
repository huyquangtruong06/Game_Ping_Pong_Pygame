import pygame
from define import *

class Ball:
    def __init__(self, color, x, y, ball_size) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.ball_size = ball_size
        self.speed_x = BALL_SPEED[0]
        self.speed_y = BALL_SPEED[1]

    def show_ball(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.ball_size)

    def move_ball(self, player_left, player_right):
        self.x += self.speed_x
        self.y += self.speed_y

        # Va chạm với cạnh trên/dưới
        if self.y <= self.ball_size or self.y >= WINDOW_HEIGHT - self.ball_size:
            self.speed_y = -self.speed_y

        # Tạo Rect cho bóng
        ball_rect = pygame.Rect(self.x - self.ball_size, self.y - self.ball_size,
                                self.ball_size * 2, self.ball_size * 2)

        # Tạo Rect cho người chơi
        left_rect = pygame.Rect(player_left.x, player_left.y, PLAYER_WIDTH, PLAYER_HEIGHT)
        right_rect = pygame.Rect(player_right.x, player_right.y, PLAYER_WIDTH, PLAYER_HEIGHT)

        # Kiểm tra va chạm
        if ball_rect.colliderect(left_rect) and self.speed_x < 0:
            self.speed_x = -self.speed_x
            self.x = player_left.x + PLAYER_WIDTH + self.ball_size  # Đẩy bóng ra ngoài tránh kẹt

        if ball_rect.colliderect(right_rect) and self.speed_x > 0:
            self.speed_x = -self.speed_x
            self.x = player_right.x - self.ball_size  # Đẩy bóng ra ngoài tránh kẹt

        # Va chạm lề trái/phải → trả về ai ghi điểm
        if self.x <= 0:
            return "right"  # PlayerRight'point
        if self.x >= WINDOW_WIDTH:
            return "left"   # PlayerLeft'point

        return None

