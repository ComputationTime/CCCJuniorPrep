rule1a,rule1b = input().split()
rule2a,rule2b = input().split()
rule3a,rule3b = input().split()
times,sequence,end = input().split()
times = int(times)
found = False

def bfs(past_seqs,level,sequence):
    global found
    global lists
    global end
    if sequence == end:
        for output in past_seqs:
            print(output)
        found = True
    if level > times:
        return
    if found:
        return
    for length in range(1,len(sequence)+1):
        for i in range(len(sequence)+1-length):
            if sequence[i:i+length] == rule1a:
                newseq = sequence[0:i] + rule1b + sequence[i+length:len(sequence)]
                past_seqs.append(f'1 {i+1} {newseq}')
                bfs(past_seqs,level+1,newseq)
                past_seqs.pop()
            if sequence[i:i+length] == rule2a:
                newseq = sequence[0:i] + rule2b + sequence[i+length:len(sequence)]
                past_seqs.append(f'2 {i+1} {newseq}')
                bfs(past_seqs,level+1,newseq)
                past_seqs.pop()
            if sequence[i:i+length] == rule3a:
                newseq = sequence[0:i] + rule3b + sequence[i+length:len(sequence)]
                past_seqs.append(f'3 {i+1} {newseq}')
                bfs(past_seqs,level+1,newseq)
                past_seqs.pop()

past_seqs = []
bfs(past_seqs,0,'AB')








                



