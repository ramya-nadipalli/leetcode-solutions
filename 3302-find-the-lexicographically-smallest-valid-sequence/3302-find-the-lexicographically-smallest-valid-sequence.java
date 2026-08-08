class Solution {
    public int[] validSequence(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();

        // last[j] = earliest index in word1 from which
        // word2[j...] can be matched exactly.
        int[] last = new int[m];
        java.util.Arrays.fill(last, -1);

        int i = n - 1;
        int j = m - 1;

        while (i >= 0 && j >= 0) {
            if (word1.charAt(i) == word2.charAt(j)) {
                last[j] = i;
                j--;
            }
            i--;
        }

        int[] ans = new int[m];
        int k = 0;

        boolean usedMismatch = false;
        j = 0;

        for (i = 0; i < n && j < m; i++) {

            // Characters already match.
            if (word1.charAt(i) == word2.charAt(j)) {
                ans[k++] = i;
                j++;
            }

            // Use our one allowed mismatch.
            else if (!usedMismatch) {

                // If this is the last character, we can
                // always change it.
                if (j == m - 1 || last[j + 1] > i) {
                    ans[k++] = i;
                    j++;
                    usedMismatch = true;
                }
            }
        }

        if (j == m) {
            return ans;
        }

        return new int[0];
    }
}