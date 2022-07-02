void dfs(int[][] matrix, bool[] visited, int i) {
    for (int j = 0; j < matrix.GetLength(0); j++ ) {
        if (matrix[i][j] == 1 && !visited[j]) {
            visited[j] = true;
            dfs(matrix, visited, j);
        }
    }
}

int FindCircleNum(int[][] isConnected) {
    bool[] visited = new bool[isConnected.GetLength(0)];
    int count = 0;
    for (int i = 0; i < isConnected.GetLength(0); i++) {
        if (!visited[i]) {
            dfs(isConnected, visited, i);
            count++;
        }
    }
    return count;
}

int[][] test = { 
    new int[] {1,1,0},
    new int[] {1,1,0},
    new int[] {0,0,1}
};
Console.WriteLine(FindCircleNum(test));

int[][] test2 = { 
    new int[] {1,0,0},
    new int[] {0,1,0},
    new int[] {0,0,1}
};
Console.WriteLine(FindCircleNum(test2));