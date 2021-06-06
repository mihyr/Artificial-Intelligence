import common
import student_code

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

def check_result(title, map1, map2):
	result=True
	print(title)
	for y in range(0,common.constants.MAP_HEIGHT):
		v=""
		for x in range(0,common.constants.MAP_WIDTH):
			if (map1[y][x]==map2[y][x]):
				v+=bcolors.GREEN+str(map1[y][x])+bcolors.NORMAL
			else:
				result = False
				v+=bcolors.RED+str(map1[y][x])+bcolors.NORMAL
		print(v)
	if (result):
		print("Test Result: " + bcolors.GREEN+"Passed"+bcolors.NORMAL)
	else:
		print("Test Result: " + bcolors.RED+"Failed"+bcolors.NORMAL)
	return result

data1 = (
"100000011"
"110111011"
"111111011"
"110000003"
"111111011"
"111020000")

gold_df1 = ("100000011"
"110111011"
"111111011"
"110000555"
"111111511"
"111055540")

data2 = (
"200000011"
"011111011"
"000001011"
"111011003"
"111111011"
"111000011"
"111111011")

gold_df2 = ("555555511"
"411111511"
"444441511"
"111411555"
"111111011"
"111000011"
"111111011")


data3 = (
"100000011"
"111011011"
"000011011"
"111011003"
"110011011"
"111200011")

gold_df3 = (
"100000011"
"111011011"
"000011011"
"111411555"
"110411511"
"111555511")







  
all_passed = True

gold_dfmap1 = common.init_map();
common.set_map(gold_dfmap1, gold_df1)

dfmap1 = common.init_map()
common.set_map(dfmap1, data1)
df1 = student_code.astar_search(dfmap1)
tdf1 ="Reachable goal:"
cdf1 = check_result(tdf1,dfmap1,gold_dfmap1)

all_passed = all_passed and cdf1 and df1  

gold_dfmap2 = common.init_map();
common.set_map(gold_dfmap2, gold_df2)

dfmap2 = common.init_map()
common.set_map(dfmap2, data2)
df2 = student_code.astar_search(dfmap2)
tdf2 ="Reachable goal:"
cdf2 = check_result(tdf2,dfmap2,gold_dfmap2)

all_passed = all_passed and cdf2 and df2 

gold_dfmap3 = common.init_map();
common.set_map(gold_dfmap3, gold_df3)

dfmap3 = common.init_map()
common.set_map(dfmap3, data3)
df3 = student_code.astar_search(dfmap3)
tdf3 ="Reachable goal:"
cdf3 = check_result(tdf3,dfmap3,gold_dfmap3)


all_passed = all_passed and cdf3 and df3  




all_passed = all_passed and cdf5 and df5

if all_passed:
	exit(0)
else:
	exit(1)
