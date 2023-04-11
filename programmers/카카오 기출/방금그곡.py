def solution(m, musicinfos):
    answer = ''
    
    for music in musicinfos:
        musicinfo = music.split(',')
        musicStart = musicinfo[0].split(':')
        musicStartH = musicStart[0]
        musicStartM = musicStart[1]
        musicFin = musicinfo[1].split(':')
        musicFinH = musicFin[0]
        musicFinM = musicFin[1]
        musicTit = musicinfo[2]
        musicMel = musicinfo[3]
        if musicStartH == musicFinH:
            musicTime = int(musicFinM) - int(musicStartM)
        else:
            if musicStartH > musicFinH:
                musicFinH = '24'
            musicTime = (int(musicFinH) - int(musicStartH)) * 60 + int(musicFinM) - int(musicStartM)
            
        
        musicLen = 0
        musicMels = musicMel.split("#")
        for i in range(len(musicMels)):
            if musicMels[i] == '':
                continue
            else:
                j = 0
                while j < len(musicMels[i]):
                    musicLen += 1
                    j += 1
        totalMusic = ''
        if musicTime > musicLen:
            rep = musicTime // musicLen
            sub = musicTime % musicLen
            totalMusic = musicMel * rep
            
            r= 0
            while r < sub:
                totalMusic += musicMel[r]
                if musicMel[r + 1] == '#':
                    sub += 1
                r += 1
        elif musicTime < musicLen:
            r= 0
            while r < musicTime:
                totalMusic += musicMel[r]
                if musicMel[r + 1] == '#':
                    musicTime += 1
                r += 1
        else:
            totalMusic = musicMel
        
        for i in range(len(totalMusic) - len(m) + 1):
            if totalMusic[i] == m[0]:
                k = 1
                for j in range(i + 1, i + len(m)):
                    if totalMusic[j] != m[k]:
                        break
                    if j == i + len(m) - 1:
                        if j == len(totalMusic) - 1: 
                            if answer == '':
                                answer = musicTit
                                answerTime = musicTime
                            else:
                                if musicTime > answerTime:
                                    answer = musicTit
                                    answerTime = musicTime
                        elif totalMusic[j + 1] != '#':
                            if answer == '':
                                answer = musicTit
                                answerTime = musicTime
                            else:
                                if musicTime > answerTime:
                                    answer = musicTit
                                    answerTime = musicTime
                        else:
                            break
                    k += 1

    if answer == '':
        answer = '(None)'
    return answer