n=10000
factor=2
lastFactor=1
while n>1
if n mod factor=0
 then
 lastFactor=factor
 n=n div factor
while n mod factor=0
n=n div factor
factor=factor+1
