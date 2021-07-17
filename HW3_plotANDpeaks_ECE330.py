#code returns a plot of given txt data and also returns the peaks of the plot.
import matplotlib.pyplot as plt
# import math

def find_peak(lt, start, end):
    m = start
    while(m < end):
        if(lt[m-1] <= lt[m] and lt[m] >= lt[m+1]):
            return m
        m+=1
#better algorithm but it doesnt work, errors to memory dump or recursion error
#     if((lt[middle] >= lt[middle - 1]) and (lt[middle] >= lt[middle + 1])):
#         return middle
#     elif(middle > 0 and lt[middle - 1] > lt[middle]):
#         middle2 = start + math.floor(((middle-1)- start)/2)
#         return find_peak(lt, start, middle2, (middle - 1))
#     else:
#         middle3 = (middle + 1) + math.floor(((end-1)- (middle + 1))/2)
#         return find_peak(lt, (middle + 1), middle3, end)
         

#driver function
text_file = open("giventext.txt","r")
data = text_file.read().split(',')
#text_file.close()

i=0
i2=0
i3=0
out=[]
x=[]
while(i<len(data)):
    value = float(data[i])
    out.append(value)
    x.append(i+1)
    i+=1
    
# print(len(out),out)
# print(len(x),x)
print("The Peaks of the graph are:")
while(i2 < 100):
    k = find_peak(data,i2,len(data))
    print(data[k])
    i2 += k
  
plt.plot(x, out, 'r-')
plt.show()
