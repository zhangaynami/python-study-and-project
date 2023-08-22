# -*- codeing = utf-8 -*-
def movetower(height,frompole,topole,withpole):
    if height >= 1:
        movetower(height - 1 ,frompole,withpole,topole)
        movedisk(frompole,topole)
        movetower(height -1 ,withpole,topole,frompole)

def movedisk(fp,tp):
    print("moving disk from " + fp + " to " + tp)
