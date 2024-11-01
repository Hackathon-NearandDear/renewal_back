import subprocess
from Blockchain import utils
import json
import requests


base_url = "http://localhost:7777"


def register_user(user_address:str) -> {bool}:
  try:
      url = '/'
      response = requests.get(base_url + url)
      
      if response.status_code == 200:
          # JSON 응답 데이터 파싱
          result = response.json()
          print("응답 데이터:", result)
          return True
      else:
          print("요청 실패. 상태 코드:", response.status_code)
          print("응답 메시지:", response.text)
          return False

  except requests.exceptions.RequestException as e:
      print("요청 중 에러 발생:", e)
      return False 


def register_ai(creator_address: str,  ai_id: str, prompt: str) -> str:

  return 
  
def store_rag_data(creator_address: str, ai_id: str, prompt: str) -> str:

  return 


def pay_for_chat(creatorAccountId: str, consumerAccountId :str, aiId: str, usedToken: int) -> str:
  data = {
     "creatorAccountId" : creatorAccountId,
     "consumerAccountId" : consumerAccountId,
     "aiId" : aiId,
     "usedToken" : usedToken
  }
  try:
      url = '/pay_for_chat'
      response = requests.post(base_url + url, json = data)
      
      if response.status_code == 200:
          # JSON 응답 데이터 파싱
          result = response.json()
          print("응답 데이터:", result)
          return result
      else:
          print("요청 실패. 상태 코드:", response.status_code)
          print("응답 메시지:", response.text)
          return result

  except requests.exceptions.RequestException as e:
      print("요청 중 에러 발생:", e)
      return result  
  
def claim_rewards_by_ai(user_address: str, ai_id: str) -> str:
  return 

def request_faucet(user_address : str) -> str:
  try:
    url = '/request_faucet'
    response = requests.post(url = base_url + url, json={ "userAccountId" : user_address})
    
    if response.status_code == 200:
        # JSON 응답 데이터 파싱
        result = response.json()
        print("응답 데이터:", result)
        return result
    else:
        print("요청 실패. 상태 코드:", response.status_code)
        print("응답 메시지:", response.text)
        return result

  except requests.exceptions.RequestException as e:
    print("요청 중 에러 발생:", e)
    return result 

def use_free_trial(str) -> str:
  try:
      url = '/get_consumer/' + user_adress
      response = requests.get(base_url + url)
      
      if response.status_code == 200:
          # JSON 응답 데이터 파싱
          result = response.json()
          print("응답 데이터:", result)
          return result.freeTrialCount
      else:
          print("요청 실패. 상태 코드:", response.status_code)
          print("응답 메시지:", response.text)
          return result

  except requests.exceptions.RequestException as e:
      print("요청 중 에러 발생:", e)
      return result 



# View functions

def view_exists_creator_at(str):

  return 


def view_exists_consumer_at(str):

  return 

def view_contain_ai(str):

  return 

def view_get_ai_rewards( str):

  return

def view_get_consumer_balance( str):

  return 

def view_get_free_trial_count(user_adress : str):
  try:
      url = '/get_consumer/' + user_adress
      response = requests.get(base_url + url)
      
      if response.status_code == 200:
          # JSON 응답 데이터 파싱
          result = response.json()
          print("응답 데이터:", result)
          return result.freeTrialCount
      else:
          print("요청 실패. 상태 코드:", response.status_code)
          print("응답 메시지:", response.text)
          return result

  except requests.exceptions.RequestException as e:
      print("요청 중 에러 발생:", e)
      return result 

