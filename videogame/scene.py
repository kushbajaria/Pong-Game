"""Scene objects for making games with PyGame."""

import random
import pygame
from videogame import rgbcolors

# If you're interested in using abstract base classes, feel free to rewrite
# these classes.
# For more information about Python Abstract Base classes, see
# https://docs.python.org/3.8/library/abc.html


class Scene:
    """Base class for making PyGame Scenes."""

    def __init__(self, screen, background_color, screen_flags=None, soundtrack="assets/sounds/gameplay.mp3"):
        """Scene initializer"""
        self._screen = screen
        if not screen_flags:
            screen_flags = pygame.SCALED
        self._background = pygame.Surface(self._screen.get_size(), flags=screen_flags)
        self._background.fill(background_color)
        self._frame_rate = 60
        self._is_valid = True
        self._soundtrack = soundtrack
        self._render_updates = None

    def draw(self):
        """Draw the scene."""
        self._screen.blit(self._background, (0, 0))

    def process_event(self, event):
        """Process a game event by the scene."""
        if event.type == pygame.QUIT:
            print("Good Bye!")
            self._is_valid = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("Bye bye!")
            self._is_valid = False

    def is_valid(self):
        """Is the scene valid? A valid scene can be used to play a scene."""
        return self._is_valid

    def render_updates(self):
        """Render all sprite updates."""

    def update_scene(self):
        """Update the scene state."""

    def start_scene(self):
        """Start the scene."""
        if self._soundtrack:
            try:
                pygame.mixer.music.load(self._soundtrack)
                pygame.mixer.music.set_volume(.5)
            except pygame.error as pygame_error:
                print("\n".join(pygame_error.args))
                raise SystemExit("broken!!") from pygame_error
            pygame.mixer.music.play(loops=-1, fade_ms=500)

    def end_scene(self):
        """End the scene."""
        if self._soundtrack and pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()

    def frame_rate(self):
        """Return the frame rate the scene desires."""
        return self._frame_rate


class PressAnyKeyToExitScene(Scene):
    """Empty scene where it will invalidate when a key is pressed."""

    def process_event(self, event):
        """Process game events."""
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            self._is_valid = False


class TitleScreen(Scene):
    """Title screen for Pong"""

    def __init__(self, screen, message, color, size, background_color=rgbcolors.white, soundtrack="assets/sounds/startup.mp3"):
        """Create title screen"""
        super().__init__(screen, background_color, soundtrack=soundtrack)
        self._message = message
        self._color = color
        self._size = size
        self._blinker_timer = 0
        self._blink_visible = True
        self._selected_option = 0
        self._game_mode = None
        self._quit_requested = False

    def draw(self):
        """Draw title scene to screen"""
        super().draw()
        try:
            title_font = pygame.font.Font("assets/fonts/pong.ttf", 80)
            info_font = pygame.font.Font("assets/fonts/pong.ttf", 20)
            player1_font = pygame.font.Font("assets/fonts/pong.ttf", 40)
            player2_font = pygame.font.Font("assets/fonts/pong.ttf", 40)
        except pygame.error:
            # Fallback to default font if custom font fails
            title_font = pygame.font.Font(None, 80)
            info_font = pygame.font.Font(None, 20)
            player1_font = pygame.font.Font(None, 40)
            player2_font = pygame.font.Font(None, 40)
            
        title_surface = title_font.render(self._message, True, self._color)
        
        # what to display and positioning
        instructions_surface = info_font.render(
            "Use Up/Down arrows to select mode. Enter to play", True, self._color
        )
        control_surface = info_font.render(
            "Player 1: W/S or Up/Down", True, self._color
        )
        control_surface2 = info_font.render(
            "Player 2: I/K", True, self._color
        )
        title_rect = title_surface.get_rect(
            center=(self._screen.get_width() // 2, self._screen.get_height() // 2 - 300)
        )
        instructions_rect = instructions_surface.get_rect(
            center=(self._screen.get_width() // 2, self._screen.get_height() // 2 + 250)
        )
        control_rect = control_surface.get_rect(
            center=(self._screen.get_width() // 2, self._screen.get_height() // 2 + 300)
        )
        control_rect2 = control_surface2.get_rect(
            center=(self._screen.get_width() // 2, self._screen.get_height() // 2 + 350)
        )
        player1_surface = player1_font.render(
            "1 Player", True, self._color
        )
        player2_surface = player2_font.render(
            "2 Player", True, self._color
        )
        player1_rect = player1_surface.get_rect(
            center=(self._screen.get_width() // 2, self._screen.get_height() // 2 - 50)
        )
        player2_rect = player2_surface.get_rect(
            center=(self._screen.get_width() // 2, self._screen.get_height() // 2)
        )
        # draw to screen
        self._screen.blit(title_surface, title_rect)
        self._screen.blit(instructions_surface, instructions_rect)
        self._screen.blit(control_surface, control_rect)
        self._screen.blit(control_surface2, control_rect2)
        self._screen.blit(player1_surface, player1_rect)
        self._screen.blit(player2_surface, player2_rect)

        # Blinking arrow
        if self._blink_visible:
            arrow_font = pygame.font.SysFont("Sans-serif", 40)
            arrow_surface = arrow_font.render(">", True, self._color)
            
            # Position arrow based on selected option
            if self._selected_option == 0:  # 1 Player
                arrow_rect = arrow_surface.get_rect(
                    midright=(player1_rect.left - 20, player1_rect.centery - 3.5)
                )
            else:  # 2 Player
                arrow_rect = arrow_surface.get_rect(
                    midright=(player2_rect.left - 20, player2_rect.centery - 3.5)
                )
            self._screen.blit(arrow_surface, arrow_rect)

    def update_scene(self):
        """Update the blinking arrow"""
        self._blinker_timer += 1
        if self._blinker_timer >= 30:
            self._blink_visible = not self._blink_visible
            self._blinker_timer = 0

    def process_event(self, event):
        """Process game events for menu navigation"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Exiting game")
                self._quit_requested = True
                self._is_valid = False
            elif event.key == pygame.K_UP:
                self._selected_option = 0  # Select "1 Player"
                print("Selected 1 Player")
            elif event.key == pygame.K_DOWN:
                self._selected_option = 1  # Select "2 Player"
                print("Selected 2 Player")
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                # Set game mode based on selection and exit title screen
                if self._selected_option == 0:
                    self._game_mode = "1_player"
                    print("Starting 1 Player game")
                else:
                    self._game_mode = "2_player"
                    print("Starting 2 Player game")
                self._is_valid = False
        elif event.type == pygame.QUIT:
            # Handle QUIT event
            print("Good Bye!")
            self._is_valid = False

    def get_selected_game_mode(self):
        """Return the selected game mode"""
        return self._game_mode

    def quit_requested(self):
        """Return whether the user requested to quit the game"""
        return self._quit_requested

class GameScreen(Scene):
    """Game scene for Pong"""

    def __init__(self, screen, background_color, size, game_mode="1_player", soundtrack="assets/sounds/gameplay.mp3"):
        """Create game scene"""
        super().__init__(screen, background_color, soundtrack=soundtrack)
        self._size = size
        self._game_mode = game_mode  # "1_player" or "2_player"
        self._ball = pygame.Rect(size[0] // 2 - 10, size[1] // 2 - 10, 20, 20)
        self._ball_velocity = [1, 1]
        self._player = pygame.Rect(30, size[1] // 2 - 35, 10, 70)
        self._ai = pygame.Rect(size[0] - 40, size[1] // 2 - 35, 10, 70)
        self._player_move_up = False
        self._player_move_down = False
        self._player_speed = 12
        self._ai_speed = 11
        self._ai_delay = 0
        self._player_score = 0
        self._ai_score = 0
        self._countdown = 3
        self._countdown_timer = pygame.time.get_ticks()
        self._countdown_sound = pygame.mixer.Sound("assets/sounds/beep.mp3")
        self._countdown_played = False
        self._serve = True
        self._paddle_sound = pygame.mixer.Sound("assets/sounds/hit.wav")
        self._score_sound = pygame.mixer.Sound("assets/sounds/score.wav")
        self._round_delay = 1000
        self._wait_after_score = False
        self._score_time = 0
        
        # Two-player mode variables
        self._player2_move_up = False
        self._player2_move_down = False
        self._player2_speed = 12

    def draw(self):
        """Draw the game scene"""
        super().draw()
        # draw paddles and ball
        pygame.draw.rect(self._screen, rgbcolors.white, self._player)
        pygame.draw.rect(self._screen, rgbcolors.white, self._ai)
        pygame.draw.ellipse(self._screen, rgbcolors.white, self._ball)
        # draw center dotted line
        for i, y in enumerate(range(0, self._size[1], 25)): # adjust vertical spacing on dotted line
            if i % 2 == 0:
                continue
            pygame.draw.line(
                self._screen,
                rgbcolors.white,
                (self._size[0] // 2, y),
                (self._size[0] // 2, y + 20),
                5, # adjust thickness of line
            )
        score_font = pygame.font.Font("assets/fonts/game.otf", 100)
        score_font2 = pygame.font.Font("assets/fonts/game.otf", 100)
        score_surface = score_font.render(
            f"{self._player_score}", True, rgbcolors.white
        )
        score_surface2 = score_font2.render(
            f"{self._ai_score}", True, rgbcolors.white
        )
        score_rect = score_surface.get_rect(left=self._size[0] // 2, centerx=187.5)
        score_rect2 = score_surface2.get_rect(left=self._size[0] // 2, centerx=562.5)
        self._screen.blit(score_surface, score_rect)
        self._screen.blit(score_surface2, score_rect2)

    def update_scene(self):
        """updates the game with ball and paddle movement + sound effects"""
        # countdown sound effect
        if self._serve:
            if not self._countdown_played:
                self._countdown_sound.play()
                self._countdown_start_time = pygame.time.get_ticks()
                self._countdown_played = True
            now = pygame.time.get_ticks()
            sound_length = int(
                self._countdown_sound.get_length() * 1000
            )  # milliseconds
            if now - self._countdown_start_time < sound_length:
                return
            else:
                self._serve = False
                # Set random velocity when serve actually begins
                self._ball_velocity = [8 * random.choice([-1, 1]), 8 * random.choice([-1, 1])]
        
        # round delay after scoring
        if self._wait_after_score:
            now = pygame.time.get_ticks()
            if now - self._score_time < self._round_delay:
                return
            else:
                self._wait_after_score = False
                self._serve = True
                self._countdown_played = False

        # collision sound effect
        if self._ball.colliderect(self._player):
            self._ball_velocity[0] *= random.choice([-1, -2, -3])
            self._paddle_sound.play()
        elif self._ball.colliderect(self._ai):
            self._ball_velocity[0] *= random.choice([-1, -2, -3])
            self._paddle_sound.play()

        self._ball.x += self._ball_velocity[0]
        self._ball.y += self._ball_velocity[1]

        # checks for scoring, resets ball and paddles if scored
        if self._ball.right < 0:
            self._ai_score += 1
            self._score_sound.play()
            self._reset_ball()
            self._reset_player()
            self._reset_ai()
        elif self._ball.left > self._size[0]:
            self._player_score += 1
            self._score_sound.play()
            self._reset_ball()
            self._reset_player()
            self._reset_ai()

        # ball collision with top and bottom walls
        if self._ball.bottom >= self._size[1] or self._ball.top <= 0:
            self._ball_velocity[1] *= -1
            self._paddle_sound.play()

        # paddle movement
        if self._player_move_up and self._player.top > 0:
            self._player.y -= self._player_speed
        if self._player_move_down and self._player.bottom < self._size[1]:
            self._player.y += self._player_speed

        # ai paddle movement (only in 1-player mode)
        if self._game_mode == "1_player":
            self._ai_delay += 1
            if self._ai_delay > 5:
                self._ai_delay = 0

            ai_random = random.randint(-40, 40)
            dead_zone = 25 # lower for more accuracy

            if (
                self._ball.centery + ai_random < self._ai.centery - dead_zone
                and self._ai.top > 0
            ):
                self._ai.y -= self._ai_speed
            elif (
                self._ball.y + ai_random > self._ai.centery + dead_zone
                and self._ai.bottom < self._size[1]
            ):
                self._ai.y += self._ai_speed
        else:  # 2-player mode
            # Player 2 paddle movement
            if self._player2_move_up and self._ai.top > 0:
                self._ai.y -= self._player2_speed
            if self._player2_move_down and self._ai.bottom < self._size[1]:
                self._ai.y += self._player2_speed

        # handle ball movement when out of bounds/scoring
        if self._ball.right < 0:
            self._ai_score += 1
            self._reset_ball()
        elif self._ball.left > self._size[0]:
            self._player_score += 1
            self._reset_ball()

        # check if game is over
        if self._player_score >= 3 or self._ai_score >= 3: # set to 1 for testing purposes
            self._is_valid = False

    def _reset_ball(self):
        """reset the ball to the center of the screen"""
        self._ball.x = self._size[0] // 2 - 10
        self._ball.y = self._size[1] // 2 - 10
        # Stop the ball during reset - velocity will be set when serve ends
        self._ball_velocity = [0, 0]
        self._wait_after_score = True
        self._score_time = pygame.time.get_ticks()
    
    def _reset_player(self):
        """reset the player paddle to the left side of the screen"""
        self._player.x = 30
        self._player.y = self._size[1] // 2 - 35  # Center paddle vertically

    def _reset_ai(self):
        """reset the ai paddle to the right side of the screen"""
        self._ai.x = self._size[0] - 40
        self._ai.y = self._size[1] // 2 - 35  # Center paddle vertically

    def process_event(self, event):
        """handles player paddle movement"""
        if event.type == pygame.KEYDOWN:
            # Player 1 controls
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                self._player_move_up = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self._player_move_down = True
            
            # Player 2 controls (only in 2-player mode)
            if self._game_mode == "2_player":
                if event.key == pygame.K_i:  # I key for up
                    self._player2_move_up = True
                if event.key == pygame.K_k:  # K key for down
                    self._player2_move_down = True
                    
        if event.type == pygame.KEYUP:
            # Player 1 controls
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                self._player_move_up = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self._player_move_down = False
            
            # Player 2 controls (only in 2-player mode)
            if self._game_mode == "2_player":
                if event.key == pygame.K_i:  # I key for up
                    self._player2_move_up = False
                if event.key == pygame.K_k:  # K key for down
                    self._player2_move_down = False


class GameOver(Scene):
    """game over scene for pong"""

    def __init__(self, screen, winner, game_mode="1_player" or "2_player", background_color=rgbcolors.blue, soundtrack=None):
        super().__init__(screen, background_color, soundtrack=soundtrack)
        self._player_win_sound = pygame.mixer.Sound("assets/sounds/player_win.wav")
        self._ai_win_sound = pygame.mixer.Sound("assets/sounds/ai_win.wav")
        if winner == "Player" or winner == "Player 1" or winner == "Player 2":
            self._player_win_sound.play()
        elif winner == "AI":
            self._ai_win_sound.play()
        self._winner = winner
        self._game_mode = game_mode
        self._restart = False

    def draw(self):
        """draw scene to screen"""
        super().draw()
        # Draw the background
        end_font = pygame.font.Font("assets/fonts/pong.ttf", 60)
        info_font = pygame.font.Font("assets/fonts/pong.ttf", 25)

        message = f"{self._winner} Wins!"
        message_surface = end_font.render(message, True, rgbcolors.black)
        # set positioning
        screen_center_x = self._screen.get_width() // 2
        screen_center_y = self._screen.get_height() // 2
        message_rect = message_surface.get_rect(
            center=(screen_center_x, screen_center_y - 275)
        )
        self._screen.blit(message_surface, message_rect)

        # exit game instructions
        instructions_surface = info_font.render(
            "Press Q to quit or R to restart", True, rgbcolors.black
        )
        instructions_rect = instructions_surface.get_rect(
            center=(screen_center_x, screen_center_y + 200)
        )
        self._screen.blit(instructions_surface, instructions_rect)

    def process_event(self, event):
        """Process game events."""
        super().process_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self._is_valid = False
            elif event.key == pygame.K_r:
                # Set restart flag and exit scene
                self._restart = True
                self._is_valid = False
                
    def should_restart(self):
        """Return whether the game should restart"""
        return self._restart