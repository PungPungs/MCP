## MCP SERVER 구축
- 공식 홈페이지를 보고 따라하는 MCP 서버 구축

```json
// "C:\Users\keyha\AppData\Roaming\Claude\claude_desktop_config.json"
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\dev\\Code\\MCP\\weather",
        "run",
        "weather.py"
      ]
    }
  }
}

```

### [테스트 결과]
- claud desktop에 mcp 를 등록하여서 사용하였다.
- 호출 전 사용자에게 사용 여부를 물어보고 작동 시작
- 서버가 미국이라 응답이 없었던 것으로 추정함.

![result](../img/img/weather_result.png)
