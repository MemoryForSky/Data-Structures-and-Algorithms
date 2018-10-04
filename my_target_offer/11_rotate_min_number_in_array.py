class Solution:
    """
    求旋转数组的最小值：利用旋转数组的特性解决本问题；
    """
    def min(self, arr, start, end):
        if arr is None or start > end:
            raise Exception("invalid parameters")

        if arr[start] < arr[end]:
            return arr[start]

        mid = (start + end) // 2

        if arr[mid] < arr[mid-1] and arr[mid] < arr[mid + 1]:
            return arr[mid]

        if arr[mid] < arr[0]:
            result = self.min(arr, start, mid - 1)
        elif arr[mid] > arr[0]:
            result = self.min(arr, mid + 1, end)
        else:
            return self.min_in_order(arr)

        return result

    def min_in_order(self, arr):
        min = arr[0]
        for i in range(len(arr)):
            if arr[i] < min:
                min = arr[i]
        return min

    def min2(self, arr):
        if arr is None or len(arr) <= 0:
            raise Exception("invalid parameters")

        index_start = 0
        index_end = len(arr) - 1
        index_mid = index_start

        while arr[index_start] >= arr[index_end]:
            if index_end - index_start == 1:
                index_mid = index_end
                break

            index_mid = (index_start + index_end) // 2

            # 首位与中间节点相同，无法判断最小在哪边，采用顺序查找
            if arr[index_start] == arr[index_end] and arr[index_start] == arr[index_mid]:
                return self.min_in_order(arr)

            if arr[index_mid] >= arr[index_start]:
                index_start = index_mid
            elif arr[index_mid] <= arr[index_end]:
                index_end = index_mid

        return arr[index_mid]


if __name__ == '__main__':
    array = [5, 6, 7, 8, 9, 2, 3, 4]
    array1 = [1,2,3,4,5,6,7,8]
    array2 = [1,0,0,0,1,1,1,1]
    array3 = [1]
    S = Solution()
    # target = S.min(array1, 0, len(array1)-1)
    target = S.min2(array2)
    print(target)

