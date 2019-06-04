# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:07:08 2019
搅乱串
@author: comnet
"""

def isScramble(str1,str2):
    if len(str1) != len(str2):
        return False
    if str1 == str2:
        return True
    N = len(str1)
    dp = [[[False for i in range(N+1)] for j in range(N)] for z in range(N)]
    for i in range(N):
        for j in range(N):
            dp[i][j][1] = str1[i]==str2[j]
    for size in range(2,N+1):
        for l1 in range(N-size+1):
            for l2 in range(N-size+1):
                for p in range(1,size):
                    if (dp[l1][l2][p] and dp[l1+p][l2+p][size-p]) or (dp[l1][l2+size-p][p] and dp[l1+p][l2][size-p]):
                        dp[l1][l2][size] = True
                        break
    return dp[0][0][N]

print(isScramble('54321aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbb',
                 '12345bbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
#   JAVA
#	public static boolean isScramble(String s1, String s2) {
#		if (s1.length() != s2.length()) {
#			return false;
#		}
#		if (s1.equals(s2)) {
#			return true;
#		}
#		int N = s1.length();
#		char[] chs1 = s1.toCharArray();
#		char[] chs2 = s2.toCharArray();
#		boolean[][][] dp = new boolean[N][N][N + 1];
#		for (int L1 = 0; L1 < N; L1++) {
#			for (int L2 = 0; L2 < N; L2++) {
#				dp[L1][L2][1] = chs1[L1] == chs2[L2];
#			}
#		}
#		for (int size = 2; size <= N; size++) {
#			for (int L1 = 0; L1 <= N - size; L1++) {
#				for (int L2 = 0; L2 <= N - size; L2++) {
#					for (int p = 1; p < size; p++) {
#						if ((dp[L1][L2][p] && dp[L1 + p][L2 + p][size - p])
#								|| (dp[L1][L2 + size - p][p] && dp[L1 + p][L2][size
#										- p])) {
#							dp[L1][L2][size] = true;
#							break;
#						}
#					}
#				}
#			}
#		}
#		return dp[0][0][N];
#	}




































