class Solution:
    def isValidRowColBox(self, box: List[str]) -> bool:
        check = set()
        for item in box:
            if item == ".":
                continue
            i = int(item)
            if i in check:
                return False
            if i > 9 or i < 1:
                return False
            check.add(i)
        return True        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = True

        # check rows
        for i in range(0, 9):
            res = self.isValidRowColBox(board[i])
            if res == False:
                return False
        
        # check cols
        for i in range(0, 9):
            col = []
            for j in range(0, 9):
                col.append(board[j][i])
            res = self.isValidRowColBox(col)
            if res == False:
                return False
        
        # check boxes
        for i in range(0, 9):
            box = []
            row_increment = i % 3
            col_increment = i // 3
            for j in range(0, 3):
                for k in range(0, 3):
                    box.append(board[col_increment * 3 + j][row_increment * 3 + k])
            res = self.isValidRowColBox(box)
            if res == False:
                return False

        return True
        