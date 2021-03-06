#coding:utf-8
import os

# store function name
lodashList = []

def getDirList(p):
  p = str(p + '/')
  a = os.listdir(p)
  b = [x for x in a if os.path.isdir(p + x)]
  return b

def getFileList(p):
  p = str(p + '/')
  a = os.listdir(p)
  b = [x for x in a if os.path.isfile(p + x)]
  return b

def getFuncName(str):
  index = str.find('_.')
  if index != -1:
    end = -1
    for i in range(index+2, len(str)):
      if not str[i].isalpha():
        end = i
        break
    if end != -1:
      return str[index+2:end]
  else:
      return None

def filter(filePath):
  fp = open(filePath, 'r')
  content = fp.readlines()
  for line in content:
    name = getFuncName(line)
    while(name != None):
      if name not in lodashList:
        lodashList.append(name)
      line = line[line.find(name)+len(name):]
      name = getFuncName(line)

def lodashFilter(pwd):
  dirList = getDirList(pwd)
  if 'images' in dirList:
    dirList.remove('images')
  for dir in dirList:
    lodashFilter(pwd + '/' + dir)
  fileList = getFileList(pwd)
  if 'lodash.custom.min.js' in fileList:
    fileList.remove('lodash.custom.min.js')
  if 'lodashMinim.py' in fileList:
    fileList.remove('lodashMinim.py')
  for file in fileList:
    filter(pwd + '/' + file)


if __name__ == '__main__':
  print 'searching...'
  pwd = os.getcwd()
  lodashFilter(pwd)
  t = tuple(lodashList)
  str_result = 'lodash -p include='
  for a in t:
    str_result += a + ','
  print 'waiting...'
  os.system(str_result)
