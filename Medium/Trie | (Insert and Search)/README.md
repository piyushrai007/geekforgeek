<h2><a href="https://www.geeksforgeeks.org/problems/trie-insert-and-search0651/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab">Trie | (Insert and Search)</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;"><a href="https://www.geeksforgeeks.org/introduction-to-trie-data-structure-and-algorithm-tutorials/">Trie</a> is an efficient information retrieval data structure. Use this data structure to store strings and search other strings. Your task is to use <strong>Trie</strong> data structure to <strong>insert </strong>and <strong>search </strong>the given strings. Firstly, <strong>N</strong> strings will be added to the <strong>Trie </strong>and then a string will be used to test the <strong>search </strong>function. <strong>Return 1 </strong>if a given string is stored in <strong>Trie</strong>, else <strong>return 0</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Note: </strong>Strings will have all their characters as lower-case english alphabets. <strong>Read Your Task Section carefully.</strong></span></p>
<p><strong><span style="font-size: 18px;">Example 1:</span></strong></p>
<pre><strong><span style="font-size: 18px;">Input:
</span></strong><span style="font-size: 18px;">N = 8
key[] = {the, a, there, answer,<br>         any, by, bye, their}
S = the
<strong>Output: </strong>1<strong>
Explanation: <br>"</strong>the" is present in the given set of
strings "the", "a", "there", "answer", "any",<br>"by", "bye", "their"</span>
</pre>
<p><strong><span style="font-size: 18px;">Example 2:</span></strong></p>
<pre><strong><span style="font-size: 18px;">Input:
</span></strong><span style="font-size: 18px;">N = 8
key[] = {the, a, there, answer,<br>         any, by, bye, their}
S = geeks
<strong>Output: </strong>0<strong>
Explanation: <br></strong>"geeks" is not present in the
given set of strings.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You do not have to take any input or print anything. Complete <strong>insert</strong> and <strong>search</strong> functions.&nbsp;</span></p>
<p><strong><span style="font-size: 18px;">insert </span></strong><span style="font-size: 18px;">function takes a <strong>root </strong>node of the <strong>Trie </strong>and a <strong>string </strong>as an <strong>input</strong>, changes the root value <strong>in-place </strong>and <strong>returns nothing</strong>.<br><strong>search</strong> function takes a</span><span style="font-size: 18px;">&nbsp;</span><strong style="font-size: 18px;">root&nbsp;</strong><span style="font-size: 18px;">node of the&nbsp;</span><strong style="font-size: 18px;">Trie&nbsp;</strong><span style="font-size: 18px;">and a&nbsp;</span><strong style="font-size: 18px;">string&nbsp;</strong><span style="font-size: 18px;">as an&nbsp;</span><strong style="font-size: 18px;">input</strong><span style="font-size: 18px;">, returns <strong>true</strong> if <strong>string </strong>is found in the <strong>Trie</strong>, else <strong>false</strong>.</span></p>
<p><span style="font-size: 18px;">In case of <strong>true</strong>, driver code prints <strong>1 </strong>and in the case of <strong>false</strong>, <strong>0 </strong>is printed.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(M+|S|).<br><strong>Expected Auxiliary Space:</strong>&nbsp;O(M).<br>M = sum of the length of all strings which are present in the key[]&nbsp;<br></span><span style="font-size: 18px;">|S| denotes the length of the string search.</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= N &lt;= 10<sup>4</sup><br>1 &lt;= |input strings| &lt;= 30<br></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Accolite</code>&nbsp;<code>Amazon</code>&nbsp;<code>Microsoft</code>&nbsp;<code>D-E-Shaw</code>&nbsp;<code>FactSet</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Trie</code>&nbsp;<code>Design-Pattern</code>&nbsp;<code>Advanced Data Structure</code>&nbsp;