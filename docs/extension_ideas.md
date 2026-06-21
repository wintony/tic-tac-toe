# Extension ideas

## Current project

Terminal-based two-player Tic Tac Toe.

## Possible Extensions

### Computer player
Add a mode where Player Two is the computer

#### Plan
- Get available moves from GAME_STATE
- Randomly choose one valid move
- Block winning move
- Place move next to a previous move
- Take winning move if available
- Pick corners

### Mini-board variant
Tic-Tac-Toe, but each square is its own Tic-Tac-Toe game. If you win a mini-board, that square is marked for you in the overall board

#### Plan
- GAME_STATE represents the overall board
- Create a list for each mini-board (9 lists)
- Ask user for board number and square number
- First step: allow placing marks in selected mini-board
- Detect mini-board wins
- Detect overall win
