__author__ = "Ejie Emmanuel Ebuka"


def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll - 1)

dolls = openRussianDoll(10)