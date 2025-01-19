import raylibpy as rl

from utils.constants import BUTTON_HEIGHT, BUTTON_WIDTH

class Button:
    def __init__(self, x, y, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, text="", color=(100, 100, 100, 255), hover_color=(150, 150, 150, 255), text_color=(255, 255, 255, 255), action=None):
        """
        Initialize a Button instance.
        
        :param x: X-coordinate of the button
        :param y: Y-coordinate of the button
        :param width: Width of the button
        :param height: Height of the button
        :param text: Text to display on the button
        :param color: Default button color
        :param hover_color: Button color when hovered
        :param text_color: Text color
        :param action: Callable to execute when the button is clicked
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.action = action

    def is_hovered(self):
        """Check if the button is hovered."""
        mouse_pos = rl.get_mouse_position()
        return rl.check_collision_point_rec(mouse_pos, rl.Rectangle(self.x, self.y, self.width, self.height))

    def draw(self):
        """Draw the button, using hover color if hovered."""
        if self.is_hovered():
            rl.draw_rectangle(self.x, self.y, self.width, self.height, self.hover_color)
        else:
            rl.draw_rectangle(self.x, self.y, self.width, self.height, self.color)
        
        # Draw the text
        text_width = rl.measure_text(self.text, 30)
        rl.draw_text(self.text, self.x + (self.width - text_width) // 2, self.y + (self.height - 30) // 2, 30, self.text_color)

    def click(self):
        """Execute the button's action if clicked."""
        if self.is_hovered() and rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
            if callable(self.action):
                self.action()