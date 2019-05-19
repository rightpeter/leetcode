import java.util.concurrent.ThreadLocalRandom;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringJoiner;

class Solution {
    int[][] points;

    private void swap(int i, int j) {
        int x = points[i][0];
        int y = points[i][1];
        points[i][0] = points[j][0];
        points[i][1] = points[j][1];
        points[j][0] = x;
        points[j][1] = y;
    }

    private static int dist(int[] point) {
        return point[0]*point[0] + point[1]*point[1];
    }

    private void partition(int i, int j, int K) {
        // if (i >= j) return;
        if (i >= j || K == 0) return;
        int origI=i, origJ=j;
        int pivot = ThreadLocalRandom.current().nextInt(i, j);
        pivot = Solution.dist(points[pivot]);

        while (i < j) {
            while (i < j && Solution.dist(points[i]) < pivot) {
                i++;
            }
            while (i < j && Solution.dist(points[j]) > pivot) {
                j--;
            }
            swap(i, j);
        }

        if (i - origI > K) {
            partition(origI, i, K);
        } else {
            System.out.println(String.format("i: %d, origJ: %d, K: %d", i, origJ, K - i + origI));
            partition(i+1, origJ, K - i + origI - 1);
        }

    }

    public int[][] kClosest(int[][] points, int K) {
        this.points = points;
        partition(0, points.length-1, K);

        return Arrays.copyOfRange(points, 0, K);
    }

    public static void main(String[] args) {
        int[][] points, output, ret;
        int K;
        StringJoiner sjRet, sjOutput;
        Solution kClose;

        points = new int[][]{{1, 3}, {-2, 2}};
        output = new int[][]{{-2, 2}};
        K = 1;
        kClose = new Solution();
        ret = kClose.kClosest(points, K);

        sjRet = new StringJoiner(System.lineSeparator());
        for (int[] row : ret) {
            sjRet.add(Arrays.toString(row));
        }
        sjOutput = new StringJoiner(System.lineSeparator());
        for (int[] row : output) {
            sjOutput.add(Arrays.toString(row));
        }

        System.out.println(String.format("Test 1 is %s, ret: (%s), output: (%s)", (Arrays.equals(ret, output)) ? "Correct" : "Wrong", sjRet.toString(), sjOutput.toString()));

        points = new int[][]{{3, 3}, {5, -1}, {-2, 4}};
        output = new int[][]{{3, 3}, {-2, 4}};
        K = 2;
        ret = kClose.kClosest(points, K);

        sjRet = new StringJoiner(System.lineSeparator());
        for (int[] row : ret) {
            sjRet.add(Arrays.toString(row));
        }
        sjOutput = new StringJoiner(System.lineSeparator());
        for (int[] row : output) {
            sjOutput.add(Arrays.toString(row));
        }

        System.out.println(String.format("Test 2 is %s, ret: (%s), output: (%s)", (Arrays.equals(ret, output)) ? "Correct" : "Wrong", sjRet.toString(), sjOutput.toString()));

        points = new int[][]{{6, 10}, {-3, 3}, {-2, 5}, {0, 2}};
        output = new int[][]{{-2, 2}};
        K = 3;
        kClose = new Solution();
        ret = kClose.kClosest(points, K);

        sjRet = new StringJoiner(System.lineSeparator());
        for (int[] row : ret) {
            sjRet.add(Arrays.toString(row));
        }
        sjOutput = new StringJoiner(System.lineSeparator());
        for (int[] row : output) {
            sjOutput.add(Arrays.toString(row));
        }

        System.out.println(String.format("Test 3 is %s, ret: (%s), output: (%s)", (Arrays.equals(ret, output)) ? "Correct" : "Wrong", sjRet.toString(), sjOutput.toString()));
    }
}