import random 

def getGvars():
    data = {}
    data['version'] = '1.0'
    data['logo_2'] = """
  ________    _____      _____  ___________   _________________________ _____________________
 /  _____/   /  _  \    /     \ \_   _____/  /   _____/\__    ___/  _  \\______   \__    ___/
/   \  ___  /  /_\  \  /  \ /  \ |    __)_   \_____  \   |    | /  /_\  \|       _/ |    |   
\    \_\  \/    |    \/    Y    \|        \  /        \  |    |/    |    \    |   \ |    |   
 \______  /\____|__  /\____|__  /_______  / /_______  /  |____|\____|__  /____|_  / |____|   
        \/         \/         \/        \/          \/                 \/       \/           """
    data['logo_1'] = """く__,.ヘヽ.　　　　/　,ー､ 〉
　　　　　＼ ', !-─‐-i　/　/´
　　　 　 ／｀ｰ'　　　 L/／｀ヽ､
　　 　 /　 ／,　 /|　 ,　 ,　　　 ',
　　　ｲ 　/ /-‐/　ｉ　L_ ﾊ ヽ!　 i
　　　 ﾚ ﾍ 7ｲ｀ﾄ　 ﾚ'ｧ-ﾄ､!ハ|　 |
　　　　 !,/7 '0'　　 ´0iソ| 　 |　　　
　　　　 |.从"　　_　　 ,,,, / |./ 　 |
　　　　 ﾚ'| i＞.､,,__　_,.イ / 　.i 　|
　　　　　 ﾚ'| | / k_７_/ﾚ'ヽ,　ﾊ.　|
　　　　　　 | |/i 〈|/　 i　,.ﾍ |　i　|
　　　　　　.|/ /　ｉ： 　 ﾍ!　　＼　|
　　　 　 　 kヽ>､ﾊ 　 _,.ﾍ､ 　 /､!
　　　　　　 !'〈//｀Ｔ´', ＼ ｀'7'ｰr'
　　　　　　 ﾚ'ヽL__|___i,___,ンﾚ|ノ
　　　　　 　　　ﾄ-,/　|___./
　　　　　 　　　'ｰ'　　!_,.:"""


    return data

def getVars():
    vars = {}
    vars['step'] = 1
    return vars

#===============================================================     
#===============================================================   

gvars = getGvars()
vars = getVars()

print(gvars['logo_1'])
print('Game version: ' + gvars['version'])
print(gvars['logo_2'])

i = 0

while i < 10000:

    i += 1

    int_1 = random.randint(1, 6);
    int_2 = random.randint(1, 6);

    sum = int_1 + int_2;

    print("The sum of dice is " + str(int_1) + " + " + str(int_2) + " = " + str(sum));

    if(vars['step'] == 1 and (sum == 7 or sum == 11)):
        print('You won')
        break
    elif(vars['step'] == 1 and (sum == 2 or sum == 3 or sum == 12)):
        print('You lose')
        break
    elif(vars['step'] == 1 ):
        print('Now your goal number is ' + str(sum))
        vars['target_int'] = sum
        vars['step'] = 2
        continue
    elif(vars['step'] == 2 and sum == 7):
        print('You lose')
        break
    elif(vars['step'] == 2 and sum == vars['target_int']):
        print('You won')
        break
    else:
        continue