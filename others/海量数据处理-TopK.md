#### 题目1
搜索引擎会通过日志文件把用户每次检索使用的所有检索串都记录下来，每个查询串的长度为1-255字节。
假设目前有一千万个记录（这些查询串的重复度比较高，虽然总数是1千万，但如果除去重复后，不超过3百万个。
一个查询串的重复度越高，说明查询它的用户越多，也就是越热门），请你统计最热门的10个查询串，要求使用的内存不能超过1G。

**解答：**
(1) 如果数据大则划为小的，如一亿个IP求Top 10，可先%1000将ip分到1000个小文件中去(读入大文件划分为小文件的方式)，
并保证一种ip只出现在一个文件中，再对每个小文件中的ip进行hashmap计数统计并按数量排序，最后归并或者用最小堆依次处理
每个小文件的top10以得到最后的解。

(2) 如果数据规模比较小，能一次性装入内存呢？比如这一题，虽然有一千万个Query，但是由于重复度比较高，因此事实上只有
300万的Query，每个Query255Byte，因此我们可以考虑把他们都放进内存中去（300万个字符串假设没有重复，都是最大长度，
那么最多占用内存3e10*1000/4=0.75G。所以可以将所有字符串都存放在内存中进行处理），而现在只是需要一个合适的数据结构，
在这里，HashTable绝对是我们优先的选择。

所以我们放弃分而治之/hash映射的步骤，直接上hash统计，然后排序。So，针对此类典型的Top-K问题，采取的对策往往是：
hashmap + 堆。如下所示：
- **hash_map统计**：先对这批海量数据预处理。具体方法是：维护一个Key为Query字串，Value为该Query出现次数的HashTable，
即hash_map(Query，Value)，每次读取一个Query，如果该字串不在Table中，那么加入该字串，并且将Value值设为1；如果该
字串在Table中，那么将该字串的计数加一即可。最终我们在O(N)的时间复杂度内用Hash表完成了统计；
- **堆排序**：第二步、借助堆这个数据结构，找出Top-K，时间复杂度为`NlogK`。即借助堆结构，我们可以在log量级的时间内查找
和调整/移动。因此，维护一个K(该题目中是10)大小的小根堆，然后遍历300万的Query，分别和根元素进行对比。所以，我们最终
的时间复杂度是：`O(N) + N*O(logK)`，(N为1000万，N’为300万)。

#### 题目2
在100G文件中找出出现次数最多的100个IP。

(1) 对于100G的文件，先算算能有多少条IP呢？每条IP最长为15个字节，则100G/15=6.7G条，IP一共有多少种呢，不考虑IPv6，
IPv4约有256^4=2^32条=4G条，那么最极端的情况是每种IP都有，每个都出现那么一两条。

(2) 要解决该问题首先要找到一种分类方式，把重复出现的IP都放到一个文件里面，一共分成100份，这可以通过把IP对100取模得到，
具体方法：去掉IP中的点转化为一个long型变量，这样取模为0,1,2...99的IP都分到一个文件了，那么这个划分就能保证每一文件
都能载入内存吗？这可不一定，万一模为9的IP特别多怎么办，可以再对这一类IP做一次取模，直到每个小文件足够载入内存为止。
这个分类很关键，如果是随便分成100份，相同的IP被分在了不同的文件中，接下来再对每个文件统计次数并做归并，这个思路就没
有意义了，起不到“大而化小，各个击破，缩小规模，逐个解决”的效果了。

(3) 接下来把每个小文件载入内存，建立哈希表unordered_map<string,int>，将每个IP作为关键字映射为出现次数，这个哈希表
建好之后也得先写入硬盘，因为内存就那么多，一共要统计100个文件呢。

(4) 在统计完100个文件之后，我再建立一个小顶堆，大小为100，把建立好并存在硬盘哈希表载入内存，逐个对出现次数排序，挑出
出现次数最多的100个，由于统计的次数直接和IP是对应的，找出最多的次数也就找出了相应的IP。

这只是个大致的算法，还有些细节，比如第90到110大的元素出现次数一样呢，就随机舍弃掉10个吗？整个的时间复杂度分类O(n)：
建哈希表O(n)，挑出出现最多次数的O(nlogk)。

