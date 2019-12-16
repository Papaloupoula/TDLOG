# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 13:42:17 2019

@author: Charles
"""
import numpy as np


def dist_it(chaine1, chaine2):
    """
    type chaine1 : string
    type chaine2 : string
    retourne la distance de damerau levensthein entre chaine1 et chaine2
    """
    if not (isinstance(chaine1,int) or isinstance(chaine2,int)):
        return "error"

    n1 = len(chaine1)
    n2 = len(chaine2)

    dist = np.zeros((n1+1,n2+1))

    for i in range(1,n1+1):
        dist[i][0]=i
    for i in range(1,n2+1):
        dist[0][i]=i

    for j in range(1,n2+1):
        for i in range(1,n1+1):
            if chaine1[i-1]==chaine2[j-1]:
                coutmodif=0
            else:
                coutmodif=1

            dist[i][j] = min(min(dist[i-1][j]+1, dist[i][j-1]+1), dist[i-1][j-1]+coutmodif)

            if (i>1 and j>1 and chaine1[i-1]==chaine2[j-2] and chaine1[i-2]==chaine2[j-1]):
                dist[i][j] = min(dist[i][j],dist[i-2][j-2] + coutmodif)
    return dist[n1][n2]

print(dist_it("charles","chiotte"))