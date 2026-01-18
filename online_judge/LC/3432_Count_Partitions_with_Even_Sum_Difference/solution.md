[Leetcode 3432](https://leetcode.com/problems/count-partitions-with-even-sum-difference/)

設左邊的集合的總和為 $L$，右邊的集合的總和為 $R$

$L$ 和 $R$ 的差為 $D$，整個集合的總和為 $T$

$$
\begin{aligned}
T &= L + R \Rightarrow R = T - L \\
D &= L - R \\
  &= L - (T - L) \\
  &= 2L - T
\end{aligned}
$$

其中 $2L$ 必為偶數

因此若 $T$ 為奇數，則 $D$ 不可能為偶數 $\Rightarrow$ `return 0`

若 $T$ 為偶數，則 $D$ 必為偶數

因此不管怎麼切分 $D$ 都是偶數 $\Rightarrow$ `return len(nums) - 1`