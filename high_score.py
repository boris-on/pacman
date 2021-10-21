from random import randint
import pygame
import json
import os

#path_to_score = os.path.join('###')


path_to_score = 'scores.txt'

class HScore:

    def __init__(self, key, value):
        self.name=key
        self.points=value

    def saveDataIntoFile(self):
        with open(path_to_score, 'r') as file_set:
            if(file_set.readline() == ""): 
                score_dict = {}
            else:
                file_set.close()
                with open(path_to_score, 'r') as file_set:
                    score_dict = json.load(file_set)
        score_dict[self.name] = self.points

        with open(path_to_score, 'w+') as file_set:
            json.dump(score_dict, file_set, indent='   ')

def readScorefromFile():
    scores = []
    with open(path_to_score, 'r') as file_set:
            if(file_set.readline() == ""): 
                score_file = {}
            else:
                file_set.close()
                with open(path_to_score, 'r') as file_set:
                    score_file = json.load(file_set)
    for i in score_file:
        scores.append(HScore(i,score_file[i]))
    '''f = open(path_to_score, 'w')
    f.write('{}')
    f.close()'''
    return scores

def main():
    scores = readScorefromFile()
    #######################################################
    ### _______________________________________________ ### 
    ###|Если имя уже есть в файле, обновляются очки    |###
    ###|Если нет именя, просто добавляется             |###
    ###|Если в файле ничего нет, просто добаляется     |###
    ###|_______________________________________________|###
    #######################################################
    scores.append(HScore('Anton',randint(1,234)))
    for i in scores:
        i.saveDataIntoFile()
        print(i.name, i.points)
if __name__ == '__main__':
    main()