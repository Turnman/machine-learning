# testing get_maxQ fucntion

dd = {
    'state1':{
        'action1':0,
        'action2':2,
        'action3':-4},
    'state2':{
        'action1':0,
        'action2':2,
        'action3':-4},
    'state3':{
        'action1':0,
        'action2':-0.02,
        'action3':-0.4},
    'state4':{
        'action1':0,
        'action2':0,
        'action4':(-0.4)},
    }

max_dd = max(dd['state4'])
print "max_dd: {}".format(max_dd)
addi = dd['state4'][max_dd]+1
print "add: {}".format(addi)
res = [key for keys in dd['state4'] if dd['state4'][key] == 0]

print res 
