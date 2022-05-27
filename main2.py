from tokens import check_expression,add_spaces
from Graph import nodes, node
from pyvis.network import Network
net = Network('1040px', '1230px')
from random import random


rules = [["term", "exp'"],
         ["addop", "term", "exp'"],
         [],
         ["+"],
         ["-"],
         ["factor", "term'"],
         ["mulop", "factor", "term'"],
         [],
         ["*"],
         ["/"],
         ["Num"],
         ["ID"],
         ["(", "exp", ")"]]

pars=[[0,0,-1,-1,-1,-1,0,-1,-1],
      [-1,-1,1,1,-1,-1,-1,2,2],
      [-1,-1,3,4,-1,-1,-1,-1,-1],
      [5,5,-1,-1,-1,-1,5,-1,-1],
      [-1,-1,7,7,6,6,-1,7,7],
      [-1,-1,-1,-1,8,9,-1,-1,-1],
      [10,11,-1,-1,-1,-1,12,-1,-1],
      [-1,-1,-1,-1,-1,-1,-1,-1,-1]]

pars2=[[0,0,-1,-1,-1,-1,0,-1,-1],
      [-1,-1,1,1,-1,-1,-1,2,2],
      [-1,-1,3,4,-1,-1,-1,-1,-1],
      [5,5,-1,-1,-1,-1,5,-1,-1],
      [-1,-1,7,7,6,6,-1,7,7],
      [-1,-1,-1,-1,8,9,-1,-1,-1],
      [10,11,-1,-1,-1,-1,12,-1,-1],
      [2,2,2,2,2,2,2,2,2]]





def current(stack):
      match stack:
            case "exp":
                  return 0
            case "exp'":
                  return 1
            case "addop":
                  return 2
            case "term":
                  return 3
            case "term'":
                  return 4
            case "mulop":
                  return 5
            case "factor":
                  return 6
            case "ID":
                  return 7
            case "+":
                  return 7
            case "-":
                  return 7
            case "Num":
                  return 7
            case "*":
                  return 7
            case "/":
                  return 7
            case "(":
                  return 7
            case ")":
                  return 7
            case "$":
                  return 7

#lask + 2 - 213 * sak

def par(input):
      stack = ["$","exp"]
      nodes=[]
      nodes.append(node("exp","root"))
      while (True):
            for z in stack:
                  print(z,end=" ")
            print()
            if (len(input)<=0):
                  break
            if input[0] == "$":
                  tmp=stack[-1]
                  nodetmp=nodes.pop()
                  s=[]
                  stack.pop()
                  rule = pars2[current(tmp)][8]
                  s2=[]
                  for z in rules[rule]:
                        s.append(z)
                        c = node(z,z+input[0]+str(random()))
                        nodetmp.addEdge(c)
                        s2.append(c)
                  s.reverse()
                  s2.reverse()
                  for k in s:
                        stack.append(k)
                  for k in s2:
                        nodes.append(k)


            elif input[0] == "ID":
                  tmp = stack[-1]
                  nodetmp = nodes.pop()
                  s = []
                  stack.pop()
                  s2 = []
                  rule = pars2[current(tmp)][1]
                  for z in rules[rule]:
                        s.append(z)
                        c = node(z,z+input[0]+str(random()))
                        nodetmp.addEdge(c)
                        s2.append(c)

                  s.reverse()
                  s2.reverse()

                  for k in s:
                        stack.append(k)
                  for k in s2:
                        nodes.append(k)


            elif input[0] == "Num":
                  tmp=stack[-1]
                  nodetmp=nodes.pop()
                  s=[]
                  stack.pop()
                  s2=[]
                  rule = pars2[current(tmp)][0]
                  for z in rules[rule]:
                        s.append(z)
                        c = node(z,z+input[0]+str(random()))
                        nodetmp.addEdge(c)
                        s2.append(c)

                  s.reverse()
                  s2.reverse()

                  for k in s:
                        stack.append(k)
                  for k in s2:
                        nodes.append(k)


            elif input[0] == '+':
                  tmp=stack[-1]
                  nodetmp=nodes.pop()
                  s=[]
                  stack.pop()
                  s2=[]
                  rule = pars2[current(tmp)][2]
                  for z in rules[rule]:
                        s.append(z)
                        c = node(z,z+input[0]+str(random()))
                        nodetmp.addEdge(c)
                        s2.append(c)

                  s.reverse()
                  s2.reverse()

                  for k in s:
                        stack.append(k)
                  for k in s2:
                        nodes.append(k)


            elif input[0] == "-":
                  tmp=stack[-1]
                  nodetmp=nodes.pop()
                  s=[]
                  stack.pop()
                  s2=[]
                  rule = pars2[current(tmp)][3]
                  for z in rules[rule]:
                        s.append(z)
                        c = node(z,z+input[0]+str(random()))
                        nodetmp.addEdge(c)
                        s2.append(c)

                  s.reverse()
                  s2.reverse()

                  for k in s:
                        stack.append(k)
                  for k in s2:
                        nodes.append(k)


            elif input[0] == "*":
                  tmp=stack[-1]
                  nodetmp=nodes.pop()
                  s=[]
                  stack.pop()
                  s2=[]
                  rule = pars2[current(tmp)][4]
                  for z in rules[rule]:
                        s.append(z)
                        c = node(z,z+input[0]+str(random()))
                        nodetmp.addEdge(c)
                        s2.append(c)

                  s.reverse()
                  s2.reverse()

                  for k in s:
                        stack.append(k)
                  for k in s2:
                        nodes.append(k)


            elif input[0] == "/":
                  tmp=stack[-1]
                  nodetmp=nodes.pop()
                  s=[]
                  stack.pop()
                  s2=[]
                  rule = pars2[current(tmp)][5]
                  for z in rules[rule]:
                        s.append(z)
                        c = node(z,z+input[0]+str(random()))
                        nodetmp.addEdge(c)
                        s2.append(c)
                  s.reverse()
                  s2.reverse()
                  for k in s:
                        stack.append(k)
                  for k in s2:
                        nodes.append(k)


            elif input[0] == "(":
                  tmp=stack[-1]
                  nodetmp=nodes.pop()
                  s=[]
                  stack.pop()
                  s2=[]
                  rule = pars2[current(tmp)][6]
                  for z in rules[rule]:
                        s.append(z)
                        c = node(z,z+input[0]+str(random()))
                        nodetmp.addEdge(c)
                        s2.append(c)
                  s.reverse()
                  s2.reverse()
                  for k in s:
                        stack.append(k)
                  for k in s2:
                        nodes.append(k)


            elif input[0] == ")":
                  tmp=stack[-1]
                  nodetmp=nodes.pop()
                  s=[]
                  stack.pop()
                  s2=[]
                  rule = pars2[current(tmp)][7]
                  for z in rules[rule]:
                        s.append(z)
                        c = node(z,z+input[0]+str(random()))
                        nodetmp.addEdge(c)
                        s2.append(c)
                  s.reverse()
                  s2.reverse()
                  for k in s:
                        stack.append(k)
                  for k in s2:
                        nodes.append(k)

            if stack[-1]==input[0]:
                  input.pop(0)


def par2(input):
      stack = ["$","exp"]
      while (True):
            for z in stack:
                  print(z,end=" ")
            print()
            if (len(input)<=0):
                  break
            if stack[-1]==input[0]:
                  input.pop(0)
                  stack.pop()
                  continue
            tmp = stack[-1]
            stack.pop()

            if input[0] == "$":
                  s=[]
                  rule = pars[current(tmp)][8]
                  if rule == -1:
                        break
                  for z in rules[rule]:
                        s.append(z)
                  s.reverse()
                  for k in s:
                        stack.append(k)

            elif input[0] == "(":
                  s=[]
                  rule = pars[current(tmp)][6]
                  if rule == -1:
                        break
                  for z in rules[rule]:
                        s.append(z)
                  s.reverse()
                  for k in s:
                        stack.append(k)


            elif input[0] == ")":
                  s = []
                  rule = pars[current(tmp)][7]
                  if rule == -1:
                        break
                  for z in rules[rule]:
                        s.append(z)
                  s.reverse()
                  for k in s:
                        stack.append(k)

            elif input[0] == "ID":
                  s = []
                  rule = pars[current(tmp)][1]
                  if rule == -1:
                        break
                  for z in rules[rule]:
                        s.append(z)


                  s.reverse()


                  for k in s:
                        stack.append(k)

            elif input[0] == "Num":

                  s=[]
                  rule = pars[current(tmp)][0]
                  if rule == -1:
                        break
                  for z in rules[rule]:
                        s.append(z)

                  s.reverse()

                  for k in s:
                        stack.append(k)


            elif input[0] == '+':

                  s=[]
                  rule = pars[current(tmp)][2]
                  print(rule)
                  if rule == -1:
                        break
                  for z in rules[rule]:
                        s.append(z)

                  s.reverse()

                  for k in s:
                        stack.append(k)


            elif input[0] == "-":

                  s=[]
                  rule = pars[current(tmp)][3]
                  if rule == -1:
                        break
                  for z in rules[rule]:
                        s.append(z)

                  s.reverse()

                  for k in s:
                        stack.append(k)

            elif input[0] == "*":

                  s=[]
                  rule = pars[current(tmp)][4]
                  if rule == -1:
                        break
                  for z in rules[rule]:
                        s.append(z)

                  s.reverse()

                  for k in s:
                        stack.append(k)

            elif input[0] == "/":

                  s=[]
                  rule = pars[current(tmp)][5]
                  if rule == -1:
                        break
                  for z in rules[rule]:
                        s.append(z)
                  s.reverse()
                  for k in s:
                        stack.append(k)

      if input:
            return False
      else:
            return True
      if stack[-1]=='$':
            return True
      else:
            return False



def editInput(x):
      print(x)
      x=x.split()
      z=0
      for u in x:
            if u == "(" or u == ")":
                  x.pop(z)
            z += 1

      print(x)
      z=0
      for i in x:
            if  (i in "+-*/"):
                  x.pop(x.index(i))
            else:
                  continue
            z+=1
      editNodes(x)

def editNodes(inp):
      for i in nodes:
            if not inp:
                  break
            if i.name == "ID" or i.name=="Num":
                  i.name=inp.pop(0)

t=[]
l=[]
x="x + y"
x=add_spaces(x,[])
check_expression(x,l,t)
print("---------------------")
for i in t:
      print(i)
print("---------------------")
stack=[]

b=par2(t)
print("---------------------")
print("---------------------")

for i in stack:
      print(i.c)
print(b)