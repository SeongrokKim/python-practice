import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
left = 0
right = n-1
ans1 = l[left]
ans2 = l[right]
while l[left] != l[right]:
    if l[left] + l[right] > 0:
        right -= 1
    elif l[left] + l[right] < 0:
        left += 1
    else:
        print(l[left], l[right])
        exit()
    if left == right:
        break
    if abs(l[left] + l[right]) < abs(ans1 + ans2):
        ans1 = l[left]
        ans2 = l[right]
print(ans1, ans2)
        
