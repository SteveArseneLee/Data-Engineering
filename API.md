# Application Programming Interface
두 개의 시스템이 서로 상호 작용하기 위한 인터페이스
- 데이터를 주고 받는 데이터베이스
- API라 하면 보통 REST API를 지칭
- API Key란 보통 Request URL 혹은 Request헤더에 포함되는 긴 스트링

## Web API
- 웹을 통해 외부 서비스들로부터 정보를 불러오는 API
- 웹 사이트는 HTTP(S) 프로토콜을 사용하는 REST API 기반으로 구축

## Authentication VS Authorization
- Authentication : Identity(정체)가 맞다는 증명
- Authorization : API를 통한 어떠한 액션을 허용

### Basic Auth
Basic Auth의 경우 username:password와 같은 Credeential을 Base64로 인코딩한 값을 Request Header안에 포함
ex)
```python
encoded = base64.b64encode("{}:{}".format(self.client_id, self.client_secret))
base_url = "https://accounts.spotify.com/api/token"
headers = {"Authorization" : "Basic{}".format(encoded)}
```
<br>
### "Resource"는 API를 통해 리턴된 정보
> 하나의 Resource 안에 여러 개의 Endpoints가 존재

- Endpoint - Resource를 엑세스하는 경로/방법
- Method - 자원 접근에 허용된 행위 (GET, POST, PUT, DELETE 등)

Method 정의
- GET - 해당 리소스를 조회하고 정보를 가져옴
- HEAD - GET 방식과 동일하나 응답코드와 HEAD만 가져옴
- POST - 요청된 리소스를 생성
- PUT - 요청된 리소스를 업데이트
- DELETE - 요청된 리소스를 삭제
<br>
> GET /campaigns/{campaign_id}/actions/send
- method는 GET
- /campaigns/{campaign_id}/actions/send는 Endpoint
<br>
### Parameters
Endpoint를 통해 리퀘스트할때 같이 전달하는 옵션들
- Header - Request Header에 포함되는 Parameter로 주로 Authorization에 관련
- Path - Query String(?) 이전에 Endpoint Path 안에 포함되는 변수
    - ex) {id}
- Query String - Query String(?) 이후에 포함되는 Parameters
    - ex) ?utm_source=facebook&utm_campaign=summer_sales
- Request Body - Request Body안에 포함되는 Parameters. 주로 JSON형태

  
<br> 파이썬 연습
```python
import sys

def main():
    print('fastcampus')
    
if __name__=='__main__':
    main()
else: # 현 파일이 직접 실행이 안되고 어떤 모듈 패키지화되서 import되면 출력
    print('this script is being imported')
```

<br>
### 방법
Application(Request access token)에서 (client, client_secret, grant_type)을 Spotify Accounts Service에게 주고 Spotify가 access_token을 user에게 넘겨주면 우린 그걸 가지고 API를 통해 데이터를 가져온다.


