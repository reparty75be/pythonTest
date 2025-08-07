import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. 크롬 드라이버 경로 설정 (크롬드라이버가 PATH에 있으면 생략 가능)
# chromedriver_path = "C:/path/to/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chromedriver_path)
# driver = webdriver.Chrome()  # 크롬드라이버가 PATH에 있을 경우
service = Service("C:/dev/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 2. 네이버 로그인 페이지 접속
driver.get("https://nid.naver.com/nidlogin.login")

# 3. 페이지가 완전히 로드될 때까지 잠시 대기
time.sleep(2)

# 4. 아이디 입력란 찾기 및 입력
pyperclip.copy("reparty75")
id_input = driver.find_element(By.CSS_SELECTOR, "#id")
id_input.clear()
id_input.click()
id_input.send_keys(Keys.CONTROL, "v")

# 5. 비밀번호 입력란 찾기 및 입력
pyperclip.copy("1q2w3e4r!")
pw_input = driver.find_element(By.CSS_SELECTOR, "#pw")
pw_input.clear()
pw_input.click()
pw_input.send_keys(Keys.CONTROL, "v")

# 6. 로그인 버튼 클릭
login_btn = driver.find_element(By.CSS_SELECTOR, "#log\\.login")
login_btn.click()

# 7. 로그인 후 페이지가 로드될 때까지 대기 (필요에 따라 조정)
time.sleep(5)

# 로그인 성공 여부 확인 후 alert로 성공 메시지 띄우기

from selenium.common.exceptions import NoSuchElementException

try:
    # 네이버 로그인 성공 시, 네이버 메인 페이지의 특정 요소(예: 프로필 아이콘 등)가 있는지 확인
    # 여기서는 네이버 메인 로고가 있는지로 간단히 체크 (실제 서비스에 맞게 요소를 조정하세요)
    driver.find_element(By.CSS_SELECTOR, "a#NM_set_home")  # 네이버 메인 로고
    driver.execute_script("alert('로그인 성공');")
except NoSuchElementException:
    print("로그인 실패 또는 요소를 찾을 수 없습니다.")

# 브라우저를 닫으려면 아래 주석 해제
# driver.quit()