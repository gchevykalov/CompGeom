from math import *

def double_s_abc(a, b, c):
    return (a[0] * b[1] + b[0] * c[1] + a[1] * c[0]) - (b[1] * c[0] + a[1] * b[0] + a[0] * c[1])

def convex_hull(pList: list) -> list:
    if len(pList) < 2:
        return pList
    if len(pList) == 2:
        return [min(pList), max(pList)]
    
    convexHullList = []

    leftPoint, rightPoint = min(pList), max(pList)

    allPointsLeft = left_hull(leftPoint, rightPoint, pList)
    allPointsRight = left_hull(rightPoint, leftPoint, pList)

    convexHullList.append(leftPoint)
    convexHullList += allPointsRight
    convexHullList.append(rightPoint)
    convexHullList += allPointsLeft
    finalHull = [convexHullList[0]]
    i = 1
    while i < len(convexHullList) - 1:
        if double_s_abc(convexHullList[i - 1], convexHullList[i], convexHullList[i + 1]) != 0:
            finalHull.append(convexHullList[i])
        i += 1
    finalHull.append(convexHullList[-1])
    return finalHull

def left_hull(a: list, b: list, pList: list):
    if len(pList) == 0:
        return []

    leftHullPoints = []
    resultPoints = []

    maxS = 0.0
    furthestPoint = []
    for p in pList:
        pS = double_s_abc(a, b, p)
        if pS > 0:
            leftHullPoints.append(p)
            if(pS > maxS):
                maxS = pS
                furthestPoint = p

    allPointsLeft = left_hull(a, furthestPoint, leftHullPoints)
    allPointsRight = left_hull(furthestPoint, b, leftHullPoints)

    resultPoints += allPointsRight
    if furthestPoint:
        resultPoints.append(furthestPoint)
    resultPoints += allPointsLeft
    
    return resultPoints
