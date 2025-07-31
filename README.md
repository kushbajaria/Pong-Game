
# Pong!

In this exercise, we shall write a [Pong](https://en.wikipedia.org/wiki/Pong) style game. Pong was first released in 1972 and it was one of the first arcade video games. Pong is a table tennis (ping pong) themed video game.

The game play occurs on a single screen or scene where two players control two virtual paddles or racquets. The ball in play is _bounced_ back to the opposing side when it intersects the paddle. The player must move their paddle such that it intersects the ball before the ball passes behind the paddle thus scoring a point of the opposing player. The game was traditionally played in a landscape orientation where one player is at the left extreme of the display and the other player is at the right extreme of the display. Their paddles can only travel up or down, never forward or backward. No other action is taken by the player to strike the ball other than to have the paddle intersect the ball.

If you have never played Pong before, please visit the [Internet Archive](https://archive.org/) and try one of the many [Pong clones](https://archive.org/details/classicpcgames?query=pong). Playing the game will give you an appreciation for what the game mechanics are and how you can take the Pong concept and make it your own.

Additionally, you may find watching a video capture of gameplay on the original Atari Pong game informative. One such example is available [on YouTube](https://www.youtube.com/watch?v=fiShX2pTz9A). Pay attention to how far up or down the paddles can move. Notice how the ball bounces off the paddle and the walls; they are not always true reflections like a billard ball rebounding against a billiard table's bumpers.

Remember, this assignment is an individual assignment where you are creating your own Pong game clone. _Please do not follow an online tutorial or duplicate an existing Pong project._

Our Pong game shall have the following rules or requirements:

* The game must be written in Python using Pygame.

* The game must use object oriented design using the same principles from previous programming assignments. Projects which disregard this requirement will not be graded.

* The game must be graphical (not a text-based or text console game).

* The game must have a human player versus computer robot mode. (multi-human-player is at your discretion).

* The game may be controlled from the keyboard, mouse, or joystick.

* If joystick or mouse controls exist, then there must be an option to fallback to a keyboard.

* The objective of the game is to score three points. The first player to score three points wins the game. No more than one point may be earned per round.

* The program begins by presenting a title scene. The scene shows the title of the game and explains the controls of the game. To advance to the next scene, any key may be pressed. The next scene is the Pong game.

* A round begins when the ball is 'served' from the center of the game board. The direction of travel is left to your discretion. Prior to the ball being served, the game must have an auditory or visual cue that the player should get ready for the serve. For example, a visual countdown or two short beeps followed by one long beep would serve as cues to ready the player.

* The ball [reflects](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.reflect) off the walls perfectly. This means that angle of incidence is the same as the angle of [reflection](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.reflect).

* The ball may [reflect](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.reflect) perfectly off the player's paddle. It is left to your discretion is you wish to make the ball/paddle reflection be more sophisticated, similar to the Atari Pong game.

* When the ball overlaps or touches the player's paddle, a sound effect is played.

* When the ball overlaps or touches the game board's boundaries, a sound effect is played.

* A round is completed when the ball pass through a player's goal line. A sound effect is played when a point is scored.

* A player earns a point when the ball pass through their opponent's goal line. The goal line is a line immediately behind the player's paddle. This line may or may not be visible to the player(s).

* Once a round is completed, another round is started unless one of the players has amassed three points. If a player has earned a total of three points at the end of the round, then the game is over. A winner is declared.

* The players' paddles must be along the left and right edges of the window. One player will have their paddle move up and down along the left edge and the opposing player will have their paddle move up and down along the right edge.

* The player that moves along the right edge is a robot AI player. The player that moves along the left edge is a human player.

* The players' scores shall be shown along the top edge with the scores displayed off-center. (Left player with the score slightly off center to the left and right player with the score slightly off center to the right.) The score is shown as a single digit.

* Once the game has been won, the game play scene transitions to a scene where the winner is displayed (left player or right player) and the option is given to play again or quit.

* After winning or losing, selecting play again transitions back to the game play scene. Both players are now at zero points and the first round of the new game begins.

* Selecting the option to quit exits the game.

* A leaderboard is optional.

* Additional scenes may be added at your discretion.

* A soundtrack and sound effects are mandatory. The sounds may be synthesized during game play or pre-recorded sounds.

* The game play scene must have a soundtrack. All other scenes are at your discretion.

* All code related to the Pong game must be in a Python module named `videogame`.

* The main function must be called from the file named `pg.py`. The file `pg.py` is not in the `videogame` module.

* You must conform to [PEP-8](https://www.python.org/dev/peps/pep-0008/). Use [pylint](https://www.pylint.org/) and [pycodestyle](https://pypi.org/project/pycodestyle/) to conform to [PEP-8](https://www.python.org/dev/peps/pep-0008/).


There are a number of excellent resources available to you.

The first is the Pygame documentation and the Pygame source code. Within the Pygame source code is a directory of examples which can illustrate fundamental Pygame features and how to use them. Learning to navigate the source code and the system's documentation is an invaluable skill to develop.

The second is [Al Sweigart's](https://alsweigart.com/) book [Making Games with Python & Pygame](https://inventwithpython.com/pygame/). The full text of the book is available online at no cost and available for purchase through retailers. The book is very brief and focuses on building one game per chapter. The source code for all the games in the book are available from GitHub.

You are encouraged to read through the source code by Mr. Sweigart and others who have written excellent other games using Pygame. Be warned that you are tasked with creating your own game. Copying and pasting or starting from someone else's game is not ethical and strictly forbidden.

Start from scratch. Make your own game. Make something you'll be proud to share with family and friends.

# Rubric

* Functionality (12 points): Your submission shall be assessed for the appropriate constructs and strategies to address the exercise. A program the passes the instructor's tests completely receives full marks. A program that partially passes the instructors tests receives partial-marks. A program that fails the majority or all the tests receives no marks.

* Format & Readability (8 point): Your submission shall be assessed by checking whether your code passess the style and format check, as well as how well it follows the proper naming conventions, and internal documentation guidelines. Git log messages are an integral part of how readable your project is. Failure to include a header forfeits all marks.
