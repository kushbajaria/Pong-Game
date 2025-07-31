"""Game objects to create PyGame based games."""

import warnings
import sys
import pygame
from videogame import rgbcolors
from videogame.scene import TitleScreen
from videogame.scene import GameScreen
from videogame.scene import GameOver
from videogame.scenemanager import SceneManager


def display_info():
    """Print out information about the display driver and video information."""
    print(f'The display is using the "{pygame.display.get_driver()}" driver.')
    print("Video Info:")
    print(pygame.display.Info())


# If you're interested in using abstract base classes, feel free to rewrite
# these classes.
# For more information about Python Abstract Base classes, see
# https://docs.python.org/3.8/library/abc.html


# pylint: disable=too-few-public-methods
class VideoGame:
    """Base class for creating PyGame games."""

    def __init__(
        self,
        window_width=750,
        window_height=750,
        window_title="Welcome to my awesome Pong game!",
    ):
        """Initialize a new game with the given
        window size and window title."""
        pygame.init()
        self._size = (window_width, window_height)
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(self._size)
        self._title = window_title
        pygame.display.set_caption(self._title)
        self._game_is_over = False
        if not pygame.font:
            warnings.warn("Fonts disabled.", RuntimeWarning)
        if not pygame.mixer:
            warnings.warn("Sound disabled.", RuntimeWarning)
        else:
            pygame.mixer.init()
        self._scene_manager = None

    def run(self):
        """Run the game; the main game loop."""
        raise NotImplementedError


class PongGame(VideoGame):
    """Handle pong game scenes"""

    def __init__(self):
        """initialize the Pong game"""
        super().__init__(window_title="Pong")
        self._scene_manager = SceneManager(
            [
                GameScreen(self._screen, rgbcolors.blue,
                           self._size, soundtrack="assets/sounds/gameplay.mp3"),
                TitleScreen(
                    self._screen,
                    "Pong",
                    rgbcolors.black,
                    self._size,
                    background_color=rgbcolors.blue,
                    soundtrack="assets/sounds/startup.mp3"
                ),
            ]
        )

    def run(self):
        """Run the main game loop for Pong"""
        # Start the initial scene (title screen)
        if self._scene_manager._scenes:
            self._scene_manager._scenes[-1].start_scene()
        
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                else:
                    self._scene_manager.process_event(event)
            self._scene_manager.update_scene()
            self._scene_manager.draw()

            pygame.display.flip()
            self._clock.tick(60)

            if not self._scene_manager.is_valid():
                current_scene = self._scene_manager._scenes[-1]
                # End the current scene
                current_scene.end_scene()
                
                if isinstance(current_scene, GameScreen):
                    if current_scene._game_mode == "1_player":
                        winner = ("Player" if current_scene._player_score >= 3 else "AI")
                    elif current_scene._game_mode == "2_player":
                        winner = ("Player 1" if current_scene._player_score >= 3 else "Player 2")
                    game_over_scene = GameOver(self._screen, winner, current_scene._game_mode)
                    self._scene_manager.add(game_over_scene)
                    game_over_scene.start_scene()
                elif isinstance(current_scene, TitleScreen):
                    # Check if user requested to quit
                    if current_scene.quit_requested():
                        run = False
                    else:
                        # Get the selected game mode and create appropriate GameScreen
                        selected_mode = current_scene.get_selected_game_mode()
                        if selected_mode:
                            game_screen = GameScreen(
                                self._screen, 
                                rgbcolors.blue,
                                self._size, 
                                game_mode=selected_mode,
                                soundtrack="assets/sounds/gameplay.mp3"
                            )
                            self._scene_manager.add(game_screen)
                            game_screen.start_scene()
                        else:
                            # Default to 1-player if no selection was made
                            self._scene_manager.go_to_next_scene()
                            if self._scene_manager._scenes:
                                self._scene_manager._scenes[-1].start_scene()
                elif isinstance(current_scene, GameOver):
                    if current_scene.should_restart():
                        # Restart the game - go back to title screen
                        title_screen = TitleScreen(
                            self._screen,
                            "Pong",
                            rgbcolors.black,
                            self._size,
                            background_color=rgbcolors.blue,
                            soundtrack="assets/sounds/startup.mp3"
                        )
                        self._scene_manager.add(title_screen)
                        title_screen.start_scene()
                    else:
                        run = False

        pygame.quit()
        sys.exit()


# pylint: enable=too-few-public-methods
