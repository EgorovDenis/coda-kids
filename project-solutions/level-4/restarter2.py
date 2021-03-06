"""General information on your module and what it does."""
import coda_kids as coda

# load sprites
IMAGE_BUTTON = coda.Image("button.png")

# modifiable data
class Data:
    """place changable state variables here."""
    restart_button = coda.Object(IMAGE_BUTTON)
    display_text = coda.TextObject(coda.color.WHITE, 24, "Player 2 wins! Play again?")

MY = Data()

def initialize(window):
    """Initializes the restart menu state."""
    MY.restart_button.location = window / 2

def update(delta_time):
    """Updates the restart menu state."""
    for event in coda.event.listing():
        if coda.event.quit_game(event):
            coda.stop()
        if coda.event.mouse_l_button_down(event):
            if MY.restart_button.collides_with_point(coda.event.mouse_position()):
                coda.state.change(0)

def draw(screen):
    """Draws the restart menu state."""
    MY.restart_button.draw(screen)
    MY.display_text.draw(screen)

def cleanup():
    """Cleans up the restart menu state."""
