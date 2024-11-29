import java.util.ArrayList;
import java.util.List;

public class FindFarmland {
    public int[][] findFarmland(int[][] land) {
        List<int[]> result = new ArrayList<>();
        int m = land.length;
        int n = land[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (land[i][j] == 1) {
                    int[] coordinates = dfs(land, i, j);
                    result.add(coordinates);
                }
            }
        }

        return result.toArray(new int[0][]);
    }

    private int[] dfs(int[][] land, int i, int j) {
        int m = land.length;
        int n = land[0].length;

        int[] result = new int[]{i, j, i, j}; // [top-left row, top-left col, bottom-right row, bottom-right col]

        // Mark the current land as visited
        land[i][j] = 0;

        // DFS in all four directions
        if (i + 1 < m && land[i + 1][j] == 1) {
            result[2] = Math.max(result[2], dfs(land, i + 1, j)[2]);
        }
        if (j + 1 < n && land[i][j + 1] == 1) {
            result[3] = Math.max(result[3], dfs(land, i, j + 1)[3]);
        }

        return result;
    }

    public static void main(String[] args) {
        FindFarmland solution = new FindFarmland();
        int[][] land = {
            {1, 0, 0},
            {0,1,1},
            {0, 1, 1},
        };
        int[][] result = solution.findFarmland(land);
        for (int[] group : result) {
            System.out.println("[" + group[0] + ", " + group[1] + ", " + group[2] + ", " + group[3] + "]");
        }
    }
}

