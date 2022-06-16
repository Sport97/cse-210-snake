from game.scripting.action import Action
from game.casting.actor import Actor
from game.casting.cast import Cast


# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor

class MoveActorsAction(Action):
    """Override the execute method from the Action class"""

    def __init__(self):
        """Constructs a new MoveActorsAction"""
        self.actor = Actor()
        self.cast = Cast()
        self.script = ""
    
    def execute(self, cast, script):
        all_actors = self.cast.get_all_actors()
        
        for actor in all_actors:
            actor.move_next()
        