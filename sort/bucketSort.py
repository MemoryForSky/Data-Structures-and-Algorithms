"""
桶排序：

基本思想：
将一个数据表分割成许多buckets，然后每个bucket各自排序，或用不同的排序算法，或者递归的使用bucket sort算法。
也是典型的divide-and-conquer分而治之的策略。它是一个分布式的排序。

时间复杂度：O(N)+O(M*(N/M)*log(N/M)) = O(N+N*(logN-logM)) = O(N+N*logN-N*logM)
"""
class node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None


def getBucketIndex(value):
    return value//interval

def printBuckets(bucket):
    cur = bucket
    while cur:
        print(cur.data, " ",end = "")
        cur = cur.next
    print("\n")

def bucketSort(data):
    bucket = []
    for i in range(n_bucket):
        bucket.append(None)

    for i in range(n_data):
        pos = getBucketIndex(data[i])      # O(N) + O(M)
        current = node(data[i])
        cur = bucket[pos]
        # 比较排序
        if cur == None or cur.data > current.data:      # O(N/Mlog(N/M))
            current.next = cur
            bucket[pos] = current
            bucket[pos] = current
        else:
            last = cur
            while cur != None and cur.data < current.data:
                last = cur
                cur = cur.next
            current.next = cur
            last.next = current

    for i in range(n_bucket):
        print("Bucket[", i,"] : ", end = "")
        printBuckets(bucket[i])

    result = []
    for i in range(n_bucket):
        cur = bucket[i]
        while cur is not None:
            result.append(cur.data)
            cur = cur.next

    return result

if __name__ == '__main__':
    data = [20, 40, 30, 10, 80, 50, 60, 90]
    n_data = len(data)        # data size
    n_bucket = 5              # bucket size
    interval = 20             # bucket range

    print("before sort:", data)

    data_order = bucketSort(data)

    print("after sort:", data_order)


