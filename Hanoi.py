def CSD(P,nbd):
    #creation du scénario de déplacement.
    LD=[]
    nbdp=0
    if nbd!=1:
        nbdp=(2**nbd)-1
    for d in range(1,nbdp+1):
        if d%2==1:
            LD.append(1)
        elif d%256==0:
            LD.append(9)
        elif d%128==0:
            LD.append(8)
        elif d%64==0:
            LD.append(7)
        elif d%32==0:
            LD.append(6)
        elif d%16==0:
            LD.append(5)
        elif d%8==0:
            LD.append(4)
        elif d%4==0:
            LD.append(3)
        else:
            LD.append(2)
    return P,LD,nbdp

def SD(P,LD,nbd,nbdp):
    #execution du scenario de deplacement.
    LM={1:(1,2,3),2:(1,3,2)}
    for d in range(nbdp):
        for vd in range(1,nbd+1):
            if LD[d]==vd:
                if vd%2==0:
                    P[vd]=LM[2][(LM[2].index(P[vd])+1)%3]
                else:
                    P[vd]=LM[1][(LM[1].index(P[vd])+1)%3]
                print(P,d,vd)
                break
    return P

def Jeux():
    #creation du plateau et initialisation du jeux.
    P=dict()
    nbd=int(input("Combien y a t il de disques ? : "))
    assert 0<nbd<=9, "veuillez rentrer un nombre valide de disques."
    for d in range(1,nbd+1):
        P[d]=1
    #jeux.
    P,LD,nbdp=CSD(P,nbd)
    P=SD(P,LD,nbd,nbdp)
    return P


print(Jeux(),"Disque:Emplacement")