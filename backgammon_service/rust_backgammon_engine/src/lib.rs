#[derive(Debug)]
struct BackgammonState {
    board: [i32; 24],
    white_caught: i8,
    black_caught: i8,
    black_bearing: bool,
    white_bearing: bool,
    ended: bool,
    black_outside: i8,
    white_outside: i8,
}

impl BackgammonState {
    fn new(
        board: [i32; 24],
        whiteCaught: i8,
        blackCaught: i8,
        blackBearing: bool,
        whiteBearing: bool,
        ended: bool,
        blackOutside: i8,
        whiteOutside: i8,
    ) -> BackgammonState {
        BackgammonState {
            board,
            white_caught,
            black_caught,
            black_bearing,
            white_bearing,
            ended,
            black_outside,
            white_outside,
        }
    }
}

enum Player {
    White,
    Black,
}

struct BackGammonMove {
    player: Player,
    from: i32,
    to: i32,
}

impl BackGammonMove {
    fn new(player: Player, from: i32, to: i32) -> BackGammonMove {
        BackGammonMove { player, from, to }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn isBlackBearingTest1() {
        let initial_state = BackgammonState {
        board: [0; 24],
        white_caught: 0,
        black_caught: 0,
        black_bearing: false,
        white_bearing: false,
        ended: false,
        black_outside: 0,
        white_outside: 0,
    };
        let result = isBlackBearing()
        assert_eq!(result, 4);
    }

    #[test]
    fn isBlackBearingTest2() {
        let state = BackgammonState {

        }
        let result = isBlackBearing()
        assert_eq!(result, 4);
    }

}

/*
Black: is positive numbers
White negative numbers
*/

fn insertStonesBlack(
    gameState: &mut BackgammonState,
    dice: Vec<i32>,
) -> (BackgammonState, Vec<i32>) {
    let usedDice: Vec<i32> = Vec::new();
    for d in dice.iter() {}

    (gameState, usedDice)
}

fn  updateBoardMoveBlack(gameState : &mut BackgammonState, moveBlack : BackGammonMove ) -> BackgammonState {
    
    if moveBlack.from == -1 {
        gameState.blackCaught -= 1;
        gameState.board[moveBlack.to] +=1;
        gameState.blackBearing = 
    }
}

fn isBlackBearing(gameState : &mut BackgammonState) -> bool {
    if gameState.blackCaught > 0 {
        return False;
    }
    let boardSlice : &[i32] = &gameState.board[18..24];
    let sumBlackStones = boardSlice.iter().filter(|x| x > 0).sum().collect();
    (sumBlackStones + gameState.blackOutside) == 15
}
