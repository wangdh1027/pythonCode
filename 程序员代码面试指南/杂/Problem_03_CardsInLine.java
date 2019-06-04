package problems_2017_07_18;

public class Problem_03_CardsInLine {

	public static int win1(int[] arr) {
		if (arr == null || arr.length == 0) {
			return 0;
		}
		return Math.max(f(arr, 0, arr.length - 1), s(arr, 0, arr.length - 1));
	}

	public static int f(int[] arr, int i, int j) {
		if (i == j) {
			return arr[i];
		}
		return Math.max(arr[i] + s(arr, i + 1, j), arr[j] + s(arr, i, j - 1));
	}

	public static int s(int[] arr, int i, int j) {
		if (i == j) {
			return 0;
		}
		return Math.min(f(arr, i + 1, j), f(arr, i, j - 1));
	}

	public static int win2(int[] arr) {
		if (arr == null || arr.length == 0) {
			return 0;
		}
		int[][] f = new int[arr.length][arr.length];
		int[][] s = new int[arr.length][arr.length];
		for (int j = 0; j < arr.length; j++) {
			f[j][j] = arr[j];
			for (int i = j - 1; i >= 0; i--) {
				f[i][j] = Math.max(arr[i] + s[i + 1][j], arr[j] + s[i][j - 1]);
				s[i][j] = Math.min(f[i + 1][j], f[i][j - 1]);
			}
		}
		return Math.max(f[0][arr.length - 1], s[0][arr.length - 1]);
	}

	public static int win3(int[] arr) {
		if (arr == null || arr.length == 0) {
			return 0;
		}
		int sum = 0;
		for (int i = 0; i < arr.length; i++) {
			sum += arr[i];
		}
		int scores = p(arr, 0, arr.length - 1);
		return Math.max(sum - scores, scores);
	}

	public static int p(int[] arr, int i, int j) {
		if (i == j) {
			return arr[i];
		}
		if (i + 1 == j) {
			return Math.max(arr[i], arr[j]);
		}
		return Math.max(arr[i] + Math.min(p(arr, i + 2, j), p(arr, i + 1, j - 1)),
				arr[j] + Math.min(p(arr, i + 1, j - 1), p(arr, i, j - 2)));
	}

	public static int win4(int[] arr) {
		if (arr == null || arr.length == 0) {
			return 0;
		}
		if (arr.length == 1) {
			return arr[0];
		}
		if (arr.length == 2) {
			return Math.max(arr[0], arr[1]);
		}
		int sum = 0;
		for (int i = 0; i < arr.length; i++) {
			sum += arr[i];
		}
		int[][] dp = new int[arr.length][arr.length];
		for (int i = 0; i < arr.length - 1; i++) {
			dp[i][i] = arr[i];
			dp[i][i + 1] = Math.max(arr[i], arr[i + 1]);
		}
		dp[arr.length - 1][arr.length - 1] = arr[arr.length - 1];
		for (int k = 2; k < arr.length; k++) {
			for (int j = k; j < arr.length; j++) {
				int i = j - k;
				dp[i][j] = Math.max(arr[i] + Math.min(dp[i + 2][j], dp[i + 1][j - 1]),
						arr[j] + Math.min(dp[i + 1][j - 1], dp[i][j - 2]));
			}
		}
		return Math.max(dp[0][arr.length - 1], sum - dp[0][arr.length - 1]);
	}

	public static int[] generateRondomArray() {
		int[] res = new int[(int) (Math.random() * 20) + 1];
		for (int i = 0; i < res.length; i++) {
			res[i] = (int) (Math.random() * 20) + 1;
		}
		return res;
	}

	public static void main(String[] args) {
		int testTime = 50000;
		boolean err = false;
		for (int i = 0; i < testTime; i++) {
			int[] arr = generateRondomArray();
			int r1 = win1(arr);
			int r2 = win2(arr);
			int r3 = win3(arr);
			int r4 = win4(arr);
			if (r1 != r2 || r1 != r3 || r1 != r4) {
				err = true;
			}
		}
		if (err) {
			System.out.println("2333333333");
		} else {
			System.out.println("6666666666");
		}
	}

}
