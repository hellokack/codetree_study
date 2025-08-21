www=str(input())
www=list(www)
www[1]='a'
www[-2]='a'
www=''.join(www)
print(www)