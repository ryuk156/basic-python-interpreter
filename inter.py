import itertools
import time
import datetime
import math

def main():
    user_global={}
    save_user_global(user_global)
    for i,user_input in get_user_input():

        user_global=exec_user_input(i,user_input,user_global)
        save_user_global(user_global)

def select_user_global(user_global):
    return (
		(key, user_global[key])
		for key in sorted(user_global)
		if not key.startswith('__') or not key.endswith('__')
	)


def save_user_global(user_global,path='user_global.txt'):
     with open(path,'w') as fd:
         for key,val in select_user_global(user_global):
             fd.write('%s = %s(%s) ' % (key,val,val.__class__.__name__))


def exec_function(user_input):
    try:
        compile(user_input,'<stdin>','eval')
    except SyntaxError:
        return exec
    return eval

def exec_user_input(i,user_input,user_global):
    
   
   
    user_global=user_global.copy()
    try:
        retval=exec_function(user_input)(user_input,user_global)
    except Exception as e:
        print('%s :%s' % (e.__class__.__name__,e))
    else:

        if retval is not None:
            print('Out [%d]:' % (i,retval) )
    return user_global

    
    


def get_user_input():
    
    t0 = time.time()
    
    
    for i in itertools.count():
        try:
            t1 =time.time()
            dat = t1 - t0
            x=math.ceil(dat)
            yield i,input('In [%d]' % i +'['+ str(x)+' sec]' + ':'   )  
        except KeyboardInterrupt:
            pass
        except EOFError:
           
            break
