import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringJoiner;

class Solution {
    public static int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]> heap = new PriorityQueue<int[]>((p1, p2) -> p2[0]*p2[0] + p2[1]*p2[1] - p1[0]*p1[0] - p1[1]*p1[1]);
        int[][] ret = new int[K][2];

        for (int[] point : points) {
            heap.add(point);
            if (heap.size() > K) {
                heap.poll();
            }
        }

        for (int i = 0; i < K; i++) {
            ret[i] = heap.poll();
        }

        return ret;
    }

    public static void main(String[] args) {
        int[][] points, output, ret;
        int K;
        StringJoiner sjRet, sjOutput;

        points = new int[][]{{1, 3}, {-2, 2}};
        output = new int[][]{{-2, 2}};
        K = 1;
        ret = kClosest(points, K);

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
        ret = kClosest(points, K);

        sjRet = new StringJoiner(System.lineSeparator());
        for (int[] row : ret) {
            sjRet.add(Arrays.toString(row));
        }
        sjOutput = new StringJoiner(System.lineSeparator());
        for (int[] row : output) {
            sjOutput.add(Arrays.toString(row));
        }
        System.out.println(String.format("Test 2 is %s, ret: (%s), output: (%s)", (Arrays.equals(ret, output)) ? "Correct" : "Wrong", sjRet.toString(), sjOutput.toString()));
    }
}