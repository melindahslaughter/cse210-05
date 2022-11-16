import constants
from game.casting.actor import Actor
from game.casting.snake import Snake
from game.shared.point import Point

class RedSnake(Snake):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        #self._position = Point(0, 0)
        #self._velocity = Point(0, 0)
        #self._segments = []
        #self._prepare_body()

    def _prepare_body(self):
        x = int(constants.MAX_X / 2)
        y = int(3 * constants.MAX_Y / 4)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0) #original
            text = "8" if i == 0 else "#"
            color = constants.RED if i == 0 else constants.RED
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)