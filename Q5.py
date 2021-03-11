with open("input.txt") as f:
    line=f.readline()
    while line:
        line_count = 1
        a=line.split()
        count=len(a)
        f2=open("output.txt","a")
        f2.write("Number of characters in Line{} \t".format(line_count))
        f2.write(str(count))
        f2.write("\n")
        f2.close()
        line=f.readline()
        line_count+=1
f.close()

with open("input.txt") as nf:
    line=nf.readline()
    while line:
        line_count=1
        nf1=open("output.txt","a")
        nf1.write("Number of words in Line{} \t".format(line_count))
        nf1.write(str(len(line.replace(" ",""))-1))
        nf1.write("\n")
        nf1.close()
        line=nf.readline()
        line_count+=1
nf.close()
              
        
 
