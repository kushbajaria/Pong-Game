"""A class to manage transitions from one scene to another."""


class SceneManager:
    """A scene manager that works like a list. Poor quality."""

    def __init__(self, scenes_list=None):
        """Initialize a scene manager with a given list of scenes."""
        self._scenes = scenes_list

    def __iter__(self):
        """Return an iterator to move through the scenes."""
        return iter(self._scenes)

    def add(self, scene):
        """Add an additional scene to the scene list."""
        self._scenes.append(scene)

    def process_event(self, event):
        """Process an event by the current scene."""
        self._scenes[-1].process_event(event)

    def update_scene(self):
        """Update the current scene."""
        if self._scenes:
            self._scenes[-1].update_scene()
        else:
            raise RuntimeError("No scene to update.")

    def draw(self):
        """Draw the current scene."""
        if self._scenes:
            self._scenes[-1].draw()
        else:
            raise RuntimeError("No scene to draw.")

    def is_valid(self):
        """Check if the current scene is valid."""
        if self._scenes:
            return self._scenes[-1].is_valid()
        return False

    def go_to_next_scene(self):
        """Go to the next scene in the list."""
        if len(self._scenes) > 1:
            self._scenes.pop()
        else:
            raise RuntimeError("No next scene to go to.")