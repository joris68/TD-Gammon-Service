
from src.BackgammonModel  import BackgammonModel, load_model
from src.BackgammonState import BackgammonState
from src.utils import generate_dice_for_move
from pathlib import Path
import logging
import os


logger = logging.getLogger(__name__)

class BackgammonManager:

     def __init__(self):
          self.model : BackgammonModel = load_model(path=os.environ.get("MODEL_PATH", Path("src/models/50000_g_training.pt")))
     

     def get_prediction(self, is_black : bool, curr_state : BackgammonState) -> BackgammonState | None:
          try:
               next_state = self.model.infer_state(game_state=curr_state, dice=generate_dice_for_move, is_black=is_black)
               return next_state
          except Exception as e:
               logger.error(f"could not make the prediction due to : {e}")
               return None

