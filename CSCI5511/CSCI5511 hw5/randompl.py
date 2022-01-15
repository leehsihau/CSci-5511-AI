import sat_interface
import random


'''
python3 randompl.py
'''

def rand3cnf(m, n):
    neg=["", "~"]
    clauses=[]
    for i in range(0, m):
        clause=""
        uniq=set()
        for _ in range (0, 3):
            clause+=neg[random.randint(0, 1)]
            candidate=random.randint(1, n)
            while candidate in uniq:
                candidate=random.randint(1, n)
            uniq.add(candidate)
            clause+=str(candidate)
            clause+=" "
        clauses.append(clause)
    print(str(clauses))
    example_prob_ = sat_interface.KB(clauses)
    #print(example_prob_.is_satisfiable())
    return example_prob_.is_satisfiable()

def wrapper():
    m_candidates=[20,30,40,50,60,70,80]
    n_candidates=[5,10,15,20]

    #m_dic={20:0, 30:0, 40:0, 50:0, 60:0, 70:0, 80:0}
    #n_dic={5:0, 10:0, 15:0, 20:0}

    for m in m_candidates:
        for n in n_candidates:
            count=0
            for i in range(0,100):
                if rand3cnf(m, n)==True:
                    count+=1
            if float(count/100) != 0 and float(count/100) !=1:
                print("m: "+str(m))
                print("n: "+str(n))
                print("result: "+str(float(count/100)))
               # m_dic[m]+=1
                #n_dic[n]+=1
    #print(m_dic)
    #print(n_dic)


wrapper()
#rand3cnf(80,20)