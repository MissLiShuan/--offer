class Solution:
    def minNumberInRotateArray(self,rotateArray):
        if not rotateArray:
            return 0
        
        front,rear = 0,len(rotateArray)-1
        midIndex = 0
        while rotateArray[front] >= rotateArray[rear]:
            if rear - front == 1:
                midIndex = rear
                break
            midIndex =(front+rear)//2
            if rotateArray[front] == rotateArray[midIndex] and rotateArray[front]==rotateArray[rear]:
               return self.minOrder(rotateArray,front,rear)
            if rotateArray[front] <= rotateArray[midIndex]:
               front = midIndex
            elif rotateArray[rear] >= rotateArray[midIndex]:
               rear = midIndex
        return rotateArray[midIndex]
    def minOrder(self,array,front,end):
        result = array[0]
        for i in array[front:end+1]:
            if i <result:
                result = i
        return result
