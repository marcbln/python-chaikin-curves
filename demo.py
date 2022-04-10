#!/usr/bin/env python3
# 04/2022 created

from typing import List
from pysvg.builders import *

from Vector2d import Vector2d


def chaikin(points: List[Vector2d], bClosed: bool) -> List[Vector2d]:
    cutRatio = 0.25  # 25%
    newPoints = []

    if not bClosed:
        newPoints.append(points[0])

    numCuts = len(points) if bClosed else len(points) - 1
    for i in range(numCuts):
        a = points[i % len(points)]
        b = points[(i + 1) % len(points)]
        n0 = a * (1 - cutRatio) + b * cutRatio  # a*0.75 + b*0.25
        n1 = a * cutRatio + b * (1 - cutRatio)  # a*0.25 + b*0.75
        newPoints.append(n0)
        newPoints.append(n1)

    if not bClosed:
        newPoints.append(points[-1])

    return newPoints



def chaikin_iteration(points: List[Vector2d], numIterations: int, bClosed: bool) -> List[Vector2d]:
    for it in range(numIterations):
        points = chaikin(points, bClosed)

    return points


def savePolylineAsSvg(points: List[Vector2d], bClosed: bool, pathDestSvg: str):
    """ helper to save generated chalkin curve as svg file """
    sb = ShapeBuilder()
    mySVG = Svg(width=100, height=100)

    # background
    mySVG.addElement(sb.createRect(x=0, y=0, width="100%", height="100%", fill="white"))

    # ---- polyline or polygon
    if bClosed:
        polyline = sb.createPolygon(points=sb.convertTupleArrayToPoints([p.asTuple() for p in points]), strokewidth=1, stroke='blue', fill='lightblue')
    else:
        polyline = sb.createPolyline(points=sb.convertTupleArrayToPoints([p.asTuple() for p in points]), strokewidth=1, stroke='blue')
    mySVG.addElement(polyline)

    mySVG.save(pathDestSvg)


# ------------------------------------ MAIN


points = [
    Vector2d(10, 10),
    Vector2d(90, 10),
    Vector2d(90, 90),
    Vector2d(10, 90),
]

for numIterations in [0, 1, 2, 3, 4]:
    pointsChaikin = chaikin_iteration(points, numIterations, False)
    savePolylineAsSvg(pointsChaikin, False, f'./demo-out/chaikin-open-{numIterations}.svg')

    pointsChaikin = chaikin_iteration(points, numIterations, True)
    savePolylineAsSvg(pointsChaikin, True, f'./demo-out/chaikin-closed-{numIterations}.svg')
