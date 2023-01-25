#pragma once
#include <string>
#include <fstream>
#include <tuple>
#include <vector>

class SudokuGame {

 public:
  std::vector<std::vector<int>> gamegrid;
  SudokuGame() = default;

  SudokuGame(std::string filename){
    std::ifstream inputFile(filename);
    std::string str, str1;
    int val;
    for(int i = 0; i < 9; i++){
        std::vector<int> vec1 = {0, 0, 0, 0, 0, 0, 0, 0, 0};
        gamegrid.push_back(vec1);
    }
    for(int i = 0; i < 9; i++){
        getline(inputFile, str);
        for(int j = 0; j < 9; j++){
            str1 = str.substr(0, 1);
            str.erase(0, str.find(","));
            str.erase(0, str.find(" ") + 1);
            val = std::stoi(str1);
            gamegrid[i][j] = val;
        }
    }
    }
    ~SudokuGame(){
    (*this).gamegrid.clear();
    }

    SudokuGame(const SudokuGame& s){
    for(int i = 0; i < 9; i++){
        std::vector<int> vec1 = {0, 0, 0, 0, 0, 0, 0, 0, 0};
        (*this).gamegrid.push_back(vec1);
    }
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            (*this).gamegrid[i][j] = s.gamegrid[i][j];
        }
    }
    }
    SudokuGame& operator=(SudokuGame& s){
      for(int i = 0; i < 9; i++){
        std::vector<int> vec1 = {0, 0, 0, 0, 0, 0, 0, 0, 0};
        (*this).gamegrid.push_back(vec1);
    }
        for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            (*this).gamegrid[i][j] = s.gamegrid[i][j];
        }}
    return *this;}
    
  const std::vector<std::vector<int>>& grid() const;
  void print() const;
  int size() const;
  int value(int row, int column) const;
  void value(int row, int column, int newValue);
};

class SudokuPlayer {
  public:
  SudokuPlayer() = default;
  bool solve(SudokuGame& ) ;
  bool solveSudoku(SudokuGame& , int row, int col);
  bool isSafe(SudokuGame& , int row, int col, int num);
};
