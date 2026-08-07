import java.util.*;

class Solution {
    public String smallestNumber(String num, long t) {
        long temp = t;
        int[] primes = {2, 3, 5, 7};

        for (int p : primes) {
            while (temp % p == 0) {
                temp /= p;
            }
        }

        if (temp != 1) {
            return "-1";
        }

        int n = num.length();
        long[] rem = new long[n + 1];
        rem[0] = t;

        int pos = n;
        for (int i = 0; i < n; i++) {
            int d = num.charAt(i) - '0';
            if (d == 0 && pos == n) {
                pos = i;
            }
            rem[i + 1] = rem[i] / gcd(rem[i], d);
        }

        if (pos == n && rem[n] == 1) {
            return num;
        }

        char[] arr = num.toCharArray();

        int start = (pos == n) ? n - 1 : pos;

        for (int i = start; i >= 0; i--) {

            long need = rem[i];

            int begin = arr[i] - '0' + 1;
            if (i >= pos) begin = 1;

            for (int d = begin; d <= 9; d++) {

                long cur = need / gcd(need, d);

                char[] ans = arr.clone();
                ans[i] = (char) ('0' + d);

                long left = cur;

                for (int j = n - 1; j > i; j--) {
                    ans[j] = '1';
                    for (int x = 9; x >= 2; x--) {
                        if (left % x == 0) {
                            ans[j] = (char) ('0' + x);
                            left /= x;
                            break;
                        }
                    }
                }

                if (left == 1) {
                    return new String(ans);
                }
            }
        }

        ArrayList<Character> digits = new ArrayList<>();

        long need = t;

        while (need > 1) {
            boolean ok = false;

            for (int d = 9; d >= 2; d--) {
                if (need % d == 0) {
                    digits.add((char) ('0' + d));
                    need /= d;
                    ok = true;
                    break;
                }
            }

            if (!ok) break;
        }

        StringBuilder sb = new StringBuilder();

        while (sb.length() + digits.size() < n + 1) {
            sb.append('1');
        }

        Collections.reverse(digits);

        for (char c : digits) {
            sb.append(c);
        }

        return sb.toString();
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}