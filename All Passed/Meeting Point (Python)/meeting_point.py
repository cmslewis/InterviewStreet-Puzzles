# File: meeting_point.py
# Author: Chris Lewis (cmslewis@gmail.com)
# ------------------------------------------------------------------------------
# This program offers a solution to the "Meeting Point" challenge on the 
# InterviewStreet website (URL: https://www.interviewstreet.com/challenges/ 
# dashboard/#problem/4e14b2cc47f78). Here is the problem description, verbatim:
#
# ==
# There is an infinite integer grid at which N people have their houses on. They 
# decide to unite at a common meeting place, which is someone's house. 
# From any given cell, all 8 adjacent cells are reachable in 1 unit of time. 
# eg: (x,y) can be reached from (x-1,y+1) in a single unit of time.
# Find a common meeting place which minimises the sum of the travel times of all 
# the persons.
# 
# INTPUT FORMAT
# N
# The following N lines will contain two integers saying the x & y coordinate of 
# the i-th person.
# 
# OUTPUT FORMAT
# M M = min sum of all travel times; 
# 
# CONSTRAINTS
# N <= 10^5
# The absolute value of each co-ordinate in the input will be atmost 109
# 
# HINT: Please use long long 64-bit integers;
# 
# INPUT #00
# 4
# 0 1
# 2 5
# 3 1
# 4 0
# 
# OUTPUT #00
# 8
# 
# EXPLANATION
# Sums of travel times of the houses are 11, 13, 8 and 10. 8 is the minimum.
# 
# INPUT #01:
# 6
# 12 -14
# -3 3
# -14 7
# -14 -3
# 2 -12
# -1 -6
#
# OUTPUT #01
# 54
# ==

from math import copysign
from math import sqrt

# Enumerated indices for accessing X and Y coordinates in 2D points, 
# representated as 2-tuples.
X = 0
Y = 1

# A pseudo-infinite value just beyond the maximum input value specified in the 
# problem description. 
INFINITY = int(10e9) + 1

# Function: GetEuclideanMidpoint(xCoords, yCoords)
# Usage: midpoint = GetEuclideanMidpoint([0,1,2], [0,1,2])
# ------------------------------------------------------------------------------
# Returns the geometric midpoint between all points in the provided lists of x- 
# and y-coordinates, according to Euclidean geometry.
def GetEuclideanMidpoint(xCoords, yCoords):
  return (sum(xCoords) / len(xCoords), sum(yCoords) / len(yCoords))


# Function: GetEuclideanDistance(xCoords, yCoords)
# Usage: dist = GetEuclideanDistance(0, 2, 5, -3)
# ------------------------------------------------------------------------------
# Returns the Euclidean distance between the points with the provided 
# coordinates, where the first point is denoted by (x1, y1) and the second point 
# is denoted by (x2, y2).
def GetEuclideanDistance(x1, y1, x2, y2):
  return sqrt( pow(x2-x1, 2) + pow(y2-y1, 2) )


# Function: GetTaxicabDistance(xCoords, yCoords)
# Usage: dist = GetTaxicabDistance(0, 2, 5, -3)
# ------------------------------------------------------------------------------
# Returns the Taxicab distance between the points with the provided 
# coordinates, where the first point is denoted by (x1, y1) and the second point 
# is denoted by (x2, y2). In Taxicab geometry, one can only move in the 
# directions of +x, -x, +y, or -y, and all points must have integral coordinate 
# values. For this problem though, we use a slightly modified version of Taxicab 
# geometry, where one can also move diagonally by unit increments. Thus the 
# returned distance reflects the minimum number of moves required to travel from 
# point (x1, y1) to point (x2, y2), where each move can be horizontal, vertical, 
# or diagonal.
def GetTaxicabDistance(x1, y1, x2, y2):
  return max(abs(x2 - x1),
             abs(y2 - y1))


# Function: GetMeetingPoint(xCoords, yCoords)
# Usage: meetingPoint = GetMeetingPoint([0,1,2], [0,1,2])
# ------------------------------------------------------------------------------
# Returns the optimal meeting point for the points with the provided 
# coordinates. The optimal meeting point is the location that, when summing the 
# total travel distance from each provided point to the meeting point, will 
# minimize the total travel distance. Note that because the problem states that 
# one unit of distance can be traversed in one unit of time, the scalar 
# component of the total travel distance is equivalent to the scalar component 
# of the total travel time.
def GetMeetingPoint(xCoords, yCoords):
  # Find the geometric midpoint between all points.
  midpoint = GetEuclideanMidpoint(xCoords, yCoords)
  
  # Find the point closest to the midpoint we just calculated. This will be our 
  # actual meeting point. Note that we use Euclidean distance here.
  minDistance = INFINITY
  minIndex    = -1
  
  for i in range(len(xCoords)):
    distFromMidpoint = \
      GetEuclideanDistance(xCoords[i], yCoords[i], midpoint[X], midpoint[Y])
    
    if distFromMidpoint < minDistance:
      minDistance = distFromMidpoint
      minIndex    = i
  
  # Return the meeting point we just discovered.
  return (xCoords[minIndex], yCoords[minIndex])


# Function: TotalTaxicabTravelTime(xCoords, yCoords)
# Usage: totalTime = TotalTaxicabTravelTime([0,1,2], [0,1,2])
# ------------------------------------------------------------------------------
# Returns the minimum total travel time for the points with the provided 
# coordinates to arrive at the same point on the coordinate plane. Note that 
# because the problem states that one unit of distance can be traversed in one 
# unit of time, the scalar component of the total travel time is equivalent 
# to the scalar component of the total travel distance.
def TotalTaxicabTravelTime(xCoords, yCoords):
  # Find the optimal meeting point for the specified points.
  meetingPoint = GetMeetingPoint(xCoords, yCoords)
  
  # Sum the distance from each point to the chosen meeting point.
  totalDistance = 0
  for i in range(len(xCoords)):
    totalDistance += \
      GetTaxicabDistance(xCoords[i], yCoords[i],
                         meetingPoint[X], meetingPoint[Y])
  
  # Since one unit of distance can be traversed in one unit of time, we returned 
  # the total distance as the total time (ignoring units of course!).
  return totalDistance


def main():
  # Read in the number of points to expect.
  numPoints = int(raw_input())
  
  # Initialize one array for the x values and one for the y values.
  xCoords = [0] * numPoints
  yCoords = [0] * numPoints
  
  # Read in each pair of x/y coordinates into our list of points.
  for i in range(numPoints):
    xCoords[i], yCoords[i] = [int(n) for n in raw_input().split()]
  
  # Calculate and report the total travel time required.
  print TotalTaxicabTravelTime(xCoords, yCoords)


if __name__ == "__main__":
  main()
