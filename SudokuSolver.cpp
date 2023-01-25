#include <algorithm>
#include <iostream>
#include <fstream>
#include <numeric>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>
#include "main.h"

const std::vector<std::vector<int>>& SudokuGame::grid() const{
    return (*this).gamegrid;
}
void SudokuGame::print() const{
    for(int i = 0; i < 9; i++){
        if (i==3 || i ==6){
            std::cout << "---------------------------"<<std::endl;
        }
        for(int j = 0; j < 9; j++){
        if (j==2 || j==5){
            std::cout<<" "<<gamegrid[i][j] <<" |";
        } else if(j==8){
            std::cout<<" "<<gamegrid[i][j]<<std::endl;
        } else {
            std::cout <<" "<< gamegrid[i][j] <<" ";}
        }}
}
int SudokuGame::size() const{
    return (*this).gamegrid.size();
}
int SudokuGame::value(int row, int column) const{
    int val = gamegrid[row][column];
    return val;
}
void SudokuGame::value(int row, int column, int newValue){
    gamegrid[row][column] = newValue;
}
bool SudokuPlayer::solveSudoku(SudokuGame& game, int row, int col){
int N = game.size();
    if (row == N - 1 && col == N)
        return true;
    if (col == N) {
        row++;
        col = 0;
    }
    if (game.gamegrid[row][col] > 0)
        return solveSudoku(game, row, col + 1);
 
    for (int num = 1; num <= N; num++)
    {
        if (isSafe(game, row, col, num))
        {
            game.gamegrid[row][col] = num;
            if (solveSudoku(game, row, col + 1))
                return true;
        }
        game.gamegrid[row][col] = 0;
    }
    return false;
}
bool SudokuPlayer::isSafe(SudokuGame& game, int row, int col, int num){
    for (int x = 0; x <= 8; x++)
        if (game.gamegrid[row][x] == num)
            return false;
    for (int x = 0; x <= 8; x++)
        if (game.gamegrid[x][col] == num)
            return false;
    int startRow = row - row % 3,
            startCol = col - col % 3;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (game.gamegrid[i + startRow][j + startCol] == num)
                return false;
    return true;
}
bool SudokuPlayer::solve(SudokuGame& game) {
    bool s = solveSudoku(game, 0, 0);
    return s;
}
int main() {
  SudokuGame game("sudoku_game_1.csv");
  std::cout << "Puzzle" << std::endl;
  game.print();
  SudokuPlayer player;
  bool solved = player.solve(game);
  std::cout<< solved<< "\n";
  return 0;
}
