import copy

class Graph(object):
    def __init__(self, board):
        self.board = board
        self.letters = {}
        self.adj_list = {}
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(4):
            for j in range(4):
                if board[i][j] not in self.letters:
                    self.letters[board[i][j]] = []
                self.letters[board[i][j]].append((i, j))
                self.adj_list[(board[i][j], i, j)] = []
                for d1, d2 in directions:
                    k = i+d1
                    l = j+d2
                    if k >= 0 and k < 4 and l >= 0 and l < 4:
                        self.adj_list[(board[i][j], i, j)].append((board[k][l], k, l))
        print(self.letters)
        print(self.adj_list)

    def dfs(self, word):
        if len(word) < 4:
            return False
        stack = []
        if word[0] not in self.letters:
            return False
        for i, j in self.letters[word[0]]:
            stack.append((word[0], word, (word[0], i, j), set([(i, j)])))
        # print('this is stack', stack)
        while len(stack) > 0:
            sub, word, let, positions = stack.pop()
            if sub == word:
                return True
            next_letter = word[len(sub)]
            for l, i, j in self.adj_list[let]:
                if l == next_letter and (i, j) not in positions:
                    p2 = copy.deepcopy(positions)
                    p2.add((i, j))
                    stack.append((sub+next_letter, word, (l, i, j), p2))
        return False
    

d = []
def load_dictionary():
    with open('dictionary.txt') as f:
        for line in f:
            if len(line) >= 4 and not line[0].isupper():
                d.append(line.upper()[:-1])

def find_words(board):
    g = Graph(board)
    words = []
    for word in d:
        if g.dfs(word):
            words.append((word))
    return words


def boggle_input():
    board = []
    for i in range(4):
        row = input().upper()
        if len(row.split()) == 4:
            for a in row.split():
                if len(a) != 1:
                    print('illegal input')
                    return False
            board.append(row.split())
        else:
            print('illegal input')
            return False
    print('1 row of letters:', board[0])
    print('2 row of letters:', board[1])
    print('3 row of letters:', board[2])
    print('4 row of letters:', board[3])
    print(board)
    words = find_words(board)
    for word in words:
        print('Found:', word)
    print('There are', len(words), 'anagrams in total.')


if __name__ == '__main__':
    load_dictionary()
    boggle_input()