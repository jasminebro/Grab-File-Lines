import linecache 


RmOut=open("Genome.fasta","r")
JustAlu=open("Genome.out","a") 

count =0
for line in RmOut.readlines():
    if "Unspecified" in line:
        JustAlu.write(line) 
        count=count+1 
    if "SINE/Alu" in line:
        JustAlu.write(line) 
        count=count+1
        print(count) 
            
        
             
             
RmOut.close()
JustAlu.close()

print("DONE TRANSFERRING LINES!")
