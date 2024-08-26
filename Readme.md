# SHRINK.CAPUT.CLOUD

AWS 서비스인 API Gateway, Lambda, 그리고 DynamoDB를 사용하여 서버리스 프라이빗 URL 단축기를 구현하였습니다. 효율성과 비용 효과를 고려하여 설계되었으며, API Gateway의 Mapping Templates를 활용하여 기본 페이지를 제공함으로써 불필요한 리소스 사용을 줄였습니다.

- API Gateway: 들어오는 요청을 처리하고 애플리케이션의 진입점 역할을 합니다.
- Lambda: URL 단축 및 리디렉션 로직을 처리합니다.
- DynamoDB: 단축 코드와 원본 URL 간의 매핑을 저장합니다.


## AWS Architecture

![Diagram](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FLrpKi%2FbtsJenZOwY6%2F9NDayV6o5ZWEguMq1OrAr1%2Fimg.png)


## 🔗 Links
![티스토리 블로그 - AWS 개인 URL Shortener 만들기](https://caputdraconis.tistory.com/entry/AWS-%EA%B0%9C%EC%9D%B8-URL-Shortener-%EB%A7%8C%EB%93%A4%EA%B8%B0)
